from json import load, JSONDecodeError
from typing import Dict

from appium import webdriver

from utils.browserstack_api_util import upload_app_to_browserstack, get_browserstack_session_link
from utils.data_generator_util import get_current_date_and_time


def get_driver(os: str, browserstack_config: Dict) -> webdriver:
    """
    Creates webdriver object depended from given OS parameter
    :param os: which OS driver should be created
    :param browserstack_config: browserstack configuration parameters. Should be storage in config.json file
    """
    print(f"Prepare test run on {os.upper()} device:")

    config = browserstack_config

    bs_url = config["url"]
    bs_build_id = config["build_id"]
    bs_user_name = config["user_name"]
    bs_assess_key = config["access_key"]

    app_name = __get_app_name(os=os)
    browserstack_app_url = upload_app_to_browserstack(
        file_name=app_name, user_name=bs_user_name, access_key=bs_assess_key
    )
    desired_caps = __get_desired_caps(
        os=os, app_url=browserstack_app_url, user_name=bs_user_name, access_key=bs_assess_key
    )

    driver = None
    if os.upper() == "ANDROID":
        driver = webdriver.Remote(command_executor=bs_url, desired_capabilities=desired_caps)
    elif os.upper() == "IOS":
        driver = webdriver.Remote(command_executor=bs_url, desired_capabilities=desired_caps)
    else:
        raise KeyError(f"Unexpected OS '{os.upper()}'." f"Check your behave.ini file for available variables")

    session_link = get_browserstack_session_link(user_name=bs_user_name, access_key=bs_assess_key, build_id=bs_build_id)
    print(f"Browserstack session link: {session_link}")

    return driver


def __get_app_name(os: str) -> str:
    """
    Returns application name depended from chosen OS
    :param os: which environment parameters should be returned
    """
    app_name = ""
    try:
        if os.upper() == "ANDROID":
            app_name = "Test_app.apk"
        elif os.upper() == "IOS":
            app_name = "Test_app.ipa"
        return app_name
    except KeyError:
        raise KeyError(f"Unexpected os '{os.upper()}'. Check your behave.ini file for available variables")


def __get_desired_caps(os: str, app_url: str, user_name: str, access_key: str) -> Dict:
    """
    Returns desired capabilities of chosen OS
    :param os: which environment parameters should be returned
    :param app_url: url to application uploaded to browserstack
    """
    desired_caps = {}
    try:
        if os.upper() == "ANDROID":
            session_name = f"Android Test Run {get_current_date_and_time()}"
            desired_caps = {
                "browserstack.user": user_name,
                "browserstack.key": access_key,
                "build": "[Android] Mobile E2E tests",
                "name": session_name,
                "browserstack.debug": "true",
                "browserstack.networkLogs": "true",
                "device": "Samsung Galaxy S20 Ultra",
                "os_version": "10.0",
                "app": app_url,
            }
        elif os.upper() == "IOS":
            session_name = f"IOS Test Run {get_current_date_and_time()}"
            desired_caps = {
                "browserstack.user": user_name,
                "browserstack.key": access_key,
                "build": "[IOS] Mobile E2E tests",
                "name": session_name,
                "browserstack.debug": "true",
                "browserstack.networkLogs": "true",
                "device": "iPhone 11",
                "os_version": "14",
                "autoAcceptAlerts": "true",
                "app": app_url,
            }
        return desired_caps
    except KeyError:
        raise KeyError(f"Unexpected os '{os.upper()}'. Check your behave.ini file for available variables")


def get_env_data(os: str) -> Dict:
    """
    Returns environment capabilities of chosen OS
    :param os: which environment parameters should be returned
    """
    try:
        with open("config.json") as json_file:
            as_dict = load(json_file)[os.upper()]
            return as_dict

    except JSONDecodeError as error:
        raise ValueError(
            f"Incorrect config.json file. {error.msg} on line #{error.lineno}. "
            f"Please fix your config.json file and try ones again"
        )
    except KeyError:
        raise KeyError(f"Unexpected env '{os.upper()}'. Check your behave.ini file for available variables")
