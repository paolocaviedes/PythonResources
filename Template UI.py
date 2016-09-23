
import Tkinter, Tkconstants, tkFileDialog 
import Image, ImageTk
import datetime
import time
import ttk
import os


clear=lambda:os.system('cls')

imagenAnchuraMaxima=640
imagenAlturaMaxima=200

# abrimos una imagen
img = Image.open('bannermayorista.jpg')

# modificamos el tamano de la imagen
#img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)


class TkFileDialogExample(Tkinter.Frame):
 
   def __init__(self, root):
 
     Tkinter.Frame.__init__(self, root)     

    
 
     # options for buttons
     button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
 
     # define buttons
     Tkinter.Button(self, text='Seleccionar archivo', command=self.askopenfile).pack(**button_opt)
     #Tkinter.Button(self, text='askopenfilename', command=self.askopenfilename).pack(**button_opt)
#    Tkinter.Button(self, text='asksaveasfile', command=self.asksaveasfile).pack(**button_opt)
#    Tkinter.Button(self, text='asksaveasfilename', command=self.asksaveasfilename).pack(**button_opt)
#    Tkinter.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)
 
     # define options for opening or saving a file
     self.file_opt = options = {}
     options['defaultextension'] = '.txt'
     options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
     options['initialdir'] = 'C:\\'
     options['initialfile'] = 'myfile.txt'
     options['parent'] = root
     options['title'] = 'Sistema generador de reportes para CDRs'
 
     # This is only available on the Macintosh, and only when Navigation Services are installed.
     #options['message'] = 'message'
 
     # if you use the multiple file version of the module functions this option is set automatically.
     #options['multiple'] = 1
 
     # defining options for opening a directory
     self.dir_opt = options = {}
     options['initialdir'] = 'C:\\'
     options['mustexist'] = False
     options['parent'] = root
     options['title'] = 'Generador de reportes CCAF'
 
   def askopenfile(self):


    """Returns an opened file in read mode."""
    #ejecutar lectura
    filename = tkFileDialog.askopenfilename(**self.file_opt)
    #print filename
    #source=tkFileDialog.askopenfile(mode='r', **self.file_opt)


    source=open(filename,"r")

    countfile=0.0
    countlines=0.0
    lastavance=0

    for linea in source:
        countfile+=1.0
    source.close()

    for linea in archivo:


        if countlines>0:
            
                


        avance= int((countlines/countfile)*100)
        countlines+=1
        #print linea

        if lastavance!=avance:
            lastavance=avance
            #print avance
            #return avance, countlines,countfile
            pb.step()
            pb.update()

        #time.sleep(.01)

    

        
    ttk.Label(self, text="Turnos generados con exito").grid(row=1, column=1)

        #print linea 
 
     #return tkFileDialog.askopenfile(mode='r', **self.file_opt)
 
   def askopenfilename(self):
 
     """Returns an opened file in read mode.
     This time the dialog just returns a filename and the file is opened by your own code.
     """
 
     # get filename
     filename = tkFileDialog.askopenfilename(**self.file_opt)
 
     # open file on your own
     if filename:
       return open(filename, 'r')
 
#  def asksaveasfile(self): 
#   """Returns an opened file in write mode.""" 
#  return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)
 
#   def asksaveasfilename(self): 
#     """Returns an opened file in write mode.
#     This time the dialog just returns a filename and the file is opened by your own code.
#     """ 
#     # get filename
#     filename = tkFileDialog.asksaveasfilename(**self.file_opt) 
     # open file on your own
#     if filename:
#       return open(filename, 'w')
 
#   def askdirectory(self): 
#     """Returns a selected directoryname.""" 
#     return tkFileDialog.askdirectory(**self.dir_opt)

if __name__=='__main__':
   root = Tkinter.Tk()

   root.iconbitmap('py.ico')


   # Convertimos la imagen a un objeto PhotoImage de Tkinter
   tkimage = ImageTk.PhotoImage(img)
   # Ponemos la imagen en un Lable dentro de la ventana
   label= Tkinter.Label(root, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima).pack()
   root.title("Sistema de Generacion de turnos para RM10")

   pb = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")         


   pb.pack()

   TkFileDialogExample(root).pack()
   #ttk.Label(self, text="Generando reportes, por favor espere... - "+  str(avance)+ "%  - "+ str(countlines) + " lineas leidas de "+ str(countfile)+".").grid(row=1, column=1)
   

   root.mainloop()