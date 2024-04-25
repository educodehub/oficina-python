# Pré-aula - Aula 01 - Oficina de Python
Bem-vindo ao seu material de pré-aula da nossa oficina de Python sobre sintaxe básica, condicionais, loops e funções. Aqui iremos abordr alguns dos principais conceitos que iremos ver durante a aula e aproveitar praticar.

## Introdução

O início de tudo é o site http://python.org.  Os principais links relacionados à programação, documentação e downloads estão lá. A documentação é boa e bem-organizada, e cobre diversos aspectos como instalação, biblioteca padrão, distribuição etc. Se você usa Windows, consegue fazer o download do arquivo .exe e instalar facilmente (clicando no botão amarelo conforme imagem abaixo).
![Página inicial do python](https://lh7-us.googleusercontent.com/y-d17FIru66kI27_a_apMBrbwGGGvqrTypNJ03HV2MAATDTCzDRfEp-AnbtuM5FamC3I6eF2FjipM86xgzrAIT41B4nlsEX3pyjvxpf8rT3-NJw-EzU_B6D_8BlMRTDcEftEiSt8TbqZ9EgdJnvUxPcYHSipQL-F)
Já a instalação padrão da maioria das distribuições OSX/Linux instala Python como padrão, entretanto nem sempre será a versão 3, a versão mais recente do python. Caso não seja, existem dois caminhos: instalar com o mecanismo de pacotes do sistema (por exemplo, apt-get no Ubuntu, ou brew no OSX); ou compilar do código-fonte e instalar.

Python é uma linguagem de altíssimo nível (em inglês, **Very High Level Language**) orientada a objeto, de tipagem dinâmica e forte, interpretada e interativa.

A linguagem inclui diversas estruturas de alto nível (listas, dicionários, data / hora, complexos e outras) e uma vasta coleção de módulos prontos para uso, além de frameworks de terceiros que podem ser adicionados. Também possui recursos encontrados em outras linguagens modernas, tais como: geradores, introspecção, persistência, metaclasses e unidades de teste. Multiparadigma, a linguagem suporta programação modular e funcional, além da orientação a objetos. Mesmo os tipos básicos no Python são objetos. A linguagem é interpretada através de bytecode pela máquina virtual Python, tornando o código portável.

Após instalar o python, precisaremos utilizar uma IDE, nas nossas aulas, utilizaremos o Visual Studio Code que pode ser baixado em: [https://code.visualstudio.com/](https://code.visualstudio.com/) é possível utilizar nas 3 principais plataformas desktop (Windows, Mac e Linux).
*![Página inicial do projeto do Visual Studio Code](https://lh7-us.googleusercontent.com/ibMPb64ickG2lNBTPXQwCtOydqaYxAMllYJLFsJ67uSqD-MygQAf4NbjdG4lC-UKi9i_mY27K6hA8vvWLdwYRWcPnY9kesC-PHTLU6wUJn71fdZtOr6xctqFM5m4E9-J0DRMOIUwGdI-4pAY7RvFSjQ)
Para uma melhor exemplificação como instalar e configurações iniciais, além de explicação de instalação de extensões, você pode conferir este vídeo:

(Como Configurar VSCode Para Python em 2023 RÁPIDO) - [https://www.youtube.com/watch?v=7Kpd6eprz4k](https://www.youtube.com/watch?v=7Kpd6eprz4k))

Após essa ferramenta instalada já podemos começar a fazer nosso primeiro programa.

## Hello World em Python

Agora voltando ao python e o VS Code, podemos criar nosso primeiro programa abrindo a IDE e criando nosso primeiro arquivo, como por exemplo aqui, o **“hello_world.py”**. 

> [!NOTE]
>
> Ao criarmos um script em python, o arquivo deve ser salvo com a extensão.py

**![](https://lh7-us.googleusercontent.com/hhLCGsDXBgdQYc_mMrf4w8Gwqr9pUpUHwnIJMSxjcNNLIVl69pbQIgmRWk16QHuR2ALNNWFj2W2hwzik8JT8qepUY8CIau01T6w_StGFiXIJAgs9pLdlkKNz4HSPDbqAJiNQ0jGBYJ7irxIrZcG7aJQ)**

e logo após criar o arquivo e digitar o primeiro código, basta rodar a aplicação no botão “play” localizado no canto superior direito.
**![](https://lh7-us.googleusercontent.com/1C4rMSQ78TSGOS1RJId7Tnb96unCIwXHU3CUKv7e4BCmPGTX0fBDrkK54yaCoCKYATxuek3-VRovtIzyGWjKg3JcxOhNX55-b0BG-RBQ1ca1x-JCDR1aXpFRJ1h0l89m8cx-aMvl-zhrNdAvfBCIDsg)**

no seu terminal você verá o comando sendo rodado e voilà! Seu primeiro programa foi criado e está funcionando.

![](https://lh7-us.googleusercontent.com/hDFJlpn-gaXAHcC1bUpjZwGqTobSQ0Ko3jLkyU-qoLLWWZta2zDD25u0m1yuSKO6OIbZQLxkKJr2D0R13v5r0xb-oV2u40vMsSoSOwjc0Jo6eF3Cip0hsTLlJpvhxMAhMN1s5h3Okx1r5vnvuSlVzuw)

## Print
Em Python, "print" é uma função fundamental que é usada para exibir informações na tela. Ela é uma das primeiras coisas que você aprende ao começar a programar em Python. O objetivo principal da função print é mostrar dados na saída padrão, geralmente a tela do computador, para que os usuários possam ver e entender o que está acontecendo em um programa.

**Sintaxe básica do print:**

A sintaxe básica da função print é simples:

```python
print(valor1, valor2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

- **valores:** São os valores que você deseja imprimir. Eles podem ser variáveis, strings, números, etc.
- **sep (opcional):** É o separador que será utilizado entre os valores. Por padrão, é um espaço (' ').
- **end (opcional):** É o que será impresso após a finalização da impressão. Por padrão, é uma nova linha ('\n'), o que significa que o próximo print começará em uma nova linha.
- **file (opcional):** É o objeto de arquivo para o qual a saída será enviada. Por padrão, é sys.stdout, que representa a saída padrão (normalmente a tela).
- **flush (opcional):** Se True, a saída será liberada imediatamente.

**Exemplos de uso:**

```python
# Exibindo uma mensagem simples
print("Olá, mundo!")

# Exibindo o valor de uma variável
nome = "Alice"
print("Bem-vindo,", nome)

# Exibindo valores separados por outro caractere
print("Python", "é", "legal", sep="-")

# Não terminando a linha com uma nova linha
print("Essa mensagem", end="")
print(" será continuada na mesma linha.")
```

## Operadores aritméticos em Python

| Operadores | Descrição                                   | Exemplo |
| ---------- | ------------------------------------------- | ------- |
| `+`        | Realiza a soma entre número                 | x + y   |
| `-`        | Realiza a subtração entre números           | x - y   |
| `/`        | Realiza a divisão entre números             | x / y   |
| `//`       | Realiza a divisão inteira entre números     | x // y  |
| `*`        | Realiza a multiplicação entre números       | x * y   |
| `**`       | Realiza a potenciação entre números         | x ** y  |
| `%`        | Resulta no resto da divisão de dois números | x % y   |

O **resto** (%) sempre terá como resultado o resto de uma divisão. Por exemplo: 

```python
5 % 2
1
```

Lê-se: **5 resto 2, igual a 1**

## Operadores de atribuição em Python

| Descrição                       | Operador | Exemplo                             |
| ------------------------------- | -------- | ----------------------------------- |
| Atribuição simples              | `=`      | `x = 5`                             |
| Atribuição com adição           | `+=`     | `x += 3` (equivale a `x = x + 3`)   |
| Atribuição com subtração        | `-=`     | `x -= 2` (equivale a `x = x - 2`)   |
| Atribuição com multiplicação    | `*=`     | `x *= 2` (equivale a `x = x * 2`)   |
| Atribuição com divisão          | `/=`     | `x /= 2` (equivale a `x = x / 2`)   |
| Atribuição com resto da divisão | `%=`     | `x %= 2` (equivale a `x = x % 2`)   |
| Atribuição com exponenciação    | `**=`    | `x **= 2` (equivale a `x = x ** 2`) |
| Atribuição com divisão inteira  | `//=`    | `x //= 2` (equivale a `x = x // 2`) |

## Operações com texto(String)

Até agora utilizamos o termo “texto” para os códigos escritos dentro das aspas. Na realidade, o termo mais correto é **string**. Assim como nas operações matemáticas, podemos fazer operações com strings. Vamos ver o exemplo abaixo. As duas primeiras linhas são apenas prints “convencionais” sem nenhuma operação. Já a terceira e quarta linha usam 2 operadores distintos para unir textos e formar uma string única. 

``` py
print("Daniel")
print("Candiotto")
print("Daniel" + "Candiotto")
print("Daniel", "Candiotto")
```

Perceba que o sinal de `+` concatena os textos escritos nas aspas. Já a vírgula, concatena os dois textos, mas faz uma separação por um espaço.

Outra operação possível com strings é a função **in**. Essa função permite verificar se algum caractere ou conjunto de caracteres está contido em uma string. 

```py
print('D'in 'Daniel')
print('Da' in 'Daniel')
print('J' in 'Daniel')
print('d' in 'Daniel')
```

Vamos dar uma checada nos exemplos acima. ‘D’ in ‘Daniel’ -> Resultado “true”. Por que? A função in retorna sempre se o que está sendo testado é **verdadeiro** (True) ou **falso** (False). Nesse caso, como ‘D’ está em ‘Daniel’ o resultado é verdadeiro. Já no teste ‘J’ in ‘Daniel’ o resultado é falso pois não existe a letra J no nome Daniel.

## O que são Variáveis?
Variáveis são elementos fundamentais em programação, pois permitem armazenar e manipular dados. Em Python, uma variável é um nome que faz referência a um valor na memória do computador. Esses valores podem ser números, strings, listas, dicionários, entre outros.

#### Declarando Variáveis:

Em Python, declarar uma variável é simples. Basta escolher um nome para a variável e atribuir um valor a ela utilizando o operador de atribuição (`=`).

Exemplo:

```python
idade = 25
nome = "João"
```

Lê-se, **idade recebe 25** e **nome recebe João**. Na programação, o sinal `=` significa que uma determinada variável recebe um valor, e não o comumente **igual** como estamos acostumados.

#### Tipos de dados em Variáveis:

Até o momento, temos tratado as variáveis como iguais, mas na realidade, no Python cada variável possui um tipo de dado. Os tipos de dados básicos representam diferentes tipos de informações que podem ser armazenadas e manipuladas. Para saber qual o tipo de uma variável, usamos a função **Type()** como nos exemplos ao lado.

No Python, alguns dos tipos mais comuns incluem:

-   **Int:** Números inteiros, como 10, 25 ou -3 (sem casa decimal).
-   **Float:** Números reais, como 3.14, 5.20e-2 ou 1.79e10 - Basicamente são números com casas decimais. Lembrando que no Python a casa decimal é representada pelo “.” (ponto) e não pela “,” (vírgula)..
-   **Str (ou Strings):** Cadeias de caracteres, como "Olá, mundo!", "Este é um texto" ou "Python é incrível!" - Basicamente textos, um ponto de atenção é que números entre aspas são considerados strings.
-   **Bool:** Chamadas booleanas. São variáveis que só possuem 2 valores possíveis: True ou False, 1 ou 0.

Esses tipos de dados são que chamamos de tipos primitivos

#### Regras de criação de Variáveis:

Na criação de uma variável é importante levar em consideração algumas restrições e recomendações:

-   **Evite palavras reservadas:** Não utilize nomes de variáveis que são palavras reservadas em Python, como `if`, `for`, `while`, etc.
-   **Use letras minúsculas, números e sublinhados:** É permitido utilizar letras minúsculas, números (exceto no início do nome) e sublinhados para criar nomes de variáveis em Python.
-   **Diferencie maiúsculas e minúsculas:** Python é sensível a maiúsculas e minúsculas. `nota_aluno` é diferente de `NOTA_ALUNO`.
-   **Use nomes descritivos:** Utilize nomes que descrevam claramente o propósito ou conteúdo da variável.
-   **Seja consistente:** Mantenha uma convenção de nomenclatura consistente em todo o seu código.
-   **Utilize ferramentas de autoformatação:** Para garantir a padronização, utilize ferramentas que ajudem na formatação do código, como linters e formatters.

Exemplos de boas práticas de nomenclatura:

- `media_geral`: Use o caractere de sublinhado para separar palavras, indicando claramente o propósito da variável.
- `MediaGeral`: Utilize a convenção CamelCase para nomes compostos, onde cada palavra inicia com maiúscula (exceto a primeira), indicando também claramente o propósito da variável.
- `nota1`, `nota2`, `nota3`: Nomes simples e descritivos para variáveis relacionadas.
- `idade_usuario`, `nome_usuario`: Nomes que indicam claramente o conteúdo da variável.
- `contador`, `indice`: Nomes comuns para variáveis de controle em loops.



![](https://lh7-us.googleusercontent.com/k0VjYTtrncdB0yYqvTi8v5PHgYc-sUhoHqnkMtmck4l_5kJeEHPfEc3perYwP_L7Xjfna16q3oxgMyxrQKVeqYcuAQBB-GNbQ1Jve90JrSHa0xR63PKHLtc7C6D5UUt4LqQAEdFH7-dbZj1heHQRoNE)

## Input – Pegando informações do Usuário

Para capturar informações do usuário em Python, utilizamos a função `input()`. Veja abaixo a estrutura dessa função:

```py
input("Qual é o seu nome? ")
```

O texto entre as aspas serve como uma mensagem para orientar o usuário sobre o que deve ser inserido. 

Após a execução da string exibida “Qual o seu nome”, um campo em branco será disponibilizado ao usuário. Inserida a informação, o Python continuará a processar as demais linhas do código.

No entanto, o input por si só não guarda esta informação... Para armazenar um valor, precisamos **atribuir o resultado do input a uma variável**.

```py
nome = input("Qual é o seu nome? ")
print(nome)
```

Variável **nome** recebe resultado do **input**

> [!IMPORTANT]
>
> Perceba que não usamos mais o termo **igual** e sim **recebe** pois o sinal `=` deverá ser lido assim daqui para frente.

No primeiro caso, o programa apenas lê a informação fornecida pelo usuário e finaliza sem realizar nenhuma ação adicional.

No segundo caso, ao atribuirmos o resultado da função `input()` a uma variável, podemos utilizar essa informação posteriormente.

Ao inserir "Python" quando solicitado, a variável `nome` armazena essa informação. Depois, ao inserir `nome` como argumento na função `print()`, o programa irá saudar o usuário pelo nome fornecido

## Conversão entre tipos de dados
Em Python, é comum a necessidade de converter dados de um tipo para outro. Isso pode ocorrer quando precisamos garantir que os tipos de dados sejam compatíveis em uma operação ou para facilitar a manipulação de dados em um programa. Nesta pré-aula, vamos explorar as diferentes formas de realizar conversão entre tipos de dados em Python.

**1. Conversão Implícita:**

Em algumas situações, o Python realiza a conversão automaticamente, isso é chamado de conversão implícita. Por exemplo, quando você adiciona um número inteiro a um número decimal (float), o Python converte o inteiro para float para realizar a operação.

Exemplo:

```py
inteiro = 5
decimal = 3.14

soma = inteiro + decimal  # O inteiro é convertido implicitamente para float
print(soma)  # Saída: 8.14
```

**2. Conversão Explícita:**

Em outros casos, é necessário realizar a conversão explicitamente usando funções específicas para cada tipo de dado.

- **int()**: Converte para inteiro.
- **float()**: Converte para ponto flutuante (float).
- **str()**: Converte para string.
- **bool()**: Converte para booleano.

Exemplos:

```py
# Conversão para inteiro
numero = "10"
inteiro = int(numero)

# Conversão para float
numero = "3.14"
decimal = float(numero)

# Conversão para string
numero = 10
texto = str(numero)

# Conversão para booleano
numero = 0
booleano = bool(numero)  # False
```

**3. Cuidados na Conversão:**

- Nem todas as conversões são seguras. Por exemplo, converter uma string que não representa um número para um inteiro pode causar um erro.
- Certifique-se de que os valores que você está convertendo têm um formato compatível com o tipo de dado para o qual você está convertendo.

## Operadores de Comparação

|Operador|Descrição|Exemplo|
|-|-|-|
|>|	Maior que - True se o operando a esquerda for maior que o da direita|	x > y|
|<|	Menor que - True se o operando a esquerda for menor que o da direita|	x < y|
|==| Igual - True se ambos os operandos forem iguais |x == y|
|!=|	Não Igual - True se os operandos forem diferentes|	x != y|
|>=|Maior que ou Igual - True se o operando da esquerda for maior ou igual ao da direita|x >= y|
|<=|Menor que ou Igual - True se o operando da esquerda for menor ou igual ao da direita|x <= y|
## Operadores Lógicos
Operadores Lógicos são usados para combinar comandos condicionais.

|Operador|Descrição|Exemplo|
|-|-|-|
|`and`|Retorna True se ambos os comandos são verdadeiros|	x < y and x < 10|
|`or`|Retorna True se um dos comandos é verdadeiro|	x < y or x > 3|
|`not`|Reverte o resultado, retorna False se o resultado for True e vice-versa|not(x > 10)|

Vamos considerar então alguns exemplos com operadores lógicos:
```py
n1, n2, n3 = 3, 6, 7
print(n1 < n2 and n1 < n3) # True
print(n1 == n2 or n3 == n2) # False
print(not True) # False
```
## Operadores de Identidade
Operadores de identidade são usados para comparar os objetos, não se são iguais, mas se eles forem realmente o mesmo objeto, com o mesmo local de memória.

`is` e `is not` são operadores de identidade em Python, eles são usados para checar se dois valores (ou variáveis) estão localizados na mesma área de memória, duas variáveis iguais não significam que são idênticas!

|Operador|Descrição|
|-|-|
|`is`|True se os operandos são idênticos (referem ao mesmo objeto)|
|`is not`|True se os operandos não são idênticos (não referem ao mesmo objeto)|

Exemplo com números:
```py
x = 1
y = 1 
print(x is y)     # True
print(x is not y) # False
```
Exemplo com strings:
```py
a = "cachorro"
b = "cachorro"
print(a is b)      # True
print(a is not b)  # False
```
Exemplo com listas:
```py
z = [1,2,3]
k = [1,2,3]
print(z is k)      # False
print(z is not k)  # True
```
Perceba aqui que x e y são inteiros do mesmo valor, então eles são iguais e idênticos, o mesmo vale para a e b (strings). Porém o mesmo não ocorre com z e k, que são iguais, porem não idênticos, isso porque o interpretador localiza eles separadamente em memória, mesmo eles sendo iguais.

## Operadores de Membros
Operadores de membros são usados para testar se uma sequência é apresentada em um objeto.

|Operador|Descrição|Exemplo|
|-|-|-|
|`in`|Retorna True se o valor/variável é encontrado na sequência|"c" `in` "cachorro"|
|`not in`|Retorna True se o valor/variável não está presenta na sequência|	1 `not in` [1,2,3]|

Exemplo básico:
```py
a = [1,2,3]
b = "Guilherme"
print(1 in a)   # Retorna True, pois 1 se encontra na lista a
print("o" in b) # Retorna False, pois o não se encontra na string b
```
## Condições no Python

Algo muito comum e quase certo de ser utilizado em algum código que você venha a fazer, é a necessidade de definir ações baseadas em condições específicas.

Se você já usou o Excel ou já programou em outras linguagens, deve conhecer esse conceito como o SE ou IF em inglês. Essencialmente no Python é a mesma coisa, só mudando a forma de como é feita.

**Vamos entender a estrutura do IF:**

![](https://lh7-us.googleusercontent.com/bfIYyWLKqMEpxFnKYNYykh3pvps9Cyqst-VZjLYmqazyoJAtSPC5TV7X19UAeUopGfKT9yvuf1buCdjxi_L6RIDGLCwkX00T-dHYUxXFrgHnOXqNUOIqd_lRlJjaqiq0ENemcbUfydUL6eJV8SyI_M4)

Vamos olhar um exemplo aplicável. O programa deverá ler a nota do aluno. Nesse caso, nota = 10

``` py
nota = 10
if nota >= 7:
	print('Aprovado')
else:
	print('Reprovado')
```

Após a leitura da nota, o programa irá através do IF verificar uma condição pré-programada.
Nesse caso, a condição é: o valor da variável nota é **maior** ou **igual** a 7?

Como nota = 10 a resposta é **VERDADEIRA**.

Como a **condição**  é verdadeira, nosso programa printará: 'Aprovado'.

Vamos agora para um caso onde a nota é 5.

```py
nota = 5
if nota >= 7:
	print('Aprovado')
else:
	print('Reprovado')
```

Assim como no primeiro caso, o Python lerá que a Variável nota recebe o valor 5. Ao chegar na linha do If, a condição será verificada. O valor da variável nota é **maior** ou **igual** a 7?

Como nota = 5 a resposta é **Falsa**.

Como a resposta é falsa, perceba que o Python para a linha print('Aprovado') e irá diretamente para o caso do Else.

O `else` funciona como um "Nenhuma das opções anteriores". O que isso significa? Caso nenhuma condição tenha sido atendida, o código irá para o bloco do else. Nesse caso, o termo indentado que dará como resultado **Não aprovado**.

#### `if` dentro de `if`
Em alguns casos, temos condições que só existem caso uma condição prévia tenha sido atendida.

Vamos pegar nosso exemplo anterior. Vamos dizer que ao invés de apenas "Não aprovado" também seja necessário dar um status se foi "reprovado" ou se "está de recuperação". Nesse caso vamos usar um if dentro do if, como no código abaixo.

``` py
nota = 6
if nota >= 7:
	print('Aprovado')
else:
    if nota >= 5:
        print('Não aprovado/Recuperação')
    else:
        print('Não aprovado/Reprovado direto')
```

Perceba que usamos a indentacao para diferenciarmos os 2 blocos If que temos.
**BLOCO IF EXTERNO:** considera todo o código. Perceba 0 alinhamento do if e do else.
**BLOCO IF INTERNO AO ELSE**: considera todo o bloco " interno. Só será lido caso a condição nota >= 7 do bloco externo não seja atendida.

Diferente de outras linguagens onde é necessário "fechar" o IF, no Python isso é feito pela Indentação. Perceba como o alinhamento dos blocos indica a que bloco o mesmo pertence e quando o mesmo inicia e termina.

#### Estrutura do `if` – `elif`
Agora que entendemos a estrutura do IF, vamos entender um caso mais complexo onde não temos apenas 1 condição, mas 2 ou mais
![](https://lh7-us.googleusercontent.com/MAntTOuFKiJe4DkR4q61HEq94Y2RYNN2YEXQ2aSzTniyNPTUZKWLGM3ngzSO0Cfy5C-UXl6Ripq-2aQ7v6tYGzcQeb_GKV0E-vaUhSL6cfdn_0sC3YEjs3SjA1_IXtHa2TE66HiyamENiBwXP-bVI4E)

#### Vamos avaliar o exemplo abaixo:

Nesse exemplo temos que um número pode assumir três condições.

1) Ele pode ser maior que zero.
2) Ele pode ser igual a 0.
3) Ou ele pode ser menor que 0, nesse caso, negativo.

``` py
numero = 5

if numero > 0:
    print("O número é positivo")
elif numero == 0:
    print("O número é zero")
else:
    print("O número é negativo")
```

O programa verifica se o número é maior que zero. Se for, imprime "O número é positivo". Se não for, verifica se é igual a zero. Se for, imprime "O número é zero". Caso contrário, imprime "O número é negativo".

## Estrutura Match Case em Python

Vamos falar um pouco sobre a funcionalidade Match Case em Python!

Com advento da atualização 3.10, a linguagem Python recebeu diversas melhorias e uma delas foi a funcionalidade Match Case.

Similar a estrutura Switch Case utilizadas em outras linguagens de programação, a funcionalidade Match Case trata-se de uma estrutura condicional composta, a qual avalia a combinação de múltiplas condições e executa apenas uma determinada expressão.

Antes da atualização 3.10, era comum utilizarmos as estruturas While, If, Elif, Else e/ou Funções para criar estruturas do tipo laço condicional.
```py
opcao = -1

while opcao != 0:
      opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
      if opcao == 1:
              print("Sacando...")
      elif opcao == 2:
              print("Exibindo o extrato...")
      else:
              print("Opção inválida!")
```
A estrutura Match Case pode ser utilizada quando temos situações mutualmente exclusivas, em que, se uma instrução for executada, as demais não serão.

Assim, podemos construir um bloco de comandos com múltiplas possibilidades de decisão, que compara uma expressão com uma série de valores e retorna uma instrução.
#### Sintaxe:
A sintaxe da estrutura Match Case é dada por:
```py
match <expressão>:
      case <valor 1>:
              <instruções>
      case <valor 2>:
              <instruções>
```
`match`: Comando que avalia o valor da variável para decidir qual case será executado.
expressão: Uma expressão que será comparada á cada cláusula case.
case: Representa um possível valor da da expressão.
instruções: Bloco de comando que será executado ao selecionar um case.
Agora vejamos o exemplo anterior com a utilização da estrutura Match Case:
```py
opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

match opcao:
      case 1:
              print("Sacando...")
      case 2:
              print("Exibindo o extrato...")
```
Podemos notar melhora significativa em relação a sintaxe e legibilidade do bloco de comandos, uma vez que descartamos a necessidade de utilizar While, If, Elif, Else.

Ademais, vale pontuar que não há impedimentos quanto ao uso das estruturas condicionais (if/elif/else), estruturas repetição (For, While), sub-rotinas(Funções, Procedimentos, Métodos, etc…) de forma aninhada com Match Case.

## Valores true x Truthy e valores Falsy
Vou apresentar para você esses conceitos comparando-os com os valores True e False, que são tipicamente aqueles que mais usamos.

Expressões com operandos e operadores são avaliadas como True ou False e podem ser usadas em uma condição if ou while para determinar se um bloco de código deve ser executado.
Aqui vemos um exemplo:
```py
# Expression 5 < 3
>>> if 5 < 3:
	print("True")
else:
	print("False")

# Output
False
```
Nesse exemplo, tudo funciona como esperado porque usamos uma expressão com dois operandos e um operador  5 < 3.

O que você acha que acontece, no entanto, se executarmos esse código?
```py
>>> a = 5

>>> if a:
	print(a)
```
Perceba que agora não temos uma expressão típica perto da palavra chave if, temos apenas uma variável:
![](https://www.freecodecamp.org/portuguese/news/content/images/2022/11/image-3.png)

Surpreendentemente, o resultado é 5
Se mudarmos o valor a para zero, dessa maneira:

```py
>>> a = 0

>>> if a:
	print(a)
```
Não temos um resultado.

Certamente, você deve estar se perguntando nesse momento: O que fez o código ser executado com sucesso?

A variável `a` não é uma expressão típica. Ela não tem operadores e operandos. Então, por que ela resulta em `True` ou `False` dependendo do valor?

A resposta reside no conceito de valores Truthy e Falsy, que, por si só, não são valores verdadeiros ou falsos, mas, ainda assim, são avaliados como `True` ou `False`.
### Valores Truthy e Falsy
Em Python, valores individuais podem ser avaliados como `True` ou como `False`. Eles não precisam necessariamente fazer parte de uma expressão maior para serem avaliados como um valor verdadeiro, pois eles já têm um valor predeterminado pelas regras da linguagem Python.

As regras básicas são:

Valores avaliados como `False` são considerados Falsy.
Valores avaliados como `True` são considerados Truthy.
De acordo com a documentação do Python:

Qualquer objeto pode ser testado para o valor truthy, para o uso em condições if ou while ou como operando das operações com booleanos abaixo (`and`, `or`, `not`).
### Contexto booleano
Quando usamos um valor como parte de uma expressão maior ou como uma condição `if` ou `while`, estamos usando esse valor dentro de um contexto booleano.

Você pode pensar no contexto booleano como uma "parte" do seu código que requer que um valor seja `True` ou `False` para fazer sentido.

Por exemplo, (veja abaixo) a condição depois da palavra-chave `if` ou depois da palavra-chave `while` tem que ser avaliada como `True` ou `False`:

![](https://www.freecodecamp.org/portuguese/news/content/images/2022/11/image-1.png)
- Valores Falsy
Sequências e coleções:
```
Listas vazias []
Tuplas vazias ()
Dicionários vazios {}
Sets vazios set()
Strings vazias ""
Ranges vazios range(0)
```
- Números
```
Zero de qualquer tipo numérico.
Inteiro: 0
De ponto flutuante: 0.0
Complexo: 0j
```
Constantes
```
None
False
```
Valores falsos foram a razão pela qual não houve saída em nosso exemplo inicial, quando o valor de a era zero.

O valor 0 é falsy. Portanto, a condição if será False e o condicional não será executado neste exemplo:

 ## Introdução às Estruturas de Repetição em Python (for e while)

Em programação, as estruturas de repetição são ferramentas essenciais para executar um bloco de código várias vezes. Imagine que você precise realizar uma tarefa repetitiva, como processar uma lista de itens, calcular valores iterativos ou esperar por uma condição específica antes de prosseguir. Em vez de escrever o mesmo código repetidamente, podemos utilizar as estruturas de repetição para automatizar essas tarefas.

Existem dois tipos principais de estruturas de repetição em Python: `for` e `while`. Cada uma tem suas características e usos distintos.

#### **Loop `for` em Python:**

O loop `for` é ideal para iterar sobre uma sequência de elementos, como uma lista, tupla, dicionário ou string. Ele percorre cada item na sequência e executa um bloco de código para cada item encontrado.

A sintaxe básica do loop `for` é:

```python
for item in sequencia:
    # Bloco de código a ser executado para cada item
```

- Exemplo:
```py
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:

    print(fruta)
```

Este código imprimirá cada fruta da lista `frutas` em uma linha separada.

#### **Loop `while` em Python:**

O loop `while` é utilizado quando queremos repetir um bloco de código enquanto uma condição específica for verdadeira. Ao contrário do loop `for`, que percorre uma sequência, o loop `while` continua repetindo enquanto a condição especificada for verdadeira.

A sintaxe do loop `while` é:

```python
while condição:
    # Bloco de código a ser executado enquanto a condição for verdadeira
```

- Exemplo:

```py
contador = 0

while contador < 5:

    print(contador)

    contador += 1 
```

É crucial prestar muita atenção na estrutura do loop `while`, pois ele pode entrar em um loop infinito se a condição nunca for falsa.


- Exemplo de while loop infinito:

```py
nome = input ('insira um nome')

while nome:

    input ('insira um nome')
```

Em resumo, as estruturas de repetição `for` e `while` são ferramentas poderosas em Python para automatizar tarefas repetitivas. O `for` é adequado para iterar sobre sequências conhecidas, enquanto o `while` é útil quando a condição de término não é facilmente determinada ou quando precisamos de flexibilidade em um loop.

## Funções

#### Chamadas de funções

Uma função é um bloco de código que executa uma tarefa específica. No Python, você pode chamar uma função fornecendo o nome da função seguido por parênteses contendo zero ou mais argumentos.

Você já viu um exemplo de uma chamada de função:

```python
type('32')
```

A saída será:

```python
<class 'str'>
```

O nome da função é `type` e ela exibe o tipo de um valor ou variável. O valor ou variável, que é chamado de argumento da função, deve estar entre parênteses. Aqui, `'32'` é o argumento da função `type`.

Em vez de imprimir um valor de retorno, podemos atribuí-lo a uma variável:

```python
bia = type('32')
print(bia)
```

A saída será:

```python
<class 'str'>
```

Isso significa que a função `type('32')` retorna `<class 'str'>` e o armazenamos em `bia`.

Outro exemplo é a função `id`, que recebe um valor ou uma variável e retorna um inteiro, que atua como um identificador único para aquele valor:

```python
id(3)
```

A saída será:

```python
140737410932272
```

Isso significa que `id(3)` retorna o identificador único `140737410932272` para o valor `3`.

```python
bia = 3
id(bia)
```

A saída será o mesmo identificador único:

```python
140737410932272
```

Isso ocorre porque `bia` agora está referenciando o mesmo valor `3`.

Todo valor tem um ID, que é um número único relacionado ao local onde ele está guardado na memória do computador. O ID de uma variável é o ID do valor ao qual ela se refere. As funções `type()` e `id()` são exemplos de funções integradas no Python.

#### Definindo funções em Python

Uma função é definida com a palavra-chave `def`, seguida pelo nome da função e, opcionalmente, uma lista de parâmetros entre parênteses. O corpo da função é indentado e pode conter qualquer número de instruções Python.

**Sintaxe para Definir uma Função:**

```py
def nome_da_funcao(parametros):
    # Bloco de código da função
    # Pode conter operações e instruções
    return resultado (opcional)
```

- `nome_da_funcao`: Nome que identifica a função.
- `parametros`: Valores que a função recebe como entrada (opcional).
- `return`: Palavra-chave usada para retornar um resultado (opcional).

**Exemplo de uma Função Simples:**

```py
def saudacao(nome):
    print("Olá,", nome)

# Chamando a função
saudacao("João")  # Saída: Olá, João
```

**Exemplo de Função com Retorno:**

```py
def soma(a, b):
    resultado = a + b
    return resultado

# Chamando a função
resultado = soma(3, 5)
print(resultado)  # Saída: 8
```

**Até Logo!**

Espero que este material pré-aula sobre Python tenha sido útil e tenha despertado sua curiosidade para aprender mais. Nos vemos na aula! Se você tiver alguma dúvida, não hesite em perguntar durante a aula. Até lá! 🚀👋
