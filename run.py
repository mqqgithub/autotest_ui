import time
import os
import unittest
import HTMLReport


path = os.getcwd()
case_path = os.path.join(path, "test_case")
report_path = os.path.join(os.getcwd(), 'report')
report_time = time.strftime("%Y_%m_%d_%H_%M_%S_")
report_name = report_time + "report"

discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')


def run():
    runner = HTMLReport.TestRunner(title="测试报告", description='测试deafult报告',
                                   output_path=report_path, report_file_name=report_name, thread_count=2)
    runner.run(discover)


if __name__ == "__main__":
    run()