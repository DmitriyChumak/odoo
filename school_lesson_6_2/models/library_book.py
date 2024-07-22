from odoo import models, fields, api

class LibraryBook(models.Model):
    _inherit = 'library.book'

    author_id = fields.Many2one(
        comodel_name='library.author',
        string='Author'
    )

    @api.model
    def default_get(self, fields_list):
        res = super(LibraryBook, self).default_get(fields_list)
        res.update({
            'is_active': True,
        })
        return res

    def action_scrap_book(self):
        for book in self:
            book.is_active = False
