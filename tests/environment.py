from allure import attach, attachment_type
from behave.model import Scenario, Feature
from behave.runner import Context
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

from objects.pages.android.question_page import AndroidQuestionPage
from objects.pages.android.authorization_page import AndroidLoginPage
from objects.pages.android.main_menu_section import AndriodMainMenuSection
from objects.pages.android.user_profile_page import AndroidUserProfilePage
from objects.pages.android.question_ask_page import AndroidAskQuestionPage
from objects.pages.android.markets_list_page import AndroidMarketsListPage
from objects.pages.android.search_by_text_page import AndriodSearchByTextPage
from objects.pages.android.search_by_image_page import AndriodSearchByImagePage

from objects.pages.ios.authorization_page import IosLoginPage
from objects.pages.ios.main_menu_section import IosMainMenuSection
from objects.pages.ios.markets_list_page import IosMarketsListPage
from objects.pages.ios.question_ask_page import IosAskQuestionPage
from objects.pages.ios.question_page import IosQuestionPage
from objects.pages.ios.user_profile_page import IosUserProfilePage
from objects.pages.ios.search_by_text_page import IosSearchByTextPage
from objects.pages.ios.search_by_image_page import IosSearchByImagePage

from utils.capabilities_util import get_env_data, get_driver


def before_all(context: Context):
    # setup global variables
    setup = context.config.userdata
    context.os = setup["os"]
    context.env = get_env_data(os=setup["os"])

    # setup page_objects
    if context.os.upper() == "ANDROID":
        context.driver = get_driver(os=context.os, browserstack_config=context.env["browserstack"])

        context.android_login_page = AndroidLoginPage(context=context)
        context.android_question_page = AndroidQuestionPage(context=context)
        context.android_question_ask_page = AndroidAskQuestionPage(context=context)
        context.android_markets_list_page = AndroidMarketsListPage(context=context)
        context.android_user_profile_page = AndroidUserProfilePage(context=context)
        context.android_search_by_image_page = AndriodSearchByImagePage(context=context)
        context.android_search_by_text_page = AndriodSearchByTextPage(context=context)
        context.android_main_menu_section = AndriodMainMenuSection(context=context)


def before_feature(context: Context, feature: Feature):
    for scenario in feature.scenarios:
        patch_scenario_with_autoretry(scenario, max_attempts=3)


def before_scenario(context: Context, scenario: Scenario):
    # setup page_objects
    if context.os.upper() == "IOS":
        context.driver = get_driver(os=context.os, browserstack_config=context.env["browserstack"])

        context.ios_login_page = IosLoginPage(context=context)
        context.ios_question_page = IosQuestionPage(context=context)
        context.ios_question_ask_page = IosAskQuestionPage(context=context)
        context.ios_markets_list_page = IosMarketsListPage(context=context)
        context.ios_user_profile_page = IosUserProfilePage(context=context)
        context.ios_main_menu_section = IosMainMenuSection(context=context)
        context.ios_search_by_image_page = IosSearchByImagePage(context=context)
        context.ios_search_by_text_page = IosSearchByTextPage(context=context)


def after_scenario(context: Context, scenario: Scenario):
    if scenario.status == "failed":
        attach(context.driver.get_screenshot_as_png(), attachment_type=attachment_type.PNG)

    if context.os.upper() == "ANDROID":
        context.driver.reset()
    elif context.os.upper() == "IOS":
        context.driver.quit()


def after_all(context: Context):
    if context.os.upper() == "ANDROID":
        context.driver.quit()
