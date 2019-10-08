#Feature Labs Playlist Python 3

import sys


class MP3():
	def __init__(self):
		pass
	def playList(self,songs,k,q):
		# As the songs have duplicates we can go to the one which is nearest
		indexList = []
		indexList = [i for i in range(len(songs)) if songs[i] == q]
		#get minimum of both the directions of songs
		upward = sys.maxsize
		downward = -sys.maxsize-1
		res = sys.maxsize
		for i in indexList:
			upward = k+(len(songs)-i)
			downward = abs(i-k)%len(songs)
			res = min(upward,min(downward,res))
		return res
		
		
ol = MP3()
tc = ["wheniseeyouagain","borntorun","nothingelsematters","cecelia"]
print(ol.playList(tc,2,'borntorun'))
