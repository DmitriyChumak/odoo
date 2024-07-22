from odoo.tests.common import TransactionCase, Form, tagged


@tagged('odooschool')
class TestLibraryBookDefaultGet(TransactionCase):

    def setUp(self):
        super(TestLibraryBookDefaultGet, self).setUp()
        # Create a test author
        self.author_mark_twain = self.env['library.author'].create({
            'first_name': 'Mark',
            'second_name': 'Twain'
        })

    def test_default_get(self):
        # Create a form for the library.book model
        with Form(self.env['library.book']) as f:
            f.name = 'New Book'
            f.author_id = self.author_mark_twain

        new_book = f.save()

        # Check default values
        self.assertEqual(new_book.is_active, True, "Default value for 'is_active' should be True")
        self.assertEqual(new_book.name, 'New Book', "Book name should be 'New Book'")
        self.assertEqual(new_book.author_id, self.author_mark_twain, "Author should be 'Mark Twain'")
