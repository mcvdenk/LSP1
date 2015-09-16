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
	for i in range(len(tokens)-n+1):
		ngram = ""
		for j in range(n):
			ngram.append(tokens[i+j])
			if j<n-1: ngram.append(" ")
	return ngrams
			
def tally(ngrams):
	c = Counter()
	for ngram in ngrams:
		c[ngram] += 1
	return c

#def mergeTallies(list):

openData()
line = fData['F-train1.txt']
tokens = lineToTokens(line)
print(tally(tokens))


