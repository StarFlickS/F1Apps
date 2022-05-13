from tkinter import *
from tkinter.ttk import Progressbar

class RunningF1app():
    def __init__(self) -> Tk:
        w = 1200
        h = 800
        root = Tk()
        root.title("F1 app by StarFlickS")
        x = root.winfo_screenwidth() / 2 - w / 2
        y = root.winfo_screenheight() / 2 - h / 2
        root.geometry("%dx%d+%d+%d" %(w, h, x, y))
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        
        self.downloadImg()
        self.LoadingFrame(root)
        root.mainloop()
    

    def LoadingFrame(self, master):
        def barProgressing(bar):
            import time
            for i in range(5):
                bar["value"] += 20
                master.update_idletasks()
                time.sleep(1)
                loading_frm.destroy()
        
        loading_frm = Frame(master)
        loading_frm.rowconfigure(0, weight=1)
        loading_frm.columnconfigure(0, weight=1)
        loading_frm.grid(row=0, column=0, sticky="news")
       
        Label(
            loading_frm,
            image=logo_img
        ).grid(row=0, column=0)

        loadingBar = Progressbar(
            loading_frm,
            orient=HORIZONTAL,
            length=500,
            mode="determinate"
        )
        loadingBar.grid(row=1, column=0)
        barProgressing(loadingBar)
        self.MainFrame(master)


    def downloadImg(self):
        global logo_img
        logo_img = PhotoImage(file="img/f1logo.png")

    
if __name__ == "__main__":
    RunningF1app()
    