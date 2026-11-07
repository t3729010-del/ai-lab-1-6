from task2_chunks import DOCS, make_chunks
from lab6_search import Retriever, show_hits
queries = ["I was ill, can I hand in my work after the deadline?",   # late
           "How can I regain access to my account?",                 # password
           "Are outside workers allowed to work from home?"]         # contractor
records = make_chunks(DOCS, "sentence")
for backend in ["tfidf", "embedding"]:
    engine = Retriever(records, backend)
    print("Backend:", backend)
    for query in queries:
        print("Query:", query)
        show_hits(engine.search(query, k=2))