from tkinter import messagebox, ttk
from datetime import datetime
from tree import *
from tkcalendar import DateEntry
from tkinter import *
from PIL import ImageTk, Image
import os
from functools import partial


now = datetime.now()
lst = myTree.get_elements()
count = 0

main = Tk()
main.title("اطلاعات دانشجو ها")
main.geometry('800x530')
main.resizable(False, False)

canvas = Canvas(main, bg="#CDCDAA")
canvas.pack(fill="both", expand=True)


# icons
current_directory = os.path.abspath(os.getcwd())
print(current_directory)
edit_icon = ImageTk.PhotoImage(Image.open(f"{current_directory}\\icon_edit.jpg"))
delete_icon = ImageTk.PhotoImage(Image.open(f"{current_directory}\\icon_delete.jpg"))
search_icon = ImageTk.PhotoImage(Image.open(f"{current_directory}\\icon_search.jpg"))
bind_icon = ImageTk.PhotoImage(Image.open(f"{current_directory}\\icon_Refresh.jpg"))
add_icon = ImageTk.PhotoImage(Image.open(f"{current_directory}\\icon_add.jpg"))

# show students
def make_cell(content, x, y, color):
    label_frame = LabelFrame(canvas, text="")
    label = Label(label_frame, text=f"{content}", bg=color)
    label.pack()
    canvas.create_window(x, y, window=label_frame, anchor='nw')


def show_students(first=0, last=6):
    global count
    j = 0
    for i in lst[first:last]:
        make_cell(i.name, 35, 100+j*60, "lightgray")
        make_cell(i.lastName, 130, 100+j*60, "lightgray")
        make_cell(i.fatherName, 205, 100+j*60, "lightgray")
        make_cell(i.birthDate, 300, 100+j*60, "lightgray")
        make_cell(i.certificateNum, 430, 100+j*60, "lightgray")
        make_cell(i.codeMelli, 530, 100+j*60, "lightgray")
        make_cell(i.phoneNumber, 620, 100+j*60, "lightgray")
        btn_edit = Button(canvas,
                          command=partial(form_edit_or_add, "ویرایش دانشجو", i), image=edit_icon)
        canvas.create_window(690, 100+j*60, window=btn_edit, anchor="nw")
        btn_delete = Button(canvas,
                            command=partial(btn_delete_handler, i), image=delete_icon)
        canvas.create_window(730, 100+j*60, window=btn_delete, anchor="nw")
        j += 1


def reNew_students():
    canvas.delete('all')

# buttons handeler


def btn_add_handler(newWindow, name, lastName, fatherName, birthDate, certificateNum, codeMelli, number, phoneNumber):
    if name == "" or lastName == "" or fatherName == "" or birthDate == "" or certificateNum == "" or codeMelli == "" or number == "" or phoneNumber == "":
        messagebox.showerror("توجه", "همه کادر ها را پر کنید")
    else:
        s = Students(name, lastName, fatherName, birthDate,
                     certificateNum, int(codeMelli), number, phoneNumber)
        myTree.insert_node(root, s)

        global lst
        newWindow.destroy()
        reNew_students()
        lst = myTree.get_elements()
        show_students()


def intValidation(S):
    if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False


def limit_entry(str_var, length):
    def callback(str_var):
        c = str_var.get()[0:length]
        str_var.set(c)
    str_var.trace("w", lambda name, index, mode,
                  str_var=str_var: callback(str_var))


def maxLenghtValidation(*args):
    value = args[0].get()
    if len(value) > args[1]:
        args[0].set(value[:args[1]])


