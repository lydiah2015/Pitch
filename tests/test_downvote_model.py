from app.models import Downvote
from unittest import TestCase

class TestDownvoteModel(TestCase):
    def setUp(self):
        self.downvote=Downvote()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.downvote,Downvote)