import tree_sitter_java as tsjava
from tree_sitter import Language, Parser, Node
import re
from pathlib import Path
from warnings import warn

JAVA_LANGUAGE = Language(tsjava.language())
JAVA_PARSER = Parser(JAVA_LANGUAGE)

SPLIT_QUERY = JAVA_LANGUAGE.query(
    """
( interface_declaration
    body: ( interface_body
        ( method_declaration 
            ( modifiers 
                ( annotation ) *
                ( marker_annotation ) *
            ) @modifierses
            type: [
                (integral_type)
                (floating_point_type)
                (boolean_type)
                (void_type)
                (type_identifier)
                ( generic_type )
            ] @types
            name: ( identifier ) @names
            parameters: ( formal_parameters) @parameterses
        )
    )
)
"""
)
MODIFIER_QUERY_JAVA = JAVA_LANGUAGE.query(
    """
[ 
    ( annotation 
        name: ( identifier ) @headers
        arguments: ( annotation_argument_list
            ( element_value_array_initializer 
                ( string_literal 
                    ( string_fragment ) @pairs
                )*
            )
        )
    )
    ( annotation
        name: ( identifier ) @method
        arguments: ( annotation_argument_list
            ( string_literal 
                ( string_fragment ) @url
            )
        )
    )
    ( marker_annotation 
        name: ( identifier ) @marker_name
    )
]
"""
)
TYPE_QUERY_JAVA = JAVA_LANGUAGE.query(
    """
[
	(integral_type) @depth1_type
	(floating_point_type) @depth1_type
	(boolean_type) @depth1_type
	(void_type) @depth1_type
	(type_identifier) @depth1_type
    ( generic_type 
    	(type_identifier) @depth1_type
        ( type_arguments 
        	[
                
                (integral_type) @depth2_type
                (floating_point_type) @depth2_type
                (boolean_type) @depth2_type
                (void_type) @depth2_type
                (type_identifier) @depth2_type
                ( generic_type 
                    (type_identifier) @depth2_type
                    ( type_arguments 
                        [
                            (integral_type)
                            (floating_point_type)
                            (boolean_type)
                            (void_type)
                            (type_identifier)
                        ] @depth3_type
                    )
            	)
        	]
        )
    ) 
]
"""
)
PARAMETERS_QUERY_JAVA = JAVA_LANGUAGE.query(
    """
( formal_parameter 
    ( modifiers 
        [
        	( annotation 
            	name: ( identifier ) @parameter_locations
            	arguments: ( annotation_argument_list 
                	( string_literal
                    	( string_fragment ) @parameter_location_paths
                	)
            	)
            )
            ( marker_annotation
            	name: ( identifier ) @parameter_locations
            )
        ]
    )
    type: [
	  	(integral_type)
	  	(floating_point_type)
  		(boolean_type)
  		(void_type)
  		(type_identifier)
	] @parameter_types
    name: ( identifier ) @parameter_names
)
"""
)

SAMPLE_PYTHON_ENDPOINT = """
@overload
def {name}(session: AsyncClient[JsonSerializeable]{parameters}) -> Awaitable[{return_type}]: ...
@overload
def {name}(session: SyncClient[JsonSerializeable]{parameters}) -> {return_type}: ...
def {name}(session: Client{parameters}):
    if session.is_closed():
        raise Exception("Can't make request without an active session!")
{token_check}
    return session.request(
        "{METHOD}",
        BASE_URL + {url},
        {headers}
        {query_parameters}
        {body}
    )
"""
TOKEN_CHECK = """    if session.token is None or session.token.is_expired():
        raise Exception("Can't make this request without an active token!")"""

MISSING = next(
    a
    for a in JAVA_LANGUAGE.query('(";") @a').captures(
        JAVA_PARSER.parse(b"a b").root_node
    )["a"]
    if a.is_missing
)


