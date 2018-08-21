# coding:utf8

# Aurthor: Cai, Jiefei
# Date   : 2018/08/14 11:20

# ---------- 1.Names ---------- #
SPARK_APPNAME = 'Kettle_Log'
HADOOP_MASTER = 'local[*]'


# ---------- 2.Config ---------- #
SPARKCONFIG = {
    "spark.task.maxFailures" : 4
}