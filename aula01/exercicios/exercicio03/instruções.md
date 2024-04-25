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
> Antes de continuarmos, você precisa baixar alguns arquivos. No seu primeiro exercício você criou uma pasta **exercicios_python** no diretório `C:\Temp`. Abra um terminal do seu prompt de comando e vá para esse diretório (`C:\Temp\exercicios_python`). Uma vez no prompt de comando, digite: `curl -o media.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio03/media.py`. Isso fará o download do arquivo **media.py**, um arquivo base que contém o esqueleto do programa que está sendo proposto. É nele que você implementará todo o seu código. **Não mude o nome do arquivo**. 

Ao abrir o arquivo **media.py**, você notará que possuímos 3 funções definidas, no entanto, sem escopo, o qual será implementado por você, aluno, durante a resolução deste exercício. Essas funções serão as responsáveis por deter toda a lógica de programação da sua calculadora de média. Dentre essas funções, a **main()** é o que chamamos de função principal e as demais funções (**calcular_media** e **verificar_aprovacao**) devem ser chamadas através dela.

## Instruções para bateria de testes

Para rodar a sua base de testes, precisará seguir alguns passos:
> [!IMPORTANT]
> Antes de tudo precisamos baixar também os arquivos **test_media.py** e **pytest.ini**. Novamente, abra um terminal do seu prompt de comando e siga até este diretório **C:\Temp\exercicios_python**. Então, uma vez no diretório correto digite `curl -o test_media.py https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio03/test_media.py` para baixar o arquivo **test_media.py** e `curl -o pytest.ini https://raw.githubusercontent.com/educodehub/oficina-python/main/aula01/exercicios/exercicio03/pytest.ini ` para baixar o arquivo **pytest.ini**. Feito isso, agora você pode prosseguir para os próximos passos.

1. Abra um terminal do seu prompt de comando.
2. Contamos que você já tenha a biblioteca **Pytest** instalada e configurada no seu computador. Caso não possua, siga este [tutorial](https://github.com/educodehub/oficina-python/blob/7687045011e7058f89afa1a526c5115dc4266b90/Instala%C3%A7%C3%A3o_pytest.md).
3. Ainda no prompt de comando, vá para o mesmo diretório no qual você incluiu o arquivo **test_media.py**. No seu caso `C:\Temp\exercicios_python`.
4. Uma vez no prompt, e no diretório correto, execute `pytest -k test_media.py`.

| **Testes que falharam** |
|-------------------------|
![FAILED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/dee2cb0d-4eee-4c1f-b9ab-f85004138294)


| **Testes que passaram** |
|-------------------------|
![PASSED test](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/b065be28-7ae9-4162-b139-f8b4b963c25e)

## Como enviar?

Acesse o link do [Exercício 03 - Oficina de Python - Aula 1](https://classroom.google.com/c/Njc1ODQ0MDM4MTU5/a/Njc1OTgxMzQ2MTQy/details) e você será redirecionado para a sua atividade no Classroom. Lá conterão as instruções para que submeta seu trabalho **media.py**. 

**Boa sorte!!! Nos vemos no próximo exercício** 👋
