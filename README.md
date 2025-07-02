# HF-Chroma

## Descripción

HF-Chroma es un proyecto que combina el poder de los modelos de embeddings de Hugging Face con ChromaDB, una base de datos vectorial de código abierto. Esta aplicación permite realizar búsquedas semánticas en un conjunto de documentos utilizando representaciones vectoriales (embeddings) del texto.

## Características

- Utiliza el modelo `all-MiniLM-L6-v2` de Sentence Transformers para generar embeddings
- Almacena documentos y sus embeddings en ChromaDB
- Permite realizar consultas semánticas para encontrar documentos similares
- Responde preguntas basadas en el contenido de los documentos

## Requisitos previos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/SantiagoSuarezL/HF-Chroma.git
   cd HF-Chroma
   ```

2. Crea un entorno virtual (recomendado):
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate
   
   # En macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Uso

Ejecuta el script principal:

```bash
python main.py
```

El programa te pedirá que ingreses una pregunta relacionada con IA o ChromaDB. Basándose en los documentos almacenados, el sistema encontrará y mostrará la respuesta más relevante.

### Ejemplo de uso

```
Ask a question about AI or Chroma: ¿Qué es ChromaDB?

Respuesta aproximada encontrada: 
ChromaDB es una base de datos vectorial de código abierto ideal para trabajar con IA.
```
