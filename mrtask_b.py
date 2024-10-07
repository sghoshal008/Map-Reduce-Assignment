# Which pickup location generates the most revenue? 

from mrjob.job import MRJob
import csv

class MyMapReduce(MRJob):

    # Mapper function: emits key-value pairs where key is word and value is 1
    def mapper(self, _, line):
        vals = next(csv.reader([line]))
        if vals and vals[0] != "VendorID" and vals[0] != "":
            yield vals[7], (1, float(vals[16]))

    # Reducer function: sums the counts for each word and sorts the results
    def reducer(self, key, values):
        total_count = 0
        total_vals = 0
        for count, val in values:
            total_count += count
            total_vals += val
        yield key, (total_count, total_vals)

if __name__ == '__main__':
    MyMapReduce().run()

'''
python mrtask_b.py < sampledata.csv > out.txt

"249"	[7,57.05]
"141"	[2,24.72]

:: pickup location 249 generates the most revenue 
'''