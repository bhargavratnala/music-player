import pygame,os,time,datetime
from tkinter import *
from tkinter import filedialog,messagebox
pygame.init()
n=1
i=0
vol=0
timenow='time  day:\n{}'.format(time.strftime('%H:%M:%S  %A'),datetime.date.today())
status=-1
musiclist=[]
path=''
cont=True
def choosemusic():
	global n,song
	song=filedialog.askopenfile()
	try:
		pygame.mixer.music.load(song)
		pygame.mixer.music.play()
		n=1
	except:
		messagebox.showwarning(title='formate error',message='please choose a mp3 file')
def addpath():
	global songname,path,musiclist
	for i in songname:
		musiclist.append(str(path+'/'+i))
def final():
	global path,tack,musiclist,cont
	path=str(tack.get())
	pathenter.destroy()
	file=open('./path.txt','w')
	file.write(path)
	file.close()
	count=False
	while count:
		continue
	count=True
	songname=os.listdir(path)
	addpath()
	cont=False
def cur_time():
	timenow='time  day:\n{}\nDate:\n{}'.format(time.strftime('%H:%M:%S  %A'),(datetime.date.today()).strftime('%B-%d-%y'))
	timeshow['text']=timenow
	rt.after(1000,cur_time)
'''def pathresetfun():
	pathenter=Tk()
	info=Label(pathenter, text='enter the path fixed path of file which containing only songs:')
	info.pack()
	tack=Entry(pathenter)
	tack.pack()
	ok=Button(pathenter,text='ok',command=final)
	ok.pack(side='bottom')
	pathenter.mainloop()
	while cont:
		continue
	cont=True
	file=open('./path.txt','w+')
	file.close()'''
try:
	file=open('./path.txt','r+')
	path=file.read()
	file.close()
	songname=os.listdir(path)
	addpath()
except:
	pathenter=Tk()
	info=Label(pathenter, text='enter the path fixed path of\n file which containing only songs:')
	info.pack()
	tack=Entry(pathenter)
	tack.pack()
	ok=Button(pathenter,text='ok',command=final)
	ok.pack(side='bottom')
	pathenter.mainloop()
	while cont:
		continue
	cont=True
def setvolume(e):
	vol=int(e)/100
	pygame.mixer.music.set_volume(vol)
def playpuse():
	global n
	if n%2==0:
		pygame.mixer.music.unpause()
		n+=1
	else:
		pygame.mixer.music.pause()
		n+=1
rt=Tk()
def zerovol():
	d.set(0)
	pygame.mixer.music.set_volume(0)
def loadmusic():
	global n,musiclist,i,status
	try:
		if status==1:
			status=-1
			pygame.mixer.music.load(musiclist[i])
			pygame.mixer.music.play()
		n=1
	except:
		messagebox.showwarning(title='file error',message='file not found \n or end of songs')
def playnext():
	global status,i
	status=1
	if (len(musiclist)-1)>=i:
		i+=1
	elif (len(musiclist)-1)==i:
		i=0
	loadmusic()
def playpreviou():
	global status,i
	status=1
	if (len(musiclist)*-1)<=i:
		i-=1
	elif len(musiclist)*-1==i:
		i=-1
	loadmusic()
def exit():
	rt.destroy()
pygame.mixer.music.load(musiclist[i])
pygame.mixer.music.play()
timeshow=Label(rt,text=timenow,bg='blue',fg='white',relief='solid',font='Times 7')
timeshow.grid(row=1,column=12)
pygame.mixer.music.set_volume(0.5)
d=Scale(rt,orient=HORIZONTAL,command=setvolume)
d.set(50)
makespace=Label(rt,text=' ')
makespace.grid(row=0,column=0)
d.grid(ipadx=35,ipady=32,row=8,column=12)
mutephoto=PhotoImage(file='mute.png')
mutebutton=Button(rt,image=mutephoto,text='mute',command=zerovol)
mutebutton.grid(ipadx=35,ipady=32,row=16,column=12)
nextphoto=PhotoImage(file='next.png')
h=Button(rt,image=nextphoto,text='play next',command=playnext)
h.grid(ipadx=35,ipady=32,row=32,column=24)
pausephoto=PhotoImage(file='play-button.png')
a=Button(rt,text='play/pause',image=pausephoto,command=playpuse)
a.grid(ipadx=35,ipady=32,row=32,column=12)
choosephoto=PhotoImage(file='choose-music.png')
previousphoto=PhotoImage(file='previous.png')
playprevious=Button(rt,image=previousphoto,text='play previous',command=playpreviou)
playprevious.grid(ipadx=50,ipady=47,row=32,column=1)
c=Button(rt,image=choosephoto,text='chose music',command=choosemusic)
c.grid(ipadx=35,ipady=32,row=24,column=12)
exitphoto=PhotoImage(file='logout.png')
f=Button(rt,image=exitphoto,text='exit',command=exit)
f.grid(ipadx=35,ipady=32,row=40,column=24)
my_name=Label(rt,text='app made by :-\nBhargav Ratnala',bg='black',fg='white',relief='solid',font='Times 6 bold')
my_name.grid(row=40,column=12,ipadx=20)
'''pathreset=Button(rt,text='reset path',command=pathresetfun)
pathreset.grid(row=40,column=0)'''
cur_time()
rt.mainloop()
