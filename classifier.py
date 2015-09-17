# -*- coding: utf-8 -*-

import os
import re

trainDir = "./train/"
testDir = "./test/"

mData = {}
fData = {}
mTokens = {}
fTokens = {}
p = re.compile("[.,'\":;!@#$%^&*()_\-+=?/|\u201C\u201D\u2018\u2019]")

class Counter(dict):
	def __missing__(self, key):
		return 0

def openData():
	allData = os.listdir(trainDir)
	allData.sort()
	for file in allData:
		if file.startswith("M"):
			mData[file] = fileToEntry(trainDir + file)
		elif file.startswith("F"):
			fData[file] = fileToEntry(trainDir + file)
		else:
			print("Loading of data failed")

def fileToEntry(fileName):
	tweetFile = open(fileName, errors='replace')
	return tweetFile.read().encode('ascii','ignore').decode('ascii')

# def dictToLines(dic):
	# lines = []
	# for key in dic:
		# lines.append(dic[key].splitlines())
	# return lines
	
def lineToTokens(line):
	tokenArray = []
	tokens = line.split()
	for token in tokens:
		token = normalize(token)
		tokenArray.append(token)
	return tokenArray
	
def normalize(str):
	normWord = str.lower()
	normWord = p.sub("", normWord)
	return normWord

def tokenToNgram(tokens, n):
	ngrams = []
	for i in range(n-1, len(tokens)):
		ngram = ""
		for j in range(0, n):
			if j == 0:
				ngram = tokens[i-j] + ngram
				ngrams.append(ngram)
			else:
				ngram = tokens[i-j] + " " + ngram
				ngrams.append(ngram)
	return ngrams

def tally(ngrams):
	c = Counter()
	for ngram in ngrams:
		c[ngram] += 1
	return c

#def mergeTallies():
	
openData()

for key in mData.items():
	lineToTokens(mData[key])

for key in fData.items():
	lineToTokens(fData[key])

for i in range(1,4):
	ngrams = tokenToNgram([mData, fData], i)
	tally(ngrams)




