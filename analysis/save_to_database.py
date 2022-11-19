from dataclasses import astuple
import sqlite3
from sys import argv

from db_utils import INSERT_QUERY, JobData, parse_data, parse_file


def main():
    conn = get_connection('./stubdb.sqlite')
    cur = conn.cursor()
    data = parse_file(get_file_name())
    for item in data:
        try:
            print('salvando item')
            save(conn, cur, item)
        except Exception:
            print('não dei pra salvar esse dado')
    conn.close()


def save(conn, cur, item):
    job = parse_data(item)
    print('item parseado')
    save_on_db(job, cur)
    conn.commit()


def save_on_db(job: JobData, cursor: sqlite3.Cursor):
    cursor.execute(
        INSERT_QUERY,
        astuple(job)
    )


def get_connection(db_name: str):
    return sqlite3.connect(db_name)


def get_file_name():
    if len(argv) >= 2:
        return argv[1]
    print('passa o nome do arquivo caramba\nExemplo:\nsave_to_database.py nome')
    exit(1)


main()

