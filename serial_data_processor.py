import time
import numpy as np
import statistics


sensor_readings = np.random.randint(0,1024,1000)

#average
average = np.average(sensor_readings)

#standard deviation
#std_dev = statistics.stdev(sensor_readings)

data_queue = []

for i , sen_reading in enumerate(sensor_readings):
    data_queue.append(sen_reading)
    print("\n\nNew adc reading obtained : "+ str(sen_reading) + " <--> Sequence Number : "+str(i))
    print("Data queue Size "+str(len(data_queue)))
    if len(data_queue) == 100:
        average = np.average(data_queue)
        std_dev = statistics.stdev(data_queue)
        minimum = min(data_queue)
        maximum = max(data_queue)
        data_queue.pop(0)
        print("Results of last 100 data set")
        print("Maximum\t\t :",maximum)
        print("Minimum\t\t :",minimum)
        print("Average\t\t : {:.2f}".format(average))
        print("Std Dev\t\t : {:.2f}".format(std_dev))
        print("\n")
        time.sleep(0.001)
    time.sleep(0.001)
