f = open("res2_mostUsed.txt","r")
myList={}
for line in f:
	line = line.split()
	hashtag = line[0][1:-1]
	hashtag = hashtag.lower()
	if hashtag not in myList:
		myList[hashtag] = 0
	myList[hashtag] += int(line[1])

for m in myList:
	if myList[m] > 10000:
		print m, ': ', myList[m]
	
