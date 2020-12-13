from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step("[Android] Search by Image page is presented")
def step_impl(context: Context):
    assert_that(context.android_search_by_image_page.check_if_search_by_image_page_is_presented(), is_(True))


@step('[Android] I click "Search by text" button')
def step_impl(context: Context):
    context.android_search_by_image_page.click_search_by_text_button()
