from django.test import TestCase
from edc_lab.site_labs import site_labs

from ..labs import lab_profile


class TestLabs(TestCase):

    def setUp(self):
        site_labs._registry = {}
        site_labs.loaded = False
        site_labs.register(
            lab_profile=lab_profile,
            requisition_model='ambition_subject.subjectrequisition')

    def test_(self):
        obj = site_labs.get(lab_profile_name='ambition_subject')
        self.assertEqual(obj, lab_profile)

    def test_lab_profile_model(self):
        obj = site_labs.get(lab_profile_name='ambition_subject')
        self.assertEqual('ambition_subject.subjectrequisition',
                         obj.requisition_model)

    def test_panel_model(self):
        for panel in site_labs.get(lab_profile_name='ambition_subject').panels.values():
            self.assertEqual(
                panel.model, 'ambition_subject.subjectrequisition')
