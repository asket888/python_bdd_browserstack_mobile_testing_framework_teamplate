from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step("[Android] correct user nickname is presented on the header of the page")
def step_impl(context: Context):
    expected_user_name, actual_user_name = context.android_user_profile_page.get_actual_and_expected_user_nicknames()
    assert_that(actual_user_name, is_(expected_user_name))
