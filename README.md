
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/devsuperior/sds1-wmazoni/blob/master/LICENSE) 

# Sobre o projeto

Essa é uma simples api de um de estilo spotify com dados fictício.

# REST API
A api utiliza arquitetura rest.

# Clone

Uma vez que o projeto estiver clonado na sua maquina você pode fazer as configuração das variaveis de ambiente no arquivo `.env.sample`.

```
cp .env.sample .env
```
Com isso o arquivo `.env` foi criado onde la você vai preencher as variaveis de ambiente.
```
Exemplo:
    SECRET_KEY=xxx                  # chave segura do Django(caso não passada é gerada uma randomicamente)
    DEBUG=False                     # debug do django     
    ALLOWED_HOSTS=['*']             # hosts de acesso
    DB_NAME=db_music                # nome do banco de dados
    DB_USER=postgres                # usuario do banco
    DB_PASSWORD=abc123              # senha de acesso ao banco
    DB_HOST=db                      # host do postgres
    DB_PORT=5432                    # porta para acesso ao postgres
    JWT_TIME=30                     # tempo de expiração do token JWT (em minutos)
```
>  **Note**
> : Caso não copie esse arquivo valores padrão serão gerados.


>  **Note**
> : A **SECRET_KEY** é gerada randomicamente para sua segurança.
# Run

Você vai precisar tem o **docker** e **docker-compose instalado** na sua maquina.

Utilizando Docker juntamente com o docker-compose você vai ter o projeto instalado e rodando na porta 8000.

Depois de git clone entre no diretorio raiz do projeto e execute **docker-compose up**.

```
docker-compose up
```

# autenticação JWT
Todos os endpoints são autentificados via JWT.

É preciso passar no **header** da request seu **access_token** por padrão ele fica ativo por 30 minutos mas você pode alterar esse tempo passando o tempo(em minutos) na variavel **JWT_TIME**.

Uma vez com a chave expirada você vai precisar usar o **refresh_token** para gerar uma nova.


# Solicitando tokens de acesso

Uma vez o sistema instalado é criado um usuario admin para uso.

+ email: admin@example.com
+ senha: Admin123!

## Gerando novas chaves:
`POST /api/token/`

```
curl --location --request POST 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "admin@example.com", 
    "password": "Admin123!"
}'
```
### Response
     {
          "access": "access_token",
          "refresh": refresh_token"
     }

## Recuperando chave:
`POST /api/token/refresh/`

```
curl --location --request POST 'http://localhost:8000/api/token/refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "refresh": "refresh_token"
}'
```
### Response
     {
          "access": "access_token",
          "refresh": refresh_token"
     }



# Usuarios

Uma vez o sistema instalado é criado um usuario admin para uso, mas caso queria criar um novo.

+ email: admin@example.com
+ senha: Admin123!

## Criando um usuario:
`POST /users/`

```
curl --location --request POST 'http://127.0.0.1:8000/users/' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"pedro",
    "last_name":"lucas",
    "email":"lucas@gmail.com",
    "password":"Senhadolucas123!"
}'
```
### Response
    {
        "email": "lucas@gmail.com",
        "first_name": "pedro",
        "last_name": "lucas"
    }

## Listando usuarios
`GET /users/`

```
curl --location --request GET 'http://127.0.0.1:8000/users/' \
--header 'Authorization: Bearer ...access_token...'
```

>  **Note**
> : Superuser tem acesso a todos os usuarios, usuarios normal so tem acesso as informações dele mesmo.

### Response
    [
        {
            "id": 1,
            "last_login": null,
            "is_superuser": true,
            "username": "admin@example.com",
            "is_active": true,
            "date_joined": "2022-09-28T19:00:16.731679Z",
            "email": "admin@example.com",
            "first_name": "super",
            "last_name": "admin",
            "playlists": 0,
            "is_staff": true,
            "groups": [],
            "user_permissions": []
        }
    ]


## Editando usuarios

Estão disponiveis os metodos **PUT** para editar todos os campos e o metodo **PATCH** para editar campos especificos, para ambos é necessario passar o id do usuario.

`PUT /users/id` OU `PACTH /users/id`

```
curl --location --request (PUT ou PACTH) 'http://127.0.0.1:8000/users/2' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"mudei",
    "last_name":"mudei",
    "email":"lucas@gmail.com",
    "password":"MUdei123!!"
}'
```

