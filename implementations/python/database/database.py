import sqlite3

def setup_db():
    conn = sqlite3.connect('application.db')
    return conn.cursor()

def main():
    cur = setup_db()

if __name__ == "__main__":
    main()