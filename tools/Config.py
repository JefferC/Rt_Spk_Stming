# coding:utf8

# Aurthor: Cai, Jiefei
# Date   : 2018/08/14 11:20

# ---------- 1.Names ---------- #
SPARK_APPNAME = 'Kettle_Log'
HADOOP_MASTER = 'local[*]'

SPARK_WAREHOUSE_DIR = r"D:\github\Rt_Spk_Stming\tools\spark-warehouse"

# ---------- 2.Config ---------- #
SPARKCONFIG = {
    "spark.sql.warehouse.dir": SPARK_WAREHOUSE_DIR,
    "spark.task.maxFailures" : 4
}


# Kafka IP
KAFKA_SERVER = "localhost:9092"
