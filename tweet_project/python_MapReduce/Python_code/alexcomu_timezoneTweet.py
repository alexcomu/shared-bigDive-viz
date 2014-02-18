from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol
import time

class TwitterJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    #OUTPUT_PROTOCOL = JSONValueProtocol

    def steps(self):
        return [self.mr(mapper=self.filter_geo, reducer=self.filter_geo_reducer)]

    def filter_geo(self, _, tweet):
        #check the list of hashtags
        for t in tweet['entities']['hashtags']:
            #check if there is #Egypt
            if t['text']=='Egypt':
                #if yes, find the utc time zone
                if tweet['user']['utc_offset']:
                    t = tweet['created_at'].split()[3]
                    yield t[0:2], [(tweet['user']['utc_offset'])/3600, 1]
                    #Forma: hour , {time_zone: 1}
                


    def filter_geo_reducer(self, key, value):
        myList = {}
        for tz,v in value:
            if tz not in myList:
                myList[tz] = 0
            myList[tz] += 1
        #myJson = json.dumps({int(key):str(myList)},separators=(',', ': '))
        yield key, myList
        #Result: {hour: {time_zone: occurency}}
        


if __name__ == '__main__':
    TwitterJob().run()


'''
if tweet['entities']['hashtags'] == 'Egypt':
if tweet['user']['utc_offset']:
yield (tweet['user']['utc_offset'])/3600, 1




if tweet['entities']['hashtags']:
            for t in tweet['entities']['hashtags']:
                yield t['text'], 1

total = sum(value)
        if total>20:
            yield key, total
        else:
            pass

'''
