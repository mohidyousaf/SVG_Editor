from tkinter import *
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk, ImageGrab, ImageDraw, ImageFont
from  tkinter import  filedialog
import sys
import svgutils.transform as sg
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
registerFont(TTFont('Times-Roman','times-roman.ttf'))

# drawing = svg2rlg("test.svg")
# renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
# img = Image.open('temp.png')
# title_font = ImageFont.truetype('font.ttf', 200)
# image_editable = ImageDraw.Draw(img)
# image_editable.text((0,0), "Text goes here", (0, 219, 237), align='left')
img= Image.new('RGB', (400,400))
fig= sg.SVG
# fig= sg.fromfile('test.svg')
# txt= sg.TextElement(5,12, "mohid", size=3)
# fig.append(txt)
# fig.save("final.svg")

root = Tk()
root.geometry("600x300")
root.title("SVG Editor")

def quit():
    sys.exit()

def upload():
    # upload functionality here
    print('ready to upload')
    global img,fig
    imgname= filedialog.askopenfilename(title='open')
    fig = sg.fromfile(imgname)
    # print(imgname)
    if imgname:
        drawing = svg2rlg(imgname)
        renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
        img = Image.open('temp.png')
        displayimage(img)

def save():
    global img, fig
    # fig.save('test.svg')
    imgname= filedialog.asksaveasfilename(title='save', defaultextension='.svg')
    print(imgname)
    if imgname:
        fig.save(imgname)
    pass

def getLabel():
    global img, fig
    val= labelValue.get()
    print(f"label is {val}")
    # image_editable = ImageDraw.Draw(img)
    # image_editable.text((0, 0), val, (0, 219, 237), align='left')
    txt = sg.TextElement(5, 12, val, size=5)
    fig.append(txt)
    fig.save("final.svg")
    save()

# gui logic
# frame = Frame(root, bg="grey", relief=SUNKEN)
# frame.pack(side=LEFT, anchor="nw")


def displayimage(img):

    img= img.resize((100,100))
    pimg = ImageTk.PhotoImage(img)
    panel.configure(image=pimg)
    panel.image=pimg
    panel.label='hello'
    size = img.size


panel= Label(root, bg= 'white', text='hello')
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)

# frame = Canvas(root, width=size[0], height=size[1])
# frame.pack()
# frame.create_image(0, 0, anchor='nw', image=pimg)
#
#


m1= Menu(root)
m1.add_command(label='Open', command= upload)
m1.add_command(label="Exit", command=quit)
root.config(menu=m1)
#
b1 = Button(fg="red", text='Upload SVG', pady=14, command=upload)
b1.grid(row=0, column=2)

label = Label(root, text="Enter label for SVG", pady=20)
label.grid(row=1, column=1)

labelValue= StringVar()

labelEntry= Entry(root, textvariable= labelValue)
labelEntry.grid(row=1, column=2)

Button(text="Confirm Label and Save", command=getLabel).grid(row=2,column=2)

root.mainloop()
