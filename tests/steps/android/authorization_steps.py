from behave import step
from behave.runner import Context


@step("[Android] I login to application with correct credentials")
def step_impl(context: Context):
    context.android_login_page.login_with_correct_parameters()
