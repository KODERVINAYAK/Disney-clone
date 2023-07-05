
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