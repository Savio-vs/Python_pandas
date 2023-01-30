import pandas as pd 
import numpy as np
import matplotlib as mpl
from tkinter import *
from tkinter import ttk
from main import * 
comp_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Computers.xlsx')
# # doc_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Docking stations.xlsx')
# # mon_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Monitors.xlsx')

# comp_df = comp_df.sort_values(by=['Primary User'], ascending=True,ignore_index=True)

# valor = comp_df.iloc[1,0]
# print(valor)

#>>>> Criação de janela com tkinter
root = Tk()
root.title("Test")
root.geometry("200x150")

frame = Frame(root,bd=5,bg='purple')
frame.pack()

leftframe = Frame(root,bd=3,bg='red')
leftframe.pack(side=LEFT)

rightframe = Frame(root,bd=3,bg='blue')
rightframe.pack(side=RIGHT)
 
label = Label(frame, text = "Hello world")
label.pack()
 
button1 = Button(leftframe, text = "Button1")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Button2")
button2.pack(padx = 3, pady = 3)
button3 = Button(leftframe, text = "Button3")
button3.pack(padx = 3, pady = 3)
 

root.mainloop()



#print(com)
#for i in range(len(com)):
#   print(com[i][5])
# doc_df = doc_df.sort_values(by=['Primary User'],ascending=True,ignore_index=True)

# mon_df= mon_df.sort_values(by=['Primary User'],ascending=True,ignore_index=True)

# comp_df.to_csv('csv/PC.csv',index=False)
# doc_df.to_csv('csv/DOC.csv',index=False)
# mon_df.to_csv('csv/MON.csv',index=False)




# comp_df = pd.read_excel('HQcomputers.xlsx')

# df = comp_df.to_numpy()
# nome = input("Buscar Usuário:")
# for i in range(len(df)):
#     if nome in df[i][4]:
#         print(df[i][3])
#         df[i][3] = "outra coisa"
        

# mon_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Monitors.xlsx')
# mon_df = mon_df.sort_values(by=['Primary User'],ascending=True,ignore_index=True)
# print(mon_df.dtypes)



