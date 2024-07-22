from odoo.tests.common import TransactionCase, tagged


@tagged('odooschool')
class TestLibraryBookMethods(TransactionCase):

    def setUp(self):
        super(TestLibraryBookMethods, self).setUp()
        # Create a test author
        self.author_mark_twain = self.env['library.author'].create({
            'first_name': 'Mark',
            'second_name': 'Twain'
        })
        # Create a test book
        self.book = self.env['library.book'].create({
            'name': 'The Adventures of Tom Sawyer',
            'author_id': self.author_mark_twain.id
        })

    def test_action_scrap_book(self):
        # Check initial state of the book
        self.assertTrue(self.book.is_active, "Book should be active initially.")

        # Call the action_scrap_book method
        self.book.action_scrap_book()

        # Check the state of the book after calling the method
        self.assertFalse(self.book.is_active, "Book should be inactive after scrapping.")
