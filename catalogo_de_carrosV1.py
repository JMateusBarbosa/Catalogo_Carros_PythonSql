import getpass
import pandas as pd
import mysql.connector
# Abrindo uma conexão com o banco de dados:
cnx = mysql.connector.connect(
    host="localhost", 
    user='root', 
    password="123456", 
    db= 'catalogo_de_carrosV1')
print('Banco de dados conectado!!')
cursor = cnx.cursor()
print('-------------------------------------------------------------------')
print('BEM VINDO AO SISTEMA DE CATALOGO DE CARROS JM')
print('-------------------------------------------------------------------')

res = True
while res:
    print('\n MENU PRINCIPAL')
    print('-------------------------------------------------------------------')
    print("""
    DESEJA:
    1.Visualizar o Catalogo    
    2.Realizar Login  
    3.SAIR
    """)         
    res = int(input('escolha uma das opições acima: '))
    print('-------------------------------------------------------------------')

    if res == 1:
        resposta = True
        
        while resposta:
            print("""
            MENU CATEGORIAS:
            1.Esportivos    
            2.Caminhonetes  
            3.Sedãs
            4.SAIR
            """)         
            resposta = int(input('escolha uma das categorias acima: '))
            print('-------------------------------------------------------------------')

            if resposta== 1 :
                r1 = True
                while r1:
                    print('\n Esportivos')
                    print("""
                    MENU CARROS ESPORTIVOS:
                    1.visualizar todos os itens    
                    2.visualizar somente um  especifico
                    3.visualizar a descrição de um item especifico
                    4.visualizar o valor de um item especifico  
                    5.VOLTAR
                    """)
                    r1 = int(input('Escolha uma das opições acima digitando o numero da opição: '))
                    print('-------------------------------------------------------------------')

                    if r1 == 1:
                        print('\n ## VISUALIZA TODOS OS ITEMS ##')
                        print('\n')
                        db = []
                        
                        cursor.execute("SELECT * FROM catalogo_de_carrosv1.esportivos")
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                        
                        
                    elif r1 == 2:
                        print('\n ## VISUALIZAR SOMENTE UM ESPECIFICO ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro: '))
                        cursor.execute("SELECT * FROM catalogo_de_carrosv1.esportivos WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                    
                        
                    elif r1 == 3:
                        print('\n ## VISUALIZAR A DESCRIÇÃO ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro que deseja visualizar a descrição: '))
                        cursor.execute("SELECT nome,descrição FROM catalogo_de_carrosv1.esportivos WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["NOME","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)   
                    
                    elif r1 == 4:
                        print('\n ## VISUALIZAR O VALOR ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro que deseja visualizar o valor: '))
                        cursor.execute("SELECT nome,valor FROM catalogo_de_carrosv1.esportivos WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["NOME","VALOR"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)   
                    
                    elif r1 == 5:
                        print('\n Fim do Menu para carros Esportivos')
                        print('-------------------------------------------------------------------')
                        r1 = None
                    else:
                        print('\n Resposta ivalida!! DIGITE NOVAMENTE: ')
                
            elif resposta == 2:
                
                r2 = True
                while r2:
                    print('\n Caminhonete')
                    print("""
                    MENU CAMINHONETES:
                    1.visualizar todos os itens    
                    2.visualizar somente um  especifico
                    3.visualizar a descrição de um item especifico
                    4.visualizar o valor de um item especifico  
                    5.VOLTAR
                    """)
                    r2 = int(input('Escolha uma das opições acima digitando o numero da opição: '))
                    print('-------------------------------------------------------------------')

                    if r2 == 1:
                        print('\n ## VISUALIZA TODOS OS ITEMS ##')
                        print('\n')
                        db = []
                        cursor.execute("SELECT * FROM catalogo_de_carrosv1.caminhonete")
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                        
                    elif r2 == 2:
                        print('\n ## VISUALIZAR SOMENTE UM ESPECIFICO ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro: '))
                        print('\n')
                        cursor.execute("SELECT * FROM catalogo_de_carrosv1.caminhonete WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                    elif r2 == 3:
                        print('\n ## VISUALIZAR A DESCRIÇÃO ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro que deseja visualizar a descrição: '))
                        print('\n')
                        cursor.execute("SELECT nome,descrição FROM catalogo_de_carrosv1.esportivos WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["NOME","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)  
                    elif r2 == 4:
                        print('\n ## VISUALIZAR O VALOR ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro que deseja visualizar o valor: '))
                        print('\n')
                        cursor.execute("SELECT nome,valor FROM catalogo_de_carrosv1.caminhonete WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["NOME","VALOR"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                    
                    elif r2 == 5:
                        print('\n Fim do Menu para carros Caminhonetes')
                        print('-------------------------------------------------------------------')
                        r2 = None
                    else:
                        print('\n Resposta ivalida!! DIGITE NOVAMENTE: ')
                
            elif resposta == 3:
                
                r3 = True
                while r3:
                    print('\n Sedãs')
                    print("""
                    MENU SEDÂS:
                    1.visualizar todos os itens    
                    2.visualizar somente um  especifico
                    3.visualizar a descrição de um item especifico
                    4.visualizar o valor de um item especifico  
                    5.VOLTAR
                    """)
                    r3 = int(input('Escolha uma das opições acima digitando o numero da opição: '))
                    print('-------------------------------------------------------------------')

                    if r3 == 1:
                        print('\n ## VISUALIZA TODOS OS ITEMS ##')
                        print('\n')
                        db = []
                        cursor.execute("SELECT * FROM catalogo_de_carrosv1.sedãs")
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                    elif r3 == 2:
                        print('\n ## VISUALIZAR SOMENTE UM ESPECIFICO ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro: '))
                        print('\n')
                        cursor.execute("SELECT * FROM catalogo_de_carrosv1.sedãs WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                    elif r3 == 3:
                        print('\n ## VISUALIZAR A DESCRIÇÃO ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro que deseja visualizar a descrição: '))
                        print('\n')
                        cursor.execute("SELECT nome,descrição FROM catalogo_de_carrosv1.sedãs WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["NOME","DESCRIÇÃO"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)
                            
                    elif r3 == 4:
                        print('\n ## VISUALIZAR O VALOR ##')
                        db = []
                        cod = int(input('\n Digite o Codigo do carro que deseja visualizar o valor: '))
                        print('\n')
                        cursor.execute("SELECT nome,valor FROM catalogo_de_carrosv1.sedãs WHERE id = %d" % cod)
                        resultado = cursor.fetchall()
                        for result in resultado :
                            result = list(result)
                            db.append(result)
                            print('\n')
                            
                        columns = ["NOME","VALOR"]
                        df = pd.DataFrame(db,columns=columns)
                        print(df)         
                        
                    elif r3 == 5:
                        print('\n Fim do Menu para carros Sedãs')
                        print('-------------------------------------------------------------------')

                        r3 = None
                    else:
                        print('\n Resposta ivalida!! DIGITE NOVAMENTE: ')
            elif resposta == 4:
                resposta = None
            else:
                print('Resposta invalida, digite novamente: ') 
        
    elif res ==2:
        replogin = True
        print('##LOGIN##')
        print("""
        DESEJA:
        1.Realizar Login    
        2.Criar conta 
        3.volta
        """)
        resplogin = int(input('escolha uma das opições acima: '))
        print('-------------------------------------------------------------------')
        while resplogin:
            if resplogin == 1:
                print('realizar login:')
                nome = input('Digite seu nome: ')
                verifica_nome = "SELECT nome  FROM login WHERE nome ='{}'".format(nome)
                cursor.execute(verifica_nome)
                resultado_nome = cursor.fetchall()
                senha = input('Informe sua senha: ')
                print('-------------------------------------------------------------------')
                verifica_senha = "SELECT senha FROM login WHERE senha ='{}'".format(senha)
                cursor.execute(verifica_senha)
                resultado_senha = cursor.fetchall()
                if len(resultado_nome and resultado_senha)!= 0:
                    adm = True
                    print('Bem vindo ADM!')
                    print('-------------------------------------------------------------------')
                        
            
                    print("""
                    DESEJA:
                    1.Visualizar banco de dados    
                    2.Alterar item de uma tabela  
                    3.Excluir item de uma tabela  
                    4.Sair
                    """)
                    adm = int(input('Informe uma opição: '))
                    print('-------------------------------------------------------------------')
                    while adm:
                            
                        if adm == 1:
                            print('Visualizar banco de dados ')
                            print('-------------------------------------------------------------------')
                            
                            respostADM = True
        
                            while respostADM:
                                print("""
                                MENU CATEGORIAS:
                                1.Esportivos    
                                2.Caminhonetes  
                                3.Sedãs
                                4.SAIR
                                """)         
                                respostADM = int(input('escolha uma das categorias acima: '))
                                print('-------------------------------------------------------------------')

                                if respostADM== 1 :
                                    print('\n ## VISUALIZA TODOS OS ITEMS DA CATEGORIA ESPORTIVOS ##')
                                    print('\n')
                                    db = []
                                    
                                    cursor.execute("SELECT * FROM catalogo_de_carrosv1.esportivos")
                                    resultado = cursor.fetchall()
                                    for result in resultado :
                                        result = list(result)
                                        db.append(result)
                                        print('\n')
                                        
                                    columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                                    df = pd.DataFrame(db,columns=columns)
                                    print(df)
                                elif respostADM==2:
                                    print('\n ## VISUALIZA TODOS OS ITEMS DA CATEGORIA CAMINHONETES ##')
                                    print('\n')
                                    db = []
                                    
                                    cursor.execute("SELECT * FROM catalogo_de_carrosv1.caminhonete")
                                    resultado = cursor.fetchall()
                                    for result in resultado :
                                        result = list(result)
                                        db.append(result)
                                        print('\n')
                                        
                                    columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                                    df = pd.DataFrame(db,columns=columns)
                                    print(df)
                                elif respostADM==3:
                                    print('\n ## VISUALIZA TODOS OS ITEMS DA CATEGORIA SEDÃS ##')
                                    print('\n')
                                    db = []
                                    
                                    cursor.execute("SELECT * FROM catalogo_de_carrosv1.sedãs")
                                    resultado = cursor.fetchall()
                                    for result in resultado :
                                        result = list(result)
                                        db.append(result)
                                        print('\n')
                                        
                                    columns = ["ID","MARCA","NOME","VALOR","DESCRIÇÃO"]
                                    df = pd.DataFrame(db,columns=columns)
                                    print(df)
                                elif respostADM == 4:
                                    respostADM = None
                                else:
                                    print('Resposta invalida, digite novamente: ')    
                            
                            adm = None
                        elif adm == 2:
                            print('## UPdate de um item ##')
                            print('-------------------------------------------------------------------')
                            print("""
                                1.Sedãs    
                                2.Esportivos  
                                3.Caminhonetes  
                                """)
                            tabela = int(input('Infoem e de qual tabela desej excluir um item: '))
                            if tabela == 1:
                                cod = int(input('\n Informe o ID do item a ser realizado o UPdate: '))
                                cursor.execute("UPDATE catalogo_de_carrosv1.sedãs SET nome = 'Maria' WHERE id = %d" % cod)
                                sql = "INSERT INTO login(nome, senha) values (%s, %s)"
                                sql_data = (nome, senha1)
                                cursor.execute(sql, sql_data)
                                cnx.commit()
                                print('Dados inseridos com sucesso!!')
                                print('-------------------------------------------------------------------')
                            
                            
                            adm = None
                        elif adm == 3:
                            print('Excluir item de uma tabela')
                            print('-------------------------------------------------------------------')
                            print("""
                                1.Sedãs    
                                2.Esportivos  
                                3.Caminhonetes  
                                """)
                            tabela = int(input('Infoem e de qual tabela desej excluir um item: '))
                            if tabela == 1:
                                cod = int(input('\n Digite o id do carro  que desseja excluir: '))
                                print('\n')
                                cursor.execute("DELETE  FROM catalogo_de_carrosv1.sedãs WHERE id = %d" % cod)
                                resultado = cursor.fetchall()
                                cnx.commit()
                                print('Carro excluido com sucesso!!')
                                print('-------------------------------------------------------------------')
                            elif tabela == 2:
                                cod = int(input('\n Digite o id do carro  que desseja excluir: '))
                                print('\n')
                                cursor.execute("DELETE  FROM catalogo_de_carrosv1.esportivos WHERE id = %d" % cod)
                                resultado = cursor.fetchall()
                                cnx.commit()
                                print('Carro excluido com sucesso!!')
                                print('-------------------------------------------------------------------')
                            elif tabela == 3:
                                cod = int(input('\n Digite o id do carro  que desseja excluir: '))
                                print('\n')
                                cursor.execute("DELETE  FROM catalogo_de_carrosv1.esportivos WHERE id = %d" % cod)
                                resultado = cursor.fetchall()
                                cnx.commit()
                                print('Carro excluido com sucesso!!')
                                print('-------------------------------------------------------------------')
                            else:
                                print('Opição invalida')
                            adm = None
                        elif adm == 4:
                            print('\n Fim do Menu')
                            print('-------------------------------------------------------------------')
                            adm = None
                        else:
                            print('\n Resposta invalida ')
                            adm = int(input('Informe uma opição: '))    
                    resplogin = None           
                else:
                    print('Nome ou senha digitado errado')
                    
                    
                        
                
                
                
                
            elif resplogin == 2:
                print('## CRIAR CONTA ##')
                nome = input('Digite um nome para cadastro: ')
                senha1 = input('Informe uma senha para cadastro: ')
                senha2 = input('Digite novamente a  senha: ')
                print('-------------------------------------------------------------------')
                
                verifica_nome = "SELECT nome FROM login WHERE nome ='{}'".format(nome)
                cursor.execute(verifica_nome)
                resultado = cursor.fetchall()
                while len(resultado)!= 0:
                    print('Este usuario ja possui um cadastro!')
                    nome = str(input('Digite outro nome para cadastro: '))
                    verifica_nome = "SELECT nome FROM login WHERE nome ='{}'".format(nome)
                    cursor.execute(verifica_nome)
                    resultado = cursor.fetchall()
                print('Nome de usuario aceito')
                while (senha1 != senha2):
                    print('\n Senha invalida, as duas dever ser iguais! ')
                    senha1 = input('Informe uma senha novamente: ')
                    senha2 = input('Digite novamente a  senha: ')
                    print('-------------------------------------------------------------------')
                print('Senha aceita')
                
                sql = "INSERT INTO login(nome, senha) values (%s, %s)"
                sql_data = (nome, senha1)
                cursor.execute(sql, sql_data)
                cnx.commit()
                print('Dados inseridos com sucesso!!')
                print('-------------------------------------------------------------------')
                resplogin = None
            elif resplogin == 3:
                resplogin = None
            else:
                print('Resposta invalida ')
    elif res == 3:
        res = None
    else:
        print('Resposta invalida, digite novamente: ')



print('\n FIM DO PROGRAMA')
cnx.close()
print('Conexão com o banco encerrada!!')