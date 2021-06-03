#GPA calculator

from tkinter import *
window = Tk()
window.configure(bg="Gray")

def get_Recent():
    global recent
    recent = entry1.get()
    


def displayGpa():
    labelGpa = Label(window, text = "Your gpa is " + str(average), bg ="Gray")
    labelGpa.place(x=130, y = 380)

def calculateGpa():
    get_Recent()
    grades = []
    grades.append(class1.get())
    grades.append(class2.get())
    grades.append(class3.get())
    grades.append(class4.get())
    grades.append(class5.get())
    grades.append(class6.get())
    
    x = 0
    for x in range (len(grades)):
        if grades[x] == 'a':
            grades[x] = 4.0
            x += 1
        elif grades[x] == 'b':
            grades[x] = 3.5
            x += 1
        elif grades[x] == 'c':
            grades[x] = 3.0
            x += 1
        elif grades[x] == 'd':
            grades[x] = 2.5
            x += 1
        elif grades[x] == 'n':
            break
        else:
            grades[x] = 2.0
            x += 1
    count = 0
    global total
    total = 0
    for count in range (len(grades)):
        total += grades[count]
    total += float(recent)
    
    
    
    global average
    
    average = total / (len(grades) + 1)
    displayGpa()


    
    
    
    
    
    

def classes():
    
    label2 = Label(window, text="Enter your letter grade for each class, \nif no more class grades, enter 'n' \nfor rest of classes: ", bg = "Gray").place(x = 90, y = 100)
    global class1, class2, class3, class4, class5, class6
    class1 = Entry(window, width = 5, relief = FLAT)
    class2 = Entry(window, width = 5, relief = FLAT)
    class3 = Entry(window, width = 5, relief = FLAT)
    class4 = Entry(window, width = 5, relief = FLAT)
    class5 = Entry(window, width = 5, relief = FLAT)
    class6 = Entry(window, width = 5, relief = FLAT)
    class1.place(x = 110, y = 200)
    class2.place(x = 110, y = 250)
    class3.place(x = 110, y = 300)
    class4.place(x = 230, y = 200)
    class5.place(x = 230, y = 250)
    class6.place(x = 230, y = 300)
    
  
   
    calculateButton = Button(window, text = "calculate", command = calculateGpa).place(x = 165, y = 350)

    

    
        
        

        
    
    
    
    
    
    



window1 = window
window.title("GPA Calculator")
window.geometry("400x400")
label1 = Label(window, text="Enter most recent GPA if available, otherwise enter '0': ", bg = "Gray")
label1.pack(side = TOP)


entry1 = Entry(window, width = 5, relief = FLAT)
entry1.pack(side = TOP)

enterButton = Button(window, text="Enter", command = classes).place(x = 178, y = 70)


window.mainloop()



