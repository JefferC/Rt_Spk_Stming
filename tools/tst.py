# coding:utf8

# Aurthor: Cai, Jiefei
# Date   : 2018/09/29 13:58
#https://www.jianshu.com/p/c65008b29549

from pyspark.sql import SparkSession
from pyspark import SparkConf
import Config

conf = SparkConf().setAppName(Config.SPARK_APPNAME).setMaster(Config.HADOOP_MASTER)
for i in Config.SPARKCONFIG:
    conf.set(i, Config.SPARKCONFIG[i])
ss = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()

sc = ss.sparkContext

sc.setLogLevel('WARN')

df = ss.readStream.format('kafka')\
    .option("kafka.bootstrap.servers", Config.KAFKA_SERVER)\
    .option("subscribe", 'test')



# r = ss.sql("show databases")

# r.show()

df = df.option("group.id", 'first1').load()

df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()


query.awaitTermination()
