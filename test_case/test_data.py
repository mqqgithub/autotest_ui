# 数据驱动测试，首先需要安装DDT包
from ddt import ddt, data, unpack
from common.get_data import GetData
import unittest,os
path1 = os.path.join(os.path.dirname(os.path.realpath('__file__')), 'data1.txt')
test_data = GetData().txt_data(path1)
print(test_data)


# 使用前必须先声明
@ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        print("test start...")

    def tearDown(self):
        print("test over...")

    @data('aa', 'bb')  # 单个参数分2次运行用例
    def test_1(self, s):
        print("test1%s" % s)

    @data((1, 1), (2, 2))  # 多个参数必须要拆包,不然会作为一个参数
    @unpack
    def test_2(self, x, y):
        print("test2%d" % (x+y))

    @data(*test_data)  # data的数据必须是元祖，加*是把数据变成元祖类型  test_data 可以是函数*test_data()返回值
    @unpack
    def test_3(self, a, b, c):
        print(a)
        print(b)
        print(c)


if __name__ == '__main__':
    unittest.main()
