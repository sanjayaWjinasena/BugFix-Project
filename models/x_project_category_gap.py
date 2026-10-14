from odoo import fields, models


class XProjectCategoryGap(models.Model):
    _inherit = 'x_project_category'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Category')
