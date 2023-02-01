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
CHECK = "✓"
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text= "00:00")
    time_label.config(text="Timer")
    check_labels.config(text="")
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():

    global REPS
    REPS += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN *60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        time_label.config(text="Take a Break!",fg=GREEN)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        time_label.config(text="Take a Break!",fg=PINK)
    else:
        count_down(work_sec)
        time_label.config(text="Get to work!",fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    global REPS
    global CHECK
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if REPS % 2 == 0:
            check_labels.config(text=CHECK)
            CHECK += "✓"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

time_label = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
time_label.config(padx=50,pady=50)
time_label.grid(column=1,row=0)

start_button = Button(text="Start",font=(FONT_NAME,12,"bold"),command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",font=(FONT_NAME,12,"bold"),command=reset_timer)
reset_button.grid(column=2,row=2)


check_labels = Label(font=(FONT_NAME,25,"bold"),bg=YELLOW,fg=GREEN)
check_labels.grid(column=1,row=3)

window.mainloop()











