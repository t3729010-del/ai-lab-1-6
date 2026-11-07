import re 
 
def word_spans(text): 
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)] 
 
def windows(text, size=40, overlap=10, offset=0): 
    if size <= 0 or not 0 <= overlap < size: 
        raise ValueError("Require size > 0 and 0 <= overlap < size") 
    spans = word_spans(text) 
    result = [] 
    for i in range(0, len(spans), size-overlap): 
        j = min(i+size, len(spans)) 
        result.append((offset+spans[i][0], offset+spans[j-1][1])) 
        if j == len(spans): 
            break 
    return result 
 
def sentence_chunks(text, size=40): 
    if size <= 0: 
        raise ValueError("size must be positive") 
    # Teaching splitter: punctuation followed by whitespace. 
    cuts = [0] + [m.end() for m in 
                  re.finditer(r"[.!?]\s+", text)] + [len(text)] 
    out, pending, count = [], None, 0 
    for a, b in zip(cuts, cuts[1:]): 
        segment = text[a:b] 
        n = len(segment.split()) 
        if not n:  
            continue 
        if n > size: 
            if pending is not None: 
                out.append(pending) 
            out.extend(windows(segment, size, 0, a)) 
            pending, count = None, 0 
        elif pending is not None and count+n <= size: 
            pending, count = (pending[0], b), count+n 
        else: 
            if pending is not None: 
                out.append(pending) 
            pending, count = (a, b), n 
    if pending is not None: 
        out.append(pending) 
    return out 
 
def make_chunks(docs, strategy): 
    result = [] 
    for doc_id, text in docs.items(): 
        spans = (sentence_chunks(text) if strategy == "sentence" 
                 else windows(text, 40, int(strategy))) 
        for i, (a, b) in enumerate(spans): 
            result.append(dict(id=f"{doc_id}:{i}", doc=doc_id, 
                               start=a, end=b, text=text[a:b])) 
    return result 

def clean(text):
    return " ".join(text.split())
 
 
DOCS = {
    "late": clean("""
        Assessment Policy. All coursework must be submitted through the
        learning portal before the stated deadline. Files should be uploaded
        as a single PDF, and the file name should include the student number
        and the course code. Late submission is normally penalized by ten
        percent per day, except when the student provides medical evidence
        before the deadline. The coordinator reviews every extension request
        individually and records the decision in the course file. Students
        should keep a copy of each submission receipt because the portal
        does not send reminders after a file has been uploaded. Group
        assignments follow the same deadline rules, and every member of the
        group is responsible for confirming that the final file contains the
        contributions of all members, that the references are complete, that
        the formatting follows the template provided by the instructor, and
        that the document opens correctly before the deadline passes.
        Plagiarism checks run automatically on every upload. Questions about
        marking criteria should be sent to the course coordinator by email
        during office hours.
    """),
 
    "password": clean("""
        IT Help Desk Guide. Students who forget a password can reset it
        using the recovery link on the login page, except when the account
        has been locked after five failed attempts. A locked account can be
        opened only at the help desk, where the student must show a valid
        student card. Staff such as Dr. Ahmed and Prof. Rana in the IT
        office, e.g. the service desk team, handle locked accounts between
        nine and four on working days. Recovery codes must never be shared
        with anyone, including friends, classmates and teaching staff, and
        students should store them in a safe place away from their devices
        because a lost code cannot be regenerated without a new identity
        check at the help desk. The portal also supports a second
        verification step by phone, which is recommended for every account.
        Passwords should contain at least twelve characters and should not
        reuse an earlier password. The link stays active for thirty minutes
        and is sent only to the registered email address.
    """),
 
    "contractor": clean("""
        Remote Work Policy. Employees may request remote work for up to two
        days each week with written manager approval. Requests are reviewed
        within five working days and the decision is stored in the personnel
        record. Contractors can work remotely only if the signed contract
        permits it, and no manager can grant an exception verbally.
        Employee rules do not apply to contractors, because contractors are
        engaged under separate agreements that describe the place of work,
        the working hours, the equipment provided by the company, the
        security requirements for any device used outside the office and the
        notice period for ending the agreement. Remote workers must remain
        available during core hours and must use the company virtual private
        network when accessing internal systems. Equipment taken home must
        be returned in good condition. Staff must report any change of home
        address to the personnel office. Managers should review remote
        arrangements every six months and report any security problems to
        the information security office.
    """),
}

