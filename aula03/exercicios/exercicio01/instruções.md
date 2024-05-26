> [!CAUTION]
> ## como enviar
> atv_nome [Exercício 01 - Oficina de Python - Aula 1]
> 
> atv_link

[Voltar](https://github.com/educodehub/oficina-python/blob/main/aula03/instru%C3%A7%C3%B5es.md)

# adivinhe.py

## Instruções
Estou pensando em um número entre 1 e 100...
> <details>
>    <summary>Qual o número?</summary>
>    <ol>
>        É o 7! Mas e se fosse mais aleatório?
>    </ol>
> </details>
\
Nessa atividade você irá criar um jogo no qual o jogador tem que adivinhar qual foi o número sorteado pelo programa. O programa deverá cumprir com os seguintes requisitos:
1. O programa deverá receber um número inteiro ***n*** como argumento, que ajustará a dificuldade do jogo;
    1. Se nenhum argumento for dado, o programa deverá encerrar prematuramente e exibir uma mensagem avisando da ausência do argumento;
3. O programa deverá selecionar um número inteiro aleatório entre **1** e ***n***;
4. O jogador terá que adivinhar o número selecionado;
    1. Se o número digitado for menor que o sorteado, o programa deverá exibir "Muito baixo!";
    2. Se o número digitado for maior que o sorteado, o programa deverá exibir "Muito alto!";
    3. Se o número digitado for igual o sorteado, o programa deverá exibir "Na mosca!", e encerrar a execução.

> [!TIP]
> <details>
>    <summary>Pistas</summary>
>    <ol>
>        <li>A biblioteca random vem com uma função dedicada à seleção de números inteiros aleatórios</li>
>        <li>A biblioteca sys possibilita o uso de argumentos por meio do sys.argv e o encerramento do programa com sys.exit()</li>
>        <li>Lembre-se de usar o int() para converter o argumento e as entradas</li>
>    </ol>
> </details>


## Demo
| **adivinhe.py**                                                                                            |
| :-------------------------------------------------------------------------------------------------------------- |
| ![demo-code](https://github.com/educodehub/oficina-python/assets/99366724/2449cd86-d051-4cbc-b7fd-472bcc02e1a1) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻


## Antes de Começar
Antes de continuar, é preciso preparar seu workspace.
<ul>
    <li>Em um diretório da sua escolha, crie uma pasta chamada <strong>python-exercicios</strong>.</li>
    <li>Abra a pasta no VSCode, ou usando o atalho <code>Ctrl+K Ctrl+O</code>, ou arrastando-a pasta para a janela do VSCode. É nessa pasta que você alocará todos os programas e arquivos desenvolvidos para todos os exercícios.</li>
    <li>Com a pasta aberta, crie uma nova pasta chamada <strong>adivinhe</strong> para armazenar os arquivos desta atividade em específico.</li>
    <li>Digite <code>Ctrl+Shift+"</code> para abrir um terminal do seu prompt de comando e, em seguida, digite <code>cd adivinhe</code> para abrir o diretório da atividade.</li>
    <li>No diretório da atividade crie um arquivo chamado <code>adivinhe.py</code> e use-o para desenvolver o código da atividade.</li>
</ul>

Feito isso, você vai estar pronto para começar a atividade.


## Como testar
Com o terminal aberto na pasta contendo o programa, é assim que você vai testá-lo:
<ul>
    <li>Execute o script sem <code>nenhum argumento</code>. O programa deverá retornar uma mensagem de erro como "<code>Você precisa inserir um número para a dificuldade como argumento</code>".</li>
    <li>Execute o script com um <code>10</code> como argumento. O programa deverá pedir por um <code>número entre 1 e 10</code>.</li>
    <li>Execute o script com um inteiro com argumento, digite um <code>número abaixo do sorteado</code> e depois <strong>Enter</strong>. O programa deverá retornar <code>Muito baixo!</code>.</li>
    <li>Execute o script com um inteiro com argumento, digite um <code>número acima do sorteado</code> e depois <strong>Enter</strong>. O programa deverá retornar <code>Muito alto!</code>.</li>
    <li>Execute o script com um inteiro com argumento, digite <code>o número sorteado</code> e depois <strong>Enter</strong>. O programa deverá retornar <code>Na mosca!</code>.</li>
</ul>

Se algum dos testes falhar, tente corrigir o programa antes de enviá-lo. Caso contrario, você *provavlemente* está pronto para seguir para a próxima etapa.


## Como enviar
Acesse o link do [atv_nome](atv_link) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **adivinhe.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
