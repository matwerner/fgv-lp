# Projeto Similaridade de Documentos

Este projeto tem como objetivo demonstrar o desenvolvimento de um projeto em Python, focando na organização do código, criação de testes automatizados e documentação. Para isso, foi criado um sistema de busca de documentos baseado em palavras-chave e similaridade de texto.

**Aviso**:
Este projeto é apenas um exemplo e, portanto, não inclui documentação completa, tratamento de exceções ou testes unitários abrangentes.

## Estrutura do projeto

O projeto está organizado da seguinte forma:
    
```markdown
projeto_similaridade_de_documentos/

├── data/
│   └── wikipedia_good_articles_video_games.txt
├── src/
│   ├── main.py    
│   ├── data_loader.py
│   ├── search.py
|   ├── text.py
|   └── metrics.py
├── tests/
│   ├── test_data_loader.py
│   ├── test_search.py
|   ├── test_text.py
|   └── test_metrics.py
├── README.md
├── requirements.txt
```

## Como executar o projeto

1. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

2. Decompacte o arquivo `wikipedia_good_articles_video_games.zip` na pasta `data`:

3. Execute o script `main.py`:
    ```bash
    cd src/
    python3 main.py
    ```

## Como testar o projeto

1. Execute o script de testes do diretório raiz:
    ```bash
    python3 -m unittest
    ```