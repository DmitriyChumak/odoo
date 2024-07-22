from odoo.tests.common import TransactionCase

class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        # Create a record for author Mark Twain to use in tests
        self.author_mark_twain = self.env.ref('school_lesson_6_4.author_mark_twain')

    def test_author_creation(self):
        # Test to check the creation of author
        self.assertEqual(self.author_mark_twain.first_name, 'Mark')
        self.assertEqual(self.author_mark_twain.second_name, 'Twain')
