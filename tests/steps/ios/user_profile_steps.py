from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step("[IOS] correct user nickname is presented on the header of the page")
def step_impl(context: Context):
    assert_that(context.ios_user_profile_page.check_if_user_nickname_is_presented(), is_(True))
