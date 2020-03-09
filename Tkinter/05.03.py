import tkinter as tk
from tkinter import Text
from tkinter import INSERT
from tkinter import END
from tkinter import ttk
import tkinter.messagebox
from tkinter import Y, RIGHT, LEFT, TOP, BOTTOM


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Index(Page):
    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self,
                         text="This is the Index page",
                         font=('Verdana', 15))

        label.pack(side="top",
                   fill="both",
                   expand=True)


class Faq(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="This is the Faq Page")
        label.pack(side="top", fill=None, expand=False)

        faq_text = Text(self)
        faq_text.configure(height=200, width=200, bd=5, bg="blue", fg="black")
        faq_text.pack(side="top", fill=Y, expand=True)

        text_input = ("This is a collection of frequently asked questions and answers.",
                      "Do you have a specific question? Try the keyword search!\n\n\n\n"
                      "Contains information about how to get your personal details deleted from the internet"
                      "\nContact information:www.slettmeg.no\n\n"
                      "  A lot of good information on dealing with the bullies and where to contact\n\n"
                      "webpage:  https://nettvett.no/\n\n"
                      "If cases go too far, the only real solution in Norway is file a case against the bullies. The police will help further on investigating the case.\n"
                      "Evidence needed before filing a case\n"
                      ""
                      "https://www.politiet.no/")

        faq_text.insert(INSERT, text_input)


class Guide(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        guide_label = tk.Label(self, text="\n Guide on how to report Cyberbullying!\n", font=40, bg="red", fg="pink")
        guide_label.pack(side="top", fill="both", expand=True)


class Report(Page):
    """Docstring"""
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        report_frame = tk.Frame(self, height=50, width=50)
        report_frame.pack(side="top")
        text_frame = tk.Frame(self, height=300, width=300)
        text_frame.pack(side="bottom")

        report_label = tk.Label(report_frame, text="Welcome to the Reporting page")
        report_label.pack(side="top", fill="both", expand=True)
        report_scrollbar = tk.Scrollbar(text_frame)
        report_text = Text(text_frame)

        report_text.configure(height=4, width=85, bd=5, bg="blue", fg="black", padx=5, pady=5, selectborderwidth=8)
        report_text.insert(INSERT, "Welcome to the Reporting Section of this app", "\n\n\n")
        report_scrollbar.pack(side=RIGHT, fill=Y)
        report_text.pack(side=TOP, fill=Y)

        report_scrollbar.config(command=report_text.yview)
        report_text.config(yscrollcommand=report_scrollbar.set)
        quote = "\n This is where the user can input any information, \n"
        report_text.insert(tk.END, quote)

        reportbutton = tk.Button(self)
        reportbutton.configure(height=5, width=8, text="Report", command=lambda: register_input())
        reportbutton.pack(side=LEFT)
        checkbutton = tk.Button(self)
        checkbutton.configure(height=5, width=8, text="Check status", command=lambda: check_file())
        checkbutton.pack(side=RIGHT)

        def register_input():

            file = "test.txt"
            with open(file, "a") as f:
                f.write(report_text.get("1.0", "end-1c"))
                print("\nThe report has currently been reported!\n")
                f.close()

        def check_file():

            file = "test.txt"
            with open(file) as f_obj:
                for line in f_obj:
                    print(line.rstrip())


class MainWindow(tk.Frame):
    """Docstring"""
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

# Setting variables to store the path to the classes (in order to rotate pages)
        page_one = Index(self)
        page_two = Faq(self)
        page_three = Guide(self)
        page_four = Report(self)


# Creating a container in order to rotate the pages
# Creates a extra frame, so that we can divide the pages into two different frames
# If needed we can create multiple more frames and place different widgets inside each.
        button_frame = tk.Frame(self)
        container = tk.Frame(self)
        button_frame.pack(side="left", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        page_one.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page_two.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page_three.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page_four.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        button_one = tk.Button(button_frame, height=10, width=10,
                               text="Index", command=page_one.lift, foreground="Blue", background="#18b3ef")

        button_two = tk.Button(button_frame, height=10, width=10,
                               text="Faq", command=page_two.lift, foreground="Blue", background="#18b3ef")

        button_three = tk.Button(button_frame, height=10, width=10,
                                 text="Guide", command=page_three.lift, foreground="Blue", background="#18b3ef")

        button_four = tk.Button(button_frame, height=10, width=10,
                                text="Report Page", command=page_four.lift, foreground="Blue", background="#18b3ef",)

        button_one.pack(side="bottom", padx=5, pady=5)
        button_two.pack(side="bottom", padx=5, pady=5)
        button_three.pack(side="bottom", padx=5, pady=5)
        button_four.pack(side="bottom", padx=5, pady=5)

        page_one.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Our current title")
    root.minsize(600, 800)
    root.resizable(False, False)
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)

    main.mainloop()
