import unittest
import os,ddt
from module.registModule import RegistModule
from util.readfile import readexecl

@ddt.ddt
class TestRegist(unittest.TestCase):
    path = os.path.join('./data/testdata.xlsx')
    excldata = readexecl(path, 'regist')
    @ddt.data(*excldata)
    @ddt.unpack
    def test_user_regist(self,accounts, pwd, tp, is_agree_agreement):
        asserttext=RegistModule().user_regist(accounts, pwd, tp, is_agree_agreement)
        self.assertEqual(asserttext['msg'],'注册成功')


if __name__ == '__main__':
    unittest.main()