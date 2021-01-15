import requests
from util.config import Config


class GetSession():

    def get_session(self):
        session = requests.Session()
        session.get(f'http://{Config.get_host()}/index.php?s=/index/user/reginfo.html')
        # 如果会话已经创建，就直接返回之前已经生成的session
        return session

    def get_loginsession(self):
        session = requests.Session()
        url = f'http://{Config.get_host()}/index.php?s=/index/user/login.html'
        headers = {
            'Content-Type': 'multipart/form-data',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'accounts': Config.get_username(),
            'pwd': Config.get_password()
        }
        r = session.post(url, headers=headers, data=data)
        print(r.text)
        return session



