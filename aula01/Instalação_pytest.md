# Instalação da biblioteca pytest
Antes de usar o Pytest, você deve ter instalado na sua máquina a versão mais recente do Python. Para baixar e instalar o Python, acesse a página de [downloads](https://www.python.org/downloads/) no site oficial do Python. Se você já possui o Python no seu computador, confira se a versão que você tem instalada é a 3.5 ou superior. O Pytest só funciona nestas versões do Python. Outra ferramenta que você irá precisar instalar é o pip, para isso, execute este comando no seu prompt:

```bash
python -m ensurepip --default-pip
```
Com o pip instalado, podemos prosseguir para a instalação do pytest. Ainda no seu prompt de comando, digite:

```bash
pip install pytest
```
Pronto, está instalado, mas antes vamos fazer algumas verificações. No seu computador, abra a barra de pesquisa utilizando a tecla do windows. Na barra de pesquisa, digite Variáveis de ambiente e clique na primeira opção que aparecer.

![code2](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/8c91c305-82a7-428f-a43f-a76e341ecf45)

Em seguida, na janela que abrir, clique em Variáveis de Ambiente

![code4](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/c24da465-8394-4d32-89cb-7719e3c85c36)

Após isso irá abrir uma janela com duas opções: **Variáveis de Usuário** e **Variáveis de Sistema**. Em variáveis de sistema, selecione Path e clique em **Editar**

![code3](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/f5d437d6-d4b6-494b-9af2-b65651a40f2b)

Na próxima janela que se abrir, verifique se você possui um caminho como no especificado na imagem abaixo:

![code5](https://github.com/cavalcantgus/oficina-de-python/assets/142106838/de6c7943-508c-4f9b-b38c-3abc6fe563b7)

Caso você já possua, pode sair deste tutorial e prosseguir com sua atividade, caso contrário, vamos configurar uma variável de ambiente:

- No seu prompt de comando, digite `pip show pytest`, isso nos dirá onde sua biblioteca foi instalada.
- A resposta será algo mais ou menos assim: **Location: C:\Users\seu_usuario\AppData\Roaming\Python\PythonXX\site-packages**, onde **seu_usuário** será substituido pelo seu nome de usuário no seu sistema, e **PythonXX** será substituido pela pasta Python com a versão correspondente.
- Nessa pasta **PythonXX**, dentro dela terá uma outra pasta, **Scripts**, abra-a e copie o caminho dela.
- O caminho todo será algo como: **C:\Users\seu_usuario\AppData\Roaming\Python\PythonXX\Scripts**.
- Na janela de edição das variáveis de ambiente, a imagem acima que vimos, clique em um espaço vazio e em **Novo**.
- Em seguida, cole o caminho que você copiou.
- Aplique todas as alerações clicando em **Ok** nas três janelas que apareceram e prontinho, sua biblioteca pytest está instalada e configurada.

**Você já pode voltar para o tutorial de instruções da sua atividade!!**