### Response
    {
        "email": "lucas@gmail.com",
        "first_name": "mudei",
        "last_name": "mudei"
    }













# Musicas

## Criando um musica:
Para criação de uma musica é necessario passar o id do artista dela.

`POST /musicas/`

```
curl --location --request POST 'http://127.0.0.1:8000/musicas/' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "uma pela musica",
    "duracao": 1.3,
    "genero": "mbp",
    "artista": 1
}'
```
### Response
    {
        "id": 22,
        "nome": "uma pela musica",
        "duracao": 1.3,
        "genero": "mbp",
        "artista": 1
    }

## Listando musicas
`GET /musicas/`

```
curl --location --request GET 'http://127.0.0.1:8000/musicas/' \
--header 'Authorization: Bearer ...access_token...'
```

### Response
    [
        {
            "id": 22,
            "nome": "uma pela musica",
            "duracao": 1.3,
            "genero": "mbp",
            "artista": 1
        },
    ]


## Editando musica

Estão disponiveis os metodos **PUT** para editar todos os campos e o metodo **PATCH** para editar campos especificos, para ambos é necessario passar o id da musica.

`PUT /musicas/id` OU `PACTH /musicas/id`

```
curl --location --request (PUT ou PACTH) 'http://127.0.0.1:8000/musicas/2' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "Waiting for End",
    "duracao": 6.58,
    "genero": "rock",
    "artista": 7
}'
```

### Response
    {
        "id": 2,
        "nome": "Waiting for End",
        "duracao": 6.58,
        "genero": "rock",
        "artista": 7
    }

## Deletando uma musica

`DELETE /musicas/id`

```
curl --location --request DELETE 'http://127.0.0.1:8000/musicas/1/' \
--header 'Authorization: Bearer ...access_token...'
```







# Artista

## Criando um artista:

`POST /artistas/`

```
curl --location --request POST 'http://127.0.0.1:8000/artistas/' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "Paramore"
}'
```
### Response
    {   
        "id": 2
        "nome": "Paramore"
    }

## Listando artistas
`GET /artistas/`

```
curl --location --request GET 'http://127.0.0.1:8000/artistas/' \
--header 'Authorization: Bearer ...access_token...'
```

### Response
    [
        {
            "id": 2,
            "nome": "Iron Maiden",
            "quantidade_musicas": 5
        },
    ]


## Editando artista

Estão disponiveis os metodos **PUT** para editar todos os campos e o metodo **PATCH** para editar campos especificos, para ambos é necessario passar o id do artista.

`PUT /musicas/id` OU `PACTH /musicas/id`

```
curl --location --request (PUT ou PACTH) 'http://127.0.0.1:8000/musicas/2' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "Henrique E Juliano"
}'
```

### Response
    {
        "nome": "Henrique E Juliano"
    }

## Deletando uma musica

`DELETE /musicas/id`

```
curl --location --request DELETE 'http://127.0.0.1:8000/musicas/1/' \
--header 'Authorization: Bearer ...access_token...'
```











# Play List

## Criando um playlist:

`POST /playlists/`

```
curl --location --request POST 'http://127.0.0.1:8000/playlists/' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nome": "PlayList - 1"
}'
```
### Response
    {
        "id": 1
        "nome": "PlayList - 2"
    }

## Listando playlists
`GET /playlists/`

```
curl --location --request GET 'http://127.0.0.1:8000/playlists/' \
--header 'Authorization: Bearer ...access_token...'
```

### Response
    [
        {
            "id": 1,
            "nome": "PlayList - 1",
            "quantidade_musicas": 0,
            "duracao": 0.0,
            "musica": []
        },
    ]


## Adicionando uma musica

Para adicionar uma musica é preciso passar uma lista com os ids das musicas. 

`POST /playlists/id_playlist/add/`

```
curl --location --request POST 'http://127.0.0.1:8000/playlists/1/add/' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "musica": [2,14,3]
}'
```

### Response
    {
        "musica": [
            2,
            14,
            3
        ]
    }


## Removendo uma musica

Para remover uma musica é preciso passar uma lista com os ids das musicas. 

`POST /playlists/id_playlist/add/`

```
curl --location --request POST 'http://127.0.0.1:8000/playlists/1/remover/' \
--header 'Authorization: Bearer ...access_token...' \
--header 'Content-Type: application/json' \
--data-raw '{
    "musica": [2,14,3]
}'
```

### Response
    {
        "musica": []
    }
