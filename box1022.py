from tkinter import *



root = Tk()
frame = Frame(root)
frame.grid()

bottomframe = Frame(root)
bottomframe.grid( )
photo=PhotoImage(file="cutters.png")
redbutton = Button(frame,  image = photo)
redbutton.grid(row=0, column=0 )

photo1=PhotoImage(file='plane.png')
greenbutton = Button(frame, image = photo1)
greenbutton.grid(row=0,  column=1
)

photo2=PhotoImage(file='hammer.png')
bluebutton = Button(frame, image = photo2)
bluebutton.grid(row=0, column=2
)

photo3=PhotoImage(file='wrench.png')
blackbutton = Button(frame, image = photo3)
blackbutton.grid(row=1,  column=0)

photo4=PhotoImage(file='measure.png')
orangebutton = Button(frame, image = photo4)
orangebutton.grid(row=1, column=1)

photo5=PhotoImage(file='plyers.png')
plyersbutton = Button(frame, image = photo5)
plyersbutton.grid(row=1, column=2)
                  

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
