"""Ship Selection-typed defaults via SQL (bypasses XML validation)."""

def migrate(cr, version):
    if not version:
        return
    data = [
        ('project.task', 'x_studio_priority', '"Normal"', ''),
        ('x_project_category', 'x_studio_claimability', '"None"', ''),
        ('project.update', 'x_studio_selection_field_0zgmv', '"Pending"', ''),
    ]
    for model, name, jval, cond in data:
        cr.execute("""
            INSERT INTO ir_default (field_id, json_value, condition, create_uid, create_date, write_uid, write_date)
            SELECT f.id, %s, NULLIF(%s, ''), 1, NOW() AT TIME ZONE 'UTC', 1, NOW() AT TIME ZONE 'UTC'
            FROM ir_model_fields f
            WHERE f.model = %s AND f.name = %s AND NOT EXISTS (
                SELECT 1 FROM ir_default d WHERE d.field_id = f.id AND d.json_value = %s
            )
        """, (jval, cond, model, name, jval))