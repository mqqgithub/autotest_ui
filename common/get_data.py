'''
获取数据
'''
import xlrd, csv

txt_path = "./data1.txt"
xls_path = "./data2.xls"
csv_path = "./data3.csv"


class GetData(object):

    def __init__(self):
        pass

    def txt_data(self, path):
        with open(path, 'r+', encoding='utf-8') as f:
            s = [i[:-1].split(',') for i in f]  # 最后一行要回车
            print(s)
            return s

    def excel_data(self, path):
        # 打开execl
        workbook = xlrd.open_workbook(path)

        # 输出Excel文件中所有sheet的名字
        # print(workbook.sheet_names())

        # 根据sheet索引或者名称获取sheet内容
        Data_sheet = workbook.sheets()[0]  # 通过索引获取
        # Data_sheet = workbook.sheet_by_index(0)  # 通过索引获取
        # Data_sheet = workbook.sheet_by_name(u'名称')  # 通过名称获取

        # print(Data_sheet.name)  # 获取sheet名称
        rowNum = Data_sheet.nrows  # sheet行数
        colNum = Data_sheet.ncols  # sheet列数

        # 获取所有单元格的内容
        lis = []
        for i in range(rowNum):
            rowlist = []
            for j in range(colNum):
                rowlist.append(Data_sheet.cell_value(i, j))
            lis.append(rowlist)
        # print(lis)
        return lis

    def csv_data(self, path):
        lis = []
        with open(path, "r", encoding='gbk') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                lis.append(line)
        print(lis)
        return lis

    def mysql_data(self):
        pass


if __name__ == "__main__":
    data = GetData()
    txt = data.txt_data(txt_path)
    #excel = data.excel_data()
    #csv = data.csv_data()
    #mysql = data.mysql_data()
