from tkinter import *



root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
photo=PhotoImage(file="cutters.png")
redbutton = Button(frame,  image = photo, text="cutters")
redbutton.pack( side = LEFT)

photo1=PhotoImage(file='plane.png')
greenbutton = Button(frame, image = photo1, padx=200,  pady=100,   text="plane", fg="brown")
greenbutton.pack( side = LEFT )

photo2=PhotoImage(file='hammer.png')
bluebutton = Button(frame, image = photo2,  text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

photo3=PhotoImage(file='wrench.png')
blackbutton = Button(frame, image = photo3,  text="Black", fg="black")
blackbutton.pack( side = LEFT)

photo4=PhotoImage(file='measure.png')
orangebutton = Button(frame, image = photo4)
orangebutton.pack()

photo5=PhotoImage(file='plyers.png')
plyersbutton = Button(frame, image = photo5)
plyersbutton.pack()
                  

root.mainloop()





##cutters.png
##hacksaw.png
##hammer.png
##handsaw.png
#measure.png
##plane.png
##plyers.png
##powerdriver.png
##screwdriver.png
##wrench.png
