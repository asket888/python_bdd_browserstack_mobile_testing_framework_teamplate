from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step('[IOS] "Ask your question" page is presented')
def step_impl(context: Context):
    assert_that(context.ios_question_ask_page.check_if_ask_question_page_is_presented(), is_(True))


@step('[IOS] "Asked question" page is presented')
def step_impl(context):
    assert_that(context.ios_question_ask_page.check_if_asked_question_page_is_presented(), is_(True))


@step('[IOS] I add "{text}" text and {number:d} random symbols to the text block on Add Question page')
def step_impl(context: Context, text: str, number: int):
    context.ios_question_ask_page.fill_text_field_on_ask_question_page(text=text, symbols_num=number)


@step('[IOS] I select "{subject_name}" subject in the Subjects list')
def step_impl(context: Context, subject_name: str):
    context.ios_question_ask_page.select_subject(subject_name=subject_name.upper())


@step('[IOS] I click "Ask question" button on Add Question page')
def step_impl(context: Context):
    context.ios_question_ask_page.click_submit_button()


@step('[IOS] I choose "Ask Community" on Add Question page')
def step_impl(context):
    context.ios_question_ask_page.click_ask_community_on_who_you_want_to_ask_popup()
