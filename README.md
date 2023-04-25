# grafos
Repositório para trabalhos de grafos

Para instalar as dependências:
poetry install

Para execetuar:
poetry run python graph OPTION FILE

Sendo OPTION susbtítuido por um número:

1 - Apresenta as informações básicas do grafo
2 - Apresenta a busca em largura
3 - Apresenta a existência, ou não, de ciclo euleriano
4 - Apresenta Bellman-Ford
5 - Apresenta Floyd-Warshall

Sendo FILE substítuido por um arquivo de grafo num modelo como o exemplo a seguir:

*vertices n
1 label1
2 label2
3 label3
4 label4
...
n labeln
*edges
label1 label2 weight1
label1 label3 weight2
label2 label4 weight3
...
