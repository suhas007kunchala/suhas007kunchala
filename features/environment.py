import logging
from behave.log_capture import LoggingCapture
import behave.configuration
from helpers.Paths import projectpaths
from helpers.helper_base import Helperbase
from behave.configuration import Configuration


def before_feature(context, feature):
    hlbs = Helperbase()
    context.drive = hlbs


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    context.drive.closebrowser()
    context.drive.stopplaywright()


def before_all(context):
    pass


def after_all(context):
    pass
