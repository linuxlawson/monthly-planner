#!/usr/bin/python3
#Monthly Planner

import tkinter as tk
import tkinter.filedialog as tkFileDialog

root = tk.Tk()
root.title("Monthly Planner")
root.geometry("514x660")
root.option_add("*Font", "TkDefaultFont 9")
root.resizable(0,0)
my_entries = []


#title
lab = tk.Label(root, text="Monthly Planner", font='Arial 10 bold')
lab.grid(row=0, column=0, sticky='w', padx=12, pady=4)
lab1 = tk.Label(root, text="Monthly Chores for You and Yours")
lab1.grid(row=1, column=0, sticky='w', padx=12, pady=(4,30))

#name
name = tk.Label(root, text="Name:")
name.grid(row=2, column=0,  sticky='nw', padx=12, pady=4)
name = tk.Entry(root, width='12')
name.grid(row=2, column=0, sticky='nw', padx=64, pady=2)
name.focus_set()

#month
mon = tk.Label(root, text="Month:")
mon.grid(row=3, column=0,  sticky='nw', padx=12, pady=4)
mon = tk.Entry(root, width='12')
mon.grid(row=3, column=0, sticky='nw', padx=64, pady=(2,30))


#chores/duties
chore_lbl = tk.Label(root, text="Chores / Duties:",
								fg='#1A1A1A', font=('Arial 10 bold'))
chore_lbl.grid(row=4, column=0, sticky='w', padx=12, pady=4)


#daily (entry field labels)
daily = tk.Label(root, text="Daily:")
daily.grid(row=5, column=0, sticky='w', padx=16, pady=2)

#weekly
week = tk.Label(root, text="Weekly:")
week.grid(row=5, column=0, sticky='w', padx=187, pady=2)

#monthly
month = tk.Label(root, text="Monthly:")
month.grid(row=5, column=0, sticky='w', padx=357, pady=2)


#midFrame (contains entry boxes)
midframe = tk.Frame(relief='flat')
midframe.grid(row=6, column=0, sticky='nw', padx=0, pady=(0, 20))

#column/row loops
for y in range(3):
	for x in range(9):
		my_entry = tk.Entry(midframe, bd=1, width='16')
		my_entry.grid(row=x, column=y, sticky='w', padx=18, pady=2)
		my_entries.append(my_entry)


#pre-existing entries (examples)
#my_entries[0].insert('0', "Make Bed")
#my_entries[9].insert('0', "Vacuum")
#my_entries[18].insert('0', "Clean Room")


#text box
addi = tk.Label(text="Additional:")
addi.grid(row=16, column=0,  sticky='w', padx=18, pady=0)
tex = tk.Text(bd=1, width=58, height='10')
tex.grid(row=17, column=0, sticky='w', padx=18, pady=(2,20))
tex.config(wrap="word")
tex.insert('1.0', "No allowance until chores are completed. :)")



#functions
def clear_fields(event=None):
	name.delete('0', 'end')
	mon.delete('0', 'end')
	my_entries[0].delete('0', 'end')
	my_entries[1].delete('0', 'end')
	my_entries[2].delete('0', 'end')
	my_entries[3].delete('0', 'end')
	my_entries[4].delete('0', 'end')
	my_entries[5].delete('0', 'end')
	my_entries[6].delete('0', 'end')
	my_entries[7].delete('0', 'end')
	my_entries[8].delete('0', 'end')
	my_entries[9].delete('0', 'end')
	my_entries[10].delete('0', 'end')
	my_entries[11].delete('0', 'end')
	my_entries[12].delete('0', 'end')
	my_entries[13].delete('0', 'end')
	my_entries[14].delete('0', 'end')
	my_entries[15].delete('0', 'end')
	my_entries[16].delete('0', 'end')
	my_entries[17].delete('0', 'end')
	my_entries[18].delete('0', 'end')
	my_entries[19].delete('0', 'end')
	my_entries[20].delete('0', 'end')
	my_entries[21].delete('0', 'end')
	my_entries[22].delete('0', 'end')
	my_entries[23].delete('0', 'end')
	my_entries[24].delete('0', 'end')
	my_entries[25].delete('0', 'end')
	my_entries[26].delete('0', 'end')
	tex.delete('1.0', 'end')
	name.focus_set()


