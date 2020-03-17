"""
    服务端
    数据处理部分
"""

import pymysql

class Database:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root"
        self.password = "123456"
        self.database = "my_project"
        self.charset = "utf8"
        self.connect_database()

    def connect_database(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user = self.user,
                                  password = self.password,
                                  database = self.database,
                                  charset=self.charset)

    def create_cursor(self):
        self.cur = self.db.cursor()

    def s_register(self,name,password):
        """
            用户注册
        :param name: str 用户名
        :param password: str 密码
        :return: 注册成功返回True  失败返回False
        """
        sql = "select name from user where name = %s;"
        self.cur.execute(sql, [name])
        result = self.cur.fetchone()
        if result:
            return False
        else:
            try:
                sql = "insert into user (name, password) values (%s, %s);"
                self.cur.execute(sql, [name, password])
                self.db.commit()
                return True
            except:
                self.db.rollback()
                return False

    def s_login(self, name, password):
        sql = "select name,password from user where name = %s;"
        self.cur.execute(sql, [name])
        result = self.cur.fetchone()
        # print("数据库:用户名+密码 ", result)
        if result[1] == password:
            return True
        else:
            return False

    def s_find(self,word):
        sql = "select chinese from words where word = %s;"
        self.cur.execute(sql, [word])
        result = self.cur.fetchone()
        if result:
            return result[0]
        else:
            return "没有找到该单词"

    def s_insert_history(self,name, word):
        sql = "insert into history (name, word) values (%s, %s);"
        try:
            self.cur.execute(sql, [name, word])
            self.db.commit()
        except:
            self.db.rollback()

    def s_history(self, name):
        sql = "select name,word,time from history where name = %s order by time desc limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()

