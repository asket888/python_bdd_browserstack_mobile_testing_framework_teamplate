from behave import step
from behave.runner import Context


@step("[IOS] I login to application with correct credentials")
def step_impl(context: Context):
    context.ios_login_page.login_with_correct_parameters()
