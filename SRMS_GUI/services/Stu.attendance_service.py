from db.connection import get_connection

def view_attendance(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("EXEC dbo.ViewAttendance ?", (username,))
    rows = cur.fetchall()
    conn.close()
    return rows
