# -*- coding: utf-8 -*-
from odoo import models, fields

class XProjectCategoryGroGap(models.Model):
    _inherit = 'x_project_category_gro'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Category Group')
