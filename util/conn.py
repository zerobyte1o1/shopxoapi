import pymysql
from util.config import Config


class Conn:
    conn = pymysql.connect(host=Config.addr, port=Config.port, user=Config.mysql_user, passwd=Config.mysql_pwd,
                           db=Config.database)

    def select(self, sql):
        cur = self.conn.cursor()
        self.conn.ping(reconnect=True)
        cur.execute(sql)
        res = cur.fetchall()[0][0]
        self.conn.commit()
        self.conn.close()
        return res

    def delete(self, sql):
        cur = self.conn.cursor()
        self.conn.ping(reconnect=True)
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':

    a=Conn().select('select assets_id from assets where bar_code="12910483721";')
    print(a)
