import os
import re
def main():
	f = open("list.txt","r")
	f1 = f.readlines()
#	f1 = f1.rstrip('\n')
	f1 = [(el.strip()) for el in f1]
	f1[:] = [item for item in f1 if item != '']	
	print(f1)
	for line in f1:
		os.makedirs(line, exist_ok=True)
	f.close()
main()
