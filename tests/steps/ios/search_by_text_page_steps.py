from behave import step
from behave.runner import Context
from hamcrest import assert_that, contains_string, is_


@step('[IOS] I search for "{text}" in the searching field')
def step_impl(context: Context, text: str):
    context.ios_search_by_text_page.fill_search_by_text_field(text=text)


@step("[IOS] Search results block is presented on the page")
def step_impl(context: Context):
    assert_that(context.ios_search_by_text_page.check_if_search_results_block_is_presented(), is_(True))


@step('[IOS] "{expected_number:d}" results are presented in search results on the page')
def step_impl(context: Context, expected_number: int):
    search_results = context.ios_search_by_text_page.get_all_search_results()
    assert_that(len(search_results), is_(expected_number))


@step("[IOS] I click first question in the list on Search page")
def step_impl(context: Context):
    context.ios_search_by_text_page.click_first_question_link()


@step('[IOS] I click "Ask question" button on Search page')
def step_impl(context: Context):
    context.ios_search_by_text_page.click_ask_question_button()
