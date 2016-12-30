import os
import glob


def get_num(filename):
	with open(filename) as f:
		with open("output.txt", "a") as text_file:
			text_file.write("\n\nNumbers in %s file"%filename)
			for line in f: ## read every textfile line by line
				line_list = line.split() ## covert all words in a line to list item
				for item in line_list:
					item = item.replace("+91", "").replace("-", "") ## remove +91 from the beginning of a number for example "+918290093302 = 8290093302"
					item = item.replace("(", "").replace(")", "")
					if len(item) == 10 and item.isdigit():
						if item.startswith("7") or item.startswith("8") or item.startswith("9"): ## indian Mobile numbers startswith 7, 8 or 9 
							text_file.write("\n%s\n" %item) ## write the numbers in output.txt
							print item


if __name__ == "__main__":
	path  = os.getcwd()  ## getcwd() will give the current working directory.
	## if there is output file already there then delete it to get the new output file everytime script is run. 
	try:
		os.remove(os.path.join(path, "output.txt"))
	except Exception as e:
		pass

	map(get_num, glob.glob(os.path.join(path, "test_directory/*.txt"))) ## map every text file to get_num() function to get all the numbers.


