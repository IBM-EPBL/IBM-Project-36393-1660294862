import random
temp=random.randint(10,120)
hum=random.randint(10,120)
print (temp)
print (hum)
a= temp
b= hum
if ((a<50)&(b<30)):
      
    print("Temperature is Normal")
    print("Humidity is Normal")
    print("Alarm OFF")
elif((a<50)&(b>30)):
    print("Temperature is Low")
    print("Humidity is High")
    print("Alarm OFF")
          
elif ((a>50)&(b<30)):
    print("Temperature is High")
    print("Humidity is High ")
    print("Alarm ON")
elif((a>50)&(b>30)):
    print("Temperature is High")
    print("Humidity is Low")
    print("Alarm ON")
else:
    print("Temperature is Low")
    print("Humidity is Low")
    print("Alarm OFF")
    print("all is good")
