from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Book Category'

    name = fields.Char(
        string='Category',
        required=True
    )
    description = fields.Text(string='Description')
    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name= 'category_id',
        string='Books'
    )
