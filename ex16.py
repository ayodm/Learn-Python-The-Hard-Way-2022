#close - closes the file, the equivalent of saving a file
#read - reads the contents of the file and also allows you to assing the result to a variable
#readline - reads just one line of a text file. 
#truncate -  empties the file 
#write('stuff') - write "stuff" to the file 
#seek(0) - move the read/write location to the beginning of the file. 


from sys import argv 

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file..")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("And finally, we close it.")
target.close()
