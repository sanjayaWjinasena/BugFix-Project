from odoo import fields, models


class XProjectGroups(models.Model):
    """Studio-ported custom model project_groups."""

    _name = "project_groups"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Project Groups"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Project Group")
    accounting_name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence")


class XProjectGroupsGap(models.Model):
    _inherit = "project_groups"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Project Group")
