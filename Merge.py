import pandas as pd
#from urllib import request
'''
>>>Também é possive deixar a leitura de arquivos variavel.

entrada1 = input("caminho do arquivo(sem extensão):")
comp_df = pd.read_excel(entrada1 + '.xlsx')

>>>OBS:isso possibilita a criação de executavel para leitura de planilhas
inicialmente o programa deverá unir 2 ou mais planilhas que tenham dados em comuns.
isso irá gerar uma nova planilhas retornando dados expecificos que todas as planilhas possuiam separadamente. 
'''
'''
Buscando cada planilha online 
url_OneDrive = 'http://giorgiglobal-my.sharepoint.com/:x:/r/personal/paulo_desouza_canpack_com/_layouts/15/Doc.aspx?sourcedoc=%7BB7CD2344-A2C0-4093-9D56-E3686981F08B%7D&file=HQ%20Computers.xlsx&action=default&mobileredirect=true'

comp_file = "HQ Computers.xlsx"
doc_file = "HQ Docking stations.xlsx"
mon_file = "HQ Monitors.xlsx"
#>>> baixa as planilhas para a pasta do script
request.urlretrieve(url_OneDrive,comp_file)
request.urlretrieve(url_OneDrive,doc_file)
request.urlretrieve(url_OneDrive,mon_file)
'''
# Busca as planilhas direto no One Drive, sincronizado na maquina.
comp_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Computers.xlsx')
doc_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Docking stations.xlsx')
mon_df = pd.read_excel('C://Users/paulo.desouza/OneDrive - giorgiglobal/Equipamentos HQ/HQ Monitors.xlsx')

# ordenando o DataFrame , com base na coluna Primary User, em ordem crescente e ignorando o indice. 
comp_df = comp_df.sort_values(by=['Primary User'], ascending=True,ignore_index=True)
# pegando apenas as colunas informadas
comp_df = comp_df [['Friendly Name','Primary User', 'Serial Number']]

doc_df = doc_df.sort_values(by=['Primary User'],ascending=True,ignore_index=True)
# pegando apenas as colunas informadas
doc_df = doc_df[['Primary User','Service Tag']]

mon_df= mon_df.sort_values(by=['Primary User'],ascending=True,ignore_index=True)
# pegando apenas as colunas informadas
mon_df = mon_df[['Primary User','Serial Number']]

# criando um dicionario que será a união dos 3 DataFrame
tabela = {}
tabela = pd.DataFrame(tabela)

# unindo dois dataframes dentro de tabela, utilizando 'Primary User' como chave na criação de cada linha do novo dataframe
tabela = pd.merge(comp_df, doc_df, how = 'left', left_on='Primary User' , right_on='Primary User')
# left_on e right_on podem ter nomes diferentes(colunas), o importante é terem dados similares.

tabela = pd.merge (tabela , mon_df, how='left',left_on='Primary User', right_on='Primary User')

#renomear o nome das colunas para cria uma planilha com os dados resultantes
tabela = tabela.rename(
    columns={
        "Serial Number_x":"PC",
        "Service Tag":"Dockstation",
        "Serial Number_y":"Monitores"
        }
    )

# Cria uma planilha com o data Frame "Tabela" no One Drive.
tabela.to_csv('csv/Equipamentos por pessoa.csv',index=False)
tabela.to_excel('planilha/Equipamentos_planilha.xlsx',index=False)



