from odoo import fields, models


class XDepartments(models.Model):
    """Studio-ported custom model departments."""

    _name = "departments"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Departments"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")
    sequence = fields.Integer(string="Sequence")
    user_id = fields.Many2one("res.users", string="Responsible")


class XDepartmentsGap(models.Model):
    _inherit = "departments"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
