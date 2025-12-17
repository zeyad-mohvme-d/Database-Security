from db.connection import get_connection

def validate_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "EXEC dbo.usp_ValidateLogin ?, ?",
        username, password
    )

    row = cur.fetchone()
    conn.close()
    return row
