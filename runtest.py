# # coding:utf-8
# __author__ = 'jack'
# '''
# description:执行测试
# '''
#
# import HtmlTestRunner, unittest, time
# from config.globalConf import test_case_path, report_name
# from src.common import sendEmail
#
# # 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
# suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')
#
# # 执行测试
# if __name__ == "__main__":
#     report = report_name + "report.html"
#     fb = open(report, 'w')
#
#     runner = HtmlTestRunner.HTMLTestRunner(stream=fb,
#                                            report_title=u'litLiveAPP自动化测试报告',
#                                            report_name=u'项目描述：生产环境')
#     runner.run(suite)
#     fb.close()
#     # 发送邮件
#     time.sleep(5)  # 设置睡眠时间，等待测试报告生成完毕
#     sendEmail.SendAEmail().send_report()
#
# # addTest()     #用例只能一个一个的添加，不方便（引入unittest.TestLoader()，批量加载用例）
#
# import unittest
# from  test_start_live import TestStatLive
#
# # from xxx import xxx      #测试用例的类
# suite=unittest.TestSuit()
# suite.addTest(TestStatLive("test_binding_product_stream"))    #用例名称用字符串的形式传入
# suite.addTest(TestStatLive("test_skip_product_stream"))
# suite.addTest(TestStatLive("test_edit_product_stream"))
#
# # suite = unittest.TestSuit()
# # loader = unittest.TestLoader()
# # suite.addTest(loader.loadTestsFromTestCase(TestStatLive))  # 测试用例类名直接传入