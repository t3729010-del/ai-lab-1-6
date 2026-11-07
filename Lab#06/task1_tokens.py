import re

texts = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "ہم ایک مثال ہے"
]
for text in texts:

    print("\nOriginal Text:", text)

    ws_tokens = text.split()
    print("Whitespace Tokens:", ws_tokens)
    print("Whitespace Count:", len(ws_tokens))

    regex_tokens = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Regex Tokens:", regex_tokens)
    print("Regex Count:", len(regex_tokens))

assert re.findall(r"\b\w+\b", "") == []

english = ["AI, search!", "I can't log in."]

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")

    print("\nMODEL TOKENIZER")
    for text in english:
        tokens = model.tokenizer.tokenize(text)
        print("\nOriginal Text:", text)
        print("Model Tokens:", tokens)
        print("Model Count:", len(tokens))
except Exception:
    print("\nModel tokenizer not available, skipped.")

print("""
EXPLANATION

Difference 1:
Whitespace splitting keeps punctuation attached to words ('search!'),
while the regex removes punctuation and returns 'search'.

Difference 2:
The regex splits inside words: "can't" becomes 'can' and 't',
and 'help@example.com' becomes 'help', 'example', 'com'.
Whitespace splitting keeps them as one token. So the token counts are different.

Unicode characters can have different internal representations
even when they look identical (for example 'é' as one character,
or 'e' plus a combining accent). Without Unicode normalization,
they may be treated as different text, and the regex may drop
the combining accent.

The regex is only a simple word-like extractor. It is not a
complete multilingual tokenizer.
""")