#save to text file
def save_com(event=None):
	file = tkFileDialog.asksaveasfile(mode='w', defaultextension='.txt',
	filetypes = (("Text Files", "*.txt"),("All Files", "*.*")))
	if file:
		file.write("\n")
		file.write("Monthly Chores / Duties\n\n\n")
		file.write("Name:    " + (name.get()) + "\n\n")
		file.write("Month:   " + (mon.get()) + "\n\n\n")

		file.write("Daily: ".ljust(28) + "Weekly: ".ljust(28) + "Monthly: ".ljust(28) + "\n\n")

		file.write(my_entries[0].get().ljust(28) + (my_entries[9].get().ljust(28) + (my_entries[18].get().ljust(28) + "\n")))
		file.write(my_entries[1].get().ljust(28) + (my_entries[10].get().ljust(28) + (my_entries[19].get().ljust(28) + "\n")))
		file.write(my_entries[2].get().ljust(28) + (my_entries[11].get().ljust(28) + (my_entries[20].get().ljust(28) + "\n")))
		file.write(my_entries[3].get().ljust(28) + (my_entries[12].get().ljust(28) + (my_entries[21].get().ljust(28) + "\n")))
		file.write(my_entries[4].get().ljust(28) + (my_entries[13].get().ljust(28) + (my_entries[22].get().ljust(28) + "\n")))
		file.write(my_entries[5].get().ljust(28) + (my_entries[14].get().ljust(28) + (my_entries[23].get().ljust(28) + "\n")))
		file.write(my_entries[6].get().ljust(28) + (my_entries[15].get().ljust(28) + (my_entries[24].get().ljust(28) + "\n")))
		file.write(my_entries[7].get().ljust(28) + (my_entries[16].get().ljust(28) + (my_entries[25].get().ljust(28) + "\n")))
		file.write(my_entries[8].get().ljust(28) + (my_entries[17].get().ljust(28) + (my_entries[26].get().ljust(28) + "\n")))

		file.write("\n\n")
		file.write("Additional: " +  "\n\n")
		data = tex.get('1.0', 'end-1c')
		file.write(data)
		file.close()


#file menu
def exit_com(event=None):
	win = tk.Toplevel()
	win.title("Exit")
	xit = tk.Label(win, text="\n\nAre you sure you want to exit?\n")
	xit.pack()
	ex = tk.Button(win, text="Exit", width=4, command=root.destroy)
	ex.pack(side='left', padx=28, pady=4)
	ex.focus_set()
	ex.bind("<Return>", (lambda event: root.destroy()))
	can = tk.Button(win, text="Cancel", width=4, command=win.destroy)
	can.pack(side='right', padx=28, pady=4)
	win.transient(root)
	win.geometry('240x120')
	win.wait_window()


#help menu
def about_com(event=None):
	win = tk.Toplevel()
	win.title("About")
	bout = tk.Label(win, text="""\n\nMonthly Planner\n
Monthly Chores For You and Yours\n
Fail to Plan, Plan to Fail\n\n
Made in Python""")
	bout.pack()
	clo = tk.Button(win, text="Close", width=4, command=win.destroy)
	clo.pack(padx=8, pady=16)
	win.transient(root)
	win.geometry('300x220+638+298')
	win.wait_window()


def trouble_com(event=None):
	win = tk.Toplevel()
	win.title("Troubleshooting")
	trouble = tk.Label(win, justify='left', text="""\n\n
One problem that may occur is the use of
long words/phrases typed in entry fields.
This may force the text in the next column
over, and out of alignment within the columns.\n
Note: This is noticeable only in the saved
text file, not the program itself.\n
To avoid this, use short words in entry fields.\n
The saved text file is formatted in a way
that this shouldn't happen often.

\n\n""")
	trouble.pack()
	cls = tk.Button(win, text="Close", command=win.destroy)
	cls.pack()
	win.transient(root)
	win.geometry('354x360+612+230')
	win.wait_window()



#Menu Items
menu = tk.Menu(root, bd=1, relief='flat')
root.config(menu=menu, bd=2)

#file-menu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File ", menu=filemenu)
filemenu.add_command(label="Clear Fields",
					command=clear_fields,
					accelerator="Ctrl+C ".rjust(8))
filemenu.add_command(label="Save As",
					command=save_com,
					accelerator="Ctrl+S ".rjust(8))
filemenu.add_command(label="Exit",
					command=exit_com, underline=1,
					accelerator="Ctrl+Q ".rjust(8))

#help-menu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help ", menu=helpmenu)
helpmenu.add_command(label="About", command=about_com)
helpmenu.add_command(label="Troubleshooting", command=trouble_com)


#bindings
root.bind_all('<Control-c>', clear_fields)
root.bind_all('<Control-s>', save_com)
root.bind_all('<Control-q>', exit_com)


root.protocol("WM_DELETE_WINDOW")
root.mainloop()
