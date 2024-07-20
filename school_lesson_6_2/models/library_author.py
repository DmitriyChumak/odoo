from odoo import models, fields, api
from datetime import timedelta

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Author Name', required=True)
    biography = fields.Text(string='Biography')
    create_date = fields.Datetime(string='Creation Date', default=fields.Datetime.now)
    recent_author = fields.Boolean(compute='_compute_recent_author', store=True)

    @api.depends('create_date')
    def _compute_recent_author(self):
        for record in self:
            recent_date = fields.Datetime.now() - timedelta(days=30)
            record.recent_author = record.create_date >= recent_date
