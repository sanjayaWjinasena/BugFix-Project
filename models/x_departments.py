from odoo import fields, models


class XDepartments(models.Model):
    """Studio-ported custom model x_departments."""

    _name = "x_departments"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Departments"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    x_studio_code = fields.Char(string="Code")
    description = fields.Char(string="Description")
    sequence = fields.Integer(string="Sequence")
    x_studio_user_id = fields.Many2one("res.users", string="Responsible")


class XDepartmentsGap(models.Model):
    _inherit = "x_departments"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
