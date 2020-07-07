from Tkinter import *
import tkFont
import ttk 
import RPi.GPIO as GPIO
txA= 37
txB= 31
txC= 33
txD= 35
txE= 29
GPIO.setmode(GPIO.BOARD)
GPIO.setup(txA, GPIO.OUT)
GPIO.setup(txB, GPIO.OUT)
GPIO.setup(txC, GPIO.OUT)
GPIO.setup(txD, GPIO.OUT)
GPIO.setup(txE, GPIO.OUT)

root = Tk()
root.title("SRT INTERCOM - MASTER CH 10")
root.config(cursor="none")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.rowconfigure(1, weight=1)  # make buttons stretch when
root.rowconfigure(2, weight=1)  # make buttons stretch when
root.rowconfigure(3, weight=1)  # make buttons stretch when
style = ttk.Style()
style.configure('.',background ='red')
#style.map("C.TButton",
 #   foreground=[('pressed', 'white'), ('active', 'white')],
  #  background=[('pressed', 'green'), ('active', 'green')]
   # ) 

style.map("green.TButton", background = [('!active','green'),('pressed', 'green'), ('active', 'green')])
style.map("red.TButton",   background = [('!active','red'),('pressed', 'red'), ('active', 'red')])
style.map("white.TButton",   background = [('!active','white'),('pressed', 'white'), ('active', 'white')])



root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
root.configure(bg='white')

# adding image (remember image should be PNG and not JPG) 
img = PhotoImage(file = r"/home/pi/master-gui/image2.png") 
img1 = img.subsample(1, 1) 
  
#root.rowconfigure(1, weight=1)  # make buttons stretch when
#root.columnconfigure((0,1), weight=1)  # when window is resized
Label(root, image = img1, bg='white').grid(row = 0, column = 0,
       columnspan = 3, rowspan = 1, sticky='EWNS', padx = 0, pady = 0)



# tkFont.BOLD == 'bold'
helv14 = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)
helv36 = tkFont.Font(family='Helvetica', size=22, weight=tkFont.BOLD)


#callbacks

mutedA = TRUE
mutedB = TRUE
mutedC = TRUE
mutedD = TRUE
mutedE = TRUE


def mute_A():
    global mutedA
    if mutedA:  # Unmute the music
#        mixer.music.set_volume(0.7)
        btn2.configure(image=volumePhoto)
	btn2.configure(style="green.TButton")
        GPIO.output(txA, True)

#        scale.set(70)
        mutedA = FALSE
    else:  # mute the music
#        mixer.music.set_volume(0)
        btn2.configure(image=mutePhoto)	
        btn2.configure(style="red.TButton")
        GPIO.output(txA, False)  
#        scale.set(0)
        mutedA = TRUE

def mute_B():
    global mutedB
    if mutedB:  # Unmute the music
#        mixer.music.set_volume(0.7)
        btn3.configure(image=volumePhoto)
	btn3.configure(style="green.TButton")	
        GPIO.output(txB, True)
#        scale.set(70)
        mutedB = FALSE
    else:  # mute the music
#        mixer.music.set_volume(0)
        btn3.configure(image=mutePhoto)
        btn3.configure(style="red.TButton")
        GPIO.output(txB, False) 
#        scale.set(0)
        mutedB = TRUE

def mute_C():
    global mutedC
    if mutedC:  # Unmute the music
#        mixer.music.set_volume(0.7)
        btn4.configure(image=volumePhoto)
	btn4.configure(style="green.TButton")
        GPIO.output(txC, True)  
#        scale.set(70)
        mutedC = FALSE
    else:  # mute the music
#        mixer.music.set_volume(0)
        btn4.configure(image=mutePhoto)
        btn4.configure(style="red.TButton")
        GPIO.output(txC, False) 
#        scale.set(0)
        mutedC = TRUE

def mute_D():
    global mutedD
    if mutedD:  # Unmute the music
#        mixer.music.set_volume(0.7)
        btn5.configure(image=volumePhoto)
#        scale.set(70)
	btn5.configure(style="green.TButton")
        GPIO.output(txD, True)
        mutedD = FALSE
    else:  # mute the music
#        mixer.music.set_volume(0)
        btn5.configure(image=mutePhoto)
        btn5.configure(style="red.TButton")
        GPIO.output(txD, False) 
#        scale.set(0)
        mutedD = TRUE
def mute_E():
    global mutedE
    if mutedE:  # Unmute the music
        btn1.configure(image=speakerPhoto)
        btn1.configure(style="white.TButton")
        GPIO.output(txE, True)
        mutedE = FALSE
    else:
        btn1.configure(image=headPhoto)
        btn1.configure(style="white.TButton")
        GPIO.output(txE, False)
        mutedE = TRUE



mutePhoto = PhotoImage(file='/home/pi/master-gui/mute.png')
volumePhoto = PhotoImage(file='/home/pi/master-gui/volume.png')
headPhoto = PhotoImage(file='/home/pi/master-gui/headset.png')
speakerPhoto = PhotoImage(file='/home/pi/master-gui/speaker.png')
Label1 = Label(root, text="MST U",bg="white",font=helv36)
Label2 = Label(root, text="EST 1",bg="white",font=helv36)
Label3 = Label(root, text="EST 2",bg="white",font=helv36)
Label4 = Label(root, text="TOM A",bg="white",font=helv36)
btn1 = ttk.Button(text='Est 1', image=speakerPhoto,command=mute_E,style="white.TButton")
btn2 = ttk.Button(text='Est 1', image=mutePhoto,command=mute_A,style="red.TButton")
btn3 = ttk.Button(text='Est 1', image=mutePhoto,command=mute_B,style="red.TButton")
btn4 = ttk.Button(text='Est 1', image=mutePhoto,command=mute_C,style="red.TButton")
btn5 = ttk.Button(text='Est 1', image=mutePhoto,command=mute_D,style="red.TButton")

#root.rowconfigure((0,1), weight=1)  # make buttons stretch when
#root.columnconfigure((0,2), weight=1)  # when window is resized

Label1.grid(row=1, column=0, columnspan=1, sticky='EWNS')
Label2.grid(row=1, column=1, columnspan=1, sticky='EWNS')
Label3.grid(row=1, column=2, columnspan=1, sticky='EWNS')
Label4.grid(row=1, column=3, columnspan=1, sticky='EWNS')
btn1.grid(row=0,column=3, columnspan=1,sticky='EWNS')
btn2.grid(row=2, column=0, columnspan=1, sticky='EWNS')
btn3.grid(row=2, column=1, columnspan=1, sticky='EWNS')
btn4.grid(row=2, column=2, columnspan=1, sticky='EWNS')
btn5.grid(row=2, column=3, columnspan=1, sticky='EWNS')

# button 1
#btn1 = ttk.Button(root, text = 'Quit !',style="C.TButton")
#btn1.grid(row = 0, column = 1, columnspan=2)

# button 2
#btn6 = ttk.Button(text="Test", style="C.TButton")
#btn6.grid(row = 0, column = 2, pady = 10, padx = 100)




root.mainloop()
