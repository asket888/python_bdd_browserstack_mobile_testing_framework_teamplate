from behave import step
from behave.runner import Context
from hamcrest import assert_that, contains_string, is_


@step('[Android] I search for "{text}" in the searching field')
def step_impl(context: Context, text: str):
    context.android_search_by_text_page.fill_search_by_text_field(text=text)


@step("[Android] Search results block is presented on the page")
def step_impl(context: Context):
    assert_that(context.android_search_by_text_page.check_if_search_results_block_is_presented(), is_(True))


@step('[Android] "{text}" keyword is presented in all search results on the page')
def step_impl(context: Context, text: str):
    search_results = context.android_search_by_text_page.get_all_search_results()
    for result in search_results:
        assert_that(result.lower(), contains_string(text.lower()))


@step("[Android] I click first question in the list on Search page")
def step_impl(context: Context):
    context.android_search_by_text_page.click_first_question_link()


@step('[Android] I click "Ask question" button on Search page')
def step_impl(context: Context):
    context.android_search_by_text_page.click_ask_question_button()
