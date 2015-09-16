import os

trainDir = "./train/"
testDir = "./test/"

mData = {}
fData = {}

punct = ".,'\":;!@#$%^&*()_-+=?/|\\”“’‘"

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

# def dictToLines(dic):
	# lines = []
	# for key in dic:
		# lines.append(dic[key].splitlines())
	# return lines
	
def lineToTokens(line):
	tokens = line.split()
	for token in tokens:
		token = normalize(token)
	return tokens
	
def normalize(str):
	return str.lower().strip(punct)

def tally(array, n):
	
openData()

