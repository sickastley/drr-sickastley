import csv

counter = 0

readFile1 = []

with open('data.csv', 'r') as file:

	csv1 = csv.reader(file)

	for item in csv1:
		readFile1.append(item)

readFile2 = []

with open('librandu.csv', 'r') as file:

	csv1 = csv.reader(file)

	for item in csv1:
		readFile2.append(item)

for i in readFile1:
	for j in readFile2:
		if i[0] == j[0]:
			counter += 1

print(counter)