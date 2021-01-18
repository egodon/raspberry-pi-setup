import re
import os
import subprocess
from influxdb import InfluxDBClient

HOST_TAG = os.environ['HOST_TAG']
HOST = os.environ['INFLUXDB_HOST']
PORT = 8086
USER = os.environ['INFLUXDB_USER']
PASSWORD = os.environ['INFLUXDB_PASSWORD']
DB = 'internetspeed'

client = InfluxDBClient(HOST, PORT, USER, PASSWORD, DB)

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": HOST_TAG
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping)
        }
    }
]

client.write_points(speed_data)

