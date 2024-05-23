# Pré-aula Dia 3 
### Bibliotecas
Até agora só vimos os objetos e métodos que existem dentro do próprio Python, mas uma das principais “armas” dessa linguagem são as chamadas bibliotecas.

### O que são bibliotecas
Elas são módulos prontos que podem ser importados para nossos projetos. Elas nos permitem executar códigos que nos demandariam muito tempo de desenvolvimento para executá-los. 

Existem milhares de módulos disponíveis, ter todos eles integrados no Python nos demandaria muita memória. Por isso, vamos precisar, sempre que necessário, importar esses módulos dentro de nossos projetos

Ao instalar o Python em seu computador, você recebe um presente: diversas bibliotecas pré-instaladas prontas para usar! Essas bibliotecas, chamadas de "bibliotecas padrão", oferecem um conjunto de ferramentas úteis para diversas tarefas, desde gerar números aleatórios até realizar cálculos matemáticos e manipular datas e horários.

Algumas das bibliotecas padrão mais populares incluem:

-   **random:** Para gerar números aleatórios e sequências aleatórias, ideais para simulações, jogos e testes.
-   **math:** Oferece funções matemáticas básicas como seno, cosseno, tangente, exponencial, logaritmo e muito mais.
-   **datetime:** Permite trabalhar com datas e horários de forma precisa e eficiente, formatando, manipulando e realizando cálculos entre datas.
-   **os:** Fornece acesso à funcionalidade do sistema operacional, permitindo criar e gerenciar arquivos e diretórios, executar comandos do sistema e interagir com o ambiente.
-   **sys:** Oferece informações sobre o sistema e o interpretador Python, além de funções para manipular argumentos da linha de comando e sair do programa.
-   **json:** Permite trabalhar com dados no formato JSON, popular para troca de dados entre sistemas e linguagens de programação.
-   **re:** Fornece ferramentas poderosas para manipulação de strings, incluindo busca por padrões, substituições e extração de informações.
-   **time:** Oferece funções para trabalhar com tempo, como obter a hora atual, medir o tempo de execução de um código e formatar datas e horários.

Para essa importação usaremos o comando: **import**
```py
import biblioteca
```
Vamos ver um exemplo usando um módulo chamado *`webbrowser`*.
 
