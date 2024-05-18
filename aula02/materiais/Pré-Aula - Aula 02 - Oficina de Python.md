# Pré-Aula dia 2

## String
### O que são Strings
Strings Python são sequências de caracteres entre aspas simples, duplas ou triplas. Strings são imutáveis ​​em python. Podemos acessar cada caractere de uma string usando emenda de string em python. A emenda também é denominada indexação.
## O que é String Splicing em Python?
A emenda ou indexação de strings é um método pelo qual podemos acessar qualquer caractere ou grupo de caracteres de uma string python. Em python, caracteres ou substrings de uma string podem ser acessados ​​​​com a ajuda de colchetes, [ ]assim como acessamos elementos de uma lista em python. Podemos acessar um caractere de uma string usando índices positivos e também índices negativos.

Ao usar índices positivos para emenda de string em python, o primeiro caractere da string recebe o índice zero e o índice dos caracteres subsequentes é aumentado em 1 até o final.

Por exemplo, podemos imprimir o primeiro caractere, o terceiro caractere e o décimo primeiro caractere de uma string usando o programa a seguir. Observe que a indexação é 0 baseada em python . ou seja, o primeiro caractere recebe o índice 0 e não 1.
```py
myString="PythonForBeginners"
x=myString[0]
print(x)
x=myString[2]
print(x)
x=myString[10]
print(x)
```
Saída:

> P
>
>t
>
>e

Ao usar índices negativos para emenda de string em python, o último caractere da string python recebe o índice -1 e, movendo-se para trás, cada caractere recebe o índice 1 menor que seu caracter anterior.

No exemplo a seguir, usamos indexação negativa para imprimir caracteres de uma string python.
```py
myString="PythonForBeginners"
x=myString[-1]
print(x)
x=myString[-5]
print(x)
x=myString[-10]
print(x)
```
Saída:
>s
>
>n
>
>r

### Como capturar uma substring de uma string python?
Uma substring é uma parte contínua de uma string python. Pode começar em qualquer índice e terminar em qualquer índice.

Usando indexação positiva, podemos capturar uma substring usando `[ ]`o operador de colchetes. Podemos especificar o índice do caractere inicial e o índice do caractere final da string que será incluída na substring. A sintaxe para retirar a substring é `string_name[start_index:last_index]`. O caractere at `start_index` está incluído na substring, mas o caractere at `last_index` não está incluído. Somente caracteres até o índice `last_index-1` são incluídos. Portanto, `start_index` é inclusivo enquanto `last_index` é exclusivo.

Nos exemplos abaixo, podemos ver que os caracteres `start_index` foram incluídos na saída e os caracteres `last_index` não foram incluídos na saída.
```py
myString="PythonForBeginners"
x=myString[0:5]
print(x)
x=myString[6:9]
print(x)
x=myString[0:6]
print(x)
```
Saída:

>Pytho
>
>For
>
>Python

Para capturar uma substring desde o início até um determinado índice, podemos deixar o start_indexvalor vazio.

```py
myString="PythonForBeginners"
x=myString[:6]
print(x)
x=myString[:9]
print(x)
x=myString[:18]
print(x)
```
Saída:
>Python
>
>PythonFor
>
>PythonForBeginners

Para capturar uma string começando em um determinado índice e terminando no último índice, podemos simplesmente deixar o last_indexvalor vazio.
```py
myString="PythonForBeginners"
x=myString[0:]
print(x)
x=myString[6:]
print(x)
x=myString[9:]
print(x)
```
Saída:

>PythonForBeginners
>
>ForBeginners
>
>Beginners

Também podemos capturar substrings de strings python usando índices negativos da mesma forma que acima.
```py
myString="PythonForBeginners"
x=myString[-10:-1]
print(x)
x=myString[:-1]
print(x)
x=myString[-5:-1]
print(x)
```

>rBeginner
>
>PythonForBeginner
>
>nner

### Slice [start:stop:step]
`slice(start:stop[:step])` é um objeto que geralmente contém uma parte de uma sequência. Uma fatia é criada usando a notação subscrita,com dois pontos entre números quando vários são fornecidos, como em nome_da_variável[1:3:5].

Argumentos
Esta função pode ser usada para dividir tuplas, arrays e listas.

O valor do `start` parâmetro (ou None se não for fornecido)

O valor do `stop` parâmetro (ou último índice da sequência)

O valor do `step` parâmetro (ou None se não for fornecido). Não pode ser 0.

Todos os três devem ser do tipo inteiro.

Retornar
Se for `stop` fornecido, ele gera parte da sequência do índice 0 até `stop`.

Se apenas `start` for fornecido, ele gera parte da sequência após o índice `start` até o último elemento.

Se ambos `start` e `stop` forem fornecidos, ele gera parte da sequência após o índice `start` até `stop`.

