from unittest import TestCase

from mimibot.src.db import db


class TestPickleDB(TestCase):
    def test_db_works(self):
        db.set('foo', 'bar')
        self.assertEqual(db.get('foo'), 'bar')
