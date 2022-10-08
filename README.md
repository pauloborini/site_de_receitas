# Criando um site de Receitas - Primeiro Projeto Python-Django

Projeto iniciado no curso de Django da Alura, desenvolvido em Python3 com framework Django.

<div align="center">
[screen-capture.webm](https://user-images.githubusercontent.com/86570695/194682270-94d11c20-6d05-4d5a-b63b-53fc94fc33fc.webm)
</div>

## Semana 1

Enquanto estudo e assisto as aulas, coloco alguns pontos que aprendi e estou utilizando nesse projeto no Readme.


- Aprendi a utilizar o módulo venv, que fornece suporte para a criação de ambientes virtuais leves com seus próprios diretórios, isolados dos diretórios do sistema, criando suas próprias dependências por projeto.

- Utilizei o pip para instalar o Django e vincular o Postgre SQL no projeto.

- Iniciei com o comando django-admin start project alurareceita e subi o servidor com o comando python manage.py runserver.

- Instalei primeiramente um app, chamado receitas, adicionei os parâmetros necessários para ele ser utilizado nos arquivos localizados em:
alurareceita.settings = INSTALLED_APPS, alurareceitas.urls.

- Configurações e comandos utilizando um template cedido pela Alura, refatorando e utilizando block content e partials para melhorar o código do site.

- Configurações de models para as receitas e integração com PostgreSQL.

- Configurações para facilitar criação e edição das receitas na parte de administrador do site.

- Criação de novo app, chamado pessoas, para diferenciar quem está contribuindo com o crescimento do db.

- Implementado alteração de miniaturas das receitas e fotos.

- Implementado sistema de pesquisa por palavra.

- Testes com permissões de usuários na parte de administração do site.

- Refatoração de código.

- Implementado novo app de usuários, utilizando autenticação com o db, para criação e manutenção de usuários.

- Adicionadas páginas de formulários de login e cadastro.

- Adicionado novas páginas de dashboard (utilizada quando usuário está logado no site).

- Nova função de Criar receita, com formulário completo, com campos específicos para tal.

- Adicionei mensagens de sucesso e erro através do messages framework do Django e mais algumas validações de segurança.

Obs.: Lembrando que as receitas criadas por usuários serão analisadas antes de serem publicadas.

## Semana 2

- Finalizado o CRUD de receitas, possibilitando a atualização das receitas, como também deletá-las.

- Criado uma paginação para tornar a experiência do usuário melhor e não sobrecarregar a index e a dashboard do usuário.

- Organizei algumas pastas e refatorei algumas funções para melhorar a legibilidade do código, adicionada algumas docstrings nos views dos apps.



