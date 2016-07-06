# -*- coding: utf-8 -*-
__author__ = 'leemon'
import hashlib
import MySQLdb
from dbutil import *
from config import db_config
db = DB(host=db_config['host'], mysql_user=db_config['user'], mysql_pass=db_config['passwd'], \
                mysql_db=db_config['db'])
class User(object):
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
    def __gen(self,passwd):
        salt="test123456"
        m2 = hashlib.md5()
        m2.update(salt+passwd)
        return m2.hexdigest()
    def check(self):
        sql = "select * from user where username='%s' and password='%s'" % (self.username,self.__gen(self.passwd))
        cur = db.execute(sql)
        if cur.fetchone():
            return True
        else:
            return False
    def update(self,newpasswd):
        sql = "update user set password='%s' where username='%s'" % (self.__gen(newpasswd),self.username)
        db.execute(sql)
        return True
    def add(self):
        if self.username and self.passwd:
            password = self.__gen(self.passwd)
            sql = "insert INTO user(username,password) VALUES ('%s','%s')" % (self.username,password)
            db.execute(sql)
            return True
        else:
            return False
if __name__ == '__main__':
    pass
