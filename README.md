# Desafio portal Lacrei

Este repositório se trata de um desafio de back end onde foi solicitado a criação de uma API de tarefas (listagem e criação de novas tarefas) feito com Django Rest Framework. Cujo objetivo é o ingresso ao trabalho voluntário no portal Lacrei.
***


## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

<ul>
    <li>Versão do python utilizada: 3.10.7</li>
    <li>Versão do django: 4.1.2</li>
    <li>Versão do django rest framework: 3.14.0</li>
</ul>

#### 1 - Passo: Clone
Realize um clone do projeto em seu computador

```
git clone https://github.com/walexhenrique/lacrei-teste.git
```

#### 2 - Passo: Ambiente virtual
Crie um ambiente virtual na pasta <b>raiz</b> do projeto. No seu terminal use:

Comando para a criação do ambiente virtual no Windows:
```
python -m venv venv
```

Comando para a criação do ambiente virtual no Linux:
```
python3 -m venv venv
```

#### 3 - Passo: Ativação do ambiente virtual
Agora você precisa ativar o ambiente virtual para a posterior instalação das dependências do projeto.

Na pasta raiz do projeto, onde você criou o seu ambiente virtual anteriormente. Use:

Comando para a ativação do ambiente virtual no Windows:
```
.\venv\Scripts\activate
```

Comando para a ativação do ambiente virtual no Linux:
```
source venv/bin/activate
```
Se tudo estiver ocorrido bem, terá (venv) em seu <b>terminal!</b>

#### 4 - Passo: Instalação de depedências
É preciso instalar as depedências do projeto para o funcionamento correto. Com o seu ambiente virtual <b>ativo</b> use o comando no seu terminal:

```
pip install -r requirements.txt
```

#### 5 - Passo: Variáveis de ambiente
Para a correta execução do projeto é necessário a configuração das variáveis de ambiente.

* Renomeie o arquivo .env-example para .env

Dentro do arquivo .env (já renomeado), coloque sua PRIMARY KEY do projeto.
```
# /.env

# Django secret key
SECRET_KEY = 'COLOQUE SUA SECRET-KEY AQUI'
```

#### 6 - Passo: Realize as migrações
Para o correto funcionamento do projeto é preciso que seja feito as migrações do banco de dados.

No seu terminal digite:
Windows:
```
python manage.py migrate
```

Linux:
```
python3 manage.py migrate
```

#### 7 - Passo: Executar o projeto
Comando para a execução do projeto no windows:

```
python manage.py runserver
```

Comando para a execução do projeto no linux:

```
python3 manage.py runserver
```

## ⚙️ Executando os testes
Foram realizados diversos testes na API para garantir a qualidade e o funcionamento.

Comando para a realização dos testes unitários. 
No windows:
```
python manage.py test
```

No linux:
```
python3 manage.py test
```

Todos os testes foram documentados e comentados para o melhor entendimento.

## 📦 Mais informações

O desafio pediu a criação das funcionalidades:
* Criar tarefa 
* listar tarefas. 

Além dessas funcionalidades, adicionei:
* Detalhar uma tarefa
* Editar uma tarefa 
* Excluir uma tarefa

No teste não foi pedido que o código fosse criado em inglês, então optei por escrever tudo em português.

## Documentação da API

* #### Listagem de todas as tarefas cadastradas anteriormente
    ```
    GET /api/v1/tarefas/
    ```
    Exemplo de resposta:
    ```json
    Response: 200
    [
        {
            "id": 1,
            "titulo": "Acordar as 6h da manhã",
            "descricao": "Comprar um pão ao acordar",
            "data_e_hora_de_criacao": "2022-10-16T03:45:54.596234Z",
            "ultima_modificacao": "2022-10-16T03:47:47.827224Z",
            "finalizado": true
        },
        {
            "id": 2,
            "titulo": "Fazer um bolo",
            "descricao": "primeiro preparar o arroz",
            "data_e_hora_de_criacao": "2022-10-16T04:20:42.525372Z",
            "ultima_modificacao": "2022-10-16T18:38:32.378482Z",
            "finalizado": true
        }
    ]
    ```

    Caso não possua nenhuma tarefa cadastrada anteriormente, a resposta se parecerá com o seguinte:
    
    ```json
    Response: 200
    []
    ```

* ##### Criação de novas tarefas
    ```
    POST /api/v1/tarefas/
    ```
    Exemplo de cadastro de nova tarefa:
    ```json
    {
		"titulo": "Acordar as 6h da manhã",
		"descricao": "Teste"
    }
    ```

    Exemplo de resposta:
    ```json
    Response: 201
    {
        "id": 1,
        "titulo": "Acordar as 6h da manhã",
        "descricao": "Teste",
        "data_e_hora_de_criacao": "2022-10-16T21:42:24.680799Z",
        "ultima_modificacao": "2022-10-16T21:42:24.680799Z",
        "finalizado": false
    }
    ```
    Possíveis erros que podem ocorrer:
    * titulo ou descricao não serem enviados ao criar uma nova tarefa. Retornará o status response: 400

### Funcionalidades extras adicionadas:
* #### Pegar detalhes de apenas uma tarefa
    ```
    GET /api/v1/tarefas/<id>/
    ```

    Exemplo de resposta:
    ```json
    Response: 200
    {
        "id": 1,
        "titulo": "Acordar as 6h da manhã",
        "descricao": "Comprar um pão ao acordar",
        "data_e_hora_de_criacao": "2022-10-16T03:45:54.596234Z",
        "ultima_modificacao": "2022-10-16T03:47:47.827224Z",
        "finalizado": true
    }
    ```
    Possível erro:
    * Não encontrar a tarefa com o determinado id. Retornará o status response: 404
    ```json
    {
	    "detail": "Não encontrado."
    }  
    ```
* #### Atualizar uma tarefa
    ```
    PATCH /api/v1/tarefas/<id>/
    ```
    Exemplo de atualização de uma tarefa:
    ```json
    {   
        "titulo": "Fazer uma paçoca",
        "finalizado": true
    }
    ```

    Exemplo de resposta:
    ```json
    Response: 200
    {
        "id": 1,
        "titulo": "Fazer uma paçoca",
        "descricao": "Comprar um pão ao acordar",
        "data_e_hora_de_criacao": "2022-10-16T04:23:24.144857Z",
        "ultima_modificacao": "2022-10-16T22:00:56.182265Z",
        "finalizado": true
    }
    ```
    Possível erro:
    * Não encontrar a tarefa com o determinado id. Retornará o status response: 404
    ```json
    {
	    "detail": "Não encontrado."
    }  
    ```
* #### Apagar uma tarefa
    ```
    DELETE /api/v1/tarefas/<id>/
    ```

    Exemplo de resposta:
    ```json
    Response: 204
    NO CONTENT
    ```
    Possível erro:
    * Não encontrar a tarefa com o determinado id. Retornará o status response: 404
    ```json
    {
	    "detail": "Não encontrado."
    }  
    ```

## 🛠️ Construído com

* [Django](https://www.djangoproject.com/) - O framework web usado
* [Django rest framework](https://www.django-rest-framework.org/) - Para a criação da api.

## 📌 Versão

A api está na versão 1.0

## ✒️ Autor

* **Desenvolvedor** [Walex](https://github.com/walexhenrique)



## 🎁 Considerações

* Foi divertido construir esse projeto, pude aprender diversas coisas relacionadas ao django rest framework e a testes com o mesmo.

---

