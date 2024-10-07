# What are the different payment types used by customers and their count? The final results should be in a sorted format.

from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class MyMapReduce(MRJob):

    # Mapper function: emits key-value pairs where key is word and value is 1
    def mapper(self, _, line):
        vals = next(csv.reader([line]))
        if vals and vals[0] != "VendorID" and vals[0] != "":
            yield vals[9], (1, float(vals[16]))

    # Reducer function: sums the counts for each word and sorts the results
    def reducer(self, key, values):
        total_count = 0
        total_vals = 0
        for count, val in values:
            total_count += count
            total_vals += val
        yield key, (total_count, total_vals)

    def reducer_sort(self, _, pairs):
        for key, value in sorted(pairs, key=lambda x: [1], reverse=True):
            yield key, value

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer_sort)
        ]

if __name__ == '__main__':
    MyMapReduce().run()


'''
python mrtask_c.py < sampledata.csv > out.txt

"1"	[4,41.019999999999996]
"4"	[3,24.450000000000003]
"3"	[1,8.15]
"2"	[1,8.15]

:: payment_type 1 generates the most revenue 
'''
