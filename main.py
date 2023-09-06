from tkinter import*


class Caculation:
    def __init__(self):
        pass

class App:
    def __init__(self) -> None:
        self.root=Tk()
        self.root.title("Caculator")
        self.root.geometry("309x430")
        # TV
        current= 0
        show_caculator_entry=Entry(self.root,width=13,font=("Arial",30),justify="right")
        show_caculator_entry.insert(0,current)
        show_caculator_entry.place(x=5,y=50)
        #caculus
        division_button = Button(self.root,text="/",font=("Arial",11),justify="center",width=5,height=2)
        division_button.place(x=250,y=142)
        
        times_button = Button(self.root,text="X",font=("Arial",11),justify="center",width=5,height=2)
        times_button.place(x=250,y=201)
        
        minus_button = Button(self.root,text="-",font=("Arial",11),justify="center",width=5,height=2) 
        minus_button.place(x=250,y=261)
        
        plus_button = Button(self.root,text="+",font=("Arial",11),justify="center",width=5,height=2) 
        plus_button.place(x=250,y=319)
        
        equal_button = Button(self.root,text="=",font=("Arial",11),justify="center",width=5,height=2) 
        equal_button.place(x=250,y=377)
        
        delete_button = Button(self.root,text="Delete",font=("Arial",11),justify="center",width=5,height=2) 
        delete_button.place(x=160,y=142)
        
        per_cent_button = Button(self.root,text="%",font=("Arial",11),justify="center",width=5,height=2) 
        per_cent_button.place(x=78,y=142)
        
        clear_button = Button(self.root,text="C",font=("Arial",11),justify="center",width=5,height=2) 
        clear_button.place(x=2,y=142)
        
        # number
        zero_button = Button(self.root,text="0",font=("Arial",11),justify="center",width=5,height=2) 
        zero_button.place(x=78,y=377)
        
        one_button = Button(self.root,text="1",font=("Arial",11),justify="center",width=5,height=2) 
        one_button.place(x=2,y=319)
        
        two_button = Button(self.root,text="2",font=("Arial",11),justify="center",width=5,height=2) 
        two_button.place(x=78,y=319)
        
        three_button = Button(self.root,text="3",font=("Arial",11),justify="center",width=5,height=2) 
        three_button.place(x=161,y=319)
        
        four_button = Button(self.root,text="4",font=("Arial",11),justify="center",width=5,height=2) 
        four_button.place(x=2,y=261)
        
        five_button = Button(self.root,text="5",font=("Arial",11),justify="center",width=5,height=2) 
        five_button.place(x=78,y=261)
        
        six_button = Button(self.root,text="6",font=("Arial",11),justify="center",width=5,height=2) 
        six_button.place(x=161,y=261)
        
        seven_button = Button(self.root,text="7",font=("Arial",11),justify="center",width=5,height=2) 
        seven_button.place(x=2,y=203)
        
        eight_button = Button(self.root,text="8",font=("Arial",11),justify="center",width=5,height=2) 
        eight_button.place(x=78,y=203)
        
        nine_button = Button(self.root,text="9",font=("Arial",11),justify="center",width=5,height=2) 
        nine_button.place(x=161,y=203)
        
        three_zero_button = Button(self.root,text="0 0 0",font=("Arial",11),justify="center",width=5,height=2) 
        three_zero_button.place(x=2,y=377)
        
        dot_button = Button(self.root,text=".",font=("Arial",11),justify="center",width=5,height=2) 
        dot_button.place(x=161,y=377)
        
        self.root.mainloop()

if __name__=="__main__":
    new_app=App()