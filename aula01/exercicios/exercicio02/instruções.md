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
> Antes de continuarmos, você precisa baixar alguns arquivos. No exercício anterior você criou uma pasta **exercicios_python** no diretório `C:\Temp`. Abra um terminal do seu prompt de comando e vá para esse diretório (`C:\Temp\exercicios_python`). Uma vez no prompt de comando, digite: `curl -o fatorial.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio02/fatorial.py`. Isso fará o download do arquivo **fatorial.py**, um  arquivo de base para o exercício proposto, para a sua pasta **exercícios_python**. É nessa pasta que todos seus programas e testes devem ficar. **Não mude o nome do arquivo**.

Ao abrir o arquivo **fatorial.py**, você notará que possuímos duas funções definidas, no entanto sem escopo, o qual será implementado por você, aluno, durante a resolução do exercício. Note que a função **calcular_fatorial** é responsável por deter a lógica do cálculo de fatorial. Fique bastante atento também as dicas que demos no tópico **Problema**, pois para entrada de números negativos, é imprescindível que sua função **calcular_fatorial** retorne "O número deve ser não negativo". E como sempre, a função **main()** é a nossa função principal, a qual as demais funções devem ser chamadas através dela.

## Instruções para bateria de testes

Para rodar a sua base de testes, precisará seguir alguns passos:
> [!IMPORTANT]
> Antes de tudo precisamos baixar também os arquivos **test_fatorial.py** e **pytest.ini**. Novamente, abra um terminal do seu prompt de comando e siga até este diretório **C:\Temp\exercicios_python**. Então, uma vez no diretório correto digite `curl -o test_fatorial.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio02/test_fatorial.py` para baixar o arquivo **test_fatorial.py** e `curl -o pytest.ini https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio02/pytest.ini ` para baixar o arquivo **pytest.ini**. Feito isso, agora você pode prosseguir para os próximos passos.

1. Abra um terminal do seu prompt de comando
2. Contamos que você já tenha a biblioteca **Pytest** instalada e configurada no seu computador. Caso não possua, siga este [tutorial](https://github.com/educodehub/oficina-python/blob/7687045011e7058f89afa1a526c5115dc4266b90/Instala%C3%A7%C3%A3o_pytest.md).
3. Ainda no prompt de comando, vá para o mesmo diretório no qual você incluiu o arquivo **test_fatorial.py**. No seu caso `C:\Temp\exercicios_python`.
4. Uma vez no prompt, e no diretório correto, execute `pytest -k test_fatorial.py`.

| **Testes que falharam**                                      |
| ------------------------------------------------------------ |
| ![FAILED test)](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/a82ecfde-f094-4717-96cc-e457bb4a00b3) |

| **Testes que passaram**                                      |
| ------------------------------------------------------------ |
| ![PASSED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/31f9c266-73fd-4ba0-9e43-77fd48f0ebee) |

## Como enviar?

Acesse o link do [Exercício 02 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc2MjEyNzIzMjkx/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **fatorial.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