![](https://lh7-us.googleusercontent.com/lx9c2WDd1aia9ljB7wUYIqT07XXpPhHU8QJqop90v4jFVcXyroQY6ooR-hdTAK2qdX4tC00vAp5re6ldJ0FjBhZBFmKwufwrDC9Si1dFl9hiRV6fcm4E7mH4B7WxwTqci9LWm9mpTnjEanU2JMlvp9E)

Em alguns casos não é interessante importar toda a biblioteca, mas apenas uma parte dela. Para isso vamos usar a seguinte sintaxe: 

```py
from biblioteca import módulo
```

Vamos ver outro exemplo, ainda com o *`webbrowser`*.
 
![](https://lh7-us.googleusercontent.com/g_S3Je2pIYbpC73iImawUGnDGGo7QOM_00YqCfRlJ3u5Axwz5Phwd7xkanN2oCSjxe7LYFAfuiBDmifYIHMaK-hEo1IZTWnpOsdShLnYJbBuj5e0PvTbTj_WDXpGfSanZcu9H5t1Xb63hEH0j14XcOw)

Resumidamente, são essas as formas de se importar uma biblioteca em Python.

Nesse momento, provavelmente você está se perguntando:

1.  **Mas o que faz o webbrowser?**
2.  **Como saber que o módulo que preciso é o webbrowser?**

**É impossível apresentarmos na oficina todas as bibliotecas existentes.** O webbrowser é só mais uma das milhares de bibliotecas existentes. Essa, especificamente, nos ajuda a interagir com a internet (abrir uma página web, por exemplo).  Mas uma ótima forma de descobrir bibliotecas é usando nosso amigo GOOGLE. A comunidade do Python é global e conseguimos achar respostas para qualquer dúvida que a gente venha a ter.


**Agora vamos nos aprofundar mais em alguns módulos recorrentes em projetos de Python.**

## Biblioteca `random` padrão

Esta é uma ferramenta poderosa para adicionar elementos aleatórios aos seus programas. Seja para simular eventos do mundo real, embaralhar listas, escolher itens aleatoriamente ou gerar números aleatórios para cálculos, a biblioteca `random` oferece uma variedade de funções para atender às suas necessidades.

Com esta biblioteca, você pode:

-   **Gerar números aleatórios:** Números flutuantes entre 0 e 1, inteiros em um intervalo específico, ou até mesmo com distribuição normal (tipo notas em uma prova).
-   **Escolher um elemento de surpresa:** Pegar um item aleatório de uma lista, como um nome em um sorteio ou uma carta em um baralho virtual.
-   **Embaralhar as cartas:** Mexer os elementos de uma lista como em um jogo, deixando o resultado sempre incerto.
-   **Simular lançamentos de moeda:** Cara ou coroa? A biblioteca decide com um toque de aleatoriedade!
-   **Criar senhas fortes:** Gerar senhas únicas e seguras com letras e números, protegendo seus segredos.

**1. Importando a biblioteca:**

Para começar, importe a biblioteca `random` no seu programa usando a seguinte instrução:
```
import random
```

**2. Gerando números aleatórios:**

A função `random.random()` gera um número flutuante aleatório entre 0.0 e 1.0.

```
numero_aleatorio = random.random()
print(numero_aleatorio)
```
Ex:

![](https://lh7-us.googleusercontent.com/IJEic5-Av8MaHwwMtHsChkQXOaD5FyjM-1fQYkcEiYaNbMnFpqP47Lq9gzU7FfmM6Dng3tUT5Cba44ZsUNXbEDGYnfnv9evNJC_p008qcWUMI9i2rok8F5T2bM-3aa6_sZjQ4HTKcQ5oJKPErg51rRE)

**3. Gerando números inteiros:**

Para gerar números inteiros aleatórios dentro de um intervalo especificado, utilize a função `random.randint()`.

```
numero10_20 = random.randint(10, 20)
print(numero10_20)
```
Neste exemplo, estamos limitando a aleatoriedade dos números entre o 10 e 20, o que resulta nas saídas:

![](https://lh7-us.googleusercontent.com/fCYdbZGjWfwEyQAdjbd1yJKi3zXfjsBZsO_HPZygtd2IjGqFVTuatUaJKFzLPOhIDWpEwjXGZLdga0uOLWHQlFoN07Nl4zo-ewQOtrXItNShnAzX-b9RJjf5x0TQ4h_lXLdAhcj73AM1L86JbNDrAwY)


**4. Escolhendo elementos aleatoriamente de uma lista:**

A função `random.choice()` seleciona um elemento aleatório de uma lista ou sequência.

```
lista_de_frutas = ["maçã", "banana", "laranja"]
fruta_aleatoria = random.choice(lista_de_frutas)
print(fruta_aleatoria)
```
Agora com a lista já defiinida, o progama pode escolher aletoriamente qualquer um dos itens em cada execução:

![](https://lh7-us.googleusercontent.com/NP0t-VWgn800TRQPMgI5BIU3Q5Txc8JvbXaFZQB4Ygsd9uYV_P1GQtNJYstK8XDIovt7CmLQ71vuRICN2D_SgzEH8UwXUajrBxPZkYrb7bfHvnA_0ZeqX1yu9kvOJFR5oeg3ucMLSt6uy6Lh3yHh6Vk)


**5. Obtendo amostras aleatórias:**

A função `random.sample()` seleciona um número específico de elementos aleatórios de uma lista, sem repetições.

```
candidatos = ["Ana", "João", "Maria", "Pedro"]
vencedores = random.sample(candidatos, 2)
print(vencedores)
```
Ao indicar o número de amostras, o programa é obrigado a sempre selecionar 2 valores ou o que fosse indicado pelo usuário ou pelo desenvolvedor:

![](https://lh7-us.googleusercontent.com/aI3t-T4ncL-gWiD_HhkflmGKqrCrpm8CuGC5rLBJxoOJixNfgaFbYZF4o5_-HbnKnG3UHDufyBLHJ-vyQf30UOVB9CCJp3KGqNd0nVjvZzq4t2ryCOYbSE5TcI-isZpw3q_I1FTQJAuW0xNSeeWeAcI)



**6. Definindo uma semente:**

A biblioteca `random` utiliza uma *semente* para gerar números aleatórios. Definindo uma semente específica, você pode reproduzir sequências de números aleatórios em diferentes execuções do programa.

```
random.seed(12345)  
numero_aleatorio1 = random.random()
numero_aleatorio2 = random.random()
print(numero_aleatorio1)
print(numero_aleatorio2)

random.seed(12345)
numero_aleatorio3 = random.random()
numero_aleatorio4 = random.random()
print(numero_aleatorio3)
print(numero_aleatorio4)

print(numero_aleatorio1 == numero_aleatorio3)  
print(numero_aleatorio2 == numero_aleatorio4) 
```
![](https://lh7-us.googleusercontent.com/GEKnhA9c4flNH6sWphKuZgF4OBZnvVxxRlcOYsTp_nuYBw-Kp3GKtxat6djH_lpRWgxkY7_nJKnISsU02aUBoRHARg4lw8ArRpyZH3MKBR2S9uxnBMxCbPS_ebcwGgOCYqg-bMURvwTB1Z93Kqys9Z0)

Ao rodar o código acima vemos que os números aleatórios acabam sendo o mesmo pois a semente que foi gerada é definida como iguais, e como o valor da semente é tender a ser único e poder ser replicado, não importa quantas vezes o código é executado, sempre será escolhido os mesmo números (como comparação podemos ver a "Seed" que é a semente, em jogos procedurais, como em minecraft, onde um mundo é criado de forma aleatória, mas quando alteramos a semente para outra, como em:
```
random.seed(12345)  
numero_aleatorio1 = random.random()
numero_aleatorio2 = random.random()
print(numero_aleatorio1)
print(numero_aleatorio2)

random.seed(54321)
numero_aleatorio3 = random.random()
numero_aleatorio4 = random.random()
print(numero_aleatorio3)
print(numero_aleatorio4)

print(numero_aleatorio1 == numero_aleatorio3)  
print(numero_aleatorio2 == numero_aleatorio4) 
```
Podemos perceber que o número aleatório agora já é completamente diferente do anterior

![](https://lh7-us.googleusercontent.com/SRGKjyPrmwq5leitA2TOEwQKox1MtvjiWSdTHWw33_ROJAx1yeBmPR2PIo6Bmp8AZTFMpmjU8fA15X9zj5MjspuUTvqmZH2TsmP0Bkq7bbnWiopykuXcs974gUg9usYQ7_A40EzcdTxPFxfwuqSFsGU)

**Lembre-se:**
-   Os números aleatórios gerados pela biblioteca `random` são pseudo-aleatórios, o que significa que são gerados por um algoritmo, mas não são completamente aleatórios como eventos no mundo real.
-   A biblioteca `random` fornece mais funções e opções para gerar números aleatórios e trabalhar com probabilidades. Consulte a documentação oficial para mais detalhes: https://docs.python.org/3/library/random.html

**Com a biblioteca `random` do Python, você pode adicionar um toque de aleatoriedade e imprevisibilidade aos seus programas, tornando-os mais dinâmicos e interessantes.**

## Biblioteca `sys` padrão
A biblioteca `sys` do Python fornece diversas funções para acessar informações do sistema, manipular argumentos da linha de comando e controlar o comportamento do programa.

**1. Argumentos da linha de comando:**

-   `sys.argv`: Uma lista de strings contendo os argumentos passados para o programa quando ele foi executado.
    -   `sys.argv[0]` é o nome do próprio script.
    -   Os argumentos subsequentes podem ser acessados por índice (por exemplo,  `sys.argv[1]`,  `sys.argv[2]`).
-   `sys.exit()`: Sai do programa com um código de saída específico (opcional).

**2. Informações do sistema:**

-   `sys.platform`: Retorna uma string identificando o sistema operacional (por exemplo, "Linux", "Windows", "Darwin").
-   `sys.version`: Retorna uma string contendo informações sobre a versão do Python em execução.
-   `sys.path`: Uma lista de strings contendo os diretórios onde o Python procura por módulos.

**3. Controle do programa:**

-   `sys.stderr`: Um objeto semelhante a um arquivo usado para escrever mensagens de erro.
-   `sys.stdout`: Um objeto semelhante a um arquivo usado para escrever mensagens de saída padrão.
-   `sys.stdin`: Um objeto semelhante a um arquivo usado para ler a entrada padrão (geralmente o teclado).

**4. Manipulação de exceções:**

-   `sys.exc_info()`: Retorna um tupla contendo informações sobre a exceção atual que está sendo tratada.
-   `sys.exit(exc_info=True)`: Sai do programa com um código de saída que indica a exceção atual.

**5. Exemplo:**
```
import sys

print(f"Sistema operacional: {sys.platform}")
print(f"Caminho do Python: {sys.executable}")
print(f"Argumentos da linha de comando: {sys.argv}")
print(f"Versão do Python: {sys.version}")
```
Com as funções citadas em informações de sistema, conseguimos ter uma noção básica de como o python integra o sistema operacional com a IDE por meio desta biblioteca

![](https://lh7-us.googleusercontent.com/tMqAPUTPNZ08LHa3Y6Bh76H6uxLzldErQO6xFhHUxNqBh6OsAO-YEn8nyiZ81LKwBusICwRFfsO8BbmlNyzxtjiPKZmknR6A27mGxFp3baA9Ly6BSVbMxo0OIMtK9xZ8zyjaDxCqwey5hXdPhhpKHcs)

**Lembre-se:**

-   A biblioteca `sys` fornece funções poderosas para interagir com o sistema e controlar o comportamento do programa.
-   Use-a com cuidado, pois algumas funções podem ter um impacto significativo na execução do programa.
-   Explore a documentação completa da biblioteca para descobrir mais funções e possibilidades:  [https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)

### Documentação

Agora fica a pergunta, recisamos decorar tudo isso??

**A resposta é NÃO!** As documentações existem para serem consultadas.

Obviamente, quanto mais você exercitar, mais saberá executar sem pesquisar. Mas FAZ PARTE DO PROCESSO usar as documentações durante a programação.

Seja ela em Python ou qualquer outra linguagem.

**Pensar na documentação como um guia, e não como um manual a ser decorado, é a chave para o aprendizado.**

**Veja alguns benefícios de usar a documentação:**

-   **Aumenta sua produtividade:** Encontrar as informações que você precisa rapidamente te permite escrever código mais rápido.
-   **Evita erros:** A documentação fornece detalhes sobre como usar cada função ou método corretamente, evitando erros comuns.
-   **Melhora a qualidade do seu código:** Consultar a documentação garante que seu código esteja escrito de forma clara, consistente e eficiente.
-   **Aumenta sua compreensão da linguagem:** Ao ler a documentação, você aprende sobre os recursos e funcionalidades da linguagem de uma forma mais profunda.
-   **Te torna um programador mais versátil:** Familiaridade com a documentação permite que você explore novas ferramentas e técnicas com mais facilidade.

**Lembre-se:**

-   **A documentação é um recurso valioso para programadores de todos os níveis.**
-   **Não tenha medo de consultar a documentação sempre que precisar.**



## Gerenciamento de Bibliotecas
Como temos diversos pacotes existentes, pode ser que durante uma pesquisa, um pacote que você achou interessante não esteja instalado no seu computador.

Como saber se a biblioteca não está instalada?

![](https://lh7-us.googleusercontent.com/OkKyThkiYbHLtMHUwGUT-sTbLD-mhq5xqPSIjogkwBRTyZO6Zb8PcpHndvTcZHcu6Hkpk1o7dXIfUXSc8Uz2DO-WqM4ToS2bXBRQED6PIIOTeO5BUXpfZ6okNNJBEmAUZw8YAL_mnWk_ocgpyL-8O4E)

Vamos pegar o exemplo acima. Ao tentar importar a biblioteca `keyboard`, você recebe o erro `ModuleNotFoundError`. Se você digitou corretamente o nome da biblioteca, isso significa que você não a tem instalada.

Para resolver esse problema, vamos usar um instalador que já existe “embutido” dentro do Python, o **PIP**.

**O PIP permite instalar, desinstalar e atualizar bibliotecas de forma fácil e rápida.**

![](https://lh7-us.googleusercontent.com/aXsC_Ppv87nukT_zN1oKTeYYUwzN5R9VdHyD5q7GC23lhKKGjqGwJLcdK1C_8-vj8-R3M71nl_uM_PTAA6xIlz56gyCQHoijSnSWOm9xoHyWUTLEMPxZKwDOKuPflwgsv12G0Rym7ratIBziOBVGN-c)

O PIP, gerenciador de pacotes embutido no Python, facilita a instalação, desinstalação e verificação do status de pacotes em seu ambiente de desenvolvimento.

**1. Verificar pacotes instalados:**

-   Utilize o comando `pip freeze` em uma célula para visualizar uma lista completa dos pacotes instalados em seu ambiente virtual.
-   Este comando gera um arquivo `requirements.txt` com a lista de pacotes e suas versões.

**2. Instalar pacotes:**

-   Para instalar um pacote específico, utilize o comando `pip install` seguido do nome da biblioteca.
-   Exemplo:  `pip install numpy` instala a biblioteca NumPy.

**3. Desinstalar pacotes:**

-   Para remover um pacote, utilize o comando `pip uninstall` seguido do nome da biblioteca.
-   Exemplo:  `pip uninstall matplotlib` desinstala a biblioteca Matplotlib.

Dicas:
-   Crie um arquivo `requirements.txt` para listar as dependências do seu projeto e facilitar a instalação em outros ambientes.
-   Utilize o comando `pip install -r requirements.txt` para instalar todas as dependências listadas no arquivo.
-   Mantenha seus pacotes atualizados com o comando `pip install --upgrade <nome_do_pacote>`.

## Biblioteca `Requests`

Outro pacote que é particularmente popular e igualmente fácil de instalar no final do uso de APIs. Agora, APIs não são algo específico do Python. De forma mais geral, uma API é uma interface de programação de aplicativos. E pode se referir a arquivos e funções Python. Mas muitas vezes, as APIs realmente se referem a serviços de terceiros com os quais você e eu podemos escrever códigos que se comunicam. 

Muitas APIs, mas não todas, vivem na Internet hoje em dia, de modo que, desde que você tenha um navegador ou alguma experiência com programação Python ou programação em qualquer linguagem, você possa escrever código que, na verdade, finge ser um navegador, conecta-se a essa API de terceiros em um servidor e baixa alguns dados que você pode incorporar em seu próprio programa. 

Agora, como você faz isso? Bem, Python tem um pacote muito popular que você pode instalar via pip chamado requests. A biblioteca de solicitações permite que você faça solicitações da web e da Internet usando código Python essencialmente como se você fosse um navegador. Você pode automatizar, portanto, a recuperação de URLs que começam com HTTP ou HTTPS.

**Para isso, siga estes passos:**

1.  **Abra o Google:** Seu portal para o conhecimento!
2.  **Pesquise por "Requests Python":** Encontre a documentação oficial em um piscar de olhos.
3.  **Acesse o primeiro link:** A página principal da documentação te espera!

**Mas aguarde! A biblioteca Requests apresenta algumas peculiaridades:**

-   **Ao pesquisar por "Requests Python", você não será direcionado diretamente para a página da documentação.**
-   **Em vez disso, chegará ao PyPI (Python Package Index), um repositório de pacotes Python.**

**O que é o PyPI?**

Imagine o PyPI como uma enorme biblioteca virtual, onde desenvolvedores compartilham e distribuem suas criações para o mundo.

**E qual a relação com a biblioteca Requests?**

-   Quando você utiliza o comando `pip install nome_da_biblioteca`, na verdade está baixando a biblioteca específica do repositório PyPI e instalando-a em seu ambiente Python local.

Ao contrário das páginas de documentação oficial das bibliotecas, a página do PyPI geralmente não oferece uma explicação completa de todas as funcionalidades da biblioteca.

Em vez disso, ela normalmente apresenta um resumo e um exemplo básico.**

No entanto, dentro dessa página, você sempre encontrará um link que o redirecionará para a documentação completa da biblioteca.

Esse link pode ser encontrado no conteúdo principal da página ou nos links de acesso no menu lateral esquerdo, "ProjectLinks" ou "Links do Projeto".

![](https://lh7-us.googleusercontent.com/Q0EEFNTBjGfFp5dngag4Nti6q5u-tRkYyuGFOYv_pcjPx2d4hb4ncvFLacwDkuteOYFlw9ewsQkB9RdGyFEdQwL4j-QxevEuI-AeywhPhAIuV9lSjRQwsl4SwZAsVXIGE6gjDAYf6CGLSxznyGdUCu8)



![](https://lh7-us.googleusercontent.com/LLaoEZyCPyNuNfANIluoMrarVsZH3w7V7CIxPUCB-5qlANZi_TdcRhnldkniMWruwWjdvkZtHqmwHq_mBBn0plEOBSvPaOFGJ0bVxlQizK2SYhBWCX3Dt_zjdW80P4xgFjCCNKd9HXzSOnbXOjI7XJo)

**Cada documentação possui suas peculiaridades e estruturas únicas.** Mas não se preocupe, a forma de explorá-las segue um padrão básico:

**1. Comece com o guia introdutório:**

-   **Quickstart:** Um guia rápido e prático para te colocar em ação em minutos.
-   **Getting Started:** Dê seus primeiros passos com a biblioteca de forma gradual e abrangente.
-   **User Guide:** Um manual completo para usuários de todos os níveis, explorando todas as funcionalidades da biblioteca.

**Através destes guias, você:**

-   **Obtém uma visão geral da biblioteca e seus recursos.**
-   **Aprende os conceitos básicos e a terminologia.**
-   **Realiza tarefas comuns com exemplos práticos.**
-   **Entende como usar as funções e métodos da biblioteca.**

**Lembre-se:**

-   A documentação é o seu guia para dominar a biblioteca.
-   Explore-a e consulte seus diferentes recursos sem medo.
-   Com prática, você se tornará um expert em encontrar as informações que precisa.

**Dicas para aproveitar ao máximo a documentação:**

-   **Leia com atenção:** A documentação contém informações valiosas sobre a biblioteca e suas funcionalidades.
-   **Pratique com os exemplos:** Os exemplos demonstram como usar a biblioteca na prática.
-   **Faça anotações:** Registre as informações importantes para consulta posterior.
-   **Utilize o índice e a função de busca:** Encontre rapidamente as informações que você precisa.

**Algumas bibliotecas, como a Requests, exigem conhecimentos adicionais para serem compreendidas totalmente.**

**A Requests, por exemplo, lida com requisições HTTP.** Sendo assim, se você não estiver familiarizado com o conceito de requisições HTTP, é provável que encontre algumas dificuldades para compreender totalmente o funcionamento dela.

Neste caso, a documentação da biblioteca pode te direcionar para recursos complementares que te ajudarão a aprofundar seus conhecimentos e dominar a biblioteca com maestria!

### Iremos agora, fazer o uso direto dessa biblioteca;
Após termos visitado a página do projeto via navegador, podemos também instalar via terminal com o `pip install requests`. Após a instalação vamos fazer um novo arquivo .py e trabalhar encima dessa biblioteca com afinco.

Acontece que a Apple tem sua própria API (interface de programação de aplicativos) para o serviço iTunes. O software que oferece a capacidade de baixar e pesquisar músicas, além de outras informações, tudo isso pode ser conferido [aqui](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/SearchExamples.html#//apple_ref/doc/uid/TP40017632-CH6-SW1).

Utilizando-se dos exemplos e dos outros termos utilizados dentro da documentação da API da apple, foi criado o URL abaixo manualmente é descrito que se eu quiser pesquisar informações sobre músicas em seu banco de dados, devo especificar entidade igual a música, para que músicas e não álbuns ou artistas ou algo parecido. Se eu quiser apenas obter informações sobre uma música, fornecerei o limite igual a 1. E se a banda que desejo pesquisar e o artista for *Weezer*, devo especificar o termo igual a *Weezer*.

https://itunes.apple.com/search?entity=song&limit=1&term=weezer.Search?entity=song&limit=1&term=weezer

Ao clicar em qualquer um dos links distribuídos da API, você verá que será baixado um arquivo de texto que a primeira vista está todo bagunçado, mas calma, vamos ver isso com calma agora:

![](https://lh7-us.googleusercontent.com/oqImTCfPmT5d26ISnXl-64zA82s9yXjgTHZQtCDyvAirUhK74xpyuOE26mNNnLt5xjWGn-enXmGX5mZIaYUPwmeK476MGRZxBNAlfFtEVbwPGRVOG2_Xc1FChXThBz2N84Ka8B3lB0aZRXrx6E7_P1Y)

Observe a chave no início e observe a chave fechada no final. 
```
{ <-----
 "resultCount":1,
 "results": [
{"wrapperType":"track", "kind":"song", "artistId":348864246, "collectionId":1547589208, "trackId":1547589209, "artistName":"Niji Liquidum", "collectionName":"Satisfaction", "trackName":"Aphex", "collectionCensoredName":"Satisfaction", "trackCensoredName":"Aphex (Original Version)", "artistViewUrl":"https://music.apple.com/us/artist/niji-liquidum/348864246?uo=4", "collectionViewUrl":"https://music.apple.com/us/album/aphex-original-version/1547589208?i=1547589209&uo=4", "trackViewUrl":"https://music.apple.com/us/album/aphex-original-version/1547589208?i=1547589209&uo=4", 
"previewUrl":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview114/v4/23/14/15/231415e7-06d3-6b05-437e-6c250a1fd3bf/mzaf_120257653372325723.plus.aac.p.m4a", "artworkUrl30":"https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/37/61/16/376116de-f9ca-e013-9274-1803c4537872/SUR022.jpg/30x30bb.jpg", "artworkUrl60":"https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/37/61/16/376116de-f9ca-e013-9274-1803c4537872/SUR022.jpg/60x60bb.jpg", "artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/37/61/16/376116de-f9ca-e013-9274-1803c4537872/SUR022.jpg/100x100bb.jpg", "collectionPrice":4.99, "trackPrice":0.69, "releaseDate":"2009-12-23T12:00:00Z", "collectionExplicitness":"notExplicit", "trackExplicitness":"notExplicit", "discCount":1, "discNumber":1, "trackCount":14, "trackNumber":1, "trackTimeMillis":300000, "country":"USA", "currency":"USD", "primaryGenreName":"Easy Listening", "isStreamable":true}]
} <-----
```
Observe que há também um colchete aberto no início e bem no final do código
``` 
"results": [ <--------
{"wrapperType":"track", "kind":"song", "artistId":348864246, "collectionId":1547589208, "trackId":1547589209, "artistName":"Niji Liquidum", "collectionName":"Satisfaction", "trackName":"Aphex", "collectionCensoredName":"Satisfaction", "trackCensoredName":"Aphex (Original Version)", "artistViewUrl":"https://music.apple.com/us/artist/niji-liquidum/348864246?uo=4", "collectionViewUrl":"https://music.apple.com/us/album/aphex-original-version/1547589208?i=1547589209&uo=4", "trackViewUrl":"https://music.apple.com/us/album/aphex-original-version/1547589208?i=1547589209&uo=4", 
"previewUrl":"https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview114/v4/23/14/15/231415e7-06d3-6b05-437e-6c250a1fd3bf/mzaf_120257653372325723.plus.aac.p.m4a", "artworkUrl30":"https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/37/61/16/376116de-f9ca-e013-9274-1803c4537872/SUR022.jpg/30x30bb.jpg", "artworkUrl60":"https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/37/61/16/376116de-f9ca-e013-9274-1803c4537872/SUR022.jpg/60x60bb.jpg", "artworkUrl100":"https://is1-ssl.mzstatic.com/image/thumb/Music114/v4/37/61/16/376116de-f9ca-e013-9274-1803c4537872/SUR022.jpg/100x100bb.jpg", "collectionPrice":4.99, "trackPrice":0.69, "releaseDate":"2009-12-23T12:00:00Z", "collectionExplicitness":"notExplicit", "trackExplicitness":"notExplicit", "discCount":1, "discNumber":1, "trackCount":14, "trackNumber":1, "trackTimeMillis":300000, "country":"USA", "currency":"USD", "primaryGenreName":"Easy Listening", "isStreamable":true}] <-----
```
E entre essas partes da sintaxe há um monte de strings e valores. Na verdade, um monte de pares de valores-chave. O que estamos vendo aqui é um formato de texto padrão conhecido como JSON - JavaScript Object Notation, que sim, está tecnicamente relacionado a outra linguagem de programação chamada JavaScript. Mas o próprio JSON é normalmente usado hoje em dia como um formato independente de linguagem para troca de dados entre computadores. 

Esse texto é formatado de maneira padrão usando chaves, colchetes, aspas e alguns dois-pontos que, em última análise, contém todas as informações no banco de dados da Apple sobre a música do Weezer, pelo menos, a primeira porque eu a limitei a uma em seu banco de dados. E isso é uma API, uma interface de programação de aplicativos. Um mecanismo pelo qual posso acessar dados no servidor de outra pessoa e de alguma forma integrá-los ao meu próprio programa. 

Agora, o seu navegador por exemplo, não é algo que eu ou você escreveu. Então vamos escrever um código através do qual eu possa usar a API do iTunes e, por sua vez, o Python para obter informações sobre qualquer banda que eu queira.

Vamos começar importando a biblioteca *requests* e a biblioteca sys que já vimos anteriormente:
```py
import requests
import sys
```
A biblioteca de requests, que fora instalada anteriormente é feita para fazer essas solicitações HTTP. Já a biblioteca sys, é usada para a finalidade de usar argumentos de linha de comando.

ao continuar nosso código podemos escrever a linha:
```py
if len(sys.argv) != 2:
	sys.exit()
```
Em resumo, esta linha `if len(sys.argv) != 2:` verifica se o número de argumentos da linha de comando passados para o script é diferente de 2, que no caso, seria a pesquisa de uma banda ou artista.

Se não houver exatamente 2 argumentos, o script sai usando `sys.exit()`. Essa é uma maneira comum de garantir que o script seja usado corretamente e tenha a entrada necessária para a execução.

Seria possível fornecer uma mensagem mais explicativa. Mas, por enquanto, será mantido de forma mais simples e apenas sair do programa prematuramente para poder confiar que sys.argv tem o que é realmente preciso. E agora, tenho a oportunidade de usar a biblioteca de solicitações para escrever algum código Python que efetivamente finge ser um navegador da Web para se conectar ao mesmo URL HTTPS no próprio servidor da Apple.

Agora que garantimos que o usuário digitou não apenas o nome do arquivo, mas também o nome de uma banda no prompt, dando-me um comprimento de dois para ``sys.argv``, vamos prosseguir e executar a função ``requests.get``, que é uma função dentro do pacote de solicitação que literalmente obterá alguma resposta de um servidor. E o URL que é exatamente o mesmo de antes. Mas tornando-o mais humanamente interativo e permitir que o usuário especifique na linha de comando quais artistas eles gostariam de procurar.

Então, podemos apagar o que seria a última parte do "Termo" pesquisado e concatenar com o sys.argv[1], tudo isso dentro de uma variável *resposta* por exemplo.
```py
resposta = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer.Search?entity=song&limit=1&term=") +  sys.argv[1]
```

Então isso ainda não vai ser muito bonito. Mas vou imprimir o resultado como JSON com:
```py
print(resposta.json())
```
o que nos deixa com o código até agora como:
```py
import requests
import sys

if  len(sys.argv) !=  2:
	sys.exit()

resposta  = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer.Search?entity=song&limit=1&term="  + sys.argv[1])
print(resposta.json())
```
Agora com o argumento  sys.argv[1] podemos digitar o nome de uma banda como Weezer e pressionar Enter.

![](https://lh7-us.googleusercontent.com/5MtPiAqg4rjPAqhRanE88uY5-yOoUOmXUJT1iOATdsVT7YsvVVgg1g6KGeGRihaIrvJPQpdFc_ZznBiGM3Vfyw1A83VORNGw0hRwaCVVdgQ5uyoVKoqgXFlcH5uyrwqylr3JbCQXs1GeVRH42R70sao)

E o que vemos na tela formatado quase igual a antes é exatamente o mesmo texto. Mas o que você verá aqui é que agora ele foi padronizado como um dicionário Python. O que de fato está retornando da Apple é tecnicamente uma resposta JSON (JavaScript Object Notation), mas Python, a biblioteca de solicitação, está convertendo-o em um dicionário Python que, por coincidência, usa quase a mesma sintaxe.

Ele usa chaves para representar o dicionário e uma chave fechada para representar o final dele. Para qualquer lista contida nele, ele usa um colchete e um colchete fechado. Ele usa aspas simples neste caso ou equivalentemente aspas duplas para representar as chaves nesse dicionário. E depois de dois pontos, ele armazena o valor dessa chave.

![](https://lh7-us.googleusercontent.com/GUK9NEhAQdnjOgISMTb1EqFfMXQgqY8ldmB02YVjnRPW4YoMP935AguN3QEPxOPZ0TSojUTupu_fMRt1YcOdChEhovben8dpjOVqU9mmLdn1nwjm7Q_PH76u2F9vMTgcfczmIn0z91m-inQ2GS5OguQ)

E então você verá que de fato temos uma chave de contagem de resultados cujo valor é 1, mas então uma chave de resultado mais interessante chamada resultados cujo valor é toda esta lista de dados. Honestamente, esta é uma bolha de texto tão grande que vou levar uma eternidade para entender o que estou vendo. Então, deixe-me propor temporariamente que usemos outra biblioteca em Python que me permitirá formatar meus dados de forma um pouco mais limpa.

Acontece que o Python também vem com uma biblioteca especial chamada [json](docs.python.org/3/library/json.html) que permite manipular dados JSON e até mesmo imprimi-los formatados de uma maneira que será muito mais fácil para você e eu entendermos. 
```py
import json
```
Deixe-me importar esta biblioteca adicional, JSON, que vem com Python. Portanto, não é preciso instalá-lo manualmente com pip.

Vamos agora usar uma outra função aqui chamada `json.dumps` e passar para essa função o valor de retorno de `resposta.json`.

Então, novamente, estou apenas apresentando outra função que, afirmo, tem um propósito na vida de imprimir visualmente de forma bonita, formatando perfeitamente na tela exatamente as mesmas informações. E de acordo com a documentação, se eu passar um parâmetro nomeado de `indent(recuo)` igual a 2 (ou `indent = 2`), isso recuará tudo em pelo menos dois espaços, é possível fazer também por exemplo quatro ou mais. Mas 2 será o suficiente para me ajudar a entender quais são os dados que estou recebendo.

![](https://lh7-us.googleusercontent.com/uOUxEH52NXANio4HYGiNTnYtXIcFWXzO3YLw-cXIIl3jElzidzZob18mvqnlba48obJYpAtSPgjDSey_OKPC0EhPuVdHcrllBVyg9X7Ly5zzyfsJKK3AdcyAbBjpVx2Fd60ACAxV4m3HF2ZO9tzwrWw)

Observe como agora as informações são as mesmas, porém, agora está bem mais organizado e fácil de interpretar.

Observe agora que ainda é possível ver a primeira chave, o que significa que, este é um dicionário em Python. Uma coleção de chaves e valores. 
```
{
	"resultCount": 1
	"results": [
	   {
	   
	[...]
```
A primeira chave é chamada contagem de resultados. Acontece que agora é exibido entre aspas duplas. Mas isso é apenas uma questão de formatação. Pode ser duplo ou simples, desde que sejamos consistentes.

O valor dessa chave é um. Por que? Bem, foi ordenado ao URL para limitar apenas as respostas a uma música do Weezer, então obtive um conjunto de resultados de uma. Se eu aumentar esse limite, provavelmente conseguirei mais. Então a parte interessante desta resposta são os próprios dados.
```
{
  "resultCount": 1,
  "results": [
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 115234,
      "collectionId": 1440878798,
      "trackId": 1440879325,
      "artistName": "Weezer",
      "collectionName": "Weezer",
      "trackName": "Buddy Holly",
      "collectionCensoredName": "Weezer",
      "trackCensoredName": "Buddy Holly",
      "artistViewUrl": "https://music.apple.com/us/artist/weezer/115234?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/buddy-holly/1440878798?i=1440879325&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview221/v4/24/d0/07/24d007fc-6bd8-618b-618b-ae5f431ee89c/mzaf_1481529079228661859.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music221/v4/d0/16/da/d016da24-577e-b584-3a5a-116efb5ca362/16UMGIM52971.rgb.jpg/100x100bb.jpg",      
      "collectionPrice": 10.99,
      "trackPrice": 1.29,
      "releaseDate": "1994-02-28T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 10,
      "trackNumber": 4,
      "trackTimeMillis": 159587,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Pop",
      "isStreamable": true
    }
  ]
}
```
 Observe na chave de resultados "Results:", há um valor muito grande. O valor é uma lista Python, conforme implícito no colchete que o precede.
 
O que esta lista contém? Bem, eu sei, por ter lido anteriormente, que este contém um dicionário. E é por isso que vemos outra chave aqui. Então, novamente, se isso ficar um pouco mais complicado, lembre-se de que um dicionário é apenas uma coleção de pares de valores-chave e Python usa chaves para indicar isso.

É perfeitamente razoável que um dicionário esteja dentro de outro dicionário se o valor de alguma chave for outro dicionário. Portanto, este é um paradigma comum. E mesmo que pareça um pouco enigmático, é apenas algo que nos permite associar mais chaves a mais valor.

Agora, voltando as informações obtidas no site do iTunes, muito provavelmente não nos importamos com a maior parte dessas informações. Por exemplo, de acordo com a Apple, o identificador exclusivo do Weezer é aparentemente 115.234. 
```
	"artistId": 115234,
	"collectionId": 1440878798,
	"trackId": 1440879325,
```

Isso pode ser útil se eu estiver criando meu próprio banco de dados e quiser que ele seja pesquisável. Mas para os propósitos de hoje, tudo que me importa é o nome da faixa, também chamado de trackName como referencial.
```
"trackName": "Buddy Holly",
```
E também é a primeira música e única porque a limitamos a uma que recebemos do iTunes,  a música em questão retornada do Weezer chamada *Buddy Holly*. Então agora, tenho uma ideia se meu objetivo aqui é implementar um programa chamado itunes.py que não apenas despeje a resposta do servidor, o que é reconhecidamente muito enigmático - mas também imprima todas as músicas que o iTunes tem para a banda chamada Weezer, talvez eu possa repetir isso de alguma forma.

Mas agora, como podemos lidar com essas informações neste dicionário? Bom, começamos não imprimimos preguiçosamente o conteúdo da variável ``resposta`` porque isso não é interessante ou bonito para ninguém. 

Deixe-me prosseguir e criar uma nova variável apenas para fins de discussão chamada ``o`` para objeto. E vou prosseguir e chamar o ``= response.json`` apenas para armazenar essa resposta JSON especificamente em uma variável chamada ``o``, desta forma:
```
o = response.json()
```
Mas esta variável pode ser nomeada como quiser, e agora, vou fazer isso. Para cada resultado na chave desse objeto chamada results, vá em frente e imprima o nome da trilha desse resultado, não entendeu? Bem, no código fica assim:
```
for result in o["results"]:
	print(result["trackName"])
```

E observe que foi utilizado exatamente a mesma capitalização. O nome da faixa tem N maiúsculo. O resultado está todo em letras minúsculas. E antes de executarmos o programa real. 

![](https://lh7-us.googleusercontent.com/Kl-abWnkzzTRFtvKRWA9COx9KVX5J8BGjT4xY8J0fmNa68-ifgaylfT8V_Qt7SE_ya-kpqiRUyBE6WgHDT9MGDbEhrkOkR3CtafWSSmHreLxLJAa1n5FBSXISYR8rCDpnYul6qvs7ZPziE9e_ErPu3s)

Na linha oito, estamos fazendo uma solicitação HTTP usando Python para o servidor, assim como você e eu, enquanto humanos, digitamos URLs em um navegador e pressionamos Enter, este é o equivalente em Python.

Estou então na linha 10 apenas pegando daquela variável que contém a resposta do servidor, o objeto JSON que me interessa. A coisa entre aquelas chaves na parte superior e inferior. Mas porque demos uma olhada, sabemos que esse objeto tem uma chave chamada resultados. E essa chave de resultados novamente é uma lista.

Agora, no momento, essa lista contém apenas uma música, a música *Buddy Holly*, porque limitei minha resposta a uma. 

**![](https://lh7-us.googleusercontent.com/cXtV_O3GqUfL3ykVMZtG4SJecOpqPYiEKXIh9Qoqq-9x2lyyQeXhXJM2du6Gb-8Tdz2sK6g7rMVXq2dVbMGyT_pSFSJPRNt4kSw6iEvofctgqixLNZeN-3QWORRi6cSKHSAtb_3P87b12Tm3_-yel5k)**

Mas mesmo assim, meu loop funcionará. Só vai iterar uma vez. E cada vez que passar por esse loop, ele imprimirá o nome da trilha do resultado atual.

Se quiser tornar isso ainda mais interessante, é possível alterar esse limite agora de 1 para 50, para que eu receba pelo menos 50 nomes de faixas, toda essa alteração sendo feita na linha 8 do código e a deixando assim:
```
resposta  = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer.Search?entity=song&limit=50&term="  + sys.argv[1])
``` 

Rodando novamente o código e procurando novamente por uma banda como o Weezer, com o código atualizado com a pequena alteração acima e teremos:

**![](https://lh7-us.googleusercontent.com/m2xUvbY40u15i997nh5B0rlfAohv2pu2iR6MjTLLyzZ6fAmBSo3jvE63iI_svTBghtYCRHcrsfJ5p55kz09DE_NT2ICQ9fPxvCIpZ6Yr7UOQZiYcRMcwW6JUrFGK7PR4E1QTXJhVHdo0fV04ZAUO_9g)**

Podemos ver que existem 50 músicas que o iTunes tem para o Weezer, e se voltarmos ao topo aqui, veremos que a primeira faixa deles é, de fato, Buddy Holly. Mas agora, Undone-- The Sweater Song, Say It Ain't So e assim por diante.


> Agora você pode aproveitar até para brincar um pouco e colocar o nome
> de uma banda ou artista também!
