#recebe um documento de testo limpo e devolve a concordancia das palavras(quantas palavras de cada uma exitem)
def concordance(document):
    if type(document) != str:
        raise ValueError('O argumento fornecido deve ser do tipo string')
    con = {}
    for word in document.split(' '):
        if word in con:
            con[word] = con[word] + 1
        else:
            con[word] = 1
    return con

a = open('teste.txt','r')
b = concordance(a.read())
print(b)