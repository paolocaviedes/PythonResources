from influxdb import client as influxdb
import time
influx = influxdb.InfluxDBClient("192.168.20.112", 8086, "root", "root", "mydata")
systemhora=time.time()
# An empty array to store data to avoid making multiple calls to influx.
#data = [{'points':[[systemhora,100]],'name':'awesomedata','columns':['time','amount']}]
data = [{"name" : "hd_used","columns" : ["value", "host", "mount"],"points" : [[23.2, "serverA", "/mnt"]]}]


# Write the points to influx
influx.write_points(data)
