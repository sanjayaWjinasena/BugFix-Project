# -*- coding: utf-8 -*-
from odoo import fields, models


class XProjectGroups(models.Model):
    """Studio-ported custom model x_project_groups."""
    _name = 'x_project_groups'
    _description = 'Project Groups'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Project Group')
    x_studio_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')
