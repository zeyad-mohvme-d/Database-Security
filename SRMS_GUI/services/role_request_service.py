from db.connection import get_connection

def submit_role_upgrade_request(username, requested_role, reason):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "EXEC dbo.SubmitRoleUpgradeRequest ?, ?, ?",
        (username, requested_role, reason)
    )
    conn.commit()
    conn.close()
