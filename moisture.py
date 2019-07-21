from grovepi import * 

moisture = 0
# A0に湿度センサ
dht_sensor_port = 7
#ポート7に温湿度センサー

while True:
    try:
        [tmp, hum] = dht(dht_sensor_port, 1)
        soil_moisture = analogRead(moisture)
        print("temp = " + tmp + "C hum = " + hum + "%" )
        print("soil moisture(analog) = " +soil_moisture)

    except(IOError,TypeError) as e:
        print ("Error")