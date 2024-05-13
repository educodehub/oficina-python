# Bem-vindo ao seu primeiro exercício em Python!

Neste exercício, você vai construir, rodar e testar um programa que conta o número de vogais em um texto.

## Problema

Escreva um programa que conte o número de vogais em um texto digitado pelo usuário. O programa deve solicitar ao usuário que insira uma texto e, em seguida, calcular e exibir o número total de vogais no texto. **Desconsidere o uso de acentos**.

<details>
    <summary>Pistas</summary>
    <ol>
        <li>Lembre-se do uso do operador <strong>in</strong> em estruturas condicionais</li>
        <li>Lembre-se que o laço <strong>for</strong> pode iterar sobre uma string
    </ol>
</details>



| **Como o programa deve ser**                                 |
| :----------------------------------------------------------- |
| ![demo-code](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/654a0fc8-bd29-4b1d-859a-3923ac6c054e) |

`# É isso, mãos na massa! É hora de codar!` 👨‍💻

## Instruções para construir e rodar o script

> [!NOTE]
> Antes de continuarmos, você precisa baixar alguns arquivos. <ul><li>Em um diretório da sua escolha, crie uma pasta chamada **exercicios_python** e abra-a no VSCode, é nessa pasta que você alocará todos os programas e arquivos de testes desenvolvidos para todos os exercícios. <li>Com a pasta aberta, crie uma nova pasta chamada **vogais** para armazenar os arquivos desta atividade em específico. <li>Digite `Ctrl+Shift+"` para abrir um terminal do seu prompt de comando e, em seguida, digite `cd vogais` para abrir o diretório da atividade. <li>Uma vez no diretório da atividade, digite: `curl -o contar_vogais.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio01/contar_vogais.py`, para fazer o download do arquivo **contar_vogais.py**, que contém o esqueleto do programa para o exercício proposto. Utilize-o de base para desenvolver seu código. **Não mude o nome do arquivo**.</ul>


Ao abrir o arquivo **contar_vogais.py**, você notará que possuímos duas funções definidas, no entanto sem escopo, o qual será implementado por você, aluno, durante a resolução do exercício. Note que a função **contar_vogais()** recebe um argumento **texto** (string) como entrada. Essa função é responsável por deter a lógica por trás da contagem de vogais no texto recebido, seja uma frase ou palavra. Já a função **main()** é a nossa função principal, a qual deve receber a entrada do usuário e chamar as demais funções, além de exibir um resultado.

**Dica:** Na função **contar_vogais()**, implemente somente a lógica de contar a quantidade de vogais para uma determinada entrada. Experimente deixar as demais lógicas e ações do seu programa na função **main()**.

## Instruções para bateria de testes

Para rodar a sua base de testes, precisará seguir alguns passos:
> [!IMPORTANT]
> Antes de tudo, para os testes funcionarem, precisamos baixar também os arquivos **test_conta_vogal.py** e **pytest.ini**: <ul><li>Uma vez no diretório da atividade, digite `curl -o test_conta_vogal.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio01/test_conta_vogal.py` para baixar o arquivo **test_conta_vogal.py**. <li>Em seguida, digite `curl -o pytest.ini https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio01/pytest.ini` para baixar o arquivo **pytest.ini**. Feito isso, agora você pode prosseguir para os próximos passos.</ul>

1. Se você ainda não possui a biblioteca **Pytest**, digite `pip install pytest` no terminal para instalá-la, caso isso não funcione, [acesse este tutorial](https://github.com/educodehub/oficina-python/blob/main/aula01/Instala%C3%A7%C3%A3o_pytest.md).
2. Com a biblioteca instalada e ainda no prompt de comando, verifique se você está no diretório da atividade (o mesmo com todos os arquivos desta atividade), caso não esteja, volte aos passos no bloco **Note** e repita-os.
3. Uma vez com o terminal no diretório correto, execute `pytest -k test_conta_vogal.py`.

| **Testes que falharam**                                      |
| ------------------------------------------------------------ |
| ![FAILED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/e4a081c3-5893-4e09-a27f-53e04148a443) |

| **Testes que passaram**                                      |
| ------------------------------------------------------------ |
| ![PASSED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/6e67b46a-dd4e-4cc6-ae86-61bdf804d8a7) |

## Como enviar?

Acesse o link do [Exercício 01 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc2MjEyOTU1NjAw/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **contar_vogais.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
