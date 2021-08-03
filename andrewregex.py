import re 
fin=open("C:/Users/Ryzen-1700X/Desktop/Andrew/andrew.txt","r",encoding="utf-8") 
fout=open("C:/Users/Ryzen-1700X/Desktop/Andrew/andrewo.txt","w",encoding="utf-8") 
fintext=fin.read() 
x= re.sub(r"\[(.*)\]\n(.*)", r"\1 \2", fintext)
fout.write(x) 
fin.close() 
fout.close() 