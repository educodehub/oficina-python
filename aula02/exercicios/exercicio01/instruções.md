[Voltar](https://github.com/educodehub/oficina-python/blob/main/aula02/instru%C3%A7%C3%B5es.md)

# lista_de_compras.py

## Instruções
Nessa atividade você deverá criar um programa que organiza os itens e quantidades de cada item de uma lista de compras em um dicionário python. 

Crie um programa que leia uma entrada no formato `item1 quantidade1; item2 quantidade2`, com os diferentes itens separados por ';' (ponto e vírgula) e suas respectivas quantidades separadas por ' ' (espaço), e organizes esses elementos em um dicionário contendo todos os pares `{item: quantidade}`. Ao fim da execução, o programa deverá exibir esse dicionário no terminal.
\
\
\
Lembre-se que as strings possuem uma grande variedade de métodos, veja uma lista deles na [documentação](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods) ou, se preferir, nessa [tabela de referência](https://www.w3schools.com/python/python_ref_string.asp).
\
Assim como as strings, os dicionários também possuem alguns métodos próprios, veja-os nessa [lista de referência](https://www.w3schools.com/python/python_ref_dictionary.asp).

> [!TIP]
> <details>
>    <summary>Pistas</summary>
>    <ol>
>        <li>Lembre-se que o laço for pode iterar sobre elementos de uma lista.</li>
>        <li>Talvez você precise de um método que possa dividir uma string.</li>
>        <li>Talvez você precise de um método que adicione elementos a um dicionário.</li>
>        <li>Os elementos de um dicionário podem vir de uma variável.</li>
>        > Ex: o código <code>{item: quantidade}</code> vai criar um dicionário com o conteúdo armazenado em <code>item</code> como chave e o conteúdo armazenado em <code>quantidade</code> como valor.
>    </ol>
> </details>


## Demo
| **lista_de_compras.py**                                                                                            |
| :-------------------------------------------------------------------------------------------------------------- |
| ![demo-code](https://github.com/educodehub/oficina-python/assets/99366724/7af82eb5-55cd-429e-9e68-eef009d01714) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻


## Antes de Começar
Antes de continuar, é preciso preparar seu workspace.
<ul>
    <li>Em um diretório da sua escolha, crie uma pasta chamada <strong>python-exercicios</strong>.</li>
    <li>Abra a pasta no VSCode, ou usando o atalho <code>Ctrl+K Ctrl+O</code>, ou arrastando-a pasta para a janela do VSCode. É nessa pasta que você alocará todos os programas e arquivos desenvolvidos para todos os exercícios.</li>
    <li>Com a pasta aberta, crie uma nova pasta chamada <strong>compras</strong> para armazenar os arquivos desta atividade em específico.</li>
    <li>Digite <code>Ctrl+Shift+"</code> para abrir um terminal do seu prompt de comando e, em seguida, digite <code>cd compras</code> para abrir o diretório da atividade.</li>
    <li>No diretório da atividade crie um arquivo chamado <code>lista_de_compras.py</code> e use-o para desenvolver o código da atividade.</li>
</ul>

Feito isso, você vai estar pronto para começar a atividade.


## Como testar
Com o terminal aberto na pasta contendo o programa, é assim que você vai testá-lo:
<ul>
    <li>Execute o script e digite <code>batata 1kg; feijão 2kg; arroz 1kg</code> depois <strong>Enter</strong>. O programa deverá retornar <code>{'batata': '1kg', 'feijão': '2kg', 'arroz': '1kg'}</code>.</li>
    <li>Execute o script e digite <code>frango 1kg; alho 3und; cebola 5und</code> depois <strong>Enter</strong>. O programa deverá retornar <code>{'frango': '1kg', 'alho': '3und', 'cebola': '5und'}</code>.</li>
    <li>Execute o script e digite <code>bisteca-bouvina 1kg; tomate 500g; pimentão 500g; cominho 50g</code> depois <strong>Enter</strong>. O programa deverá retornar <code>{'bisteca-bouvina': '1kg', 'tomate': '500g', 'pimentão': '500g', 'cominho': '50g'}</code>.</li>
</ul>

Se algum dos testes falhar, tente corrigir o programa antes de enviá-lo. Caso contrario, você *provavlemente* está pronto para seguir para a próxima etapa.


## Como enviar
Acesse o link do [Exercício 01 - Aula 02 - Oficina de Python](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/NjgyMTE2MDM2ODIw/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **lista_de_compras.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