def translate_file(path: Path | str):
    if isinstance(path, str):
        path = Path(path)
    with open(path, "r") as f:
        java_code = JAVA_PARSER.parse(f.read().encode("utf-8"))
        endpoints = SPLIT_QUERY.matches(java_code.root_node)

        metadata = path.parent / "Dtos" / "MetaData"
        if metadata.exists():
            with open(metadata, "r") as f:
                __all__ = f.readline()
            translated_endpoints = [
                f"from .Dtos import {__all__}\nfrom e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable\nfrom typing import Awaitable, Any, overload\n\n"
            ]
        else:
            translated_endpoints = [
                "from e_kreta.idp.client import Client, AsyncClient, SyncClient, JsonSerializeable\nfrom typing import Awaitable, Any, overload\n\n"
            ]

        for _, endpoint in endpoints:
            assert len(endpoint["modifierses"]) == 1
            modifiers: Node = endpoint["modifierses"][0]
            return_type: Node = endpoint["types"][0]
            name: Node = endpoint["names"][0]
            parameters: Node = endpoint["parameterses"][0]
            print(modifiers, return_type, name, parameters)

            translated_endpoints.append(
                translate_endpoint(modifiers, return_type, name, parameters) or ""
            )

    with open(path.with_suffix(".py"), "w") as f:
        f.write("".join(translated_endpoints))


