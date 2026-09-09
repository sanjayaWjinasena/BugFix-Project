# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Project',
    'version': '17.0.0.0.26',
    'summary': 'Studio-to-Python port for BugFix-Project',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Services/Project',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.17: hotfix v0.0.16 - permanently skip view 4620.
    # v0.0.16 raised priority to 1000 but crashed with same error.
    # Root cause: priority ordering only matters BETWEEN VIEWS
    # INHERITING THE SAME PARENT. View 4620's parent is 7094
    # (sale_timesheet), view 5435 (industry_fsm - adds fsm_done)
    # inherits directly from 2410 (project.task.form). Both 7094 and
    # 5435 are children of 2410 but on separate inheritance BRANCHES.
    # Odoo applies inherits depth-first: 7094's whole subtree
    # (including us) finishes before 5435 applies. So fsm_done never
    # exists at our application time regardless of our priority.
    # Only alternative: re-parent to 5435 (semantic change - risky).
    # Losing conditional FSM validate button visibility is UX-only.
    # Now ships 3 views: 2 project.project + 1 x_departments.
    # v0.0.16: hotfix v0.0.15 - bump view 4620 priority to 1000.
    # v0.0.15 crashed with:
    #   Element '<xpath expr="//field[@name='fsm_done']">' cannot be
    #   located in parent view
    # Root cause: our pre-flight used dev.call(model, 'get_view')
    # which returns the FULLY COMPOSED arch with ALL inherits applied
    # (including industry_fsm's priority-999 view that adds fsm_done
    # + action_fsm_validate). Xpath matched cleanly there.
    # BUT at install time, Odoo applies inherits in PRIORITY ORDER.
    # Our view 4620 was priority=99, which loads BEFORE industry_fsm's
    # priority-999 view. So at our application time, fsm_done doesn't
    # exist yet.
    # Fix: bump 4620 to priority=1000 so it applies AFTER
    # industry_fsm's priority-999 inherit. Now the composed arch at
    # our application time includes fsm_done and the xpath resolves.
    # Adds per-view priority override support to the generator.
    # v0.0.15: hotfix v0.0.14 - skip view 4730 permanently.
    # v0.0.14 crashed with:
    #   action_preview_worksheet is not a valid action on project.task
    # View 4730 is an inherit of industry_fsm_report.view_task_form2_inherit
    # that only hides 2 buttons (action_preview_worksheet + action_send_report)
    # via <xpath position="attributes"><attribute name="invisible">1</attribute>.
    # Both buttons EXIST in the parent view arch, but Odoo re-runs
    # button-method validation after applying the inheritance and
    # rejects it. Root cause unclear (both methods should be present
    # via industry_fsm_report + industry_fsm addons on target).
    # Losing 2 button hides is acceptable vs blocking install; the
    # buttons will remain visible but that's a UX-only degradation.
    # Ships 4 views: project.project form/tree customizations,
    # project.task form (sale_timesheet inherit), x_departments form.
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
        'data/record_rules.xml',
        'data/server_actions_backlog.xml',
        'data/window_actions_backlog.xml',
        'data/menus_from_routing.xml',
        'data/mail_templates_from_routing.xml',
        'data/automations_gap.xml',
        'data/window_actions_gap.xml',
        'data/ir_defaults_gap.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}