from odoo import fields, models


class XProjectCategory(models.Model):
    """Studio-ported custom model project_category."""

    _name = "project_category"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Project Category"

    active = fields.Boolean()
    name = fields.Char(string="Category")
    category_group = fields.Many2one("project_category_gro")
    category_name = fields.Char()
    claimability = fields.Selection(
        [
            ("None", "None"),
            ("Claimable", "Claimable"),
            ("Non-Claimable", "Non-Claimable"),
        ],
    )
    sequence = fields.Integer()
    transaction_type = fields.Selection(
        [("Item", "Item"), ("Expense", "Expense"), ("Fee", "Fee"), ("Hour", "Hour")],
        readonly=True,
    )


class XProjectCategoryGap(models.Model):
    _inherit = "project_category"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Category")
