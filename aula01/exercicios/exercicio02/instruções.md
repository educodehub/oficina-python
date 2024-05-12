# Bem-vindo ao seu segundo exercício em Python!

Neste exercício, você vai construir, rodar e testar um programa que calcula o fatorial de um número.

## Problema
Escreva um programa que receba um número natural *n* na entrada e imprima o fatorial deste número (**n!**) na saída. 

**Dica**: Lembre-se que o fatorial de 0 vale 1, e que não existe fatorial para números negativos (**n < 0**)!

| **Como o programa deve ser**                                 |
| ------------------------------------------------------------ |
| ![demo-code](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/a71b76fa-296d-438d-90cb-3b59469ce77a) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻

## Instruções para construir e rodar o script

> [!NOTE]
> Antes de continuarmos, você precisa baixar alguns arquivos. <ul><li>Caso ainda não tenha criado, em um diretório da sua escolha, crie uma pasta chamada **exercicios_python** e abra-a no VSCode, é nessa pasta que você alocará todos os programas e arquivos de testes desenvolvidos para todos os exercícios. <li>Com a pasta aberta, crie uma nova pasta chamada **fatorial** para armazenar os arquivos desta atividade em específico. <li>Digite `Ctrl+Shift+"` para abrir um terminal do seu prompt de comando e, em seguida, digite `cd fatorial` para abrir o diretório da atividade. <li>Uma vez no diretório da atividade, digite: `curl -o fatorial.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio02/fatorial.py`, para fazer o download do arquivo **fatorial.py**, que contém o esqueleto do programa para o exercício proposto. Utilize-o de base para desenvolver seu código. **Não mude o nome do arquivo**</ul>

Ao abrir o arquivo **fatorial.py**, você notará que possuímos duas funções definidas, no entanto sem escopo, o qual será implementado por você, aluno, durante a resolução do exercício. Note que a função **calcular_fatorial** é responsável por deter a lógica do cálculo de fatorial. Fique bastante atento também as dicas que demos no tópico **Problema**, pois para entrada de números negativos, é imprescindível que sua função **calcular_fatorial** retorne "O número deve ser não negativo". E como sempre, a função **main()** é a nossa função principal, a qual as demais funções devem ser chamadas através dela.

## Instruções para bateria de testes

Para rodar a sua base de testes, precisará seguir alguns passos:
> [!IMPORTANT]
> Antes de tudo, para os testes funcionarem, precisamos baixar também os arquivos **test_fatorial.py** e **pytest.ini**: <ul><li>Uma vez no diretório da atividade, digite `curl -o test_fatorial.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio02/test_fatorial.py` para baixar o arquivo **test_fatorial.py**. <li>Em seguida, digite `curl -o pytest.ini https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio02/pytest.ini` para baixar o arquivo **pytest.ini**. Feito isso, agora você pode prosseguir para os próximos passos.</ul>

1. Se você ainda não possui a biblioteca **Pytest**, digite `pip install pytest` no terminal para instalá-la, caso isso não funcione, [acesse este tutorial](https://github.com/educodehub/oficina-python/blob/main/aula01/Instala%C3%A7%C3%A3o_pytest.md).
2. Com a biblioteca instalada e ainda no prompt de comando, verifique se você está no diretório da atividade (o mesmo com todos os arquivos desta atividade), caso não esteja, volte aos passos no bloco **Note** e repita-os.
3. Uma vez com o terminal no diretório correto, execute `pytest -k test_fatorial.py`.

| **Testes que falharam**                                      |
| ------------------------------------------------------------ |
| ![FAILED test)](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/a82ecfde-f094-4717-96cc-e457bb4a00b3) |

| **Testes que passaram**                                      |
| ------------------------------------------------------------ |
| ![PASSED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/31f9c266-73fd-4ba0-9e43-77fd48f0ebee) |

## Como enviar?

Acesse o link do [Exercício 02 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc2MjEyNzIzMjkx/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **fatorial.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
