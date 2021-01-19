import os
import subprocess
import json
from influxdb import InfluxDBClient

HOST_TAG = os.environ["HOST_TAG"]
HOST = os.environ["INFLUXDB_HOST"]
PORT = 8086
USER = os.environ["INFLUXDB_USER"]
PASSWORD = os.environ["INFLUXDB_PASSWORD"]
DB = "internetspeed"

client = InfluxDBClient(HOST, PORT, USER, PASSWORD, DB)

print("Starting speedtest...")
response = (
    subprocess.Popen(
        "/usr/local/bin/speedtest-cli --json", shell=True, stdout=subprocess.PIPE
    )
    .stdout.read()
    .decode("utf-8")
)

speedcli_json = json.loads(response)

speed_data = [
    {
        "measurement": "internet_speed",
        "tags": {"host": HOST_TAG},
        "fields": {
            "download": float("{:.2f}".format(speedcli_json["download"] / 1000000)),
            "upload": float("{:.2f}".format(speedcli_json["upload"] / 1000000)),
            "ping": float("{:.2f}".format(speedcli_json["ping"])),
        },
    }
]

client.write_points(speed_data)
