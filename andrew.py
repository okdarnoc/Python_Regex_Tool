fin=open("C:/Users/Ryzen-1700X/Desktop/Andrew/andrew.txt","r",encoding="utf-8")
fout=open("C:/Users/Ryzen-1700X/Desktop/Andrew/andrewo.txt","w",encoding="utf-8")
fintext=fin.read() 
fout.write(fintext.replace('[The witness]\n','Edwin '))
fin.close()
fout.close()


