#Calculate the average tips to revenue ratio of the drivers for different pickup locations in sorted format.

from mrjob.job import MRJob
from mrjob.step import MRStep
import csv

class MyMapReduce(MRJob):

    # Mapper function: emits key-value pairs where key is word and value is 1
    def mapper(self, _, line):
        vals = next(csv.reader([line]))
        if vals and vals[0] != "VendorID" and vals[0] != "":
            yield vals[7], (float(vals[13]), float(vals[16]))

    # Reducer function: sums the counts for each word and sorts the results
    def reducer(self, key, values):
        total_tip = 0
        total_rev = 0
        c=0
        for val1, val2 in values:
            c+=1
            total_tip += val1
            total_rev += val2
        yield key, ((total_tip/c)/total_rev)

    def reducer_sort(self, _, pairs):
        for key, value in sorted(pairs, key=lambda x: [1], reverse=True):
            yield key, value

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer)
        ]

if __name__ == '__main__':
    MyMapReduce().run()

'''
python mrtask_e.py < sampledata.csv > out.txt

"249"	0.02366345311130587
"141"	0.08333333333333334

'''