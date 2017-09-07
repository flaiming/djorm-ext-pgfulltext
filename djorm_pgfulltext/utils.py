import psycopg2

from django.db import connection
from django.utils.text import force_text


def adapt(text):
    a = psycopg2.extensions.adapt(force_text(text))
    if connection.connection is None:
        # re-initialize connection
        connection.cursor().close()
    a.prepare(connection.connection)
    return a
