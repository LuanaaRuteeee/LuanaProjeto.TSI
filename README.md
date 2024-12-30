# LuanaProjeto.TSI
Projeto para gerar embeddings de texto usando o Ollama localmente.
# word-embeddings-experiment
Experimentos com embeddings de palavras usando Word2Vec.
Este projeto explora o uso de **Word Embeddings** para realizar operações de álgebra semântica em modelos de linguagem. O script principal `generate_embeddings.py` permite realizar expressões como `dog + cat - bird` e obter palavras relacionadas com base nas embeddings.

## O código usa o modelo Word2Vec para realizar operações de álgebra semântica, somando e subtraindo palavras. Ele encontra as palavras mais semelhantes à expressão dog + cat - bird e lion + tiger - elephant, e imprime as palavras e suas similaridades

## Requisitos
Antes de rodar este projeto, é necessário instalar:
Python 3.x
Ollama

## modelo de linguagem do Ollama que gera embeddings
llama3.2

## Biblioteca Python:
 gensim
## instanlando a biblioteca
pip install gensim ollama

## Observando se o Ollama está instalado correntamente
ollama --version

## Instalando o Modelo llama3.2
ollama run llama3.2 

## Mostrando meu repositório e clonando: 
git clone https://github.com/LuanaaRuteeee/LuanaProjeto.TSI.git

## Resultados

## Palavras encontradas para a expressão dog + cat - bird:

Shih_Tzu: 0.7070850133895874
dogs: 0.7015834450721741
puppy: 0.7007051110267639
golden_retriever: 0.69303959608078
pooch: 0.6847290992736816

## Palavras encontradas para a expressão lion + tiger - elephant:

lions: 0.5125596523284912
tigers: 0.47970205545425415
Siberian_tiger: 0.42824509739875793
wolf: 0.41840705275535583
leopards_elephants: 0.413523048162460



