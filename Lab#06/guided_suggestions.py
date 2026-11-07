from task2_chunks import DOCS, make_chunks
from lab6_search import Retriever
engine = Retriever(make_chunks(DOCS, "sentence"), "embedding")
query = "forgot login"
print("Suggested chunks:")
for record, score in engine.search(query, k=3):
    print(record["id"], f"({score:.3f})", record["text"])