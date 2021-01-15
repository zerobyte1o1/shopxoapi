import requests
from util.config import Config
from lib.getsession import GetSession


class RegistModule():
    def __init__(self):
        self.session = GetSession().get_session()


    def user_regist(self, accounts, pwd, tp, is_agree_agreement):

        url = f'http://{Config.get_host()}/index.php?s=/index/user/reg.html'
        headers = {
            'Content-Type': 'multipart/form-data',
            'X-Requested-With':'XMLHttpRequest'
        }
        data = {
            'accounts': accounts,
            'pwd': pwd,
            'type': tp,
            'is_agree_agreement': is_agree_agreement

        }
        r = self.session.post(url, headers=headers, data=data)
        # print(r.json())
        return r.json()


if __name__ == '__main__':
    a = RegistModule().user_regist('liuqw1', '123456', 'username', '1')
    print(a)
