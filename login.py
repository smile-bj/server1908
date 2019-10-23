import pymysql
class Database:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost', port=3306, user='root',
                             password='123456', database='test',
                             charset='utf8')
        self.cur = self.db.cursor()
        self.cur.execute()

    def close(self):
        self.cur.close()
        self.db.close()
    def register(self,name,passwd):

if __name__ == '__main__':
    db=Database()


