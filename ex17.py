from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)


print("Alright, all done.")

out_file.close()
in_file.close()

#don't forget to make a sample file using command line 
#example: echo "This is a test file." > test.txt
#Then examine it -->test.txt

#Run the script ex17.py test.txt new_file.txt
# When running in win10 terminal type the following 
# "py ex17.py test.txt new_file.txt"