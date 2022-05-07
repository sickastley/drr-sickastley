import csv

temp = []
chodi = []
sent = []

with open("chodi.csv", "r") as file:
	csv1 = csv.reader(file)
	for row in csv1:
		chodi.append(row[0])

with open("sent.csv", "r") as file:
	csv1 = csv.reader(file)
	for row in csv1:
		sent.append(row[0])

for item in chodi:
	if item not in sent:
		temp.append(item)

print(f"{len(temp)} new Users.")