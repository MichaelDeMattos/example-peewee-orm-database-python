# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase('books.db')

class Authors(Model):
    id = IntegerField(primary_key=True)
    name = CharField(null=False)

    class Meta:
        database = db

class Books(Model):
    id = IntegerField(primary_key=True)
    author_id = ForeignKeyField(Authors.id)
    name_book = TextField(null=False)

    class Meta:
        database = db

def insert_author():
    try:

        new_author = Authors(name="Carl Sagan")
        new_author.save()
        print("Insert into table authors Successfully")

    except Exception as ex:
        print("Error: %s" % ex)

def insert_book():
    try:

        new_book = Books(author_id=1, name_book="COSMOS")
        new_book.save()
        print("Insert into table books Successfully")

    except Exception as ex:
        print("Error: %s" % ex)

def select():
    try:

        Authors = Table('authors')
        Books = Table('books')
        query = (Authors
                 .select(Authors.c.name, Books.c.name_book)
                 .from_(Authors, Books)
                 .where(Authors.c.id == Books.c.author_id))

        for row in query.execute(db):
            print("Author:", row['name'], 'Book:', row['name_book'])

    except Exception as ex:
        print("Error: %s" % ex)

def update():
    try:

        Books = Table('books')
        query = (Books
                 .update({Books.c.name_book: "CONTACT"})
                 .where(Books.c.id == 1))
        query.execute(db)
        print("Name book update Successfully")

    except Exception as ex:
        print("Error: %s" % ex)

def delete():
    try:

        Books.delete().where(Books.id == 1).execute()
        print("Book deleted Successfully")

    except Exception as ex:
        print("Error: %s" % ex)

if __name__ == "__main__":
    db.create_tables([Authors, Books])
    """
    Execute as funções na ordem a seguir:
    # insert_author()
    # insert_book()
    # select()
    # update()
    # delete()
    """

