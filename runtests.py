#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join


app_name = 'ambition_labs'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    SUBJECT_VISIT_MODEL="ambition_subject.subjectvisit",
    ADVERSE_EVENT_ADMIN_SITE="ambition_ae_admin",
    ADVERSE_EVENT_APP_LABEL="ambition_ae",
    EDC_BOOTSTRAP=3,
    EDC_RANDOMIZATION_LIST_MODEL="ambition_rando.randomizationlist",
    EDC_RANDOMIZATION_LIST_FILE=join(
        base_dir, app_name, "tests", "etc", "randomization_list.csv"),
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_crypto_fields.apps.AppConfig',
        'django_revision.apps.AppConfig',
        'edc_lab.apps.AppConfig',
        'edc_protocol.apps.AppConfig',
        'edc_device.apps.AppConfig',
        'edc_identifier.apps.AppConfig',
        "edc_sites.apps.AppConfig",
        'ambition_labs.apps.AppConfig',
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    # use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=True, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
