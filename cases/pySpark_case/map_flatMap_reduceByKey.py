from pyspark import SparkConf, SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:/Users/86188/PycharmProjects/pythonProject1/venv/Scripts/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

conf = SparkConf().setMaster("local[*]").setAppName("case_1")

sc = SparkContext(conf=conf)

rdd = sc.textFile("pySpark_data.txt")

# 输出[('love', 2), ('wjj', 5), ('zpq', 6), ('wy', 3)]
rdd = rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)

# 输出[('zpq', 6), ('wjj', 5), ('wy', 3), ('love', 2)]
rdd = rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print(rdd.collect())

sc.stop()
