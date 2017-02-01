#!usr/bin/python3

def main():
	DIGITS = input("Enter number of digits: ")
	maxCombo = 10**int(DIGITS)
	f = open("combos.txt", "w")
	for i in range(maxCombo):
		difference = int(DIGITS)-len(str(i))
		zeros = "0"*difference
		print(zeros + (str(i)), file=f)
	f.close()
	


if __name__ == "__main__": main()