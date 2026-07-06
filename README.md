# AI Similarity Explorer

A command-line semantic search application that retrieves the most relevant documents for a user's query using sentence embeddings and cosine similarity.

## Overview

AI Similarity Explorer demonstrates the core retrieval concepts used in modern semantic search systems.

Unlike basic keyword search, the application converts text into numerical embeddings and compares their semantic similarity. This allows it to retrieve relevant documents even when the query and document do not contain the exact same words.

## Features

- Generates document embeddings using a pretrained Sentence Transformer model
- Accepts user queries through the command line
- Generates a query embedding for each search
- Calculates cosine similarity between the query and all documents
- Ranks documents from highest to lowest similarity
- Returns the Top-K most relevant results
- Supports repeated searches using an interactive loop
- Handles empty queries
- Supports an exit command

## How It Works

The application follows this semantic search pipeline:

1. Load the embedding model
2. Convert documents into embedding vectors
3. Accept a user query
4. Convert the query into an embedding vector
5. Compare the query embedding with document embeddings using cosine similarity
6. Rank documents by similarity score
7. Return the Top-K most relevant documents

```text
Documents
    |
    v
Document Embeddings
    |
    v
Stored Embeddings

User Query
    |
    v
Query Embedding
    |
    v
Cosine Similarity
    |
    v
Similarity Scores
    |
    v
Ranking
    |
    v
Top-K Results
```

## Technologies Used

- Python
- Sentence Transformers
- PyTorch
- Hugging Face model ecosystem
- Git
- GitHub

## Embedding Model

The project uses:

`all-MiniLM-L6-v2`

The model converts each text input into a 384-dimensional embedding vector.

## Example

Query:

```text
I want to become a software developer
```

Example results:

```text
Learn web development with JavaScript -> 0.3576
Python programming for beginners -> 0.2832
Machine learning and artificial intelligence -> 0.1315
```

The query does not contain the words `web development`, `JavaScript`, or `Python`, but the system still retrieves programming-related documents based on semantic similarity.

## Project Structure

```text
ai-similarity-explorer/
|
|-- app.py
|-- requirements.txt
|-- .gitignore
|-- README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/charan230105/ai-similarity-explorer.git
```

Move into the project directory:

```bash
cd ai-similarity-explorer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution for the current session, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

## Concepts Demonstrated

This project demonstrates:

- Text embeddings
- Vector representations
- Cosine similarity
- Semantic search
- Query embeddings
- Document embeddings
- Similarity ranking
- Top-K retrieval
- Python loops and control flow
- Interactive command-line input

## What I Learned

While building this project, I learned how text can be converted into embedding vectors and how cosine similarity can be used to compare semantic meaning.

I learned that a semantic search system follows a pipeline similar to:

```text
User Query
    |
    v
Query Embedding
    |
    v
Compare With Document Embeddings
    |
    v
Cosine Similarity Scores
    |
    v
Sort Highest to Lowest
    |
    v
Top-K Results
```

I also learned that the query and documents should be embedded using the same embedding model so their vectors exist in the same vector space and similarity comparisons are meaningful.

This project provides a foundation for learning more advanced retrieval systems, vector databases, and Retrieval-Augmented Generation (RAG).

## Future Improvements

- Allow users to choose the value of K
- Load documents from external text files
- Add similarity score thresholds
- Add a larger document collection
- Add metadata filtering
- Add a vector database
- Build a web interface
- Extend the retrieval pipeline into a RAG application

## Author

Dama Charan