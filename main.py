import sqlite3
import os
import sys

SCHEMA_PATH = "schema.sql"
DEFAULT_DB_PATH = "db/security.db"
DEFAULT_QUERY_PATH = "queries/login_by_date.sql"  # must be a file, not a directory

def create_db(conn):
    with open(SCHEMA_PATH, "r") as f:
        sql_script = f.read()
    conn.executescript(sql_script)
    print("[✔] Database created and populated from schema.sql")

def run_sql_file(conn, sql_path):
    sql_path = os.path.normpath(sql_path)
    if not os.path.isfile(sql_path):
        print(f"[!] Query file not found: {sql_path}")
        return

    with open(sql_path, "r") as f:
        sql = f.read()

    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN;")
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("[i] Query executed but returned no results.")
        cursor.execute("END;")
    except sqlite3.Error as e:
        print(f"[!] SQL Error: {e}")
        cursor.execute("ROLLBACK;")

def main():
    db_path = DEFAULT_DB_PATH
    query_path = DEFAULT_QUERY_PATH

    # Parse CLI arguments for db and query paths
    for arg in sys.argv[1:]:
        if arg.endswith(".db"):
            db_path = os.path.normpath(arg)
        elif arg.endswith(".sql"):
            query_path = os.path.normpath(arg)

    db_dir = os.path.dirname(db_path)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    db_exists = os.path.exists(db_path)
    with sqlite3.connect(db_path) as conn:
        if not db_exists:
            print(f"[+] '{db_path}' not found. Creating new database...")
            create_db(conn)
        else:
            print(f"[+] Using existing database at '{db_path}'")

        print(f"[+] Running query from '{query_path}'")
        run_sql_file(conn, query_path)

if __name__ == "__main__":
    main()
