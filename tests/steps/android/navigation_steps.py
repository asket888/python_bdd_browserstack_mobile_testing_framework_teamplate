from behave import step
from behave.runner import Context


@step("[Android] I go to test environment as Unlogged user")
def step_impl(context: Context):
    context.android_markets_list_page.go_to_test_market()


@step("[Android] I go to test environment as Logged user")
def step_impl(context: Context):
    context.android_markets_list_page.go_to_test_market()
    context.android_main_menu_section.click_navigation_tab(tab_name="Me")
    context.android_login_page.login_with_correct_parameters()
    context.android_main_menu_section.click_navigation_tab(tab_name="Ask")


@step('[Android] I click "{tab_name}" tab')
def step_impl(context: Context, tab_name: str):
    context.android_main_menu_section.click_navigation_tab(tab_name=tab_name)
