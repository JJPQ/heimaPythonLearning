import json
from pyecharts.charts import Bar
from pyecharts.options import *


class record:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"{self.date},{self.order_id},{self.money},{self.province}"


class fileReader:
    def readData(self) -> list[record]:
        pass


class textFileReader(fileReader):
    def __init__(self, path):
        self.path = path

    def readData(self) -> list[record]:
        file = open(self.path, "r", encoding="utf-8")
        record_list: list[record] = []
        for line in file.readlines():
            line = line.strip()
            data_list = line.split(",")
            r = record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(r)
        file.close()
        return record_list


class jsonFileReader(fileReader):
    def __init__(self, path):
        self.path = path

    def readData(self) -> list[record]:
        file = open(self.path, "r", encoding="utf-8")
        record_list: list[record] = []
        for line in file.readlines():
            data_dict = json.loads(line)
            r = record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(r)
        file.close()
        return record_list


text_file_reader = textFileReader("C:/Users/86188/Desktop/可视化案例数据/数据分析案例/2011年1月销售数据.txt")
json_file_reader = jsonFileReader("C:/Users/86188/Desktop/可视化案例数据/数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[record] = text_file_reader.readData()
feb_data: list[record] = json_file_reader.readData()
all_data: list[record] = jan_data + feb_data

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money

print(data_dict)

bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("销售额案例.html")
