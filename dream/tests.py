from django.test import TestCase

# Create your tests here.
import random
from django.test import TestCase
from .models import Participant


class participantModelUnitTestCase(TestCase):
    def setUp(self):
        self.participant = Participant.objects.create(
            child_name = 'Angel Umwiza',
            address = 'Namugongo',
            age_group = '19-24',
            hiv_status = 'Hiv_Status',
            date_of_birth = '24/6/2000',
            schooling_status = 'Not Applicable',
        )

    def test_participant_model(self):
        data = self.participant
        self.assertIsInstance(data, Participant)
