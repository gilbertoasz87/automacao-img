import os
import shutil
import re
from PIL import Image 

# Permite imagens maiores (ajuste conforme necessário)
Image.MAX_IMAGE_PIXELS = None

# Pasta onde estão as imagens
PASTA_IMAGENS = "imagens-produtos"
PASTA_IMAGENS_OUT = "out-imagens-produtos"

# Caminho absoluto (ajuste se necessário)
CAMINHO = os.path.join(os.getcwd(), PASTA_IMAGENS)
CAMINHO_OUT = os.path.join(os.getcwd(), PASTA_IMAGENS_OUT)

# Regex para extrair códigos e tipo de imagem
padrao = re.compile(r"([\d; ]+)\s\((\d)\)\.jpg", re.IGNORECASE)

for nome_arquivo in os.listdir(CAMINHO):
    if nome_arquivo.lower().endswith(".jpg"):
        resultado = padrao.match(nome_arquivo)
        if resultado:
            codigos = resultado.group(1).replace(" ", "").split(";")
            tipo = resultado.group(2)
            sufixo = "-img" if tipo == "1" else "-flyer" if tipo == "2" else ""
            for codigo in codigos:
                if codigo:
                    novo_nome = f"{codigo}{sufixo}.jpg"
                    origem = os.path.join(CAMINHO, nome_arquivo)
                    destino = os.path.join(CAMINHO_OUT, novo_nome)
                    #shutil.copy2(origem, destino)
                    # Reduz o tamanho do arquivo mantendo boa qualidade
                    with Image.open(origem) as img:
                        img.save(destino, "JPEG", quality=85, optimize=True)
                    print(f"Arquivo criado: {novo_nome}")

print("Processo finalizado.")