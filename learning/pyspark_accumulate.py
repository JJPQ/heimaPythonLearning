from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:/Users/86188/PycharmProjects/pythonProject1/venv/Scripts/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 设置全局分区为1
conf.set("spark.default.parallelism", "1")
# 构建sparkContext对象，是pyspark编程一切功能的入口
sc = SparkContext(conf=conf)

# 字符串和字典结构改变：字符串会拆成单个字符，字典只保留key
# 设置单个rdd分区为1
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)
# rdd1 = sc.parallelize([1, 2, 3, 4, 5], 1)
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize({1, 2, 3, 4, 5})
# rdd4 = sc.parallelize("wjjizpq")
# rdd5 = sc.parallelize({"key1": "value", "key2": "value"})
# rdd = sc.parallelize([('wjj', 21), ('wjj', 1), ('zpq', 22), ('wjj', 21), ('zpq', 0), ('wy', 27)])
# rdd = sc.textFile("../cases/pySpark_case/pySpark_data.txt")

# 获取rdd内容需要用collect()方法
# print(rdd1.collect())
# 链式调用
# map算子
# rdd = rdd1.map(lambda x: x * 10).map(lambda x: x + 5)
# reduceByKey算子
# rdd = rdd.reduceByKey(lambda a, b: a + b)
# filter算子
# rdd = rdd1.filter(lambda x: x > 2)
# distinct算子
# rdd = rdd.flatMap(lambda x: x.split(" ")).distinct()

rdd1.saveAsTextFile("D:/output1")

sc.stop()
