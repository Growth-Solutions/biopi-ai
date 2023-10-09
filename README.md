# BioPi-AI

## Descrição

BioPi-AI é uma aplicação de software que utiliza um modelo de inteligência artificial para classificar a biodiversidade na Região Florística do Cabo, na África do Sul. O projeto faz uso de dados abertos fornecidos pela NASA através do Earthdata. Os sensores utilizados para coleta de dados incluem AVHRR, EOSDIS, EMIT e MODIS.

## Algoritmo

O algoritmo utilizado para treinar o modelo de IA é o U-Net Autoencoder, conhecido por sua eficácia em tarefas de segmentação de imagens.

## Validação

Para validar a eficácia do modelo, utilizamos métricas como a matriz de confusão e a acurácia.

---

## Requisitos

- Python 3.x
- TensorFlow 2.x
- Outras bibliotecas listadas em `requirements.txt`

## Instalação

1. Clone o repositório:

    ```
    git clone https://github.com/Growth-Solutions/biopi-ai.git
    ```

2. Entre no diretório do projeto:

    ```
    cd biopi-ai
    ```

3. Instale as dependências:

    ```
    pip install -r requirements.txt
    ```

## Uso

1. Para treinar o modelo, execute:

    ```
    python train_model.py
    ```

2. Para classificar uma nova área, execute:

    ```
    python classify_area.py --input=input_image.jpg
    ```

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Abra um pull request ou uma issue para discutir o que você gostaria de mudar.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para obter detalhes.
