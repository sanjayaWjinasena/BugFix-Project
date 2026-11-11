from odoo import fields, models


class XProjectCategory(models.Model):
    """Studio-ported custom model project_category."""

    _name = "project_category"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Project Category"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Category")
    category_group = fields.Many2one(
        "project_category_gro", string="Category Group"
    )
    category_name = fields.Char(string="Category Name")
    claimability = fields.Selection(
        [
            ("None", "None"),
            ("Claimable", "Claimable"),
            ("Non-Claimable", "Non-Claimable"),
        ],
        string="Claimability",
    )
    sequence = fields.Integer(string="Sequence")
    transaction_type = fields.Selection(
        [("Item", "Item"), ("Expense", "Expense"), ("Fee", "Fee"), ("Hour", "Hour")],
        string="Transaction Type",
        readonly=True,
    )


class XProjectCategoryGap(models.Model):
    _inherit = "project_category"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Category")
