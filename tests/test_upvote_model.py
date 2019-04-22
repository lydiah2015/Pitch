from app.models import Upvote
from unittest import TestCase

class TestUpvoteModel(TestCase):
    def setUp(self):
        self.upvote=Upvote()

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.upvote,Upvote)
