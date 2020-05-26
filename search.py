import index_engine

v = index_engine.VectorCompare()

documents = {
    0:'''
Na escala, você atingirá todos os problemas de desempenho Eu costumava pensar que sabia um pouco sobre escalabilidade de desempenho e como manter as coisas em movimento quando você obtém grandes quantidades de dados. A verdade é que sei agachar-me sobre o assunto, já que o máximo que já fiz foi lido sobre como isso é feito Para entender como eu percebi isso, você precisa de alguns antecedentes ''',
    1:'''
Richard Stallman para visitar a Austrália Normalmente não sou de promover eventos e afins, a menos que eu sinta que há um benefício genuíno em participar, mas esse é um ponto em que Richard M Stallman, o guru do Software Livre, está descendo para dar uma palestra Você pode ler sobre ele aqui Open Source Celebrity para visitar a Austrália ''',
    2:'''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain ''',
    3:'''
Por que você não deveria lançar seu próprio CAPTCHA Em um TechEd que participei há alguns anos, eu assistia a uma apresentação sobre segurança apresentada por Rocky Heckman, que leu seu blog muito bom. Ele estava falando sobre algoritmos de segurança. A parte que realmente me chamou a atenção foi a seguinte: isto ''',
    4:'''
O grande benefício do desenvolvimento orientado a testes Ninguém fala sobre o sentimento de produtividade porque você está escrevendo muito código Pense nisso por um momento Pergunte a qualquer desenvolvedor que queira desenvolver por que se tornou um desenvolvedor Uma das primeiras coisas que surge é que eu aprecio escrever código Essa é uma das coisas que eu pessoalmente gosto de escrever Código, especialmente quando resolver o meu problema atual, me faz sentir produtivo. Faz com que eu sinta que estou chegando a algum lugar. ''',
    5:'''Configurando o GIT para usar um fluxo de trabalho no estilo SVN do Subversion Mover do SVN para o GIT do Subversion pode ser um pouco confuso no começo. Acho que a maior coisa que notei foi que o GIT não tem um fluxo de trabalho específico. Você precisa escolher o seu. Pessoalmente, eu queria manter meu Subversion é como um fluxo de trabalho com um servidor central no qual todas as minhas máquinas puxavam e empurravam. ''',
    6:'''Por que o CAPTCHA nunca usa números 0 1 5 7 Curiosamente, esse tipo de pergunta aparece muito nos meus termos de pesquisa referentes Por que o CAPTCHA nunca usa os números 0 1 5 7 É uma questão de relatividade simples, com uma resposta razoavelmente simples É porque cada uma das opções acima é fácil confundir números com uma letra Veja abaixo '''
}


index = {
    0:v.concordance(documents[0].lower()),
    1:v.concordance(documents[1].lower()),
    2:v.concordance(documents[2].lower()),
    3:v.concordance(documents[3].lower()),
    4:v.concordance(documents[4].lower()),
    5:v.concordance(documents[5].lower()),
    6:v.concordance(documents[6].lower()),
}


searchterm = str(input('Entre com umm termo de pesquisa: '))
matches = []


for i in range(len(index)):
    relation = v.relation(v.concordance(searchterm.lower()),index[i])
    if relation != 0:
        matches.append((relation,documents[i][:100]))


matches.sort(reverse=True)


for i in matches:
    print(i[0],i[1])