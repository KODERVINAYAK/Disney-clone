import tkinter as tk
from tkinter import CENTER, ttk
import fnmatch
import os
import heapq
from turtle import bgcolor
from ttkthemes import themed_tk
from pygame import mixer
from ttkthemes import themed_style
from mutagen.mp3 import MP3
import time

count = 0

favSongs = []
recentSongs = []
frequentSongs = []

def display_All():
    ListBox.delete(0,'end')
    global count
    for root, dir, files in os.walk(completepath):
        for filename in fnmatch.filter(files, pattern):
            count+=1
            ListBox.insert('end', filename)

def display_Favourites():
    ListBox.delete(0,'end')
    global favSongs,count
    count = 0
    for filename in favSongs:
        count+=1
        ListBox.insert('end', filename)

def display_Recents():
    ListBox.delete(0,'end')
    global recentSongs,count
    count = 0
    temp = recentSongs
    temp.reverse()
    for songs in temp:
        count+=1
        ListBox.insert('end', songs)

def display_Frequents():
    ListBox.delete(0,'end')
    global frequentSongs,count 
    count = 0
    temp = frequentSongs
    temp.reverse()
    for key,value in temp:
        count+=1
        ListBox.insert('end', value)

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x650")
canvas.config( bg = 'black')

style=themed_style.ThemedStyle()
style.theme_names()
style.theme_use('breeze')
style.configure("TScale",background="#8B6878")







toolbar = tk.Frame(canvas, bg = "#8B6878")
toolbar.pack(padx = 2, pady = 10)


allSongsButton = tk.Button(canvas, text = "All Songs", bg = "#8B8878", borderwidth = 0, command = display_All)
allSongsButton.pack(pady = 0,padx = 5, in_ = toolbar, side = 'left')

favSongsButton = tk.Button(canvas, text = "Favourite Songs", bg = "#8B8878", borderwidth = 0, command = display_Favourites)
favSongsButton.pack(pady = 0,padx = 5, in_ = toolbar, side = 'left')

recentSongsButton = tk.Button(canvas, text = "Recently Played", bg = "#8B8878", borderwidth = 0, command = display_Recents)
recentSongsButton.pack(pady = 0,padx = 5, in_ = toolbar, side = 'left')

frequentSongsButton = tk.Button(canvas, text = "Frequently Played", bg = "#8B8878", borderwidth = 0, command = display_Frequents)
frequentSongsButton.pack(pady = 0,padx = 5, in_ = toolbar, side = 'left')


TitleBox = tk.Label(canvas, text = "Song List : ", fg = "black", bg = "#8B8878", width = 100, anchor= 'w', font = ('Arial', 20))
TitleBox.pack(fill='both')



completepath = "/home/vinayak/Desktop/music/mp3/files"
pattern = "*.mp3"

mixer.init()

#images
play_from_start_img = tk.PhotoImage( file = "icons/play_from_start_img.png")
prev_img = tk.PhotoImage( file = "icons/prev_img.png")
stop_img = tk.PhotoImage( file = "icons/stop_img.png")
next_img = tk.PhotoImage( file = "icons/next_img.png")
play_img = tk.PhotoImage( file = "icons/play_img.png")
pause_img = tk.PhotoImage( file = "icons/pause_img.png")
remove_fav_img = tk.PhotoImage( file = "icons/remove_fav_img.png")
add_fav_img = tk.PhotoImage( file = "icons/add_fav_img.png")

DisplaySongsFrame = tk.Frame( canvas, bg = "#8B8878")
DisplaySongsFrame.pack(padx = 0, pady = 10)


ListBox = tk.Listbox(DisplaySongsFrame, fg = "black", bg = "#696969", width = 90, font = ('Comic Sans MS', 20))

scrolltool = tk.Scrollbar(DisplaySongsFrame, orient='vertical', command=ListBox.yview, bg='red', width=10)

ListBox['yscrollcommand']=scrolltool.set
scrolltool.pack(side = 'right', fill = 'y')
ListBox.pack(padx = 15, pady = 2, in_ = DisplaySongsFrame)


newFrame = tk.Frame(canvas, bg = '#8B7878')
newFrame.pack(padx = 2, pady = 10)

now_playingBox = tk.Label(canvas, text = "Now Playing : ", fg = "black", bg = "#8B7878", width = 10, anchor= 'w', font = ('Arial', 15))
now_playingBox.pack(fill='both', in_ = newFrame, side = 'left')

scale_bar = tk.Frame(canvas, bg = "#8B6878")
scale_bar.pack(padx = 2, pady = 10,anchor='center')

# time_elasped_label=tk.Label(canvas,text="00:00", fg = "black", bg = "#8B8878",padx = 5)
# time_elasped_label.pack(padx=10,pady=5,in_=scale_bar,side='left')


# music_duration_label=tk.Label(canvas,text="00:00", fg = "black", bg = "#8B8878",padx = 5)
# music_duration_label.pack(padx=10,pady=5,in_=scale_bar,side='right')
# # progressframe = tk.Frame( canvas, bg = "black")
# # progressframe.pack(padx=0,pady=0)

# progress_scale=ttk.Scale(canvas,orient="horizontal",length=380,command=scale_set,cursor='hand2',style="TScale")

# progress_scale.pack(padx=10,pady=5,in_=scale_bar,side='left')

# label = tk.Label(canvas, text = '', bg = "#8B8878", fg = 'yellow', width = 80, font = ('Comic Sans MS', 20))
# label.pack(pady = 15, in_ = newFrame, side = 'left')

# # play/pause user box (prev - pause - play - stop - next)

# top = tk.Frame(canvas, bg = '#8B8878')
# top.pack(padx = 10, pady = 10, anchor = 'center')

# # button for prev song

# prevButton = tk.Button(canvas, text = "Prev", image = prev_img, bg = "#8B8878", borderwidth = 0, command = play_prev)
# prevButton.pack(pady = 0,padx = 5, in_ = top, side = 'left')

# # button to pause the song

# pauseButton = tk.Button(canvas, text = "Pause",image = pause_img, bg = "#8B8878", borderwidth = 0, command = pause)
# pauseButton.pack(pady = 0,padx = 5, in_ = top, side = 'left')

# # # button to Play the song

# # playButton = tk.Button(canvas, text = "Play", image = play_from_start_img, bg = "#8B8878", borderwidth = 0, command = select)
# # playButton.pack(pady = 0,padx = 5, in_ = top, side = 'left')

# # button to stop the song

# stopButton = tk.Button(canvas, text = "Stop",image = stop_img, bg = "#8B8878", borderwidth = 0, command = stop)
# stopButton.pack(pady = 0,padx = 5, in_ = top, side = 'left')


# # button for next song

# nextButton = tk.Button(canvas, text = "Next", image = next_img, bg = "#8B8878", borderwidth = 0, command = play_next)
# nextButton.pack(pady = 0,padx = 5, in_ = top, side = 'left')


# addToFavButton = tk.Button(canvas, text = "Add To Fav", image = remove_fav_img, bg = "#8B8878", borderwidth = "2", command = add_remove_to_fav)
# addToFavButton.pack(pady = 0,padx = 5, side = 'right')

# addToFavButton = tk.Button(canvas, text = "Add To Fav", image = remove_fav_img, bg = "#8B8878", borderwidth = "2", command = add_remove_to_fav)
# addToFavButton.pack(pady = 0,padx = 5, side = 'right')


canvas.mainloop()
 


# priority queue (most played)
