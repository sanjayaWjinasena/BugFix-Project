# -*- coding: utf-8 -*-
from odoo import fields, models


class XDepartments(models.Model):
    """Studio-ported custom model x_departments."""
    _name = 'x_departments'
    _description = 'Departments'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_code = fields.Char(string='Code')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_user_id = fields.Many2one('res.users', string='Responsible')
