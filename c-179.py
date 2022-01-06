from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.title("Encapsulation")
root.geometry("800x600")
root.config(bg = "orange2")
#Heading
label_heading = Label(root, text = "Juice Center", bg = "orange2", font = ("sylfaen", 18, "bold", "italic"))
label_heading.place(relx =0.5 , rely = 0.1, anchor = W)

#logo image
juice = ImageTk.PhotoImage(Image.open ("logo.png"))
juice_image = Label(root, image = juice, bg = "orange2")
juice_image.place(relx = 0.2, rely = 0.4, anchor = CENTER)

# Load Images
apple = ImageTk.PhotoImage(Image.open ("apple_img.png"))
mango = ImageTk.PhotoImage(Image.open ("mango_img.png"))
orange = ImageTk.PhotoImage(Image.open ("orange.png"))


#Fruit Images
Fruit_Images = Label(root, bg = "orange2")
Fruit_Images.place(relx = 0.75, rely = 0.8, anchor = CENTER)

#Label Select Food
label_name = Label(root, text = "Select Food", bg = "orange2", font = ("Banchrift Light", 15))
label_name.place(relx = 0.96, rely = 0.2, anchor = E)
#Drop down
fruit_list = ["Apple", "Mango", "Orange"]
fruit_dropdown = ttk.Combobox(root, state = "readonly", values = fruit_list, justify = "right")
fruit_dropdown.place(relx = 0.95, rely = 0.25, anchor = E)
#label enter quantity
label_quantity = Label(root, text = "Enter Quantity", bg = "orange2", font = ("Banchrift Light", 15))
label_quantity.place(relx = 0.96, rely = 0.35, anchor = E)

#entry element
input_quantity = Entry(root)
input_quantity.place(relx = 0.95, rely = 0.4, anchor = E)

#Total_cost_label
label_show_amount = Label(root, bg = "orange2", font = ("Banchrift Light", 12))
label_show_amount.place(relx = 0.95, rely = 0.7, anchor = E)

#Quantity Label
label_show_Quantity = Label(root, bg = "orange2", font = ("Banchrift Light", 12))
label_show_Quantity.place(relx = 0.95, rely = 0.8, anchor = E)

class juice:
    def __init__(self, fruit_name, quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 250
    
    def __calculateCost(self):
        total_cost = self.quantity * self.__cost
        label_show_amount["text"] = "You have to pay : " + str(total_cost) + " USD"
        if (self.fruit == "Apple"):
            calorie = self.quantity * 52
            Fruit_Images['image'] = apple 
        elif (self.fruit == "Mango"):
            calorie = self.quantity * 60
            Fruit_Images['image'] = mango
        elif (self.fruit == "Orange"):
            calorie = self.quantity * 47
            Fruit_Images['image'] = orange

    def get_cost(self):
        self.__calculateCost()

def order_juice():
    fruit = fruit_dropdown.get()
    quantity = input_quantity.get()
    obj1 = juice(fruit, quantity)
    obj1.get_cost()
    
btn = Button(root, text = "TOTAL", bg = "red3", fg = "white", padx = 10, pady = 1, font = ("Arial", 11, "bold"), relief = FLAT, command = order_juice)
btn.place(relx =0.95 , rely =0.5 , anchor = E)

root.mainloop()