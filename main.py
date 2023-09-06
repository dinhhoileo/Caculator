from tkinter import*
from PIL import ImageTk
class Event:
    def __init__(self, text_input):
        self.text_input = text_input
    
    def click(self, number):
        self.text_input.set(self.text_input.get() + str(number))
    def clear(self,text_input):
        self.text_input.set("")
        
    def click_char(self, char):
        current_text = self.text_input.get()
        self.text_input.set(current_text + str(char))
    def equals(self):
        current_text = self.text_input.get()
        result=str(eval(current_text))
        self.text_input.set(result)
    def delete(self):
        current_text = self.text_input.get()
        new_text= current_text[:-1]
        self.text_input.set(new_text)
    
class App:
    def __init__(self) -> None:
        self.root=Tk()
        self.root.title("Caculator")
        self.root.geometry("309x430")
        self.root.iconbitmap("caculator.ico") 
        # TV
        # self.operator = ""
        self.text_input =StringVar()
        
        self.show_caculator_entry=Entry(self.root,textvariable=self.text_input,width=13,font=("Arial",30),justify="right")
        self.show_caculator_entry.place(x=5,y=50)
        self.event=Event(self.text_input)
        #caculus
        self.division_button = Button(self.root,text="/",command=lambda:self.event.click_char('/'),font=("Arial",11),justify="center",width=5,height=2)
        self.division_button.place(x=250,y=142)
        
        self.times_button = Button(self.root,text="*",command=lambda:self.event.click_char('*'),font=("Arial",11),justify="center",width=5,height=2)
        self.times_button.place(x=250,y=201)
        
        self.minus_button = Button(self.root,text="-",command=lambda:self.event.click_char('-'),font=("Arial",11),justify="center",width=5,height=2) 
        self.minus_button.place(x=250,y=261)
        
        self.plus_button = Button(self.root,text="+",command=lambda:self.event.click_char('+'),font=("Arial",11),justify="center",width=5,height=2) 
        self.plus_button.place(x=250,y=319)
        
        self.equal_button = Button(self.root,text="=",command=lambda:self.event.equals(),font=("Arial",11),justify="center",width=5,height=2) 
        self.equal_button.place(x=250,y=377)
        
        self.delete_button = Button(self.root,text="Delete",command=lambda:self.event.delete(),font=("Arial",11),justify="center",width=5,height=2) 
        self.delete_button.place(x=160,y=142)
        
        self.per_cent_button = Button(self.root,text="%",command=lambda:self.event.click_char('%'),font=("Arial",11),justify="center",width=5,height=2) 
        self.per_cent_button.place(x=78,y=142)
        
        self.clear_button = Button(self.root,text="C",command=lambda:self.event.clear(self.text_input),font=("Arial",11),justify="center",width=5,height=2) 
        self.clear_button.place(x=2,y=142)
        
        # number
        self.zero_button = Button(self.root,text="0",command=lambda:self.event.click(0),font=("Arial",11),justify="center",width=5,height=2) 
        self.zero_button.place(x=78,y=377)
        
        self.one_button = Button(self.root,text="1",command=lambda:self.event.click(1),font=("Arial",11),justify="center",width=5,height=2) 
        self.one_button.place(x=2,y=319)
        
        self.two_button = Button(self.root,text="2",command=lambda:self.event.click(2),font=("Arial",11),justify="center",width=5,height=2) 
        self.two_button.place(x=78,y=319)
        
        self.three_button = Button(self.root,text="3",command=lambda:self.event.click(3),font=("Arial",11),justify="center",width=5,height=2) 
        self.three_button.place(x=161,y=319)
        
        self.four_button = Button(self.root,text="4",command=lambda:self.event.click(4),font=("Arial",11),justify="center",width=5,height=2) 
        self.four_button.place(x=2,y=261)
        
        self.five_button = Button(self.root,text="5",command=lambda:self.event.click(5),font=("Arial",11),justify="center",width=5,height=2) 
        self.five_button.place(x=78,y=261)
        
        self.six_button = Button(self.root,text="6",command=lambda:self.event.click(6),font=("Arial",11),justify="center",width=5,height=2) 
        self.six_button.place(x=161,y=261)
        
        self.seven_button = Button(self.root,text="7",command=lambda:self.event.click(7),font=("Arial",11),justify="center",width=5,height=2) 
        self.seven_button.place(x=2,y=203)
        
        self.eight_button = Button(self.root,text="8",command=lambda:self.event.click(8),font=("Arial",11),justify="center",width=5,height=2) 
        self.eight_button.place(x=78,y=203)
        
        self.nine_button = Button(self.root,text="9",command=lambda:self.event.click(9),font=("Arial",11),justify="center",width=5,height=2) 
        self.nine_button.place(x=161,y=203)
        
        self.three_zero_button = Button(self.root,text="0 0 0",command=lambda:self.event.click_char('000'),font=("Arial",11),justify="center",width=5,height=2) 
        self.three_zero_button.place(x=2,y=377)
    
        self.dot_button = Button(self.root,text=".",command=lambda:self.event.click_char('.'),font=("Arial",11),justify="center",width=5,height=2) 
        self.dot_button.place(x=161,y=377)
        
        self.root.mainloop()

if __name__=="__main__":
    new_app=App()