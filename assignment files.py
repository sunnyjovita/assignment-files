exercise 1
import re
def find_hapax(filename):
    file = open(filename)
    words = re.findall('\w+', file.read().lower())
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print(word)
print(find_hapax("empress_of_austria_and_queen_of_hungary.txt"))

exercise 2
def appendLine(inputFile, outputFile):
    new_text = ""
    num = 1
    for line in open(inputFile):
        new_text += f"{num}. {line}"
        num += 1
    with open(outputFile, "w+") as new_file:
        new_file.write(new_text)
print(appendLine("input.txt", "output.txt"))

exercise 3
import re
def cal_average(filename):
    file = open(filename)
    words = re.findall("\w+", file.read())
    return sum([len(words) for word in words]) / len(words)
print(cal_average("empress_of_austria_and_queen_of_hungary.txt"))

exercise 4
import re
def poke_names(file_name):
	with open(file_name, 'r') as f:
		names = re.findall(r'\w+', f.read())
	longest_series, current_series = [], []
	def name_starts_with(lastletter, names):
		for index, name in enumerate(names):
			if name.startswith(lastletter):
				return index
		return False
	for name in names:
		current_name = name
		current_series.append(current_name)
		namelist = names[:]
		namelist.pop(namelist.index(current_name))
        # Remove the first name from the list
		index = name_starts_with(current_name[-1], namelist)
		while index is not False:
			current_name = namelist[index]
			current_series.append(current_name)
			namelist.pop(index)
			index = name_starts_with(current_name[-1], namelist)
		if len(current_series) > len(longest_series):
			longest_series = current_series
		current_series = []
	print(longest_series)
print(poke_names("pokemon.txt"))

exercise 5
import re
def sentanceSplitter(filename):
    with open(filename, "r") as f:
        split_sentence = f.read()
    sentences = re.sub(r"(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])", r".\n\1", split_sentence)
    sentences = re.sub(r"!\s", "!\n", sentences)
    sentences = re.sub(r"\?\s", "?\n", sentences)
    return sentences
print(sentanceSplitter("splitter.txt"))