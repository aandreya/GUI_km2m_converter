from Tkinter import *
import Tkinter

def pretvornik_km2m():
    kilometer = float(entry_kilometer.get())
    m = kilometer * 1.6093
    km2m_result_label.config(text=round(m, 4))

def pretvornik_m2km():
    mile = float(entry_mile.get())
    km = mile / 1.6093
    m2km_result_label.config(text=round(km, 4))

def reset():
    entry_kilometer.delete(0, Tkinter.END)
    entry_mile.delete(0, Tkinter.END)
    km2m_result_label.config(text="")
    m2km_result_label.config(text="")

frame = Tk()
frame.geometry("400x120")
frame.title("miles <--> kilometers")
greeting = Label(frame, text = "Let's jump between miles and kilometers...\n")
greeting.grid (row=0, column=0, columnspan=4)

label_kilometer = Label(frame, text="kilometers ")
label_kilometer.grid(row=1, column=0)
entry_kilometer = Entry(frame)
entry_kilometer.grid (row=1, column=1)
submit_button_1 = Button(frame, text=" = ", command = pretvornik_km2m)
submit_button_1.grid (row=1, column=2)
km2m_result_label = Label(frame, text="")
km2m_result_label.grid (row=1, column=3)
label_mile_result = Label(frame, text="miles")
label_mile_result.grid(row=1, column=4)

label_mile = Label(frame, text="mile ")
label_mile.grid(row=2, column=0)
entry_mile = Entry(frame)
entry_mile.grid(row=2, column=1)
submit_button_2 = Button(frame, text=" = ", command = pretvornik_m2km)
submit_button_2.grid (row=2, column=2)
m2km_result_label = Label(frame, text="")
m2km_result_label.grid (row=2, column=3)
label_kilometer_result = Label(frame, text="kilometers")
label_kilometer_result.grid(row=2, column=4)

reset_button_pushed = Button(frame, text="Reset", command = reset)
reset_button_pushed.grid (row=3, column=2)

frame.mainloop()
