# -*- coding: utf-8 -*-
from odoo import models, fields

class XProjectGroupsGap(models.Model):
    _inherit = 'x_project_groups'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Project Group')
