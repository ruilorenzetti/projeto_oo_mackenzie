# projeto_oo_mackenzie


## 1. Instalação do Git no Windows

### Passo 1: Baixar o Git
1. Acesse o [site oficial do Git](https://git-scm.com/).
2. Clique em "Download" para baixar a versão mais recente do Git para Windows.

### Passo 2: Instalar o Git
1. Execute o instalador baixado.
2. Siga as instruções do instalador:
   - **Selecionar componentes**: Deixe as opções padrão selecionadas, a menos que você tenha necessidades específicas.
   - **Configurações do terminal**: Recomendo usar o "Git Bash" como terminal padrão.
   - **Configurações de linha de comando**: Selecione "Use Git from the Windows Command Prompt" para facilitar o uso do Git em diferentes terminais.
   - **Configurações de CRLF**: Se você não tiver uma preferência específica, use a opção recomendada para converter final de linha (Checkout Windows-style, commit Unix-style).

### Passo 3: Verificar a Instalação
1. Abra o Git Bash ou o Prompt de Comando.
2. Digite `git --version` para verificar se o Git foi instalado corretamente.

## 2. Clonagem de Repositórios

### Passo 1: Obter a URL do Repositório
1. Vá até a página do repositório no GitHub (ou outra plataforma Git).
2. Clique no botão "Code" e copie a URL do repositório.

### Passo 2: Clonar o Repositório
1. Abra o Git Bash.
2. Navegue até o diretório onde você deseja clonar o repositório:
   ```sh
   cd caminho/para/o/diretorio
   ```
3. Execute o comando de clonagem:
   ```sh
   git clone URL_DO_REPOSITORIO
   ```
   Substitua `URL_DO_REPOSITORIO` pela URL que você copiou.

## 3. Criação de Branches

### Passo 1: Criar uma Nova Branch
1. No Git Bash, navegue até o diretório do seu repositório clonado.
2. Crie uma nova branch e mude para ela:
   ```sh
   git checkout -b nome-da-branch
   ```

### Passo 2: Verificar Branch Atual
1. Para verificar em qual branch você está, use:
   ```sh
   git branch
   ```

## 4. Pull Requests

### Passo 1: Fazer Commit das Mudanças
1. Adicione os arquivos alterados ao commit:
   ```sh
   git add .
   ```
2. Faça o commit das suas mudanças:
   ```sh
   git commit -m "Mensagem do commit"
   ```

### Passo 2: Enviar a Branch para o Repositório Remoto
1. Envie sua branch para o repositório remoto:
   ```sh
   git push origin nome-da-branch
   ```

### Passo 3: Criar um Pull Request
1. Vá até a página do repositório no GitHub.
2. Clique no botão "Compare & pull request" que aparece depois de fazer o push.
3. Preencha os detalhes do pull request e clique em "Create pull request".

## Resumo dos Comandos

- **Instalar Git**: `git --version`
- **Clonar Repositório**: `git clone URL_DO_REPOSITORIO`
- **Criar Branch**: `git checkout -b nome-da-branch`
- **Verificar Branch**: `git branch`
- **Adicionar Alterações**: `git add .`
- **Fazer Commit**: `git commit -m "Mensagem do commit"`
- **Enviar Branch**: `git push origin nome-da-branch`

