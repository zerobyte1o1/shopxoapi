

class Config:
    host='172.16.3.193:9000'
    username='liufangjing'
    password='199921Liu'
    addr='172.16.3.193'
    port=3306
    mysql_user='admin'
    mysql_pwd='admin'
    database='xocom_80_623'
    @classmethod
    def get_host(cls):
        return cls.host
    @classmethod
    def get_username(cls):
        return cls.username
    @classmethod
    def get_password(cls):
        return cls.password
