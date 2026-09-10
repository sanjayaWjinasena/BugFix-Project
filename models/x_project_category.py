# -*- coding: utf-8 -*-
from odoo import fields, models


class XProjectCategory(models.Model):
    """Studio-ported custom model x_project_category."""
    _name = 'x_project_category'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Project Category'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Category')
    x_studio_category_group = fields.Many2one('x_project_category_gro', string='Category Group')
    x_studio_category_name = fields.Char(string='Category Name')
    x_studio_claimability = fields.Selection([('None', 'None'), ('Claimable', 'Claimable'), ('Non-Claimable', 'Non-Claimable')], string='Claimability')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_transaction_type = fields.Selection([('Item', 'Item'), ('Expense', 'Expense'), ('Fee', 'Fee'), ('Hour', 'Hour')], string='Transaction Type', readonly=True)
