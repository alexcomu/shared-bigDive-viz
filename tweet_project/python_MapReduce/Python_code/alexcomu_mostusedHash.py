from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import time

class TwitterJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    #OUTPUT_PROTOCOL = JSONValueProtocol

    def steps(self):
        return [self.mr(mapper=self.filter_hash, reducer=self.filter_hash_reducer)]


    def filter_hash(self, _, tweet):
        #check the list of hashtags
        if tweet['entities']['hashtags']:
            for t in tweet['entities']['hashtags']:
                yield t['text'], 1
                

    def filter_hash_reducer(self, key, value):
        totale = sum(value)
        if totale>100:
            yield key, totale
        


if __name__ == '__main__':
    TwitterJob().run()
