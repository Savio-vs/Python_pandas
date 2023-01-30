import pandas as pd


def new_Doc(colunas,name,FN):
    doc_df = pd.read_csv('csv/DOC.csv')
    
    print(f'colunas = {colunas}')
    
    index = doc_df.columns.array
    df = {}
    for i in range (len(index)):
        if index[i] == 'Friendly Name':
            df[index[i]] = FN
        
        elif index[i] == 'Primary User':
            df[index[i]] = name
        
        elif index[i] == 'Service Tag':
            # Se faz necessario retornar um valor para atualizar a base de equipamentos por pessoa.
            # Por isso a variavel 'novo_doc' é criada.
            novo_doc = input(f'Iserir -> {index[i]}:')
            df[index[i]] = novo_doc 
        
        elif index[i] == 'Id':
            df[index[i]] = input(f'Iserir -> {index[i]}:')
        # Apenas as informações a cima são necessarias para a criação de um novo Doc, as colunas restantes são preenchidas com os valores 
        # que já existem no DataFrame 'doc_df'
        else:
            df[index[i]] = doc_df.iloc[0,i]
    
    # criando um DataFrame com o dicionario 
    df = pd.DataFrame(df,index=[0])
    
    # concatenando o DataFrame criado anteriormente com a nossa base de dados, e ordenando a base de dados.
    doc_df = pd.concat([doc_df,df],ignore_index=True)
    doc_df = doc_df.sort_values('Primary User',ignore_index=True,ascending=True)
    
    # salvando as alterações
    doc_df.to_csv('csv/DOC.csv',index=False)
    doc_df.to_excel('planilha/DOC.xlsx',index=False)
    return novo_doc

def new_Mon(colunas,name):
    mon = pd.read_csv('csv/MON.csv')
    mon_df = mon.to_numpy()
    
    for i in range (colunas):
        print(mon_df[0][i])