def form_edit_or_add(title, student=None):
    newWindow = Toplevel(main)
    newWindow.title(title)
    newWindow.geometry("360x225")
    vcmd = (newWindow.register(intValidation), "%S")

    labelName = Label(newWindow, text=":نام")
    labelName.place(x=335, y=5)
    entryName = Entry(newWindow, width=20)
    entryName.place(x=180, y=5)
    if student:
        entryName.insert(0, student.name)

    labelLastName = Label(newWindow, text=":نام خانوادگی")
    labelLastName.place(x=100, y=5)
    entryLastName = Entry(newWindow, width=14)
    entryLastName.place(x=10, y=5)
    if student:
        entryLastName.insert(0, student.lastName)

    labelFatherName = Label(newWindow, text=":نام پدر")
    labelFatherName.place(x=310, y=50)
    entryFatherName = Entry(newWindow, width=18)
    entryFatherName.place(x=180, y=50)
    if student:
        entryFatherName.insert(0, student.fatherName)

    labelBirthDate = Label(newWindow, text=":ناریخ تولد")
    labelBirthDate.place(x=120, y=50)
    year = int(now.strftime("%Y"))
    month = int(now.strftime("%m"))
    day = int(now.strftime("%d"))
    entryBirthDate = DateEntry(
        newWindow, selectmode='day', year=year, month=month, day=day, width=14)
    entryBirthDate.place(x=10, y=50)
    if student:
        dateOfBirth = datetime.strptime(str(student.birthDate), "%Y-%m-%d")
        entryBirthDate.insert(0, dateOfBirth)

    labelCertificateNum = Label(newWindow, text=":شماره شناسنامه")
    labelCertificateNum.place(x=270, y=100)
    entryCertificateNum = Entry(newWindow, width=14)
    entryCertificateNum.place(x=170, y=100)
    if student:
        entryCertificateNum.insert(0, str(student.certificateNum))
    entryCertificateNum.config(validate="key", validatecommand=vcmd)

    labelCodeMelli = Label(newWindow, text=":کد ملی")
    labelCodeMelli.place(x=120, y=100)
    textCodeMelli = StringVar()
    limit_entry(textCodeMelli, 10)
    entryCodeMelli = Entry(newWindow, width=14, textvariable=textCodeMelli)
    entryCodeMelli.place(x=10, y=100)
    if student:
        entryCodeMelli.insert(0, student.codeMelli)
    entryCodeMelli.config(validate="key", validatecommand=vcmd)

    labelNumber = Label(newWindow, text=":شماره تماس")
    labelNumber.place(x=290, y=150)
    textNumber = StringVar()
    limit_entry(textNumber, 11)
    entryNumber = Entry(newWindow, width=13, textvariable=textNumber)
    entryNumber.place(x=200, y=150)
    if student:
        entryNumber.insert(0, student.number)
    entryNumber.config(validate="key", validatecommand=vcmd)

    labelPhoneNumber = Label(newWindow, text=":شماره همراه")
    labelPhoneNumber.place(x=120, y=150)
    textPhoneNumber = StringVar()
    limit_entry(textPhoneNumber, 11)
    entryPhoneNumber = Entry(newWindow, width=14, textvariable=textPhoneNumber)
    entryPhoneNumber.place(x=10, y=150)
    if student:
        entryPhoneNumber.insert(0, student.phoneNumber)
    entryPhoneNumber.config(validate="key", validatecommand=vcmd)

    btn_submit = Button(newWindow, text=title,
                        command=lambda: btn_edit_handler(newWindow, student, entryName.get(), entryLastName.get(), entryFatherName.get(
                        ), entryBirthDate.get_date(), entryCertificateNum.get(), entryCodeMelli.get(), entryNumber.get(), entryPhoneNumber.get())
                        if title == "ویرایش دانشجو" else btn_add_handler(newWindow, entryName.get(), entryLastName.get(),
                                                                         entryFatherName.get(), entryBirthDate.get_date(
                        ), entryCertificateNum.get(), entryCodeMelli.get(), entryNumber.get(),
                            entryPhoneNumber.get()), width=45, bg="lightgreen")
    btn_submit.place(x=10, y=190)


def btn_edit_handler(newWindow, student, name, lastName, fatherName, birthDate, certificateNum, codeMelli, number, phoneNumber):
    global lst
    entry_search.delete(0, END)
    if name == "" or lastName == "" or fatherName == "" or birthDate == "" or certificateNum == "" or codeMelli == "" or number == "" or phoneNumber == "":
        messagebox.showerror(
            "توجه", "همه کادر ها را پر کنید", parent=newWindow)
    else:
        student.name = name
        student.lastName = lastName
        student.fatherName = fatherName
        student.birthDate = birthDate
        student.certificateNum = certificateNum
        student.codeMelli = int(codeMelli)
        student.number = number
        student.phoneNumber = phoneNumber
        newWindow.destroy()
        reNew_students()
        lst = myTree.get_elements()
        show_students(count, count+6)


