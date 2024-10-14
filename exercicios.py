#quantidade = 40
#preco = 20

#if quantidade > 0 and preco > 0:
#   print('valores válidos')
#else:
 #   print('valores inválidos')

#lista_de_alunos = ["geralt", "Agatha","Yennefer"]

#for i in lista_de_alunos:
    #print(i)

texto = "hoje e nossa segunda aula do bootcamp, bootcamp de python"

novo_texto = texto.replace(",","")

palavras = novo_texto.split()

print(palavras)
contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)

