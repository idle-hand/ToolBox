from tkinter import *



root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
photo=PhotoImage(file="cutters.png")
redbutton = Button(frame,  image = photo, text="cutters", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

root.mainloop()



##C:/Users/david/Downloads/tool/box1006.py
##C:/Users/david/Downloads/tool/cutters.jpeg
##C:/Users/david/Downloads/tool/cutters.png
##C:/Users/david/Downloads/tool/driver.jpeg
##C:/Users/david/Downloads/tool/hacksaw.png
##C:/Users/david/Downloads/tool/hammer.jpeg
##C:/Users/david/Downloads/tool/hammer.png
##C:/Users/david/Downloads/tool/handsaw.jpeg
##C:/Users/david/Downloads/tool/handsaw.png
##C:/Users/david/Downloads/tool/jigsaw.jpeg
##C:/Users/david/Downloads/tool/measure.jpeg
##C:/Users/david/Downloads/tool/measure.png
##C:/Users/david/Downloads/tool/plane.jpeg
##C:/Users/david/Downloads/tool/plane.png
##C:/Users/david/Downloads/tool/plyers.jpeg
##C:/Users/david/Downloads/tool/plyers.png
##C:/Users/david/Downloads/tool/powerdriver.png
##C:/Users/david/Downloads/tool/ripsaw.jpeg
##C:/Users/david/Downloads/tool/screwdriver.jpeg
##C:/Users/david/Downloads/tool/screwdriver.png
##C:/Users/david/Downloads/tool/wrench.jpeg
##C:/Users/david/Downloads/tool/wrench.png
##C:/Users/david/Downloads/tool/box1005.py
