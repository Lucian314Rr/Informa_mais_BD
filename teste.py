import mysql.connector #Importamos o concector MySQL que implementa o Banco

#Aqui vai as credenciais do nosso banco. Isso varia entre as máquinas, então por enquanto não foquemos aqui
#e sim nos códigos SQL
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = ""
)

#O cursor precisa ser criado para que possamos executar os códigos SQL no Python
#Lembra bastante os Objetos em Java.
mycursor = mydb.cursor()

#Aqui é onde a mágica acontece. Através dessa linha executando esse método, o que
#estiver entre as aspas duplas será executado no Banco propriamente dito
#Resumindo, é a ÚNICA parte do código que iramos mexer, por enquanto
mycursor.execute("CRAETE DATABASE IMFORMA_MAIS")
mycursor.execute("CRAETE TABLE Cidadao(nome VARCHAR(30) NOT NULL, PRIMARY KEY email VARCHAR(30) NOT NULL, data DATE NOT NULL, telefone VARCHAR(12) NOT NULL, FOREIGN KEY ID_Relato INTERGER NOT NULL)")
mycursor.execute("CRAETE TABLE Endereco(rua VARCHAR(25) NOT NULL, bairro VARCHAR(20) NOT NULL, cidade VARCHAR(15) NOT NULL, cep VARCHAR(10) NOT NULL, numero VARCHAR(4) NOT NULL, FOREIGN KEY email_cidadao VARCHAR(35) NOT NULL,)")
mycursor.execute("CRAETE TABLE Relato(descricao VARCHAR(100) NOT NULL, PRIMARY KEY ID_relato INTEGER NOT NULL, data DATETIME NOT NULL, FOREIGN KEY status BOoLEAN NOT NULL)")#nao sei como colocar categoria_problema, subcategoria_problema, localizacao, midia
mycursor.execute("CRAETE TABLE Prestador de servico publico(nome VARCHAR(30) NOT NULL, orgao/empresa VARCHAR(15) NOT NULL, PRIMARY KEY ID_funcionario INTERGER)")
mycursor.execute("CRAETE TABLE Midia(foto INTEGER NOT NULL, video NOT NULL, FOREIGN KEY nome VARCHAR(30) NOT NULL)")
mycursor.execute("CRAETE TABLE Problema(PRIMERY KEY categoria VARCHAR(20) NOT NULL, PRIMARY KEY subcategoria VARCHAR(20) NOT NULL, FOREIGN KEY ID_relato INTEGER NOT NULL)")
mycursor.execute("CRAETE TABLE Localizacao(rua VARCHAR(15) NOT NULL, bairro VARCHAR(20) NOT NULL, cidade VARCHAR(20) NOT NULL, cep VARCHAR(10) NOT NULL, FOREIGN KEY ID_Relato INTERGER NOT NULL)")
#Sinceramente não me lembro pra quê serve isso, mas sei que é necessário
#Quem souber, deixa aqui nos comentários
myresult = mycursor.fetchall()

#Isso daqui não vamos usar, porque digamos que isso "substitui" o SELECT no MySQL
#então o professor não permitiu usar. E pra falar a verdade, achei o SELECT muito
#mais fácil de usar. Não precisamos mexer nessa parte do código
for x in myresult:
    print(x)
