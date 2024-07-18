from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Book Category'

    name = fields.Char(
        string='Category',
        required=True
    )
    description = fields.Text(string='Description')
