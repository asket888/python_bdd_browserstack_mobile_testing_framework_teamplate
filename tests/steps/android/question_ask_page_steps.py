from behave import step
from behave.runner import Context
from hamcrest import assert_that, is_


@step('[Android] "Ask your question" page is presented')
def step_impl(context: Context):
    assert_that(context.android_question_ask_page.check_if_ask_question_page_is_presented(), is_(True))


@step('[Android] I add "{text}" text and {number:d} random symbols to the text block on Add Question page')
def step_impl(context: Context, text: str, number: int):
    context.android_question_ask_page.fill_text_field_on_ask_question_page(text=text, symbols_num=number)


@step('[Android] I click "Ask question" button on Add Question page')
def step_impl(context: Context):
    context.android_question_ask_page.click_submit_button()


@step("[Android] I select first subject in the Subjects list")
def step_impl(context: Context):
    context.android_question_ask_page.click_subject_button()
