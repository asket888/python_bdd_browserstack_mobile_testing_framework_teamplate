from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step("[IOS] Search by Image page is presented")
def step_impl(context: Context):
    assert_that(context.ios_search_by_image_page.check_if_scan_and_solve_button_is_presented(), is_(True))


@step('[IOS] I click "Search by text" button')
def step_impl(context: Context):
    context.ios_search_by_image_page.click_search_by_text_button()
