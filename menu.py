import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("JCB")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_162=tk.Button(root)
        GButton_162["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_162["font"] = ft
        GButton_162["fg"] = "#000000"
        GButton_162["justify"] = "center"
        GButton_162["text"] = "Button"
        GButton_162.place(x=250,y=220,width=70,height=25)
        GButton_162["command"] = self.GButton_162_command

        GButton_27=tk.Button(root)
        GButton_27["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_27["font"] = ft
        GButton_27["fg"] = "#000000"
        GButton_27["justify"] = "center"
        GButton_27["text"] = "Button"
        GButton_27.place(x=250,y=290,width=70,height=25)
        GButton_27["command"] = self.GButton_27_command

        GButton_906=tk.Button(root)
        GButton_906["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_906["font"] = ft
        GButton_906["fg"] = "#000000"
        GButton_906["justify"] = "center"
        GButton_906["text"] = "Button"
        GButton_906.place(x=250,y=340,width=70,height=25)
        GButton_906["command"] = self.GButton_906_command

        GButton_537=tk.Button(root)
        GButton_537["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#000000"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "Button"
        GButton_537.place(x=250,y=410,width=70,height=25)
        GButton_537["command"] = self.GButton_537_command

        GMessage_628=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_628["font"] = ft
        GMessage_628["fg"] = "#333333"
        GMessage_628["justify"] = "center"
        GMessage_628["text"] = "James' Cure for boredom"
        GMessage_628.place(x=200,y=80,width=182,height=35)

    def GButton_162_command(self):
        print("command")


    def GButton_27_command(self):
        print("command")


    def GButton_906_command(self):
        print("command")


    def GButton_537_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
