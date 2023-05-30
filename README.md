# Integrantes :            
##  -> [Gabriela Villani Moreira  - Ra:181884](ra181884@ucdb.br)
##  -> [Lucas Souza Frade         - Ra:181370](ra181370@ucdb.br)
#

# Funcionalidade do programa:
## O software recebe como entrada uma sequência de DNA e busca dentro desta sequência todas as ocorrências da subsequência inserida, utilizando o método básico de comparação e a busca de padrões pelo algoritmo KMP. 
## O software mostra a posição de cada subsequência e também a quantidade de comparações necessárias usando o método básico e o KMP, também possui uma interface gráfica mostrando as posições do autômato percorrido correspondente ao KMP.

# Inicializando programa:

## Primeiro instalar dependências:

## Não é necessário criar um ambiente, até porque é somente uma dependência, caso queira, fique a vontade
## A única dependência é para auxiliar na interface gráfica (GUIs)
```sh
    $ pip install pillow
```

## Depois já pode executar o programa, verifique antes se está na pasta correta, em seguida de:
```sh
    $ python3 kmp_principal.py
``` 

## Pode ocorrer de haver erro de não achar o modulo tkinter, se for o caso use esse codigo:
```sh
    $ sudo apt-get install python3-tk    
```
# Gabriela Villani Moreira:
* Criou a base dos 2 arquivos (kmp_codigo, kmp_principal)
* Criou a base GUIs do arquivo (kmp_principal)
* Auxiliou na criação das funções dos botões
* Corrigiu Bugs do arquivo (kmp_principal)

# Lucas Souza Frade:
*  Auxiliou na refatoração da função principal e da auxiliar do arquivo (kmp_codigo) 
* Criou parte dos componentes do formulario principal (kmp_principal)
* Criou funções dos eventos dos botões (kmp_principal)
* Auxiliou na organinação dos componentes no formulário

# Memorial do projeto:
* [Algoritmo KMP para busca de substring](https://www.ime.usp.br/~pf/estruturas-de-dados/aulas/kmp.html?authuser=0),este link foi utilizado como base para o desenvolvimento de funções auxiliares.

* [Arquivo fornecido pelo professor](https://drive.google.com/file/d/17ddQdnH-0BOE7digb3OEWITXlBnblSt6/view), este arquivo foi necessário para o raciocínio do projeto.

* [Chat](https://openai.com/blog/chatgpt),este recurso foi ultilizado para resolver bugs e duvidas durante o projeto. 

* A estimativa de tempo gasto neste projeto foi em torno de 2 meses de desenvolvimento, contendo pausas, e refatorações.
### Para mais informações abrir código fonte.