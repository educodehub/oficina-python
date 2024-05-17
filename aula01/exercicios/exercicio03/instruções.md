[Voltar](https://github.com/educodehub/oficina-python/blob/main/aula01/instru%C3%A7%C3%B5es.md)
# media.py


## Instruções
Você foi chamado para desenvolver um sistema de avaliação de notas dos alunos de uma escola. Ele deve fornecer a média do aluno na escala de 0 a 10 e o equivalente no sistema de notas por letras. Você foi ainda informado que essa escola utiliza um padrão de avaliação por **quatro** notas.

Seu programa deverá começar pedindo ao usuário para inserir as quatro notas do aluno, uma por linha. Em seguida, o programa calculará a média da aritmética de todas as notas e, após o cálculo da média, o programa verificará o status de aprovação do aluno. Por fim, o programa deverá exibir a média final na escala de 0 a 10 e no sistema de notas por letras.

> [!IMPORTANT]
> É importante saber que o sistema de notas por letras se equivale à escala de 0 a 10 da seguinte forma:
> <ul>
>     <li>A equivale a 9 ou mais;</li>
>     <li>B equivale a um valor de 8 a 8.9;</li>
>     <li>C equivale a um valor de 7 a 7.9;</li>
>     <li>D equivale a um valor de 6 a 6.9;</li>
>     <li>F equivale a qualquer valor abaixo de 6.</li>
> </ul>

> [!TIP]
> <details>
>    <summary>Pistas</summary>
>    <ol>
>        <li>O cálculo da média deverá suportar valores decimais</li>
>        <li>Lembre-se da estrutura condicional if</li>
>        <li>Lembre-se do uso do <strong>elif</strong> no encadeamento de condições</li>
>    </ol>
> </details>

## Demo
| **media.py**                                                                                                          |
| :-------------------------------------------------------------------------------------------------------------------- |
| ![demo-code](https://github.com/educodehub/oficina-python/assets/99366724/f093d76f-77bd-4104-b318-b15dabff4037) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻


## Antes de Começar
Antes de continuar, é preciso preparar seu workspace.
<ul>
    <li>Em um diretório da sua escolha, crie uma pasta chamada <strong>python-exercicios</strong>.</li>
    <li>Abra a pasta no VSCode, ou usando o atalho <code>Ctrl+K Ctrl+O</code>, ou arrastando-a pasta para a janela do VSCode. É nessa pasta que você alocará todos os programas e arquivos desenvolvidos para todos os exercícios.</li>
    <li>Com a pasta aberta, crie uma nova pasta chamada <strong>media</strong> para armazenar os arquivos desta atividade em específico.</li>
    <li>Digite <code>Ctrl+Shift+"</code> para abrir um terminal do seu prompt de comando e, em seguida, digite <code>cd media</code> para abrir o diretório da atividade.</li>
    <li>No diretório da atividade crie um arquivo chamado <code>media.py</code> e use-o para desenvolver o código da atividade.</li>
</ul>

Feito isso, você vai estar pronto para começar a atividade.


## Como testar
Com o terminal aberto na pasta contendo o programa, é assim que você vai testá-lo:
<ul>
    <li>Execute o script e digite <code>8</code>, <code>8</code>, <code>7</code> e <code>9</code>, um para cada linha do terminal, e pressione <strong>Enter</strong>. O programa deverá retornar <code>Média 8.0 - B</code>.</li>
    <li>Execute o script e digite <code>9</code>, <code>5</code>, <code>7</code> e <code>6</code>, um para cada linha do terminal, e pressione <strong>Enter</strong>. O programa deverá retornar <code>Média 6.75 - D</code>.</li>
    <li>Execute o script e digite <code>9</code>, <code>9</code>, <code>10</code> e <code>8</code>, um para cada linha do terminal, e pressione <strong>Enter</strong>. O programa deverá retornar <code>Média 9.0 - A</code>.</li>
    <li>Execute o script e digite <code>5</code>, <code>6</code>, <code>5.5</code> e <code>5.5</code>, um para cada linha do terminal, e pressione <strong>Enter</strong>. O programa deverá retornar <code>Média 5.5 - F</code>.</li>
    <li>Execute o script e digite <code>6</code>, <code>7.5</code>, <code>7</code> e <code>8.5</code>, um para cada linha do terminal, e pressione <strong>Enter</strong>. O programa deverá retornar <code>Média 7.25 - C</code>.</li>
</ul>

Se algum dos testes falhar, tente corrigir o programa antes de enviá-lo. Caso contrario, você *provavlemente* está pronto para seguir para a próxima etapa.


## Como enviar?
Acesse o link do [Exercício 03 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc1OTgxMzQ2MTQy/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **media.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
