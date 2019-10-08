#Form the priority caching system such that
# Case 1 If priority of log is greater than 5 move to cache storage
# Case 2 if the priority is less than or equal to 3 move to main memory
#Case 3 if the log is used once increment the priority of the log at that instance by 2 
# if the priority is incremented by 2*no.of times that was used in that particular instance 


# Idea is to form a dictionary with the time as key and the process that we are accessed in that particular 
# time. While doing so calculate the max time and min time
# Finally at each instance of time apply three cases listed above.
# While doing so access elelments of the cache and main memory
#As listed in the question sort the list containing process in cache and return the list.
import sys

def prioirtyQueue(callLogs):
	callLogDict = {}
	timeStart = sys.maxsize
	timeEnd = -sys.maxsize-1
	countDict = {}
	cacheItems = []
	for time, value in callLogs:
		if time > timeEnd:
			timeEnd = time
		if time < timeStart:
			timeStart = time
		if callLogDict.get(time):
			callLogDict[time].append(value)
		else:
			callLogDict[time] = [value]
	
	for time in range(timeStart,timeEnd+1):
		if callLogDict.get(time):
			values = callLogDict[time]
		for key,value in countDict.items():
			if value > 0 and key not in values:
				countDict[key] -=1
		for value in values:
			if countDict.get(value):
				countDict[value]+=2
			else:
				countDict[value] = 2
		for cnt_key,value in countDict.items():
			if value > 5 and cnt_key not in cacheItems:
				cacheItems.append(cnt_key)
			if value <= 3 and cnt_key in cacheItems:
				cacheItems.remove(cnt_key)
	if len(cacheItems) == 0:
		return [-1]
	cacheItems.sort()
	return cacheItems
	
q = [[1,1],[2,1],[3,1],[4,2],[5,2],[6,2]]

print(prioirtyQueue(q))
			
		
		
	