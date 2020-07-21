import time
import os
import unittest
import HTMLReport
from common.emails import Email

path = os.getcwd()
case_path = os.path.join(path, "test_case")
report_path = os.path.join(os.getcwd(), 'report')
report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
report_name = report_time + "report"
report = report_path + r'\\' + report_name + '.html'

discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')


def run():
    runner = HTMLReport.TestRunner(title="测试报告", description='测试deafult报告',
                                   output_path=report_path, report_file_name=report_name, thread_count=2)
    runner.run(discover, debug=False)
    time.sleep(5)
    Email.send_email(report)


if __name__ == "__main__":
    run()
