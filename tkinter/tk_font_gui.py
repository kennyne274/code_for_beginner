import tkinter
import tkinter.font as tkFont

# Creating the GUI window.
root = tkinter.Tk()
root.title("Tkinter Font Test") 
root.geometry("400x240")
  
# Creating our text widget.
sample_text = tkinter.Text(root, height =1)
sample_text.pack()
fontlist=list(tkFont.families())
fontindex=0

print(*fontlist,sep="\n")

def setTextInput():
    global fontindex,fontlist
    Font_tuple = (fontlist[fontindex], 20)
    sample_text.configure(font = Font_tuple)
    sample_text.delete(1.0,"end")
    sample_text.insert(1.0, fontlist[fontindex]+" : 한글")
    fontindex=(fontindex+1)%len(fontlist)

btnSet = tkinter.Button(root, 
                   height=1, 
                   width=10, 
                   text="Set", 
                   command=lambda:setTextInput())
btnSet.pack(side=tkinter.BOTTOM)
root.mainloop()
