from sentence_transformers import SentenceTransformer, util


# Load model from local cache
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    local_files_only=True
)


# Documents
documents = [
    "Python programming for beginners",
    "Machine learning and artificial intelligence",
    "How to cook chicken biryani",
    "Best exercises for building muscle",
    "Learn web development with JavaScript"
]


# Generate document embeddings once
document_embeddings = model.encode(documents)

top_k = 3


# Search loop
while True:

    query = input("\nEnter your search query (or 'exit' to quit): ")

    if query.lower() == "exit":
        print("Program ended.")
        break

    if not query.strip():
        print("Please enter a valid query.")
        continue


    # Generate query embedding
    query_embedding = model.encode(query)


    # Calculate cosine similarity
    similarities = util.cos_sim(
        query_embedding,
        document_embeddings
    )


    # Get similarity scores
    scores = similarities[0]


    # Rank highest to lowest
    ranked_indices = scores.argsort(descending=True)


    # Select Top-K
    top_indices = ranked_indices[:top_k]


    # Display results
    print("\nTop results:")

    for index in top_indices:
        print(
            documents[index],
            "→",
            round(scores[index].item(), 4)
        )