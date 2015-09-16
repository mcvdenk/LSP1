import os

trainDir = "./train/"
testDir = "./test/"

mData = {}
fData = {}

def openData():
	allData = os.listdir(trainDir)
	allData.sort()
	for file in allData:
		if file.startswith("M"):
			fileToMap(trainDir + file,mData)
		elif file.startswith("F"):
			fileToMap(trainDir + file,fData)
		else:
			print("We tried to do some loading but, well it failed!")

def fileToMap(fileName, dic):
	tweetFile = open(fileName, errors='replace')
	dic[fileName] = tweetFile.read().encode('ascii','ignore').decode('ascii')
			
openData()
print(len(fData))