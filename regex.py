# The line import re, re is a python library which allow python to carry out regular expression operations.
import re 

# Tin is a customize name, we use tin to be a variable to open 'input.txt', input.txt must be located with the same folder as the script. 
# The reason of doing this is simple, if we don't open a file, we cannot read or write.
tin=open('input.txt',"r",encoding="utf-8") 

# Tout is a customize name, we use tin to be a variable to open 'output.txt', input.txt must be located with the same folder as the script.
# The reason of doing this is simple, if we don't open a file, we cannot read or write.
tout=open('output.txt',"w",encoding="utf-8") 

# tintext is a customize name, we use tintext to be a variable to read tin (The read() method returns the specified number of bytes from the file).
tintext=tin.read() 

# x is a customize name, we use x to store the results of re.sub manipulation of the data in tintext.
# There are 3 input in re.sub 
# 1. Pattern [Recognized Pattern]
# 2. Replacement Patter [Replacement Patter, repl]
# 3. The input [String]
# In our function x, we are telling them we want to look for a pattern r"\[(.*)\]\n(.*)" in tintext and replace it with pattern r"\1 \2"
x= re.sub(r"\[(.*)\]\n(.*)", r"\1 \2", tintext)

# Once we have finished all the operation, its store in the computer's ram, we have to ask the computer to store it into the file we want.
# Threfore we have to use the function write. 
# This line basically means in tout we erase whats on there and write x to it. X is the result of re.sub manipulation of the data in tintext.
tout.write(x) 

# Here we close our files.
tin.close() 
tout.close() 