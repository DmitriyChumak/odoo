from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    category_id = fields.Many2one(
        comodel_name='library.book.category',
        string='Category'
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        default=lambda self: self.env.ref('base.user_admin').id
    )
    # author_id = fields.Many2one(
    #     comodel_name='library.author',
    #     string='Author'
    # )
    #
