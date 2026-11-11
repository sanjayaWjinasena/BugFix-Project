"""Sentinel declaration for project_category_gro so cross-references resolve."""

from odoo import fields, models


class XProjectCategoryGro(models.Model):
    _name = "project_category_gro"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Project Category Group"

    active = fields.Boolean()
    name = fields.Char(string="Category Group")
    category_group_name = fields.Char()
    line_property = fields.Char(string="Line property")
    sequence = fields.Integer()
    transaction_type = fields.Selection(
        [("Item", "Item"), ("Expense", "Expense"), ("Fee", "Fee"), ("Hour", "Hour")],
    )


class XProjectCategoryGroGap(models.Model):
    _inherit = "project_category_gro"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Category Group")