def btn_search_handler():
    global lst
    if entry_search.get() != "":
        codeMelli = int(entry_search.get())
        founded_student = myTree.search(root, codeMelli)
        entry_search.delete(0, END)
        if(founded_student):
            reNew_students()
            lst = [founded_student]
            show_students()
        else:
            messagebox.showerror("توجه", "شخصی با این کد ملی یافت نشد")
    else:
        messagebox.showerror("توجه", "لطفا کد ملی را وارد کنید")


def btn_bind_handler():
    global lst
    reNew_students()
    state_order_label.config(text="پبش ترتیب")
    lst = myTree.get_elements()
    show_students()


def order_handler(event):
    global lst
    selected = change_order.get()
    reNew_students()
    if(selected == "پبش ترتیب"):
        lst = myTree.get_elements()
        state_order_label.config(text="پبش ترتیب")
    if(selected == "میان ترتیب"):
        lst = myTree.get_elements('in')
        state_order_label.config(text="میان ترتیب")
    if(selected == "پس ترتیب"):
        lst = myTree.get_elements('post')
        state_order_label.config(text="پس ترتیب")
    show_students()


def btn_delete_handler(student):
    global lst
    if(messagebox.askyesno(title="هشدار", message=f"آیااز حذف مطمئن هستید{student.name}؟")):
        myTree.delete_node(root, student)
        reNew_students()
        lst = myTree.get_elements()
        show_students(count, count+6)


def btn_next_handler():
    global count
    if count+6 < len(lst):
        count += 6
        reNew_students()
        show_students(count, count+6)


def btn_prev_handler():
    global count
    if count > 1:
        count -= 6
        reNew_students()
        show_students(count, count+6)


# Labels
headerName = Label(main, bg="yellow", text="نام")
headerName.place(x=40, y=60)
headerLastName = Label(main, bg="yellow", text="نام خانوادگی")
headerLastName.place(x=110, y=60)
headerFatherName = Label(main, bg="yellow", text="نام پدر")
headerFatherName.place(x=220, y=60)
headerBirthDate = Label(main, bg="yellow", text="تاریخ تولد")
headerBirthDate.place(x=305, y=60)
headerCertificateNum = Label(main, bg="yellow", text="شماره شناسنامه")
headerCertificateNum.place(x=400, y=60)
headerCodeMelli = Label(main, bg="yellow", text="کد ملی")
headerCodeMelli.place(x=525, y=60)
headerPhoneNumber = Label(main, bg="yellow", text="شماره همراه")
headerPhoneNumber.place(x=610, y=60)

change_order_label = Label(main, bg="orange", text="ترتیب: ")
change_order_label.place(x=35, y=18)
order_label = Label(main, bg="#F0F0F8", text="نوع ترتیب: ")
order_label.place(x=500, y=18)
state_order_label = Label(main, bg="lightyellow", text="پیش ترتیب")
state_order_label.place(x=570, y=18)


# buttons
btn_add = Button(main, text="افزودن دانشجو جدید", image=add_icon, compound=LEFT, bg='orange',
                 command=lambda: form_edit_or_add("افزودن دانشجو جدید"))
btn_add.place(x=305, y=465)
btn_search = Button(main, image=search_icon, bg='lightblue',
                    command=lambda: btn_search_handler())
btn_search.place(x=280, y=15)
btn_bind_grid = Button(main, image=bind_icon,
                       command=lambda: btn_bind_handler())
btn_bind_grid.place(x=720, y=15)

change_order = ttk.Combobox(values=["پبش ترتیب", "میان ترتیب", "پس ترتیب"])
change_order.bind("<<ComboboxSelected>>", order_handler)
change_order.place(x=80, y=19)

btn_next = Button(main, text="بعدی", bg='orange',
                  command=lambda: btn_next_handler())
btn_next.place(x=750, y=470)
btn_prev = Button(main, text="قبلی", bg='orange',
                  command=lambda: btn_prev_handler())
btn_prev.place(x=10, y=470)


# entry
vcmd = (main.register(intValidation), "%S")
entry_search = Entry(main, width=15)
entry_search.place(x=320, y=19)
entry_search.config(validate="key", validatecommand=vcmd)


try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    show_students()
    main.mainloop()