Se todos os três starte stop forem `step` fornecidos, ele gera parte da sequência após o índice `start` até stop com incremento do índice `step`.

Exemplo
```py
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a[:5])    # prints [1, 2, 3, 4, 5]
print(a[2:])    # prints [3, 4, 5, 6, 7, 8]
print(a[2:5])    # prints [3, 4, 5]
print(a[2:7:2])    # prints [3, 5, 7]
```
Você pode indexar o último índice de uma sequência usando -1:
```py
a = [1, 2, 3, 4, 5, 6]
print(a[-1])    # prints 6
print(a[2:-1])    # prints [3, 4, 5]
```
Você pode inverter uma sequência usando a [::-1] notação de fatia:
```py
a = [1, 2, 3, 4, 5, 6]
print(a[::-1])    # prints [6, 5, 4, 3, 2, 1]
```
## Métodoos String
### O que são Métodos de String em Python?

Métodos de string em Python são funções embutidas na linguagem que permitem manipular e trabalhar com textos. Uma string é uma sequência de caracteres, e esses métodos fornecem diversas operações para realizar tarefas como busca, substituição, concatenação, entre outras, em strings.

### Como Utilizar os Métodos de String em Python
Os métodos de string em Python são utilizados através da notação de ponto, onde o nome da string é seguido por um ponto e o nome do método desejado. Por exemplo, se tivermos uma string chamada “texto” e quisermos converter todas as letras para maiúsculas, podemos utilizar o método “upper()” da seguinte forma: “texto.upper()”.

Os principais métodos são:

1.  `lower()`

    O método `lower()` retorna uma nova string com todas as letras em minúsculas. Ele não modifica a string original, apenas retorna uma versão modificada. Por exemplo:
    ```py
    texto = "PYTHON STRING METHODS"
    texto_lower = texto.lower()
    print(texto_lower)  # saída: "python string methods"
    ```
1. `upper()`

    O método `upper()` retorna uma nova string com todas as letras em maiúsculas. Da mesma forma que o método `lower()`, ele não altera a string original. Veja o exemplo:
    ```py
    texto = "Python String Methods"
    texto_upper = texto.upper()
    print(texto_upper)  # saída: "PYTHON STRING METHODS"
    ```
1. `capitalize()`

    O método `capitalize()` retorna uma nova string com o primeiro caractere em maiúscula e os demais em minúscula. Os caracteres que não são letras não são modificados. Exemplo:
    ```py
    texto = "python string methods"
    texto_capitalize = texto.capitalize()
    print(texto_capitalize)  # saída: "Python string methods"
    ```
1. `count(substring)`

    O método `count(substring)` retorna o número de ocorrências de uma determinada substring na string. Por exemplo:
    ```py
    texto = "Python é uma linguagem de programação poderosa"
    ocorrencias = texto.count("a")
    print(ocorrencias)  # saída: 5
    ```
1. `replace(old, new)`

    O método `replace(old, new)` substitui todas as ocorrências de uma substring por outra. Por exemplo:
    ```py
    texto = "Python é uma linguagem de programação poderosa"
    novo_texto = texto.replace("Python", "Java")
    print(novo_texto)  # saída: "Java é uma linguagem de programação poderosa"
    ```
1. `split()`

    O método `split()` divide a string em uma lista de substrings com base em um separador. Por padrão, o separador é o espaço em branco. Exemplo:
    ```py
    texto = "Python é uma linguagem de programação"
    palavras = texto.split()
    print(palavras)  # saída: ["Python", "é", "uma", "linguagem", "de", "programação"]
    ```

    Esses são apenas alguns dos principais métodos de string em Python. Existem muitos outros disponíveis, cada um com sua funcionalidade específica. Aprender a utilizar esses métodos é essencial para manipular textos com facilidade e eficiência em seus programas Python.

## Listas em Python

