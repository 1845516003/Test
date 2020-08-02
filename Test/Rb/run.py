# 统一运行入口
import unittest
import HTMLReport
from Test_Suite import total_suite

# 总的测试套件
suite = unittest.TestSuite()

# 将需要执行的测试加入到总的测试套件中
suite.addTests(total_suite.return_suite())
if __name__ == '__main__':
    # 执行测试并生成报告
    HTMLReport.TestRunner(
        report_file_name="录播web自动化测试",
        title="录播web自动化测试",
        description="python3+selenium3+unittest+ddt+HTMLReport webUI自动化测试框架",
        thread_count=1,    # 多线程启动chromedriver运行测试用例
        thread_start_wait=3     #设置线程启动的延迟时间
    ).run(suite)