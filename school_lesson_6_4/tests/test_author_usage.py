from odoo.tests.common import TransactionCase

class TestAuthorUsage(TransactionCase):

    def setUp(self):
        super(TestAuthorUsage, self).setUp()
        # Use the common test record for author Mark Twain
        self.author_mark_twain = self.env.ref('school_lesson_6_4.author_mark_twain')

    def test_usage_of_author(self):
        # Test to check the usage of author Mark Twain in other tests
        self.assertEqual(self.author_mark_twain.first_name, 'Mark')
        self.assertEqual(self.author_mark_twain.second_name, 'Twain')
