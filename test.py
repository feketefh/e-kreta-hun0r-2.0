import os

import api

username = os.getenv("username")
pwd = os.getenv("pwd")
institiute_code = os.getenv("institute_code")

with api.idp.Auth_Session.login(username, pwd, institiute_code) as session:
    response = api.mobile.endpoints.get_notes(session)
    print(response)
    session.refresh()
    response = api.mobile.endpoints.get_device_state(session)
    print(response)
