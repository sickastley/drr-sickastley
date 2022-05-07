import csv

def addWords(doc):

	wordList = []

	with open(doc, "r") as file:
		csv1 = csv.reader(file)

		for row in csv1:
			wordList.append(row)

		wordList = wordList[1: ]

	while True:
		text = input()
		if text != "":
			word, alternative = text.split(' ')
			word = word.capitalize()

			alternative = alternative.capitalize()
			wordList.append([word, alternative])

		else: break

	temp = []
	[temp.append(x) for x in wordList if x not in temp]

	wordList = temp

	wordList = sorted(wordList)
	wordList.insert(0, ["Word", "Alternative"])

	#push to csv
	with open(doc, "w", newline = '') as file:
		writer = csv.writer(file)

		for element in wordList:
			writer.writerow(element)

	print("Task completed.")

addWords("__hindi.csv")