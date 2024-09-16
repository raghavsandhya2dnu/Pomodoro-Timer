from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

window=Tk()
window.title("Pomodore")
window.minsize(height=400,width=600)
window.config(padx=150,bg=YELLOW)
title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
title_label.grid(column=2, row=1)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    checkmark.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps=0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    # if count_sec==0:
    #     count_sec="00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)

    else:
        start_timer()
        mark=""
        for i in range(math.floor(reps/2)):
            mark+="✔"
        checkmark.config(text=mark)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        title_label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps%2==0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work Time", fg=GREEN)
        count_down(work_sec)


# ---------------------------- UI SETUP ------------------------------- #
reset_button=Button(text="RESET",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)

start_button=Button(text="START",highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)

var = IntVar()  # Create an IntVar to store the check button state
checkmark =Label(fg=GREEN,bg=YELLOW)
checkmark.grid(row=4,column=2)











window.mainloop()