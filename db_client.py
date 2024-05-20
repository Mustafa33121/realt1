import sqlite3
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def get_conn():
    conn = sqlite3.connect('flat.db')
    return conn


def create_table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS flat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flat_id TEXT unique,
    title TEXT,
    price INTEGER,
    image TEXT,
    description TEXT,
    room TEXT,
    square TEXT,
    year TEXT,
    floor TEXT,
    type_house TEXT,
    region TEXT,
    city TEXT,
    street TEXT,
    district TEXT,
    coordinate TEXT
    ) 
    """)

    conn.close()


def insert_flat(flat: dict) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO flat(
    flat_id,
    title,
    price,
    image,
    description,
    room,
    square,
    year,
    floor,
    type_house,
    region,
    city,
    street,
    district,
    coordinate
    ) VALUES (
    :flat_id,
    :title,
    :price,
    :image,
    :description,
    :room,
    :square,
    :year,
    :floor,
    :type_house,
    :region,
    :city,
    :street,
    :district,
    :coordinate
    ) ON CONFLICT (flat_id) DO UPDATE SET price = :price
    """, flat)

    conn.commit()

    conn.close()


def get_data(query: str, params=None):
    conn = get_conn()
    cur = conn.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    res = cur.fetchall()


    conn.close()

    return res

if __name__ == '__main__':
    q = """SELECT * FROM flat"""
    flats = get_data(q)
    print(flats)
    print(__file__)


