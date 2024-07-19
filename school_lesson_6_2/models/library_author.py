from odoo import models, fields, api

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(
        string='Name',
        required=True
    )
    biography = fields.Text(string='Biography')
    date_added = fields.Datetime(
        string='Date Added',
        default=fields.Datetime.now
    )

    @api.model
    def create(self, vals):
        vals['date_added'] = fields.Datetime.now()
        return super(LibraryAuthor, self).create(vals)
