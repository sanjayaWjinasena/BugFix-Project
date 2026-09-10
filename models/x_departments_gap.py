# -*- coding: utf-8 -*-
from odoo import models, fields

class XDepartmentsGap(models.Model):
    _inherit = 'x_departments'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
