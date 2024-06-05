import random
from pyecharts.charts import *
from pyecharts.options import *
import json

# import time
# from typing import TextIO


## 字符串使用
# name = "wjj"
# age = 21
# height = 1.78
# weight = 161.7
# print("我的名字是：%s，我的年龄是：%d，我的身高是：%.2f M，体重是：%f 斤" % (name, age, height, weight))
# print(f"我的名字是{name}，我的年龄是{age}，我的身高是{height}米，我的体重是{weight}斤")
# print("我的年龄是：%s" % (type(2023 - 2001)))
# print("my name is %s ," % name + "and age is %d" % age)
# ----------------------------------------------------------------------------------------------------------------------

## 表达式充当字符串
# print(f"current stock price is :{19.99 * 1.2 ** 7}")
# print("current stock price is :%.2f" % (19.99 * 1.2 ** 7))
# ----------------------------------------------------------------------------------------------------------------------


## 输入语句
# name = input("please input your name\n")
# print("your name is : '%s', type of your name is : %s" % (name, type(name)))
# age = input("please input your age\n")
# print("your age is : %s, the type of your age is: %s" % (age, type(int(age))))
# ----------------------------------------------------------------------------------------------------------------------


## if语句
# age=int(input("请输入年龄"))
# if age>=18:
#  print("welcome to school")
# else:
#  print("sorry")
# ----------------------------------------------------------------------------------------------------------------------


## while循环----1~100求和
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)
# ----------------------------------------------------------------------------------------------------------------------


## for循环字符匹配
# i = 0
# name = "wjjnb"
# for x in name:
#     if x == "j":
#         i += 1
# print(i)
# ----------------------------------------------------------------------------------------------------------------------


## range函数
# for x in range(10):
#     print(x)
# count = 0
# for x in range(1, 89):
#     if x % 2 == 0:
#         count += 1
# print(f"共有{count}个偶数")
# ----------------------------------------------------------------------------------------------------------------------


# 遍历列表
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 = []
# for element in my_list:
#     if element % 2 == 0:
#         list_2.append(element)
# print(f"通过for循环，从列表中取出偶数，组成新列表：{list_2}")
# list_2 = []
# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 1:
#         list_2.append(my_list[index])
#     index += 1
# print(f"通过while循环，从列表中取出奇数，组成新列表：{list_2}")

# 元组基本操作
# t1 = ("wjj", 21, ["football", "music"])
# t1.index(21)
# print(f"学生姓名是{t1[0]}")
# del t1[2][0]
# t1[2].append("coding")
# print(f"元组内容是:{t1}")

# 数据容器字符串
# my_str = "wjj love zpq forever"
# new_my_str = my_str.split(" ")
# 去除首和尾的 w 或 j
# new_my_str = my_str.strip("wj")
# new_my_str = my_str.replace("wjj", "王俊杰")
# print(my_str.index("zpq"))
# print(my_str.count("o"))
# print(new_my_str)

# 序列操作--切片
# my_str = "黑马程序员,学python,月薪过万"
# new_my_str = my_str[::-1]
# print(new_my_str)
# str_1 = new_my_str[::-1]
# print(str_1[:5])

# 集合操作
# my_list = ['赵浦乔', '王俊杰\'\'', '王俊杰', '赵浦乔', 'zpq', 'wjj', 'wjj', 'zpq']
# my_set = set()
# for i in my_list:
#     my_set.add(i)
# print(my_list)
# print(my_set)

# 字典操作
# my_dic = {"wjj": {"apartment": "mar", "salary": 5000, "level": 3}
#     , "zpq": {"apartment": "mar", "salary": 5000, "level": 3}
#     , "yyl": {"apartment": "tel", "salary": 4000, "level": 2}
#     , "hyf": {"apartment": "tel", "salary": 3000, "level": 1}
#           }
# print(my_dic)
# for key in my_dic:
#     if my_dic[key]["level"] == 1 or my_dic[key]["level"] == 2:
#         my_dic[key]["level"] += 1
#         my_dic[key]["salary"] += 1000
# print(my_dic)

# 不定长参数--元组/字典
# def user_info(*args):
#     print(args)
# user_info(1,2,3,4,'hhh')
# def user_info_2(**kwargs):
#     print(kwargs)
# user_info_2(name='wjj',age=21,gender='male')

