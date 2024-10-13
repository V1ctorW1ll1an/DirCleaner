<p align="center">
  <img src="https://github.com/V1ctorW1ll1an/desktopCleaner/blob/main/assets/img.webp" alt="Desktop File Manager" width="400"/>
</p>
--

# Desktop File Manager

Este projeto foi criado com o propósito de aprender a trabalhar com manipulação de arquivos no Python. Ele permite listar e excluir arquivos e pastas de um diretório especificado, fornecendo uma interface simples para essas operações.

## Propósito

O projeto foi desenvolvido para aprender a utilizar:

- Manipulação de arquivos e diretórios com Python
- Argumentos de linha de comando com `argparse`
- Gerenciamento de exceções e logging
- Integração com ambientes virtuais usando `pyenv` e `venv`

## Requisitos

- **Python 3.12.2** (especificado no `.python-version` via `pyenv`)
- **Bibliotecas padrão do Python** (sem dependências externas)
- **UV Python package and project manager** [link](https://docs.astral.sh/uv/)

## Como Utilizar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/desktopcleaner.git
cd desktopcleaner
```

### 2. Criar o ambiente virtual

O ambiente virtual será criado automaticamente ao rodar o comando `uv run main.py`, mas também pode ser criado manualmente da seguinte forma:

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

- **Linux/MacOS**:

  ```bash
  source venv/bin/activate
  ```

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 4. Executar o programa

Você pode listar ou excluir os arquivos de uma pasta passando o caminho como argumento. Por exemplo, para trabalhar com o desktop:

```bash
uv run main.py --path="<path/desktop>"
```

Para apenas listar os arquivos:

```bash
uv run main.py --path="<path/desktop>" --list
```

O programa perguntará se você deseja confirmar a exclusão antes de realizar qualquer operação destrutiva.

### 5. Logging

Todas as operações realizadas, assim como erros, serão registradas no arquivo `file_operations.log` para fins de monitoramento.

## Como Contribuir

Contribuições são bem-vindas! Siga as etapas abaixo para colaborar:

1. Faça um **fork** do projeto
2. Crie uma **branch** para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. **Commit** suas alterações:
   ```bash
   git commit -m "Adicionei uma nova feature"
   ```
4. Envie para o **branch** principal:
   ```bash
   git push origin minha-feature
   ```
5. Abra um **pull request**

Sinta-se à vontade para abrir **issues** caso encontre bugs ou tenha sugestões de melhorias!

## Licença

Este projeto é aberto para fins educacionais e não possui uma licença formal. Utilize-o para aprender e explorar!

```

Este `README.md` cobre os objetivos de aprendizado do projeto, explica como configurá-lo e rodá-lo, além de incluir instruções claras sobre como contribuir.
```
