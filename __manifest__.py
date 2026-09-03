# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Project',
    'version': '17.0.0.0.14',
    'summary': 'Studio-to-Python port for BugFix-Project',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Services/Project',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.14: hotfix v0.0.13 - cross-module xmlid refs stripped.
    # v0.0.13 view 4748 arch had 7 stat-buttons targeting actions
    # pinned to modules that DEPEND ON Project (BugFix-Accounting,
    # BugFix-Sales) or don't exist (studio_customization). Odoo
    # rejected them at load-time:
    #   Invalid xmlid studio_customization.cash_advance_bills_...
    # Root cause: BugFix-Accounting depends on BugFix-Project,
    # so Accounting's xmlids aren't in the registry when Project
    # loads. BugFix-Sales is a peer (no dep either way) so its
    # xmlids also unreliable at Project load-time.
    # Fix: generator's action-ref converter now checks that the
    # resolved xmlid's module is in Project's own transitive
    # depends chain (BugFix-Project + Jinasena_Masterdata_Reporting +
    # standard Odoo). References to any other module get STRIPPED
    # with an explanatory comment inline.
    # Net: 7 stat-buttons removed from project.project form
    # customization inherit (2115 Gross Margin / 2120 Month End /
    # 2195 Line Items + 4 cash-advance workflow shortcuts).
    # Standard project.project form buttons remain intact.
    # v0.0.13: close remaining Project migration gaps.
    #   Fields (8 gap -> 0):
    #     Added _inherit = ['mail.thread', 'mail.activity.mixin'] to
    #     x_departments, x_project_category, x_project_category_gro,
    #     x_project_groups. Odoo auto-creates the 8 activity_* fields
    #     matching CDB.
    #   Views (13/13 -> 18/20 shipped, 2 SKIPPED with all xpaths
    #     unresolvable on target after addon-stack drift):
    #     * 5 Studio priority=99 inherits shipped:
    #       - project.project form (Studio button block)
    #       - project.project tree customization
    #       - project.task form customization
    #       - x_departments form customization
    #     * 2 SKIPPED (4895 project.project form-button and
    #       4775 project.task tree - all xpaths dropped by
    #       pre-flight validation against target's composed arch).
    #   New file: views/studio_ported_7_views.xml.
    # Full pre-flight applied: xpath resolution, orphan field strip
    # (reverse-deps rule), modifier sentinel injection, numeric
    # action ref conversion.
    # v0.0.12: rename module label to match the other companion
    # modules ("Jinasena : Module : Project"), add the shared
    # Jinasena icon at static/description/icon.png (byte-identical
    # copy from BugFix-Sales / BugFix-Purchase / etc).
    # v0.0.11: close remaining server-action + window-action gap.
    # Deep dedup on cross-module audit:
    #   Server actions: 5 -> 9 shipped (100% effective).
    #     4 truly-new state=code Studio cash-advance workflow actions
    #     on project.project (Create/Issue/Settle Cash Advance +
    #     Month End Entries). 7 TRUE dups + 3 ir_cron skipped.
    #   Window actions: 8 -> 12 shipped (100% effective).
    #     3 look-alikes with Studio-specific domains (Assigned Tasks,
    #     Tasks, Project Sharing with project_id/active_id filters) +
    #     1 truly-new (Project Category Group on custom model).
    #     28 verified TRUE dups skipped.
    # New files: data/server_actions_v2.xml + data/window_actions.xml.
    # v0.0.10: added Jinasena_Masterdata_Reporting to depends.
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
        'data/server_actions_v2.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'data/window_actions.xml',
        'views/x_departments_studio_ported.xml',
        'views/x_project_category_studio_ported.xml',
        'views/x_project_category_gro_studio_ported.xml',
        'views/x_project_groups_studio_ported.xml',
        'views/x_sales_report_model_studio_ported.xml',
        'views/project_project_studio_ported.xml',
        'views/project_task_studio_ported.xml',
        'views/project_update_studio_ported.xml',
        'views/project_project_stage_studio_ported.xml',
        'views/studio_ported_7_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}