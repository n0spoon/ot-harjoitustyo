from db_connection import get_db_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Calculations;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Calculations (
            id INTEGER PRIMARY KEY, result TEXT
        );
    ''')

    connection.commit()


def init_db():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    init_db()
