# BugFix-Project — views to hand-port

26 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 2320 | form | `x_departments` | Default form view for x_departments | — |
| 2 | 4740 | form | `x_project_category` | Default form view for x_project_category | — |
| 3 | 4743 | form | `x_project_groups` | Default form view for x_project_groups | — |
| 4 | 4931 | gantt | `project.project` | Default gantt view for project.project | — |
| 5 | 2319 | tree | `x_departments` | Default list view for x_departments | — |
| 6 | 4739 | tree | `x_project_category` | Default list view for x_project_category | — |
| 7 | 4742 | tree | `x_project_groups` | Default list view for x_project_groups | — |
| 8 | 2321 | search | `x_departments` | Default search view for x_departments | — |
| 9 | 4741 | search | `x_project_category` | Default search view for x_project_category | — |
| 10 | 4744 | search | `x_project_groups` | Default search view for x_project_groups | — |
| 11 | 6068 | tree | `project.sale.line.employee.map` | Default tree view for ir.model(646,) | — |
| 12 | 2322 | form | `x_departments` | Odoo Studio: Default form view for x_departments customization | Default form view for x_departments |
| 13 | 4746 | tree | `x_project_category` | Odoo Studio: Default list view for x_project_category customization | Default list view for x_project_category |
| 14 | 4747 | tree | `x_project_groups` | Odoo Studio: Default list view for x_project_groups customization | Default list view for x_project_groups |
| 15 | 4748 | form | `project.project` | Odoo Studio: project.project.form customization | project.project.form |
| 16 | 4895 | form | `project.project` | Odoo Studio: project.project.form-button | project.project.form |
| 17 | 5899 | tree | `project.project.stage` | Odoo Studio: project.project.stage.view.tree customization | project.project.stage.view.tree |
| 18 | 4893 | tree | `project.project` | Odoo Studio: project.project.tree customization | project.project.tree |
| 19 | 3019 | form | `project.task` | Odoo Studio: project.task.form customization | project.task.form |
| 20 | 4775 | tree | `project.task` | Odoo Studio: project.task.tree customization | project.task.tree |
| 21 | 4924 | form | `project.update` | Odoo Studio: project.update.view.form customization | project.update.view.form |
| 22 | 4932 | form | `project.update` | Odoo Studio: project.update.view.form_button | project.update.view.form |
| 23 | 4933 | kanban | `project.update` | Odoo Studio: project.update.view.kanban customization | project.update.view.kanban |
| 24 | 4925 | tree | `project.update` | Odoo Studio: project.update.view.tree customization | project.update.view.tree |
| 25 | 4730 | form | `project.task` | Odoo Studio: task.form.inherit | task.form.inherit |
| 26 | 4620 | form | `project.task` | Odoo Studio: view.task.form2.inherit | view.task.form2.inherit |
