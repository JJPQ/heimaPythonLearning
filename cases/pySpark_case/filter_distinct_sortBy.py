from pyspark import SparkConf, SparkContext
import os
import json

os.environ['PYSPARK_PYTHON'] = "C:/Users/86188/PycharmProjects/pythonProject1/venv/Scripts/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

conf = SparkConf().setMaster("local[*]").setAppName("case_1")

sc = SparkContext(conf=conf)

# TODO 需求1：城市销售额排名
# 输出[('北京', 91556), ('杭州', 28831), ('天津', 12260), ('上海', 1513), ('郑州', 1120)]
# 读文件得到RDD
rdd = sc.textFile("orders.txt")
# 获取JSON字符串
rdd1_1 = rdd.flatMap(lambda x: x.split("|"))
# 将json转化为dict
rdd1_2 = rdd1_1.map(lambda x: json.loads(x))
# 取出城市和销售额数据
rdd1_3 = rdd1_2.map(lambda x: (x['areaName'], int(x['money'])))
# 按城市累加销售额
rdd1_4 = rdd1_3.reduceByKey(lambda a, b: a + b)
# 销售额降序排序
rdd1_5 = rdd1_4.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print("需求1的输出结果是：",rdd1_5.collect())

# TODO 需求2：全部城市有哪些商品在售卖
# 输出['平板电脑', '家电', '书籍', '手机', '电脑', '家具', '食品', '服饰']
# 取出全部商品类别并去重
rdd2_1 = rdd1_2.map(lambda x: x['category']).distinct()
print("需求2的输出结果是：",rdd2_1.collect())

# TODO 需求3：上海市有哪些商品在售卖
# 输出['电脑']
# 过滤出上海的销售数据
rdd3_1 = rdd1_2.filter(lambda x: x['areaName'] == '上海')
# 查看北京在售商品类别并去重
rdd3_2 = rdd3_1.map(lambda x: x['category']).distinct()
print("需求3的输出结果是：",rdd3_2.collect())

sc.stop()
