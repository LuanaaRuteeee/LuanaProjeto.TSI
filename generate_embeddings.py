# Importar a biblioteca necessária
import gensim.downloader as api

# Carregar o modelo de Word2Vec pré-treinado
model = api.load("word2vec-google-news-300")  # Modelo com maior capacidade para capturar relações semânticas

# Realizar operações envolvendo palavras relacionadas a animais
resultado = model.most_similar(positive=['dog', 'cat'], negative=['bird'], topn=5)

# Imprimir os resultados
print("Palavras encontradas para a expressão 'dog + cat - bird':")
for palavra, similaridade in resultado:
    print(f"{palavra}: {similaridade}")

# Teste adicional envolvendo outros animais
resultado_extra = model.most_similar(positive=['lion', 'tiger'], negative=['elephant'], topn=5)

print("\nPalavras encontradas para a expressão 'lion + tiger - elephant':")
for palavra, similaridade in resultado_extra:
    print(f"{palavra}: {similaridade}")