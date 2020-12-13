from behave import step
from behave.runner import Context


@step("[IOS] I go to test environment as Unlogged user")
def step_impl(context: Context):
    context.ios_main_menu_section.click_navigation_tab(tab_name="Profile")
    context.ios_login_page.click_change_market_button()
    context.ios_markets_list_page.change_to_test_market()


@step("[IOS] I go to test environment as Logged user")
def step_impl(context: Context):
    context.ios_main_menu_section.click_navigation_tab(tab_name="Profile")
    context.ios_login_page.click_change_market_button()
    context.ios_markets_list_page.change_to_test_market()
    context.ios_main_menu_section.click_navigation_tab(tab_name="Profile")
    context.ios_login_page.login_with_correct_parameters()
    context.ios_main_menu_section.click_navigation_tab(tab_name="Ask")


@step('[IOS] I click "{tab_name}" tab')
def step_impl(context: Context, tab_name: str):
    context.ios_main_menu_section.click_navigation_tab(tab_name=tab_name)
