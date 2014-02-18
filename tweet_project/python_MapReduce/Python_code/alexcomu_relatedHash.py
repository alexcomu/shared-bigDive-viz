from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import time

class TwitterJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def steps(self):
        return [self.mr(mapper=self.filter_geo, reducer=self.filter_geo_reducer)]

    '''
    def filter_geo(self, _, tweet):
        if tweet['entities']['hashtags']:
            for t in tweet['entities']['hashtags']:
                yield t['text'], 1

    '''
    def filter_geo(self, _, tweet):
        #check the list of hashtags
        hasht = []
        for t in tweet['entities']['hashtags']:
            hasht.append(t['text'])
        if 'Egypt' in hasht:
            for tw in hasht:
                yield None, [tw,1]
                

    def filter_geo_reducer(self, key, value):
        myList = {}
        for tz,v in value:
            if tz not in myList:
                myList[tz] = 0
            myList[tz] += 1
        #myJson = json.dumps({int(key):str(myList)},separators=(',', ': '))
        yield None, myList
        #totale = sum(value)
        #if totale>10:
        #    yield key, totale
        #yield key, sum(value)
        #Result: {hour: {time_zone: occurency}}
        


if __name__ == '__main__':
    TwitterJob().run()


'''
if tweet['entities']['hashtags'] == 'Egypt':
if tweet['user']['utc_offset']:
yield (tweet['user']['utc_offset'])/3600, 1


'''
