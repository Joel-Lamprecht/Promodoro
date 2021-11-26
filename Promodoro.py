from tkinter import *
import math


ROT = "#e7305b"
GRUEN = "#9bdeac"
GELB = "#f7f5dd"
WEISS = "#ffffff"
SCHWARZ = "#000000"
FONT = "Courier"
arbeitszeit = 25
kurze_pause = 5
lange_pause = 15
reps = 0
timer = None


def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="N/A")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = arbeitszeit * 60
    short_break_sec = kurze_pause * 60
    long_break_sec = lange_pause * 60
  
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="lange Pause", fg=GRUEN)
  
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Pause", fg=GRUEN)
   
    else:
        count_down(work_sec)
        title_label.config(text="Arbeit", fg=ROT)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        
def einstellungen_fenster():

    def get_zeiten():
        global arbeitszeit
        global kurze_pause
        global lange_pause
        arbeitszeit = int(arbeitszeit_entry.get())
        kurze_pause = int(kurze_pause_entry.get())
        lange_pause = int(lange_pause_entry.get())
        
    def default():
        global arbeitszeit
        global kurze_pause
        global lange_pause
        arbeitszeit = 25
        kurze_pause = 5
        lange_pause = 10

    einstellungen = Toplevel()
    einstellungen.minsize(width=200, height = 200)
    einstellungen.resizable(0, 0)
    einstellungen.title("Einstellungen")
    label1 = Label(einstellungen, text = "Arbeitszeit")
    label1.pack() 
    arbeitszeit_entry = Entry(einstellungen)
    arbeitszeit_entry.pack()
    label2 = Label(einstellungen, text = "Kurze Pause")
    label2.pack() 
    kurze_pause_entry = Entry(einstellungen)
    kurze_pause_entry.pack()
    label3 = Label(einstellungen, text = "Lange Pause")
    label3.pack() 
    lange_pause_entry = Entry(einstellungen)
    lange_pause_entry.pack()
    fertig_button= Button(einstellungen, text = "Bestätigen",command = get_zeiten)
    fertig_button.pack()
    fertig_button= Button(einstellungen, text = "Default",command = default)
    fertig_button.pack()
    


root = Tk()
root.title("Pomodoro Timer")
root.config(padx=100, pady=50, bg=WEISS)
root.resizable(0, 0)
title_label = Label(text="Pause", fg=GRUEN, bg=SCHWARZ, font=(FONT, 50))
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=WEISS, highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
einstellungen_button = Button(text="Einstellungen", highlightthickness=0, command=einstellungen_fenster)
einstellungen_button.grid(column=1, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)




root.mainloop()



