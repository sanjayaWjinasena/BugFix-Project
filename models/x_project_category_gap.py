# -*- coding: utf-8 -*-
from odoo import models, fields

class XProjectCategoryGap(models.Model):
    _inherit = 'x_project_category'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Category')
