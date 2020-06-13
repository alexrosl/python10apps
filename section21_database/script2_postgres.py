import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='10apps' user='postgres' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='10apps' user='postgres' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()


# insert("Coffee Glass", 10, 5)


def view():
    conn = psycopg2.connect("dbname='10apps' user='postgres' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect("dbname='10apps' user='postgres' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = psycopg2.connect("dbname='10apps' user='postgres' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()

insert("Copy", 10, 29.9)
insert("Waiter Glass", 10, 29.9)
update("Waiter Glass", 111, 19.2)
delete("Wine Glass")
rows = view()
for row in rows:
    print(row)
