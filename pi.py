
import fcntl, socket, struct, dweepy, time, platform, sqlite3


from grovepi import*


ultrasonic_ranger = 4 #Digital port 4

dht_sensor_port = 7 #digital port 7


#Temperature
def getTemp():

        try:

                [temp,humidity] = dht(dht_sensor_port,0)




                return (temp)

        except (IOError, TypeError) as e:
            print("Error reading the temperature sensor")

#Humidity
def getHumidity():

        try:

                [temp,humidity] = dht(dht_sensor_port,0)


                return (humidity)

        except (IOError, TypeError) as e:

                print("Error loading humidity sensor")

#Ultrasonic
def getDistant():
 while True:
        try:

                distant = ultrasonicRead(ultrasonic_ranger)


                return (distant)

        except (IOError, TypeError) as e:

                print("Error loading distance reading")


#def getOS():
 #   return platform.platform()

# from http://stackoverflow.com/questions/159137/getting-mac-address
#def getHwAddr(ifname):

 #   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  #  info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
   # return ':'.join(['%02x' % ord(char) for char in info[18:24]])


def load_config():
  with open('configurationfile.txt', 'r')as file:
   for line in file:
      return line.strip('\n')

def post(star):
    thing = load_config() #calls thing ()
    dweepy.dweet_for(thing, star)
    print (thing)

def getReadings():
    star = {}
    star["distant"] = getDistant();
    star["temperature"] = getTemp();

    star["humidity"] = getHumidity()

    conn = sqlite3.connect('databasename.db')
    c = conn.cursor()
   # c.execute('CREATE TABLE databasetablename(getDistant INT, getTemp INT, getHumidity INT)')
    c.execute('INSERT INTO databasetable VALUES(?, ?, ?)',(getDistant(), getTemp(), getHumidity()))
    conn.commit()

    return star

while True:
    star = getReadings();
    post(star)
    print(star)
    time.sleep(3)

