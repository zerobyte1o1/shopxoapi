import os, time, unittest
from common.HTMLTestRunner import HTMLTestRunner

#指定测试报告的标题
report_title = "全量测试"
report_desc = "对于蜗牛boss4.0所有功能进行测试"
report_path = "./report/"

#获取时间，在生成的测试报告名字上带上时间进行区分，避免重名
new_time = time.strftime("%Y%m%d%H%M%S")

#创建测试报告存放的位置和名字
report_file = report_path + f'report{new_time}.html'

#判断当前项目中是否有report目录，如果有了就直接存放，没有则先创建一个目录
if not os.path.exists(report_path):
    os.mkdir(report_path)

#写入内容，生成测试报告
with open(report_file, "wb") as reportfile:
    #模糊匹配创建测试套件
    #指定查找的测试用例的路径
    test_dir = './test_case'
    #指定项目根目录下，所有的以tes开头的.py文件中的测试用例
    discover = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')
    #生成运行器
    runner = HTMLTestRunner(stream=reportfile, title=report_title, description=report_desc)
    #执行
    runner.run(discover)