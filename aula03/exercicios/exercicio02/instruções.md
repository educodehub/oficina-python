[Voltar](https://github.com/educodehub/oficina-python/blob/main/aula03/instru%C3%A7%C3%B5es.md)

# pokedex.py

## Instruções
Na nossa aula vimos o conceito de *APIs* e como acessá-las por meio de requisições HTTP usando a biblioteca ***requests***. 

Nessa atividade, vamos nos aprofundar um pouco mais na utilização da biblioteca requests criando uma pokedex simplificada que recebe o nome de um pokemon e retorna seu id e seus tipos (normal, ghost, fire etc.).
\
\
\
![](https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi_256.png)

Para conseguir as informações, você deverá fazer requisições à API *[PokeAPI](https://pokeapi.co/)* usando a biblioteca requests, e extrair as informações de ***id*** e ***tipos*** do JSON obtido como respsota.

A sua pokedex deverá cumprir com os seguintes requisitos:
1. Ao executar o programa, deverá ser inserido, como argumento, o nome de um pokedex para ser analisado;
    1. Se nenhum argumento for dado, o programa deverá encerrar prematuramente e exibir uma mensagem avisando da ausência do argumento;
    2. Se o pokedex não existir, o programa deverá encerrar prematuramente e exibir uma mensagem avisando que o pokemon não existe (veja: [como verificar o código de status da resposta de uma requisição](https://requests.readthedocs.io/projects/pt/pt-br/latest/user/quickstart.html#codigo-do-status-da-resposta));
2. Caso o pokemon exista, o programa deverá retornar:
   1. O id da pokedex para o pokemon escolhido;
   2. **Todos** os tipos associados ao pokemon.

\
Para mais informações sobre os usos de *requests*, veja o [guia de início rápido](https://requests.readthedocs.io/projects/pt/pt-br/latest/user/quickstart.html) da biblioteca.
> [!TIP]
> <details>
>    <summary>Pistas</summary>
>    <ol>
>        <li>Você pode fazer uma requisição à PokeAPI da seguinte forma:</li>
>
>    `https://pokeapi.co/api/v2/pokemon/nome_do_pokemon`
>  
>    <li>Como o JSON retornado por essa API é muito grande, talvez seja uma boa ideia usar o método <strong>keys()</strong> para analisá-lo, ao invés de printar tudo no terminal</li>
>
> ```py  
> print(resposta.json().keys())
> ```
>
><li>Use <code>resposta.status_code</code> para ver o código de staus da requisição (200: requisição bem sucedida, 404: resposta não encontrada)</li>
> 
><li>Lembre-se que você pode iterar sobre os elemento de uma lista usando o laço for</li>
>    </ol>
> </details>


## Demo
| **pokedex.py**                                                                                            |
| :-------------------------------------------------------------------------------------------------------------- |
| ![demo-code](https://github.com/educodehub/oficina-python/assets/99366724/20101fa1-90c4-476b-98aa-ec3a9439e997) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻


## Antes de Começar
Antes de continuar, é preciso preparar seu workspace.
<ul>
    <li>Em um diretório da sua escolha, crie uma pasta chamada <strong>python-exercicios</strong>.</li>
    <li>Abra a pasta no VSCode, ou usando o atalho <code>Ctrl+K Ctrl+O</code>, ou arrastando-a pasta para a janela do VSCode. É nessa pasta que você alocará todos os programas e arquivos desenvolvidos para todos os exercícios.</li>
    <li>Com a pasta aberta, crie uma nova pasta chamada <strong>pokedex</strong> para armazenar os arquivos desta atividade em específico.</li>
    <li>Digite <code>Ctrl+Shift+"</code> para abrir um terminal do seu prompt de comando e, em seguida, digite <code>cd pokedex</code> para abrir o diretório da atividade.</li>
    <li>No diretório da atividade crie um arquivo chamado <code>pokedex.py</code> e use-o para desenvolver o código da atividade.</li>
</ul>

Feito isso, você vai estar pronto para começar a atividade.


## Como testar
Com o terminal aberto na pasta contendo o programa, é assim que você vai testá-lo:
<ul>
    <li>Execute o script sem <code>nenhum</code> argumento. O programa deverá encerrar e retornar uma mensagem de erro como <code>Insira o nome de um pokemon como argumento</code>.</li>
    <li>Execute o script com <code>mario</code> como argumento. O programa deverá encerrar e retornar uma mensagem de erro como <code>Pokemon não encontrado</code>.</li>
    <li>Execute o script com <code>charmander</code> como argumento. O programa deverá retornar uma mensagem contendo:</li>
  
```
Pokedex id: 4
Tipo: fire
```

<li>Execute o script com <code>snorlax</code> como argumento. O programa deverá retornar uma mensagem contendo:</li>
  
```
Pokedex id: 143
Tipo: normal
```

<li>Execute o script com <code>gengar</code> como argumento. O programa deverá retornar uma mensagem contendo:</li>
  
```
Pokedex id: 94
Tipo: ghost poison
```

<li>Execute o script com <code>nidoking</code> como argumento. O programa deverá retornar uma mensagem contendo:</li>
  
```
Pokedex id: 34
Tipo: poison ground
```
</ul>

Se algum dos testes falhar, tente corrigir o programa antes de enviá-lo. Caso contrario, você *provavlemente* está pronto para seguir para a próxima etapa.


## Como enviar
Acesse o link do [Exercício 02 - Oficina de Python - Aula 3](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/NjgyMjQzNDgzOTk0/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **pokedex.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
