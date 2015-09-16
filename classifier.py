import os

trainDir = "./train/"
testDir = "./test/"

mData = {}
fData = {}
mTokens = {}
fTokens = {}

punct = ".,'\":;!@#$%^&*()_-+=?/|\\”“’‘"

def openData():
	allData = os.listdir(trainDir)
	allData.sort()
	for file in allData:
		if file.startswith("M"):
			mData[file] = fileToEntry(trainDir + file)
		elif file.startswith("F"):
			fData[file] = fileToEntry(trainDir + file)
		else:
			print("We tried to do some loading but, well it failed!")

def fileToEntry(fileName):
    tweetFile = open(fileName, errors='replace')
	return tweetFile.read().encode('ascii','ignore').decode('ascii')

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

def tokenToNgram(tokens, n):
    	ngrams = []
    for i in range(len(tokens)-n+1):
        ngram = ""
        for j in range n:
            ngram.append(tokens[i+j])
            if j<n-1: ngram.append(" ")
            
def tally(ngrams):
    dict = {}
    for ngram in ngrams:
        dict[ngram] += 1
    return dict

def mergeTallies(list):

openData()

