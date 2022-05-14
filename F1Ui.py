from tkinter import *
from tkinter.ttk import Progressbar
from tkmacosx import Button
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

        grand_prix_canvas = Canvas(main_frm, bg="lightgray", highlightthickness=0)
        grand_prix_canvas.columnconfigure(0, weight=1)
        grand_prix_canvas.grid(row=1, column=0, sticky="news")

        scrollbar = Scrollbar(main_frm, orient=VERTICAL, command=grand_prix_canvas.yview, width=20)
        scrollbar.grid(row=1, column=0, sticky='nse')

        grand_prix_canvas.configure(yscrollcommand=scrollbar.set)
        grand_prix_canvas.bind("<Configure>", lambda e: grand_prix_canvas.configure(scrollregion= grand_prix_canvas.bbox("all")))

        grand_prix_frm = Frame(grand_prix_canvas, bg="white")
        grand_prix_canvas.create_window((480,0), window=grand_prix_frm, anchor="nw")

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
            
            button_layout = Frame(grand_prix_frm, bg="lightgray")
            button_layout.rowconfigure(0, weight=1)
            button_layout.columnconfigure(0, weight=1)
            button_layout.grid(row=i, column=0, sticky="news")
            
            details = f"Round {i+1}\n{key}\n{value}"
            Button(
                button_layout,
                text = details,
                fg = "black",
                bg = "white",
                font = "verdana 16",
                borderless = 1,
                justify=CENTER
            ).grid(row=i ,column=0, sticky="news", pady=5)

            i += 1


    def downloadImg(self):
        global logo_img
        logo_img = PhotoImage(file="img/f1logo.png")

    
if __name__ == "__main__":
    RunningF1app()
    