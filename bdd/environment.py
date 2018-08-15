#!usr/bin/python3
# -*- coding: UTF-8 -*-

import os, time

import faker, splinter
from behave.log_capture import capture

import config

@capture
def before_all(context):
    # Add fake factory
    context.fake = faker.Faker()

    # Add logging
    context.config.setup_logging()

    # Add base url from config
    context.base_url = config.url

    # Dir to output test artifacts
    context.artifacts_dir = 'artifacts'

@capture
def before_scenario(context, scenario):

    # Initialize browser and add driver to global context
    context.browser = splinter.Browser(driver_name=os.getenv('BROWSER', 'firefox'))


@capture
def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.jpg')
        context.browser.driver.save_screenshot(scenario_file_path)

    context.browser.quit()


def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)

# from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values
# from behave4cmd0.setup_command_shell import setup_command_shell_processors4behave
# import platform
# import sys
# import six

# # -- MATCHES ANY TAGS: @use.with_{category}={value}
# # NOTE: active_tag_value_provider provides category values for active tags.
# python_version = "%s.%s" % sys.version_info[:2]
# active_tag_value_provider = {
#     "python2": str(six.PY2).lower(),
#     "python3": str(six.PY3).lower(),
#     "python.version": python_version,
#     # -- python.implementation: cpython, pypy, jython, ironpython
#     "python.implementation": platform.python_implementation().lower(),
#     "pypy":    str("__pypy__" in sys.modules).lower(),
#     "os":      sys.platform,
# }
# active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)

# # -----------------------------------------------------------------------------
# # HOOKS:
# # -----------------------------------------------------------------------------
# def before_all(context):
#     # -- SETUP ACTIVE-TAG MATCHER (with userdata):
#     # USE: behave -D browser=safari ...
#     setup_active_tag_values(active_tag_value_provider, context.config.userdata)
#     setup_python_path()
#     setup_context_with_global_params_test(context)
#     setup_command_shell_processors4behave()

# def before_feature(context, feature):
#     if active_tag_matcher.should_exclude_with(feature.tags):
#         feature.skip(reason=active_tag_matcher.exclude_reason)

# def before_scenario(context, scenario):
#     if active_tag_matcher.should_exclude_with(scenario.effective_tags):
#         scenario.skip(reason=active_tag_matcher.exclude_reason)

# # -----------------------------------------------------------------------------
# # SPECIFIC FUNCTIONALITY:
# # -----------------------------------------------------------------------------
# def setup_context_with_global_params_test(context):
#     context.global_name = "env:Alice"
#     context.global_age  = 12

# def setup_python_path():
#     # -- NEEDED-FOR: formatter.user_defined.feature
#     import os
#     PYTHONPATH = os.environ.get("PYTHONPATH", "")
# os.environ["PYTHONPATH"] = "."+ os.pathsep + PYTHONPATH


# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
# from behave import fixture, use_fixture
# from selenium.webdriver import Firefox

# @fixture
# def browser_firefox(context):
#     # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
#     context.browser = Firefox()
#     yield context.browser
#     # -- CLEANUP-FIXTURE PART:
#     context.browser.quit()

# def before_all(context):
#     use_fixture(browser_firefox, context)
#     # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.

# # -- FILE: features/environment.py
# # USE: behave -D BEHAVE_DEBUG_ON_ERROR         (to enable  debug-on-error)
# # USE: behave -D BEHAVE_DEBUG_ON_ERROR=yes     (to enable  debug-on-error)
# # USE: behave -D BEHAVE_DEBUG_ON_ERROR=no      (to disable debug-on-error)

# BEHAVE_DEBUG_ON_ERROR = False

# def setup_debug_on_error(userdata):
#     global BEHAVE_DEBUG_ON_ERROR
#     BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")

# def before_all(context):
#     setup_debug_on_error(context.config.userdata)

# def after_step(context, step):
#     if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
#         # -- ENTER DEBUGGER: Zoom in on failure location.
#         # NOTE: Use IPython debugger, same for pdb (basic python debugger).
#         import ipdb
#         ipdb.post_mortem(step.exc_traceback)