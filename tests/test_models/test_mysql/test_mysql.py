#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
import MySQLdb
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the db system """

    def test_create(self):
        """ Test the creation of the database """
        # get the user and password from the environment variables
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        my_sqldb = os.getenv('HBNB_MYSQL_DB')

        db = MySQLdb.connect(host="localhost", port=3306, user=user,
                             passwd=pwd, db=my_sqldb)
        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()
        self.assertEqual(len(rows), 0)
        cur.close()
        db.close()
