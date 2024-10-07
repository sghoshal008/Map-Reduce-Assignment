#What is the average trip time for different pickup locations?

from mrjob.job import MRJob
import csv
from datetime import datetime

class MyMapReduce(MRJob):

    # Mapper function: emits key-value pairs where key is word and value is 1
    def mapper(self, _, line):
        vals = next(csv.reader([line]))
        if vals and vals[0] != "VendorID" and vals[0] != "":
            pickup_time = datetime.strptime(vals[1], "%Y-%m-%d %H:%M:%S")
            dropoff_time = datetime.strptime(vals[2], "%Y-%m-%d %H:%M:%S")
            time_difference = (dropoff_time - pickup_time).total_seconds() / 60  # Compute difference in minutes
            yield vals[8], (1, time_difference)

    # Reducer function: sums the counts for each word and sorts the results
    def reducer(self, key, values):
        total_count = 0
        total_vals = 0
        for count, val in values:
            total_count += count
            total_vals += val
            average_time = total_vals/total_count if total_count > 0 else 0
        yield key, (total_count, average_time)

if __name__ == '__main__':
    MyMapReduce().run()

'''
python mrtask_d.py < sampledata.csv > out.txt

"90"	4.416666666666667
"142"	9.683333333333334

Average trip for different locations
'''