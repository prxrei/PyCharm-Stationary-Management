#Yong Xuan Wei Johan , 235008L, IT2153-01

from stationary import Stationary

#Function provided by IT2153 DSA Assignment 1 to populate the system.
def populateData():
    prodList = []
    newStudA = Stationary("PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021, 2000)
    prodList.append(newStudA)
    newStudA = Stationary("PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022, 320)
    prodList.append(newStudA)
    newStudA = Stationary("PD1015", "Water Color Pencils", "Pencils", "Faber-Castell", 2011, 150)
    prodList.append(newStudA)
    newStudA = Stationary("PD1050", "Noris 320 Fiber Tip Pen", "Pens", "Staedtler", 2021, 350)
    prodList.append(newStudA)
    newStudA = Stationary("PD1001", "Copier Paper (A4) 70GSM", "Paper", "PaperOne", 2021, 1500)
    prodList.append(newStudA)
    newStudA = Stationary("PD1033", "Scientific Calculator FX-97SG X", "Calculator", "Casio", 2022, 50)
    prodList.append(newStudA)
    newStudA = Stationary("PD1005", "POP Bazic File Separator Clear", "Office Supplies", "Popular", 2000, 500)
    prodList.append(newStudA)
    print("Data populated!\n")
    return prodList