EVIDENCE = {
    "late": clean("""
        Late submission is normally penalized by ten percent per day,
        except when the student provides medical evidence before the deadline.
    """),
    "password": clean("""
        Students who forget a password can reset it using the recovery
        link on the login page, except when the account has been locked
        after five failed attempts.
    """),
    "contractor": clean("""
        Contractors can work remotely only if the signed contract
        permits it, and no manager can grant an exception verbally.
    """),
}
 
if __name__ == "__main__": 
    assert windows("") == [] 
    assert windows("short text") == [(0, 10)] 
    try: 
        windows("a b", 2, 2) 
    except ValueError: 
        pass 
    else: 
        raise AssertionError("Invalid overlap was accepted") 
    long = " ".join(["word"]*95) + "." 
    assert all(len(long[a:b].split()) <= 40 
               for a, b in sentence_chunks(long)) 
    docs = {"example": "Reset your password. Keep recovery codes private."} 
    for strategy in ["0", "10", "sentence"]: 
        for c in make_chunks(docs, strategy): 
            assert c["text"] == docs[c["doc"]][c["start"]:c["end"]] 
            print(strategy, c)
            
    print("\nDOCUMENTS")
    for doc_id, text in DOCS.items():
        n = len(text.split())
        longest = max(len(s.split()) for s in re.split(r"(?<=[.!?])\s+", text))
        print(doc_id, "words:", n, "| longest sentence:", longest, "words")
        assert 150 <= n <= 250
        assert EVIDENCE[doc_id] in text

    original_words = sum(len(t.split()) for t in DOCS.values())
    names = {"0": "window overlap 0", "10": "window overlap 10",
             "sentence": "sentence-aware"}

    print("\nCOMPARISON (original words:", original_words, ")")
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(DOCS, strategy)

        for c in chunks:
            assert c["text"] == DOCS[c["doc"]][c["start"]:c["end"]]

        sizes = [len(c["text"].split()) for c in chunks]
        repeated = sum(sizes) - original_words
        print("\n" + names[strategy])
        print("chunks:", len(chunks), "| words per chunk min/avg/max:",
              min(sizes), round(sum(sizes)/len(sizes), 1), max(sizes),
              "| repeated words:", repeated)
        for doc_id in DOCS:
            kept = any(EVIDENCE[doc_id] in c["text"]
                       for c in chunks if c["doc"] == doc_id)
            print("  rule+exception in one chunk -", doc_id + ":", kept)

    assert sentence_chunks("") == []
    assert sentence_chunks("short text") == [(0, 10)]
    assert len(sentence_chunks(long)) == 3     # 95-word sentence -> 3 windows
    for size, overlap in [(2, 3), (2, -1), (0, 0)]:
        try:
            windows("a b c", size, overlap)
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid overlap was accepted")
    print("\nAll tests passed")

    demo = "Dr. Khan approved the extension. Ask the registrar, e.g. Mr. Ali."
    print("\nABBREVIATION DEMO (budget 4 words)")
    for a, b in sentence_chunks(demo, size=4):
        print(repr(demo[a:b]))

    print("""
EXPLANATION: where sentence splitting fails
The splitter cuts after '.', '!' or '?' followed by a space. It cannot tell
a full stop from an abbreviation, so 'Dr. ', 'Prof. ' and 'e.g. ' are treated
as sentence ends. In the demo above, 'Dr. ' becomes a chunk on its own and
is separated from 'Khan'. It also does not handle the Urdu full stop,
headings or bullet points without punctuation, or text that has no final
punctuation, so those can be merged or cut at the wrong place.
""")