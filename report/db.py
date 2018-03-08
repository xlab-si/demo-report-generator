import psycopg2

"""
Module with database related functionality.
"""


class Database(object):
    def __init__(self, host, port, user, password, dbname):
        # http://initd.org/psycopg/docs/module.html#psycopg2.connect
        self.connection = psycopg2.connect(
            host=host, port=port, user=user, password=password, dbname=dbname
        )

    def execute(self, query, variables=None):
        # http://initd.org/psycopg/docs/usage.html#with-statement
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(query, vars=variables)
                # http://initd.org/psycopg/docs/cursor.html#cursor.fetchall
                return cursor.fetchall()
