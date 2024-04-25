# Bem-vindo ao seu primeiro exercício em Python!

Neste exercício, você vai construir, rodar e testar um programa que conta o número de vogais em um texto.

## Problema

Escreva um programa que conte o número de vogais em um texto digitado pelo usuário. O programa deve solicitar ao usuário que insira uma texto e, em seguida, calcular e exibir o número total de vogais na texto. **Desconsidere o uso de acentos**.



| **Como o programa deve ser**                                 |
| :----------------------------------------------------------- |
| ![demo-code](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/654a0fc8-bd29-4b1d-859a-3923ac6c054e) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻

## Instruções para construir e rodar o script

> [!NOTE]
> Antes de continuarmos, você precisa baixar alguns arquivos. No diretório `C:\Temp`, crie uma pasta chamada **exercicios_python**, é nessa pasta que você alocará todos os programas e arquivos de testes desenvolvidos para os exercícios. Com a pasta criada, abra um terminal do seu prompt de comando e navegue até o diretório `C:\Temp\exercicios_python` usando o comando `cd` para isso. [Aqui está um tutorial do CMD](https://medium.com/@adsonrocha/como-abrir-e-navegar-entre-pastas-com-o-prompt-de-comandos-do-windows-10-68750eae8f47). Uma vez no prompt de comando e no diretório correto, digite: `curl -o contar_vogais.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio01/contar_vogais.py`. Isso fará o download do arquivo **contar_vogais.py**, contendo o esqueleto do programa para o exercício proposto. Utilize-o de base para desenvolver seu código. **Não mude o nome do arquivo**.

Ao abrir o arquivo **contar_vogais.py**, você notará que possuímos duas funções definidas, no entanto sem escopo, o qual será implementado por você, aluno, durante a resolução do exercício. Note que a função **contar_vogais** recebe um texto (string) como entrada. Essa função é responsável por deter a lógica por trás da contagem de vogais no texto recebido, seja uma frase ou palavra. Já a função **main()** é a nossa função principal, a qual as demais funções devem ser chamadas através dela. É nela em que você implementa as demais funcionalidades do seu programa.

**Dica:** Na função **contar_vogais()**, implemente somente a lógica de contar a quantidade de vogais para uma determinada entrada. Experimente deixar as demais lógicas e ações do seu programa na função **main()**.

## Instruções para bateria de testes

Para rodar a sua base de testes, precisará seguir alguns passos:

> [!IMPORTANT]
> Antes de tudo precisamos baixar também os arquivos **test_conta_vogal.py** e **pytest.ini**. Novamente, abra um terminal do seu prompt de comando e siga até este diretório **C:\Temp\exercicios_python**. Então, uma vez no diretório correto digite `curl -o test_conta_vogal.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio01/test_conta_vogal.py` para baixar o arquivo **test_conta_vogal.py** e `curl -o pytest.ini https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio01/pytest.ini ` para baixar o arquivo **pytest.ini**. Feito isso, agora você pode prosseguir para os próximos passos.

1. Abra um terminal do seu prompt de comando
2. Se você ainda não possui a biblioteca **Pytest**, vamos instalar. Para isso, [acesse este tutorial para instalar](https://github.com/educodehub/oficina-python/blob/main/aula01/Instala%C3%A7%C3%A3o_pytest.md). Siga todos os seus passos e quando finalizar, volte aqui e conclua sua bateria de testes. Mas caso já possua a biblioteca instalada e configurada, pode pular esse passo.
3. Com a biblioteca instalada e ainda no prompt de comando, vá para o mesmo diretório no qual você incluiu o arquivo **test_conta_vogal.py**. No seu caso `C:\Temp\exercicios_python`.
4. Uma vez no prompt, e no diretório correto, execute `pytest -k test_conta_vogal.py`.

| **Testes que falharam**                                      |
| ------------------------------------------------------------ |
| ![FAILED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/e4a081c3-5893-4e09-a27f-53e04148a443) |

| **Testes que passaram**                                      |
| ------------------------------------------------------------ |
| ![PASSED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/6e67b46a-dd4e-4cc6-ae86-61bdf804d8a7) |

## Como enviar?

Acesse o link do [Exercício 01 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc2MjEyOTU1NjAw/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **contar_vogais.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
