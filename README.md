# e-kreta-hunor-2.0

e-kreta-hunor-2.0 is an api wrapper for the e-kreta system

## installation

for now download the repo and install requirements.txt

```bash
py -m pip install -r requirements.txt
```

later i plan to add it on pypi

## Usage

```python
import json
from api import idp
from api.mobile import endpoints

with idp.Auth_session.login(username, pwd, institute_code) as session:
    groups = endpoints.get_groups(session)
    print(json.dumps(groups.model_dump_json(indent=4)))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

tests would be appreaciated

## License

[MIT](https://choosealicense.com/licenses/mit/)
