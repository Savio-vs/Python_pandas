import pandas as pd
from novo_item import *

# altera o Primary User em cada planilha particular. 
# Os arquivos csv e xlsx são atualizados.
def alterar_nome(name,new_name):
    comp = pd.read_csv('csv/PC.csv')
    doc = pd.read_csv('csv/DOC.csv')
    mon = pd.read_csv('csv/MON.csv')
    
    comp_df = comp.to_numpy()
    doc_df = doc.to_numpy()
    mon_df = mon.to_numpy()
    

    for i in range(len(comp_df)):# percorre todos os dados em comp_df e procurar o usuário cadastrado
        if name in comp_df[i][5]:
            comp_df[i][5] = new_name
            comp.to_csv("csv/PC.csv",index=False)
            comp.to_excel("planilha/COM.xlsx",index=False)
        
        if name in mon_df[i][7]:
            mon_df[i][7] = new_name
            mon.to_csv("csv/MON.csv",index=False)
            mon.to_excel("planilha/MON.xlsx",index=False)
    
    for d in range(len(doc_df)):   
        if name in doc_df[d][7]:
            doc_df[d][7] = new_name
            doc.to_csv("csv/DOC.csv",index=False)
            doc.to_excel("planilha/DOC.xlsx",index=False)
       
    

def alterar_comp(ST):
    com = pd.read_csv("csv/PC.csv")
    comp_df = com.to_numpy()
    
    
    for i in range (len(comp_df)):
        if ST == comp_df[i][5]:
            novo = input('novo equipamento:')
            comp_df[i][5] = novo
            com.to_csv('csv/COM.csv',index=False)
            com.to_excel('planilha/COM.xlsx',index=False)
            return novo               

def alterar_doc(ST,name,FN):
    doc = pd.read_csv("csv/DOC.csv")
    doc_df = doc.to_numpy()
    
    cont = 0 
    for i in range (len(doc_df)):
        if ST == doc_df[i][5]:
            novo = input("novo Equipamento:")
            doc_df[i][5] = novo
            doc.to_csv('csv/DOC.csv',index=False)
            doc.to_excel('planilha/DOC.xlsx',index=False)
            cont+= 1
            return novo
            

    if cont == 0:# Adicionar uma pessoa ao arquivo.
        colunas = len(doc_df[collum])
        novo_doc = new_Doc(colunas,name,FN)
        return novo_doc
        
def alterar_mon(ST,name):
    mon = pd.read_csv("csv/MON.csv")
    mon_df = mon.to_numpy()
    
    cont = 0 
    
    for i in range (len(mon_df)):
        if ST == mon_df[i][5]:
            novo = input("novo Equipamento:")
            mon_df[i][5] = novo
            mon.to_csv('csv/MON.csv',index=False)
            mon.to_excel('planilha/MON.xlsx',index=False)
            cont+= 1
            return novo
            
    
    if cont == 0:# Adicionar uma pessoa ao arquivo.
        colunas = len(mon_df[collum])
        novo_mon = new_Mon(colunas,name)
        return novo_mon

       
pessoas_df = pd.read_csv('csv/Equipamentos por pessoa.csv')

pessoas_df = pessoas_df.sort_values(by=["Primary User"],ignore_index=True,ascending=True)

# df vai ser uma matriz com os dados do DataFrame pessoas_df 
# posibilitando uma melhor alteração dos dados.
df= pessoas_df.to_numpy()# OBS: o DataFrame de entrada precisa ter todas as colunas do mesmo dtype.(dados Homogenios)
loop = True
while loop:
    nome = input("Buscar Usuário:")
    for i in range(len(df)):
        if nome in df[i][1]:# df[i][1] representa a coluna "Primary User" 
            print(f"\n\nUsuário: {df[i][1]}\nPC: {df[i][2]}\nDockstation: {df[i][3]}\nMonitor:{df[i][4]}")
            collum=int(input('''
            1-Primary User:
            2-PC:
            3-Dockstation:
            4-Monitores:
            5-Continuar Busca:
            6-Sair:
            Identifique a Coluna que será alterada:'''))
            
            if collum == 1:
                nome_novo = input("Novo Nome:") 
                alterar_nome(name=nome ,new_name=nome_novo)
                df[i][1] = nome_novo

            elif collum == 2:
                
                service_tag = df[i][2]
                df[i][2] = alterar_comp(service_tag)
                
                x= (input('Continuar?\nS ou N')).upper
                if x == "N":
                    break
                else:pass  

            elif collum == 3:
                service_tag = df[i][3]
                df[i][3] = alterar_doc(service_tag,name=df[i][1],FN=df[i][0]) 
                
                x= (input('Continuar?\nS ou N')).upper
                if x == "N":
                    break
                else:pass
       
            elif collum == 4:
                service_tag = df[i][4]
                df[i][4] = alterar_mon(service_tag,name=df[i][1])
                
                x= (input('Continuar?\nS ou N')).upper
                if x == "N":
                    break
                else:pass
       
            elif collum == 5 :
                pass
       
            elif collum ==6:
                loop = False
            else:
                print("indice incorreto:\n")
        

pessoas_df.to_csv("csv/Equipamentos por pessoa.csv",index=False)
pessoas_df.to_excel("planilha/Equipamentos_planilha.xlsx",index=False)

