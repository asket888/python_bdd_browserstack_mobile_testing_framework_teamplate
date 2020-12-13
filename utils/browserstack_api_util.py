import requests

from utils.file_management_util import get_absolute_path_to_folder

__BROWSERSTACK_API_URL = "https://api-cloud.browserstack.com/app-automate"


def upload_app_to_browserstack(file_name: str, user_name: str, access_key: str) -> str:
    print(f"{file_name} is uploading to browserstack...")
    path_to_file = f"{get_absolute_path_to_folder(folder_name='apps')}/{file_name}"

    url = f"{__BROWSERSTACK_API_URL}/upload"
    files = {"file": (file_name, open(path_to_file, "rb"))}

    response = requests.post(url=url, files=files, auth=(user_name, access_key))

    try:
        assert response.status_code == 200
        app_url = response.json()["app_url"]
    except (AssertionError, KeyError, TypeError):
        raise ConnectionError(
            f"Can not upload application to Browserstack. "
            f"Status code: {response.status_code}. "
            f"Response message: {response.text}"
        )

    print(f"{file_name} is successfully uploaded...")
    print(f"Browserstack application link: {app_url}")

    return app_url


def get_browserstack_session_link(user_name: str, access_key: str, build_id: str) -> str:

    url = f"{__BROWSERSTACK_API_URL}/builds/{build_id}/sessions.json?status=running"
    response = requests.get(url=url, auth=(user_name, access_key))
    link_to_build = response.json()[0]["automation_session"]["browser_url"]

    return link_to_build
