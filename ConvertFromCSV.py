import csv
questionFile = open('Questions.csv')
questionReader = csv.reader(questionFile)
questionData = list(questionReader)
string = ""
finalData = []
for data in questionData:
	string += 'questions.Add(new Question ( Convert.ToDateTime("' + data[0] + '")'
	data.pop(0)
	for s in data:
		string += ', "' + s + '"'
	string += "));\n"
file = open('C:\\Users\\KAdmin\\Documents\\PythonPrograms\\BibleTriviaConvertCSV\\QuestionsCode.txt', 'w')
file.write(string)
file.close()