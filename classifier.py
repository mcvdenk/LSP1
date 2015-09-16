# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# importeer de functies van de os bibliotheek.
import os, operator
import re

# define characters that are punctuation and should be deleted from the tweets.
punctuation = ".,:;/\\|\"!'@#$%^&*()_-+=?”“’‘"
# declare two empty arrays to store the normalized words for females and males.
femaleData = []
maleData = []

# sample 'stopword list', words that do not provide relevant information while classifying.
# also, the word 'usermention' is added, because usermention refers to usernames, and these will not provide
# any relevant information for the classifier.
stopwords = ['het', 'een', 'aan', 'zijn', 'http', 'www', 'com', 'ben', 'jij', 'hmm', 'uhm', 'ehm', 'dus', ...,
			'maar', 'want', 'joh', 'ofzo', 'nou', 'eigenlijk', 'usermention']

# ga naar de goede directory
os.chdir('C:\\Users\\SANNE\\Documents\\UT_ZAKEN\\Huidig\\SLP1\\twitter\\train')

# set the train file directory to current directory
TFD = os.curdir

def openTweets():
	allTweetFiles = os.listdir(TFD)
	#open('F-train1.txt', errors='replace')
	for file in allTweetFiles:
		if file.startswith("M"):
			writeWordsToArray(file,maleData)
		elif file.startswith("F"):
			writeWordsToArray(file,femaleData)
		else:
			print("Loading failed")

# A function to write the words in the Tweets to an array for males and females (see function openTweets).
def writeWordsToArray(file, arr):
	# open the textfile.
	textFile = open(file, errors='replace')
	# split the text into lines.
	lines = textFile.read().splitlines()
	# close the textfile. we do not need it anymore here, because we now use textLines.
	textFile.close()
	# create an empty array to store normalized words.
	wordFile = []

	# lets loop over all lines in the text
	for line in lines:
		for w in words(line):
			if w != '':
				# delete punctuation.
				w = w.strip(punctuation)
				# append word w to wordFile[].
				wordFile.append(w)
	# append normalized words array to either male or female array.
	arr.append(wordFile)

# simple word splitter. \W+ means at least one any alphanumeric character.
pattern = re.compile('\W+')
	
# the function words() splits the text into lowercase words, not in the list of stopwords (see above) and if the word
# is longer or equal to three characters, because words that are too short won't add meaningful information to classifier.
def words(message):
	# use pattern to split text into words.
	tokens = pattern.split(message)
	# lowercase all words.
	tokens = map(lambda w: w.lower(), tokens)
	# filter out words that are in the list of stopwords.
	tokens = filter(lambda w: w not in stopwords, tokens)
	# filter out words that are shorter than three characters.
	tokens = filter(lambda w: len(w) > 2, tokens)
	return tokens

# 4 - Vocabulary

def nGramCount(input, n):
	nGrams = {}
	# do this for both male and female
	for files in input:
		# check for all files
		for file in files:
			#loop through all words in file
			for i in range(n-1,len(file)):
			#	declare a nGram string to store N-gram in
				nGram = ""
				for j in range(0,n):
					if j == 0:
						nGram = file[i-j] + nGram
					else:
						# add words and include a space
						nGram = file[i-j] + " " + nGram
				# keep track of the freq of occurrence of that N-gram
				if nGram in nGrams:
					nGrams[nGram] += 1
				else:
					nGrams[nGram] = 1
	# sort the nGrams and reverse the sorting, to get nGrams that occur most first.
	# key=operator.itemgetter(1), to get the counts of the nGrams.
	sorted_nGrams = sorted(nGrams.items(), key=operator.itemgetter(1), reverse=True)
	return sorted_nGrams
	
def vocabulary():
	# loop to do this for 1-Grams, 2-Grams and 3-Grams
	for i in range(1,4):  
		sorted_NGrams = nGramCount([maleData,femaleData],i)
		# print a top 10 of most frequently observed nGrams
		for j in range(0,11):
			print(sorted_NGrams[j])
		
		# print number of N-grams that occur 1 to 4 times.
		for j in range(1,5):
			count = 0;
			for word in sorted_NGrams:
				if word[1] == j:
					count += 1
			print("Number of " + str(i) + "-grams that occur " + str(j) + " times: " + str(count))
		print("Number of unique " + str(i) + "-grams : " + str(len(sorted_NGrams)))
		print("")

## TODO 


#  Text classification using a unigram language model
#  Characteristic words
		
openTweets()
vocabulary()


