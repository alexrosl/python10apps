import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("bookstore/books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book "
                         "(id INTEGER PRIMARY KEY, "
                         "title TEXT, "
                         "author TEXT, "
                         "year INTEGER, "
                         "isbn INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",
                         (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, book_id):
        self.cur.execute("DELETE FROM book WHERE id=?", (book_id,))
        self.conn.commit()

    def update(self, book_id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                         (title, author, year, isbn, book_id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