O Python tem um ótimo tipo de lista embutido chamado "list". Os literais de lista são escritos entre colchetes [ ]. As listas funcionam de maneira semelhante às strings: use a função len() e os colchetes [ ] para acessar os dados, com o primeiro elemento no índice 0.
```py
  colors = ['red', 'blue', 'green']
  print(colors[0])    ## red
  print(colors[2])    ## green
  print(len(colors))  ## 3
```
![](https://developers.google.com/static/edu/python/images/list1.png?hl=pt-br)

A atribuição com um = nas listas não faz uma cópia. Em vez disso, a atribuição faz com que as duas variáveis apontem para a única lista na memória.
```py
  b = colors   ## Não copia a lista
```
![](https://developers.google.com/static/edu/python/images/list2.png?hl=pt-br)

A "lista vazia" é apenas um par vazio de colchetes [ ]. O "+" funciona para acrescentar duas listas, então [1, 2] + [3, 4] gera [1, 2, 3, 4] (isso é como um + com strings).

### FOR e IN
As construções *for* e *in* do Python são extremamente úteis, e o primeiro uso que veremos é com listas. A construção *for*, for var in list, é uma maneira fácil de analisar cada elemento de uma lista (ou outra coleção). Não adicione nem remova da lista durante a iteração.
```py
  squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print(sum)  ## 30
  ```
Se você sabe o que está na lista, use um nome de variável no loop que capture essa informação, como "num", "name" ou "url". Como o código Python não tem outra sintaxe para se lembrar dos tipos, os nomes das variáveis são uma maneira fundamental de identificar o que está acontecendo. Isso é um pouco enganoso. À medida que você ganhar mais exposição ao Python, verá referências a dicas de tipo que permitem adicionar informações de digitação às definições de função. O Python não usa essas dicas de tipo ao executar seus programas. Eles são usados por outros programas, como ambientes de desenvolvimento integrados (IDEs, na sigla em inglês) e ferramentas de análise estática, como linters/verificadores de tipo, para validar se as funções são chamadas com argumentos compatíveis.

A construção *in* por si só é uma maneira fácil de testar se um elemento aparece em uma lista ou outra coleção (`value in collection`). Ela testa se o valor está na coleção e retorna Verdadeiro/Falso.
```py
  list = ['larry', 'curly', 'moe']
  if 'curly' in list:
    print('yay') ## yay
```
As construções for/in são muito usadas no código Python e funcionam em tipos de dados diferentes de "list", então você precisa apenas memorizar a sintaxe. Você pode ter hábitos de outras linguagens em que você começa a iterar manualmente em uma coleção e, em Python, precisa usar apenas for/in.

Também é possível usar for/in para trabalhar em uma string. A string age como uma lista de caracteres. Portanto, a `for ch in s: print(ch)` mostra todos os caracteres dela.

### Intervalo 

A função range(n) gera os números 0, 1, ... n-1, e range(a, b) retorna a, a+1, ... b-1 - até, mas não incluindo, o último número. A combinação das funções for-loop e range() permite a criação de um loop numérico tradicional for:
```py
  ## imprima os números de 0 a 99
  for i in range(100):
    print(i)
```
Há uma variante xrange() que evita o custo de criar toda a lista para casos sensíveis de desempenho (no Python 3, range() terá o bom comportamento de desempenho e você pode esquecer o xrange()).
### Repetição while
O Python também tem a repetição "while" padrão. As instruções *break* e *continue* funcionam como em C++ e Java, alterando o curso do loop mais interno. As repetições "for/in" acima resolvem o caso comum de iteração em cada elemento de uma lista, mas a repetição "while" oferece controle total sobre os números do índice. Confira uma repetição "while" que acessa cada terceiro elemento de uma lista:
```py
  ## Access every 3rd element in a list
  i = 0
  while i < len(a):
    print(a[i])
    i = i + 3
```
Métodos de lista
Veja alguns outros métodos de lista comuns.

- list.append(elem) -- adiciona um único elemento ao final da lista. Erro comum: não retorna a nova lista, apenas modifica a original.
- list.insert(index, elem) -- insere o elemento no índice especificado, deslocando os elementos para a direita.
- list.extend(list2) adiciona os elementos de list2 ao final da lista. O uso de + ou += em uma lista é semelhante ao uso de expand().
- list.index(elem) -- pesquisa o elemento especificado no início da lista e retorna o índice dela. Lança um ValueError se o elemento não aparecer (use "in" para verificar sem um ValueError).
- list.remove(elem) -- pesquisa a primeira instância do elemento especificado e a remove (gera ValueError se não estiver presente)
- list.sort() -- classifica a lista no lugar (não a retorna). É preferível usar a função scheduled() exibida posteriormente.
- list.reverse(): inverte a lista atual (não a retorna)
- list.pop(index) -- remove e retorna o elemento no índice especificado. 

Retorna o elemento mais à direita se o índice for omitido (aproximadamente o oposto de anexar()).

Observe que esses são *métodos* em um objeto de lista, enquanto len() é uma função que usa a lista (ou string ou qualquer outra coisa) como um argumento.
```py
  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## anexar elemento no final
  list.insert(0, 'xxx')        ## insira o elemento no índice 0
  list.extend(['yyy', 'zzz'])  ## adicione lista de elementos no final
  print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print(list.index('curly'))    ## 2

  list.remove('curly')         ## pesquise e remova esse elemento
  list.pop(1)                  ## remove e retorna 'larry'
  print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
  ```

  Erro comum: os métodos acima não *retornam* a lista modificada, apenas modificam a lista original.
  ```py
  list = [1, 2, 3]
  print(list.append(4))   ## NO, does not work, append() returns None
  ## Correct pattern:
  list.append(4)
  print(list)  ## [1, 2, 3, 4]
  ```
 ### Criar lista

Um padrão comum é iniciar uma lista como uma lista vazia [] e usar anexar() ou expand() para adicionar elementos a ela:
```py
  list = []          ## Start as the empty list
  list.append('a')   ## Use append() to add elements
  list.append('b')
```
### Listar frações
Os Slices funcionam em listas da mesma forma que com strings e também podem ser usados para alterar subpartes da lista.
```py
  list = ['a', 'b', 'c', 'd']
  print(list[1:-1])   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print(list)         ## ['z', 'c', 'd']
```
## Dicionário e arquivo do Python 

Tabela de hash de dicionário
A estrutura eficiente de tabela de hash de chave-valor de Python é chamada de "dict". O conteúdo de um dict pode ser escrito como uma série de pares de chave-valor dentro de chaves { }, por exemplo, dict = {key1:value1, key2:value2, ... }. O "dict vazio" é apenas um par vazio de chaves {}.

A pesquisa ou definição de um valor em um dict usa colchetes. Por exemplo, `dict['foo']` procura o valor sob a chave "foo". Strings, números e tuplas funcionam como chaves, e qualquer tipo pode ser um valor. Outros tipos podem ou não funcionar corretamente como chaves (strings e tuplas funcionam perfeitamente, porque são imutáveis). Procurar um valor que não está no dict gera um KeyError. Use "in" para verificar se a chave está no dict, ou dict.get(key), que retorna o valor, ou None se a chave não estiver presente (ou get(key, não encontrado) permitirá que você especifique o valor a ser retornado no caso não encontrado).
```py
  ## Pode criar um ditado começando com o ditado vazio {}
  ## e armazenar pares chave/valor no dict assim:
  ## dict[key] = valor-para-essa-chave
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'

  print(dict) ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

  print(dict['a'])     ## Pesquisa simples, retorna 'alfa'
  dict['a'] = 6       ## Coloque nova chave/valor no dict
  'a' in dict         ## True
  ## print(dict['z'])                  ## Lança KeyError
  if 'z' in dict: print(dict['z'])     ## Evite KeyError
  print(dict.get('z'))  ## Nenhum (em vez de KeyError)
```
![](https://developers.google.com/static/edu/python/images/dict.png?hl=pt-br)

Uma repetição "for" em um dicionário itera nas chaves por padrão. As chaves aparecerão em ordem aleatória. Os métodos `dict.keys()` e `dict.values()` retornam listas de chaves ou valores explicitamente. Há também um items() que retorna uma lista de tuplas (chave, valor), que é a maneira mais eficiente de examinar todos os dados de chave-valor no dicionário. Todas essas listas podem ser passadas para a função `classify()`.
```py
## Por padrão, a iteração sobre um dict itera sobre suas chaves.
## Observe que as chaves estão em ordem aleatória.
  for key in dict:
    print(key)
  ## prints a g o

##Exatamente igual ao anterior
    for key in dict.keys():
    print(key)

## Obtenha a lista .keys():
  print(dict.keys())  ## dict_keys(['a', 'o', 'g'])

## Da mesma forma, há uma lista de valores .values()
  print(dict.values())  ## dict_values(['alpha', 'omega', 'gamma'])

## Caso comum - percorre as chaves em ordem de classificação,
## acessando cada chave/valor
  for key in sorted(dict.keys()):
    print(key, dict[key])

  ## .items() é o ditado expresso como tuplas (chave, valor)
  print(dict.items())  ##  dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')])

  ## Esta sintaxe de loop acessa todo o dict fazendo um loop
  ## sobre a lista de tuplas .items(), acessando um (chave, valor)
  ## par em cada iteração.
  for k, v in dict.items(): print(k, '>', v)
  ## a > alpha    o > omega     g > gamma
  ```
  **Nota estratégica**: do ponto de vista do desempenho, o dicionário é uma de suas melhores ferramentas, e você deve usá-lo onde puder como uma maneira fácil de organizar os dados. Por exemplo, você pode ler um arquivo de registro em que cada linha começa com um endereço IP e armazenar os dados em um dict usando o endereço IP como chave e a lista de linhas em que ele aparece como o valor. Depois de ler o arquivo inteiro, você pode procurar qualquer endereço IP e ver instantaneamente sua lista de linhas. O dicionário recebe dados dispersos e os transforma em algo coerente.

  ### Formatação de dicionário
  O operador % funciona convenientemente para substituir valores de um dict em uma string pelo nome:
```py
    h = {}
    h['word'] = 'garfield'
    h['count'] = 42
    s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
    #'Quero 42 cópias do Garfield'

    # Você também pode usar str.format().
    s = 'I want {count:d} copies of {word}'.format(h)
```
[Clique Aqui](https://pythonacademy.com.br/blog/dicts-ou-dicionarios-no-python) para mais referências sobre dicionários em python.
