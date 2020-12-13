from invoke import task


@task
def run(context, os="", tags=""):
    """
    Run tests without allure report generating. Used for debug on localhost
    :param context: invoke context object
    :param os: run tests on specific OS (Android, IOS)
    :param tags: run only tests marked by specific tag
    :keyword: '$ invoke run --os=IOS'
    :keyword: '$ invoke run --os=IOS --tags=@authorization'
    """
    if not os:
        print("Parameter '--os=' is required. Chose 'ANDROID' or 'IOS' os (e.g: invoke run --os=ios)")
    elif os.upper() not in ("ANDROID", "IOS"):
        print(f"Unexpected OS '{os.upper()}'. Chose 'ANDROID' or 'IOS' os (e.g: invoke run --os=ios)")
    else:
        behave_cmd = "behave --no-capture"
        if os.upper() == "ANDROID":
            behave_cmd = f"{behave_cmd} -D os={os} --tags=@android"
        if os.upper() == "IOS":
            behave_cmd = f"{behave_cmd} -D os={os} --tags=@ios"
        if tags != "":
            behave_cmd = f"{behave_cmd} --tags={tags}"

        print(behave_cmd)
        context.run(behave_cmd)


@task
def run_failed(context, os=""):
    """
    Rerun tests which were failed during previous run. Used for debug on localhost
    :param context: invoke context object
    :param os: run tests on specific OS (Android, IOS)
    :keyword: '$ invoke run-failed'
    :keyword: '$ invoke run-failed --browser=CH --env=STAGE_XF'
    """
    if not os:
        print("Parameter '--os=' is required. Chose 'ANDROID' or 'IOS' os (e.g: invoke run --os=ios)")
    elif os.upper() not in ("ANDROID", "IOS"):
        print(f"Unexpected OS '{os.upper()}'. Chose 'ANDROID' or 'IOS' os (e.g: invoke run --os=ios)")
    else:
        behave_cmd = "behave @rerun.output --no-capture"
        if os.upper() == "ANDROID":
            behave_cmd = f"{behave_cmd} -D os={os} --tags=@android"
        if os.upper() == "IOS":
            behave_cmd = f"{behave_cmd} -D os={os} --tags=@ios"

        print(behave_cmd)
        context.run(behave_cmd)


@task
def run_with_allure(context, os="", tags=""):
    """
    Run tests with html allure report generating. Used for CI/CD pipeline in TeamCity
    :param context: invoke context object
    :param os: run tests on specific OS (Android, IOS)
    :param tags: run only tests marked by specific tag
    :keyword: '$ invoke run-with-allure'
    :keyword: '$ invoke run-with-allure --browser=CH --env=STAGE_XF --tags=@registration'
    """
    if not os:
        print("Parameter '--os=' is required. Chose 'ANDROID' or 'IOS' os (e.g: invoke run --os=ios)")
    elif os.upper() not in ("ANDROID", "IOS"):
        print(f"Unexpected OS '{os.upper()}'. Chose 'ANDROID' or 'IOS' os (e.g: invoke run --os=ios)")
    else:
        behave_cmd = "behave -f allure -o artifacts -f teamcity -f pretty --no-capture"
        if os.upper() == "ANDROID":
            behave_cmd = f"{behave_cmd} -D os={os} --tags=@android"
        if os.upper() == "IOS":
            behave_cmd = f"{behave_cmd} -D os={os} --tags=@ios"
        if tags != "":
            behave_cmd = f"{behave_cmd} --tags={tags}"

        print(behave_cmd)
        context.run(behave_cmd)


@task
def lint(context):
    """
    Run black code formatter and prospector static code analyser against all repository
    :param context: invoke context object
    """
    black_cmd = "black . -l 120"
    prospector_cmd = "prospector"
    context.run(black_cmd)
    context.run(prospector_cmd)
