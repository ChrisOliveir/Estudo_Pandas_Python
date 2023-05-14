## PANDAS

### DataFrame 
DataFrame é uma tabela. Ela contém uma matriz de entradas individuais, cada uma com um determinado valor. Cada entrada corresponde a uma linha (registro) e uma coluna.
As entradas do DataFrame não estão limitadas a números inteiros.

Usamos o construtor pd.DataFrame() para gerar esses objetos DataFrame. Uma das sintaxes para declarar um  DataFrame é um dicionários por exemplo  cujas chaves são nomes das colunas e os valores são uma lista de entradas.

O contrutor de lista de dicionário atribui valores aos rótulos das colunas, mas usa apenas uma contagem crescente de (0,1,2,3,4..) para os rótulos de linhas. As vezes tudo bem, mas muitas vezes queremos atribuir esses rótulos nós mesmos.

### SERIES 

Uma série é uma sequência de valores de dados. Enquanto um DataFrame é uma tabela, uma série é uma lista. Podemos adicionar o nome do index como no DataFrame porem uma série não possui um nome de coluna, ela possui um nome geral.

### Lendo arquivos de dados

Saber criar um DatFrame e uma Série é muito útil, porém na maioria das vezes não criaremos nossos próprios dados manualmente, trabalharemos com dados já existentes.
Os dados podem ser armazenados de várias formas e formatos diferentes. O mais básico deles é p CSV (que é uma tabela de valores separados por virgulas) dai seu nome Comma-Separated Values.

 - Usamos o atributo Shape para verificar o tamanho do DataFrame.
 - Podemos usar o conteúdo do DataFrame usando o comando head() quie captura as 5 primeiras linhas.

### Seleção Nativa do Python

Selecionar valores específicos do pandas DataFrame ou Series para trabalhar é uma etapa implicita em quase todas as operações de dados que você executará, portanto, uma das primeiras coisas que precisamos aprender para trabalhar com dados em python é como selecionar pontos relevantes. Em python podemos acessar a propriedade de um objeto acessando-o como um atributo. A seleção nativa é [coluna, linha]

### Indexação no Pandas

Padrão: [Linha, Coluna]

Pandas tem seus próprios operadores de acesso:

- ILOC e LOC    

Seleção baseada em Index:

A indexação do Pandas finciona em um dos dois paradigmas. A primeira é a seleção baseada em índice: Selecionar dados com base na sua posição numérica nos dados (iloc segue esse paradigma)

Seleção baseada em Rótulos

O segundo paradigma para seleçao de atributos é aquele seguido pelo operador LOC: Seleção baseada em rótulos, nesse paradigma é o valor do índice de dados, não sua posição que importa.
Iiloc é mais simples que o LOC porque ele ignora os índices do conjunto de dados. LOC por outro lado usa as informações nos índices para fazer o seu trabalho.

### Qual escolher ILOC OU LOC?

Vale ter em mente é que os dois métodos usam esquemas de indexação diferentes
o iloc usa o esquema de indexação stdlib do Python onde o primeiro elemento do intervalo é incluído e o último excluido. Portando 0:10 selecionará entradas de 0,...,9 

Loc por sua vez indexa de forma inclusiva.Portanto 0:10 selecionará entradas 0,..,10

### Manipulando o índice

O método set_index() pode ser usado para fazer esse trabalho. 

### Seleção condicional 

Muitas vezes precisamos fazer perguntas com base nas condições.