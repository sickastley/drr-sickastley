import csv
import argparse

parser = argparse.ArgumentParser(description = "Dharmo Rakshati Rakshitah")

parser.add_argument("-f1", "--file1", 
	dest = "file1", 
	default = None, 
	help = "First file")

parser.add_argument("-f2", "--file2", 
	dest = "file2", 
	default = None, 
	help = "Second file")

args = parser.parse_args()

file1 = args.file1
file2 = args.file2

def adduser(user, File):
	with open(File, "a", newline = '') as file:
		writer = csv.writer(file)
		temp = []
		temp.insert(0, [user])
		for item in temp:
			writer.writerow(item)

data1 = []
data2 = []

with open(file1, "r") as file:
	csv1 = csv.reader(file)
	for row in csv1:
		data1.append(row[0])

with open(file2, "r") as file:
	csv1 = csv.reader(file)
	for row in csv1:
		data2.append(row[0])

for item in data2:
	if item not in data1:
		adduser(item, file1)
