import time
import requests, json
from influxdb import influxDBClient as influxdb
import serial

seri = serial.Serial('/dev/ttyACM0', baudrate = 9000, timeout = None)

while(True):
    time.sleep(1)
    if seri.in_waiting != 0:
        content = seri.readline()
        a = float(content.decode())
        data = [{
            'measurement': 'dust1',
            'tags':{
                'InhaUni': '2222',
                },
            'fields':{
                'dust': a,
                }
            }]
    client = None
    try:
        client = influxdb('localhost', 8086, 'root', 'root', 'dust')
    except Exception as e:
        print("Exception" + str(e))
    if client is not None:
        try:
            client.write.points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
    print(a)
    print("running influxdb OK")