# 文件操作
# f = open("D:/test.txt", "r", encoding="UTF-8")
# print(f.readline())
# print(f.readline())
# for i in f:
#     print(i)
# f.close()
# with open("D:/test.txt", "r", encoding="UTF-8") as f:
#     # wjj_num = f.read().count("wjj")
#     # print(wjj_num)
#     count = 0
#     for line in f:
#         word_list = line.strip().split(" ")
#     for word in word_list:
#         if word == "wjj":
#             count += 1
# print(count)
#     print(word_list)
# f = open("D:/word.txt", "w", encoding="UTF-8")
# # f.write("hello world!!!")
# # time.sleep(50000)
# # f.flush()
# f.write("hello ")
# f.write('world\n')
# f = open("D:/word.txt", "r", encoding="UTF-8")
# print(f.read())

# 文件综合案例
# f_2 = open("D:/bill_2.txt", "w", encoding="utf-8") # w 没有清空是因为写入的内容在buffer,还没有写入文件
# with open("D:/bill.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         if line.strip().split(",")[-1] != "测试": # method_1
#         # if not line.strip().count("测试"): # method_2
#             f_2.write(line)

# 异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了NameError异常")
#     print(e, type(e))
# 异常的传递性
# def func_1():
#     print("这是function_1开始")
#     name = 1 / 0
#     print("这是function_1结束")
# def func_2():
#     print("这是function_2开始")
#     func_1()
#     print("这是function_2结束")
# def main():
#     print("这是main开始")
#     try:
#         func_2()
#     except Exception as e:
#         # print(f"有--{e}--异常")
#         print(f"有--%s--异常" % e)
#     print("这是main结束")
# main()

# 模块的使用
# import time # 导入全部
# time.sleep(5)
# from time import * # 导入全部
# from time import sleep
# sleep(5)
# import time as t
# t.sleep(5)
# 异常,模块,包:综合案例
# import my_tools.str_tool
# import my_tools.file_tool
# my_tools.str_tool.str_reverse("wjjnb")
# my_tools.str_tool.substr("wjjnb",0,4)
# my_tools.file_tool.print_file_info("D:/nb.txt")


# data = [{"name": "王俊杰", "age": "21"}, {"name": "zpq", "age": "23"}]
# json_str = json.dumps(data, ensure_ascii=False)  # str类型，有中文可以添加参数，显示中文
# print(json_str, type(json_str))
# s = '[{"name": "王俊杰", "age": "21"}, {"name": "zpq", "age": "23"}]'
# l = json.loads(s)
# print(s, type(l))
# data_2 = '{"name": "wjj", "age": 11}'
# d = json.loads(data_2)
# print(d, type(d))


# pyecharts的基础使用


# 得到一个空坐标系
# line = Line()
# # 赋值于x轴
# line.add_xaxis(["chian","usa","england"])
# # 赋值于y轴
# line.add_yaxis("gdp",[30,20,10])
# # 设置全局配置
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
#     # 控制图例是否显示
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
# # 用render生成图像
# line.render()

# ## 生成折线图项目
# # 打开文件
# f_usa = open("C:/Users/86188/Desktop/可视化案例数据/折线图数据/美国.txt", "r", encoding="utf-8")
# us_data = f_usa.read()
# f_jp = open("C:/Users/86188/Desktop/可视化案例数据/折线图数据/日本.txt", "r", encoding="utf-8")
# jp_data = f_jp.read()
# f_in = open("C:/Users/86188/Desktop/可视化案例数据/折线图数据/印度.txt", "r", encoding="utf-8")
# in_data = f_in.read()
# # 替换掉开头和结尾
# us_data = us_data[26:-2]
# jp_data = jp_data[26:-2]
# in_data = in_data[26:-2]
# # 转字典
# us_dict = json.loads(us_data)
# jp_dict = json.loads(jp_data)
# in_dict = json.loads(in_data)
# # 生成x轴的数据
# us_x_data = us_dict['data'][0]['trend']['updateDate'][:314]
# jp_x_data = jp_dict['data'][0]['trend']['updateDate'][:314]
# in_x_data = in_dict['data'][0]['trend']['updateDate'][:314]
# # 生成y轴的数据
# us_y_data = us_dict['data'][0]['trend']['list'][0]['data'][:314]
# jp_y_data = jp_dict['data'][0]['trend']['list'][0]['data'][:314]
# in_y_data = in_dict['data'][0]['trend']['list'][0]['data'][:314]
# # 生成折线图
# line=Line()
# # 添加x轴数据
# line.add_xaxis(us_x_data)
# # 添加y轴数据
# line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
# # 设置折线图具体参数
# line.set_global_opts(
#     title_opts=TitleOpts(title="新冠疫情",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True,max_=22000000)
# )
# # 生成html文件
# line.render("折线图案例.html")
# # 关闭打开的文件
# f_in.close()
# f_usa.close()
# f_jp.close()

