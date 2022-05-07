import csv
import os
import sys

wordList = []

with open("test.csv", "r") as file:
	data = csv.reader(file)
	
	for row in data:
		wordList.append(row)

print(wordList)




