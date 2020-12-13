from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_, contains_string


@step("[Android] question page is presented")
def step_impl(context: Context):
    assert_that(context.android_question_page.check_if_question_page_is_presented(), is_(True))


@step('[Android] "{expected_subject}" subject is presented in question block on Question page')
def step_impl(context: Context, expected_subject: str):
    actual_subject = context.android_question_page.get_question_subject()
    assert_that(actual_subject, is_(expected_subject))


@step('[Android] "{expected_text}" text is presented in question block on Question page')
def step_impl(context: Context, expected_text: str):
    actual_text = context.android_question_page.get_question_text()
    assert_that(actual_text, contains_string(expected_text))


@step("[Android] correct user name is presented in question block on Question page")
def step_impl(context: Context):
    expected_user_name, actual_user_name = context.android_question_page.get_actual_and_expected_question_author()
    assert_that(actual_user_name, contains_string(expected_user_name))
