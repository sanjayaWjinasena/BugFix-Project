# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Project',
    'version': '17.0.0.0.10',
    'summary': 'Studio-to-Python port for BugFix-Project',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Services/Project',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v10: added Jinasena_Masterdata_Reporting to depends.
    # x_sales_report_model.py was _name='x_sales_report_model' (duplicate
    # "owner" without dep on the real owner Jinasena_Masterdata_Reporting).
    # Same root cause as BugFix-Sales v54: competing _name declarations
    # caused the registry KeyError on x_studio_journal_items_id.
    # Converted to _inherit; Jinasena_Masterdata_Reporting added here.
    'depends': ['base_setup', 'project', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_departments_studio_ported.xml',
        'views/x_project_category_studio_ported.xml',
        'views/x_project_category_gro_studio_ported.xml',
        'views/x_project_groups_studio_ported.xml',
        'views/x_sales_report_model_studio_ported.xml',
        'views/project_project_studio_ported.xml',
        'views/project_task_studio_ported.xml',
        'views/project_update_studio_ported.xml',
        'views/project_project_stage_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}