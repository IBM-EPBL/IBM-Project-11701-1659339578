from random import randint
def Generate_rand_temperature():
    return randint(1,300)
def Generate_rand_humidity():
    return randint(1,300)
random_temperature = Generate_rand_temperature()
print("TEMPERATURE=",random_temperature)
random_humidity = 80
print("HUMIDITY=",random_humidity)
if random_temperature >=38 :
    print("Warning : High Temperature")
else:
    print("Normal Temperature")
if random_humidity >= 50:
    print("Warning : High Humidity")
elif random_humidity <=30:
    print("Warning : Low Humidity")
else:
    print("Normal Humidity")