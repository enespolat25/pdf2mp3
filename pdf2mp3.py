from tkinter import * 
import tkinter as tk
from tkinter import filedialog
import os
import tkinter as tk
import tkinter.messagebox

from PyPDF4 import PdfFileReader
from gtts import gTTS


def Pdf_to_Audio(file_name):
	ilkSayfa=int(e3.get())-1
	ikinciSayfa=int(e4.get())
	pdf = PdfFileReader(file_name)
	#pdf.getNumPages()
	
	for page in range(ilkSayfa,ikinciSayfa):
		text = pdf.getPage(page).extractText()
		tts = gTTS(text=text, lang='tr')
		tts.save(f"{page+1}.mp3")
		tkinter.messagebox.showinfo("Bilgi",f"{page+1}.mp3"  + " yüklendi", icon='info')
		
		


def pdfYukle():
	fln= filedialog.askopenfilename(initialdir=os.getcwd(), title="Lütfen PDF dosyası seçiniz", filetypes=(("PDF File","*.pdf"),("All Files","*.*")))
	Pdf_to_Audio(fln)
	tkinter.messagebox.showerror("Bilgi","Tüm işlem  tamamlandı", icon='info')
	flist = os.listdir()
	#print(flist)
	var = tk.Variable(value=flist)
	listbox = tk.Listbox(root,listvariable=var,height=6,selectmode=tk.EXTENDED)
	listbox.grid(row=2, column=0)
	


root=Tk()
#root.attributes("-fullscreen", True)
root.title("PDF MP3 ÇEVİRİCİ")
root.geometry("600x300")
root.iconbitmap("icon.ico")


label1=Label(root, text="Hangi sayfalar arasını seslendirelim")
label1.grid(row=0, column=0, columnspan=1, padx=1, pady=8)
e3= Entry (root, width=8, borderwidth=2)
e3.grid(row=0, column=1,  padx=1, pady=8)

label1=Label(root, text="-")
label1.grid(row=0, column=2, columnspan=1, padx=1, pady=8)
e4= Entry (root, width=8, borderwidth=2)

e4.grid(row=0, column=3,  padx=1, pady=8)

btn=Button(root, text="PDF Kitap Yükle", command=pdfYukle)
btn.grid(row=1, column=0)

btn4=Button(root,text="Exit",command=lambda:exit())
btn4.grid(row=1, column=3)



"""
lbox=tk.ListBox(root)

for item in flist:
    lbox.insert(END, item)


lbox.grid(row=2, column=0)
"""

root.mainloop()