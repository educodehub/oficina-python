[Voltar](https://github.com/educodehub/oficina-python/blob/main/aula01/instru%C3%A7%C3%B5es.md)
# Bem-vindo ao seu terceiro exercício em Python!

Neste exercício, você vai construir, rodar e testar um programa que avalia as notas dos alunos de uma escola.

## Problema
Você foi chamado para desenvolver um sistema de avaliação de notas dos alunos de uma escola. Ele deve fornecer a média do aluno e sua situação na média escolar (aprovado ou reprovado). Você foi ainda informado que essa escola utiliza um padrão de avaliação por **quatro** notas.

Seu programa deve começar pedindo ao usuário para inserir as notas do aluno. Lembre-se de que notas e médias são valores reais, ou seja, números com casas decimais. Trabalhe com valores do tipo `float` em todo o programa. Em seguida, o programa calculará a média da soma de todas as notas, utilizando a função **calcular_media**. Após o cálculo da média, o programa verificará o status de aprovação do aluno com o uso da função **verificar_aprovacao**. A lógica por trás da implementação fica por sua conta. Lembre-se de que são considerados aprovados os alunos com média igual ou superior a 7, e os demais casos serão considerados reprovados.

| **Como o programa deve ser** |
|------------------------------|
![demo-code](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/07931736-293e-40d5-a6a8-7ce554ba6081)

`# É isso, mãos na massa! É hora de codar!` 👨‍💻

## Instruções para construir e rodar o script
> [!NOTE]
> Antes de continuarmos, você precisa baixar alguns arquivos. <ul><li>Caso ainda não tenha criado, em um diretório da sua escolha, crie uma pasta chamada **exercicios_python** e abra-a no VSCode, é nessa pasta que você alocará todos os programas e arquivos de testes desenvolvidos para todos os exercícios. <li>Com a pasta aberta, crie uma nova pasta chamada **media** para armazenar os arquivos desta atividade em específico. <li>Digite `Ctrl+Shift+"` para abrir um novo terminal do seu prompt de comando e, em seguida, digite `cd media` para abrir o diretório da atividade. <li>Uma vez no diretório da atividade, digite: `curl -o media.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio03/media.py`, para fazer o download do arquivo **media.py**, que contém o esqueleto do programa para o exercício proposto. Utilize-o de base para desenvolver seu código. **Não mude o nome do arquivo**</ul>

Ao abrir o arquivo **media.py**, você notará que possuímos 3 funções definidas, no entanto, sem escopo, o qual será implementado por você, aluno, durante a resolução deste exercício. Essas funções serão as responsáveis por deter toda a lógica de programação da sua calculadora de média. Dentre essas funções, a **main()** é o que chamamos de função principal e as demais funções (**calcular_media()** e **verificar_aprovacao()**) devem ser chamadas através dela.

## Instruções para bateria de testes

> [!IMPORTANT]
> Antes de tudo, para os testes funcionarem, precisamos baixar também os arquivos **test_media.py** e **pytest.ini**: <ul><li>Uma vez no diretório da atividade, digite `curl -o test_media.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio03/test_media.py` para baixar o arquivo **test_media.py**. <li>Em seguida, digite `curl -o pytest.ini https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio03/pytest.ini` para baixar o arquivo **pytest.ini**. Feito isso, agora você pode prosseguir para os próximos passos.</ul>

1. Se você ainda não possui a biblioteca **Pytest**, digite `pip install pytest` no terminal para instalá-la, caso isso não funcione, [acesse este tutorial](https://github.com/educodehub/oficina-python/blob/main/aula01/Instala%C3%A7%C3%A3o_pytest.md).
2. Com a biblioteca instalada e ainda no prompt de comando, verifique se você está no diretório da atividade (o mesmo com todos os arquivos desta atividade), caso não esteja, volte aos passos no bloco **Note** e repita-os.
3. Uma vez com o terminal no diretório correto, execute `pytest -k test_fatorial.py`.

| **Testes que falharam** |
|-------------------------|
![FAILED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/dee2cb0d-4eee-4c1f-b9ab-f85004138294)


| **Testes que passaram** |
|-------------------------|
![PASSED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/b065be28-7ae9-4162-b139-f8b4b963c25e)

## Como enviar?

Acesse o link do [Exercício 03 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc1OTgxMzQ2MTQy/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **media.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