## 生成地图项目
# 基础使用
# map=Map()
# data=[
#     ("北京市",99),
#     ("上海市",199),
#     ("湖南省",299),
#     ("台湾省",399),
#     ("江苏省",499)
#     ]
# map.add("测试地图",data,"china")
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
#             {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
#             {"min":100,"max":500,"label":"100-500","color":"#990033"},
#         ]
#     )
# )
# map.render()

# # 国内疫情地图
# f = open("C:/Users/86188/Desktop/可视化案例数据/地图数据/疫情.txt", "r", encoding="utf-8")
# data = f.read()
# # f.close()
# # 生成字典
# data_dict = json.loads(data)
# # 去全国各省疫情数据
# p_data_list = data_dict["areaTree"][0]["children"][31]["children"]
# # print(type(p_data_list))
# # 生成list对象储存数据
# data_list = []
# for p_data in p_data_list:
#     p_name = p_data["name"]
#     p_confirm = p_data["total"]["confirm"]
#     data_list.append((p_name, p_confirm))
# # 生成空地图对象
# map = Map()
# # 添加省份对应数据
# map.add("各省份确诊人数",data_list,"china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         # 设置视觉映射的分段
#         pieces=[
#             {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"100-999","color":"#e2f8b9"},
#             {"min":1000,"max":4999,"label":"1000-4999","color":"#ef8467"},
#             {"min":5000,"max":9999,"label":"5000-9999","color":"#df5530"},
#             {"min":10000,"max":99999,"label":"10000-99999","color":"#bd550f"},
#             {"min":100000,"label":"10000+","color":"#732f1c"},
#         ]
#     )
# )
# # 生成最终地图文件
# map.render("全国疫情地图.html")
# # 安徽省疫情地图
# f = open("C:/Users/86188/Desktop/可视化案例数据/地图数据/疫情.txt", "r", encoding="utf-8")
# # 读取str对象
# data = f.read()
# # print(type(data))
# # f.close()
# # 生成字典
# data_dict = json.loads(data)
# # 取安徽省各市疫情数据
# ah_data_list = data_dict["areaTree"][0]["children"][31]["children"]
# # print(type(p_data_list))
# # 生成list对象储存数据
# data_list = []
# for ah_data in ah_data_list:
#     ah_name = ah_data["name"]+"市"
#     ah_confirm = ah_data["total"]["confirm"]
#     data_list.append((ah_name, ah_confirm))
# # 可以手动以元组形式添加数据
# # data_list.append((”马鞍山市“,10))
# # 生成空地图对象
# map = Map()
# # 添加省份对应数据
# map.add("安徽省各市确诊人数",data_list,"安徽")
# map.set_global_opts(
#     title_opts=TitleOpts(title="安徽省疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         # 设置视觉映射的分段
#         pieces=[
#             {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
#             {"min":100,"max":999,"label":"100-999","color":"#e2f8b9"},
#             {"min":1000,"max":4999,"label":"1000-4999","color":"#ef8467"},
#             {"min":5000,"max":9999,"label":"5000-9999","color":"#df5530"},
#             {"min":10000,"max":99999,"label":"10000-99999","color":"#bd550f"},
#             {"min":100000,"label":"10000+","color":"#732f1c"},
#         ]
#     )
# )
# # 生成最终地图文件
# map.render("安徽省疫情地图.html")