def translate_endpoint(
    modifiers: Node, return_type: Node, name: Node, parameters: Node
) -> str|None:
    assert isinstance(name.text, bytes)
    assert isinstance(return_type.text, bytes)

    # handle return type
    are_parameters = True
    return_type_data = TYPE_QUERY_JAVA.captures(return_type)
    depth1_type = return_type_data["depth1_type"][0]
    assert isinstance(depth1_type.text, bytes)
    depth2_type = (
        return_type_data["depth2_type"][0]
        if "depth2_type" in return_type_data
        else MISSING
    )
    depth3_type = (
        return_type_data["depth3_type"][0]
        if "depth3_type" in return_type_data
        else MISSING
    )
    if depth1_type.text == b"Completable":
        return_type_as_string = "None"
    elif depth1_type.text == b"Observable" and depth2_type.text == b"List":
        assert isinstance(depth3_type.text, bytes)
        return_type_as_string = (
            "list[" + depth3_type.text.decode().removesuffix("Dto") + "]"
        )
    elif depth1_type.text in [
        b"Observable",
        b"Single",
    ]:  # TODO: explore deeper meaning of these
        assert isinstance(depth2_type.text, bytes)
        return_type_as_string = depth2_type.text.decode().removesuffix("Dto")
    elif depth1_type.text == b"Object":
        assert isinstance(parameters.text, bytes)
        return_type_match = re.match(
            R"^\(Continuation<(?:\? extends|\? super)? (?:(\w+)<)?(\w+?)(?:Dto)?>?> continuation\)$",
            parameters.text.decode(),
        )
        assert return_type_match is not None
        groups = return_type_match.groups()
        assert len(groups) == 2
        if groups[0]:
            return_type_as_string = f"{groups[0].lower()}[{groups[1]}]"
        else:
            return_type_as_string = groups[1]
        are_parameters = False
    else:
        warn(str((depth1_type.text, depth2_type.text, depth3_type.text)))
        return

    # handle modifiers
    body_location = b"json"
    auth_required = False
    method = None
    url = None
    headers_dict_as_list_of_strings: list[list[str]] = []
    body_location = "json"
    for modifier in modifiers.children:
        modifier_data = MODIFIER_QUERY_JAVA.captures(modifier)
        headers_modifier_name = (
            modifier_data["headers"] if "headers" in modifier_data else [MISSING]
        )
        pairs_modifier_arguments = (
            modifier_data["pairs"] if "pairs" in modifier_data else [MISSING]
        )
        method_modifier_name = (
            modifier_data["method"] if "method" in modifier_data else [MISSING]
        )
        url_modifier_argument = (
            modifier_data["url"] if "url" in modifier_data else [MISSING]
        )
        marker_name = (
            modifier_data["marker_name"]
            if "marker_name" in modifier_data
            else [MISSING]
        )

        if (
            headers_modifier_name[0].text
            and headers_modifier_name[0].text.decode() == "Headers"
        ):
            assert all(
                isinstance(pair.text, bytes) for pair in pairs_modifier_arguments
            )
            headers_dict_as_list_of_strings.extend(
                [
                    korv.strip()
                    for korv in pair.text.decode().split(":") # type: ignore
                ]
                for pair in pairs_modifier_arguments
            )
        elif method_modifier_name[0].text in [
            b"GET",
            b"PUT",
            b"POST",
            b"PATCH",
            b"DELETE",
        ]:
            assert isinstance(method_modifier_name[0].text, bytes)
            method = method_modifier_name[0].text.decode().upper()
            assert isinstance(url_modifier_argument[0].text, bytes)
            url = url_modifier_argument[0].text.decode()
        elif marker_name[0].text == b"Authentication":  # TODO: implement Multipart
            auth_required = True
        elif marker_name[0].text == b"Streaming":
            return_type_as_string = "bytes"
        elif marker_name[0].text == b"FormUrlEncoded":
            body_location = "data"
        else:
            warn(
                (
                    marker_name[0].text
                    or headers_modifier_name[0].text
                    or method_modifier_name[0].text
                    or b"even worse"
                ).decode()
            )
            return

    headers_dict_as_string = ",\n        ".join(
        '"{}": "{}"'.format(*pair)
        for pair in headers_dict_as_list_of_strings
    )

    # handle parameters
    path_dict: dict[str, str] = {}
    data_model: str = ""
    query_dict_as_list_of_strings: list[str] = []
    parameters_list: list[str] = []
    if are_parameters:
        parameters_data = PARAMETERS_QUERY_JAVA.matches(parameters)

        for _, parameter_data in parameters_data:
            parameter_location = parameter_data["parameter_locations"][0]
            parameter_type = parameter_data["parameter_types"][0]
            parameter_name = parameter_data["parameter_names"][0]

            assert isinstance(parameter_location.text, bytes)
            assert isinstance(parameter_type.text, bytes)
            assert isinstance(parameter_name.text, bytes)
            parameters_list.append(
                parameter_name.text.decode()
                + ": "
                + {"String": "str", "Boolean": "bool"}
                .get(parameter_type.text.decode(), parameter_type.text.decode())
                .removesuffix("Dto")
            )
            if parameter_location.text == b"Body":
                data_model = parameter_name.text.decode().removesuffix("Dto")
            if parameter_location.text == b"Path":
                parameter_location_path = parameter_data["parameter_location_paths"][0]
                assert isinstance(parameter_location_path.text, bytes)
                path_dict[parameter_location_path.text.decode()] = (
                    f"{{{parameter_name.text.decode()}}}"
                )
            if parameter_location.text == b"Query":
                parameter_location_path = parameter_data["parameter_location_paths"][0]
                assert isinstance(parameter_location_path.text, bytes)
                query_dict_as_list_of_strings.append(
                    parameter_location_path.text.decode()
                    + ": "
                    + parameter_name.text.decode()
                )
    query_dict_as_string = ",\n        ".join(
        '"{}": {}'.format(*pair.split(": ")) for pair in query_dict_as_list_of_strings
    )

    assert method
    assert url
    python_code = SAMPLE_PYTHON_ENDPOINT.format(
        name=name.text.decode(),
        parameters=(", " + ", ".join(parameters_list)) if parameters_list else "",
        return_type={"String": "str", "Boolean": "bool"}.get(
            return_type_as_string, return_type_as_string
        ),
        body=(
            f'{body_location}={data_model}.model_dump(mode="json")'
            if data_model
            else ""
        ),
        headers=(
            f"\n        headers = {{\n            {headers_dict_as_string}\n        }},"
            if headers_dict_as_string
            else ""
        ),
        query_parameters=(
            f"\n        query = {{\n            {query_dict_as_string}\n        }},"
            if query_dict_as_string
            else ""
        ),
        token_check=TOKEN_CHECK if auth_required else "",
        METHOD=method,
        url=("f" if path_dict else "") + f'"{url.format(**path_dict)}"',
    )
    return python_code


if __name__ == "__main__":
    translate_file(
        R"C:\Users\vajkh\e_kreta\tools\decompiler\kreta_partial\mobileapi\MobileApiV3.java"
    )
