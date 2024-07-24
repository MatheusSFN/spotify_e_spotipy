import sqlite3

def conn_db():
    con = sqlite3.connect('spotify.db')
    cur = con.cursor()
    return con, cur

def drop_tables():
    con, cur = conn_db()
    con.execute('DROP TABLE IF EXISTS artists')
    cur.execute('DROP TABLE IF EXISTS albuns')
    cur.execute('DROP TABLE IF EXISTS musicas')
    con.commit()
    con.close()

#Para armazenar dados do tipe BOOLEAN no SQLite, é necessário armazenar como INTEGER (0=False, 1=True) ou TEXT ('TRUE', 'FALSE')
#Mas é necessário realizar um check na colunas para garantir os valores inseridos
#EX: CREATE TABLE boolean_test (
#           bool_int BOOLEAN CHECK(bool_int IN (0, 1)),
#           bool_text TEXT CHECK(typeof(bool_text) = "text" AND bool_text IN ('TRUE', 'FALSE'))
#)
def create_tables():
    con, cur = conn_db()
    cur.execute('''CREATE TABLE IF NOT EXISTS artists (name TEXT, id TEXT primary key, type TEXT, genres TEXT, popularity INTEGER, followers INTEGER)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS albuns (name TEXT, id TEXT primary key, type TEXT, genres TEXT, popularity INTEGER, release_date TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS musicas (name TEXT, id TEXT primary key, type TEXT, genres TEXT, popularity INTEGER, release_date TEXT)''')
    con.commit()
    con.close()

def insert_values(table_name, tuple_values):
    con, cur = conn_db()
    cur.execute(f'INSERT INTO "{table_name}" VALUES {tuple_values}')
    con.commit()
    con.close()

def main():
    drop_tables()
    create_tables()

if __name__ == '__main__':
    main()

    