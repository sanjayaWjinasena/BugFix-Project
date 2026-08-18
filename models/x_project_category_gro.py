# -*- coding: utf-8 -*-
"""Sentinel declaration for x_project_category_gro so cross-references resolve."""
from odoo import fields, models


class XProjectCategoryGro(models.Model):
    _name = 'x_project_category_gro'
    _description = 'X Project Category Gro'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Category Group')
    x_studio_category_group_name = fields.Char(string='Category Group Name')
    x_studio_line_property = fields.Char(string='Line property')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_transaction_type = fields.Selection([], string='Transaction Type')
