#task1:

file = open("sample.txt",'r')
reading_file = file.read()
print(reading_file)
file.close()

#task2:
file = open("output.txt",'w')
writing_file = file.write("welcome to the world of python")

file.close()



file = open("output.txt",'a')
appending_file = file.write(" learning file handling in the python")

file.close()

file = open("output.txt",'r')
reading_file = file.read()
print(reading_file)
file.close()