# 基础柱状图的使用
# bar=Bar()
# bar.add_xaxis(["wjj","zpq"])
# bar.add_yaxis("恋爱天数",[100,200],label_opts=LabelOpts(position="right"))
# # 反转x，y轴
# bar.reversal_axis()
# bar.render("基础柱状图.html")
# 基础时间轴柱状图
# bar1 = Bar()
# bar1.add_xaxis(["wjj", "zpq", "nb"])
# bar1.add_yaxis("恋爱天数", [100, 200, 300])
# bar1.reversal_axis()
# bar2 = Bar()
# bar2.add_xaxis(["wjj", "zpq", "nb"])
# bar2.add_yaxis("恋爱天数", [200, 100, 300])
# bar2.reversal_axis()
# bar3 = Bar()
# bar3.add_xaxis(["wjj", "zpq", "nb"])
# bar3.add_yaxis("恋爱天数", [300, 200, 100])
# bar3.reversal_axis()
# timeline=Timeline()
# timeline.add(bar1,"点1")
# timeline.add(bar2,"点2")
# timeline.add(bar3,"点3")
# # 设置参数
# timeline.add_schema(
#     play_interval=1000, #  单位是毫秒
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=False
# )
# # 设置主题
# # timeline=Timeline({"theme":ThemeType.LIGHT})
# timeline.render("基础时间线柱状图.html")
# 动态GDP柱状图绘制
# my_list = [["wjj", 21], ["zpq", 23], ["wy", 27]]
# # 柱状图的指定元素排序
# my_list.sort(key=lambda e: e[1], reverse=True)
# print(my_list)

# # # 动态柱状图案例
# f_bar = open("C:/Users/86188/Desktop/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
# data_lines = f_bar.readlines()
# data_lines.pop(0)
# data_dict = {}
# for line in data_lines:
#     year = int(line.split(",")[0])  # 按 , 分割得到年份，并用int将年份从str转换成数字类型
#     country = line.split(",")[1]  # 得到国家名
#     gdp = float(line.split(",")[2])  # 得到gdp，并用float将科学计数法表示转换成数字表示
#     try:
#         data_dict[year].append([country, gdp])
#     except KeyError:
#         data_dict[year] = []  # 将字典中key=year的value设置为空list
#         data_dict[year].append([country, gdp])  # 在空list中追加元素
# # print(data_dict)
# # 取出所有key即年份值，并按照年份排序
# sorted_year_list = sorted(data_dict.keys())
# timeline=Timeline()
# # print(sorted_year_list)
# for year in sorted_year_list:
#     data_dict[year].sort(key=lambda e: e[1], reverse=True)  # 按照gdp排序
#     year_data=data_dict[year][:20]  # 取出gdp前10名的国家
#     x_data = []
#     y_data = []
#     for c_gdp in year_data:
#         x_data.append(c_gdp[0])
#         y_data.append(c_gdp[1]/100000000)
#     bar=Bar()
#     x_data.reverse()
#     y_data.reverse()
#     bar.add_xaxis(x_data)
#     bar.add_yaxis("GDP(亿)",y_data,label_opts=LabelOpts(position="right"))
#     bar.reversal_axis()
#     bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{year}年全球GDP前二十的国家")
#     )
#     timeline.add(bar,str(year))
# timeline.add_schema(
#     play_interval=500, #  单位是毫秒
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=False
# )
# timeline.render("1960~2019年全球GDP前十国家.html")

# 录入学生信息
# class student:
#     # 内置方法----魔术方法
#     def __init__(self,name,age,add):
#         # 定义name,age,tel变量并赋值
#         self.name=name
#         self.age=age
#         self.add=add
# for i in range(10):
#     # num=i+1
#     print(f"请输入第{i+1}位学生的信息，总共需录入10位学生信息")
#     i=student(input("请输入姓名"),input("请输入年龄"),input("请输入地址"))
#     print(f"学生{i}的信息录入完成，信息为：学生姓名是 {i.name}，年龄是 {i.age}，地址是 {i.add}")


# class student:
#     # 内置方法----魔术方法
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     # 值传给self
#     def __str__(self):
#         return f"学生信息录入完成，信息为：学生姓名是 {self.name}，年龄是 {self.age}"
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#     # ==符号默认比较地址
#     def __eq__(self, other):
#         if self.age == other.age:
#             if self.sex==other.sex:
#                 return True
#             else:
#                 return "这是错误1"
#         else:
#             return "这是错误2"

# class phone:
#     __is_5G_enable = False
#
#     def __check_5G(self):
#         if self.__is_5G_enable:
#             print("5g开启")
#         else:
#             print("5g关闭")
#
#     def call_by_5G(self):
#         self.__check_5G()
#         print("正在通话中")
#
#
# phone = phone()
# phone.call_by_5G()
