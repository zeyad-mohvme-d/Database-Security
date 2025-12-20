from db.connection import get_connection

def view_own_profile(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("EXEC dbo.ViewOwnProfile ?", (username,))
    rows = cur.fetchall()
    conn.close()
    return rows
