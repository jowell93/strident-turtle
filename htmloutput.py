from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

root=Tk()
root.fileName=filedialog.askopenfilename(filetypes=(('Text files','*.txt*'),('All Files','*.*')))


myfile = open(root.fileName,"r",encoding='utf-8-sig')
outputfile = open("output.html","w")

data = myfile.read().split('\n')
list='<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<TITLE>Bookmarks</TITLE>\n"\n<H1>Bookmarks</H1>"\n<DL><p>\n<DT><H3 ADD_DATE="1485437532" LAST_MODIFIED="1489178177" PERSONAL_TOOLBAR_FOLDER="false">Bookmarks</H3>\n<DL><p>\n'
listend='</DL><p>\n</DL><p>'
outputfile.write(list)

for line in data:
	line=str(line)
	line = line.replace("\t", '" ADD_DATE='+ str('"1485276757"') + ">")
	line=line+"</A>"
	line='<DT><A HREF="' + line
	#print(line)
	outputfile.write(line+"\n")

outputfile.write(listend)
myfile.close()
outputfile.close()
### exec(open("C:\\Users\\jqm2402\\Documents\\strident-turtle\\htmloutput.py")).read()
