from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step("[IOS] question page is presented")
def step_impl(context: Context):
    assert_that(context.ios_question_page.check_if_question_page_is_presented(), is_(True))
