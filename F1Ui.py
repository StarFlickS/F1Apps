from tkinter import *
from tkinter.ttk import Progressbar
import F1Api

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
    

    def LoadingFrame(self, master: Tk):
        def barProgressing(bar: Progressbar):
            import time
            for i in range(2):
                bar["value"] += 50
                master.update_idletasks()
                time.sleep(1)
        
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
        loadingBar.grid(row=0, column=0, sticky='s')
        barProgressing(loadingBar)
        loading_frm.destroy()
        self.MainFrame(master)


    def MainFrame(self, master: Tk):
        print("In MainFrame Function")
        main_frm = Frame(master)
        main_frm.rowconfigure(0, weight=1)
        main_frm.rowconfigure(1, weight=3)
        main_frm.columnconfigure(0, weight=1)
        main_frm.grid(row=0, column=0, sticky="news")

        header_frm = Frame(main_frm, bg="red")
        header_frm.rowconfigure(0, weight=1)
        header_frm.columnconfigure(0, weight=1)
        header_frm.grid(row=0, column=0, sticky="news")
        
        grand_prix_frm = Frame(main_frm, bg="white")
        grand_prix_frm.columnconfigure((0,1), weight=1)
        grand_prix_frm.grid(row=1, column=0, sticky="news")

        # * Header
        Label(
            header_frm,
            text = "Grand Prix",
            font = "Verdana 50 bold",
            bg = "red",
            fg = "white"
        ).grid(row=0, column=0)

        grand_prix_dict = F1Api.getGrandPrix()
        i = 0 
        for key, value in grand_prix_dict.items():
            
            Label(
                grand_prix_frm,
                text = key,
                fg = "black",
                bg = "white",
                font = "verdana 16"
            ).grid(row=i ,column=0, pady=3)

            Label(
                grand_prix_frm,
                text = value,
                fg = "black",
                bg = "white",
                font = "verdana 16"
            ).grid(row=i ,column=1, pady=3)

            i += 1

    def downloadImg(self):
        global logo_img
        logo_img = PhotoImage(file="img/f1logo.png")

    
if __name__ == "__main__":
    RunningF1app()
    