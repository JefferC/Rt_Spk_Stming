# coding:utf8

# Aurthor: Cai, Jiefei
# Date   : 2018/08/20 16:57

from pyspark.sql import SparkSession
from pyspark import SparkConf
import Config

class SparkObject(object):

    def __init__(self):
        self.SetSpkSession()

    def SetSpkSession(self, ss=None):
        if not ss is None:
            if isinstance(ss, SparkSession):
                self.SpkSs = ss
            else:
                print "Error"
        else:
            # 创建SparkConf实例
            conf = SparkConf().setAppName(Config.SPARK_APPNAME).setMaster(Config.HADOOP_MASTER)
            # 添加所有配置信息，可在Config.py中配置
            for i in Config.SPARKCONFIG:
                conf.set(i, Config.SPARKCONFIG[i])
            # 创建SparkSession实例
            self.SpkSession = SparkSession.builder.config(conf=conf).enableHiveSupport().getOrCreate()
            # 版本判断
            self.SpkVersion = self.SpkSession.version
            if not self.SpkVersion.startswith("2."):
                print "Version Error, Only Support 2.0"
                exit()

# https://blog.csdn.net/dongyunlon/article/details/52145685