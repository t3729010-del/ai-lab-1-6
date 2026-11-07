# AI LAB

| | |
|---|---|
| **Name** | Taimoor Ahmad |
| **Roll No.** | SU92-BSAIM-F25-054 |
| **Section** | BSAI-3A |
| **Course** | CAI601400 — Artificial Intelligence (Lab Manual) |
| **Repository** | `ai-lab-1-6` |

This repository contains my work for Labs 1 to 6 of the Artificial Intelligence lab manual. Each lab has its own folder with the task reports (`.docx`) and the code (`.py` scripts or Jupyter notebooks).

---

## Table of Contents

| Lab | Topic | Week | CLO |
|-----|-------|------|-----|
| [Lab 1](#lab-1--introduction-to-ai--paradigms) | Introduction to AI & Paradigms | 1 | CLO1 (C2) |
| [Lab 2](#lab-2--intelligent-agents--the-peas-framework) | Intelligent Agents & the PEAS Framework | 2 | CLO1 (C2) |
| [Lab 3](#lab-3--uninformed-search-bfs-dfs-dls-iddfs--ucs) | Uninformed Search: BFS, DFS, DLS, IDDFS & UCS | 3 | CLO2 (C3) |
| [Lab 4](#lab-4--informed-search-heuristics--a) | Informed Search: Heuristics & A* | 4 | CLO2 (C3) |
| [Lab 5](#lab-5--adversarial-search-minimax--alpha-beta-pruning) | Adversarial Search: Minimax & Alpha-Beta Pruning | 5 | CLO2 (C3) |
| [Lab 6](#lab-6--nlp-fundamentals-tokenization-embeddings--text-chunking) | NLP Fundamentals: Tokenization, Embeddings & Text Chunking | 6 | CLO3 (C3) |

---

## Repository Structure

```
ai-lab-1-6/
├── README.md
├── Lab#01/
│   ├── task#01.docx
│   ├── task#02/
│   │   ├── task#02.docx
│   │   └── task#02.py
│   └── task#03.docx
├── Lab#02/
│   ├── task01.docx
│   ├── task2.docx
│   └── task3/
│       └── task3.ipynb
├── Lab#03/
│   ├── task1/
│   │   ├── task1.docx
│   │   └── task1.ipynb
│   └── task2.ipynb
├── Lab#04/
│   ├── task1.docx
│   ├── task2.docx
│   ├── task2code.ipynb
│   └── task3.docx
├── Lab#05/
│   ├── code.ipynb
│   ├── task1.docx
│   ├── task2.docx
│   └── task3.docx
└── Lab#06/
    ├── lab6_search.py
    ├── guided_chatbot.py
    ├── guided_chunks.py
    ├── guided_embeddings.py
    ├── guided_suggestions.py
    ├── task1_tokens.py
    ├── task2_chunks.py
    └── task2_semantic.py
```

---

## Lab 1 — Introduction to AI & Paradigms

**Topic:** What constitutes AI, historical milestones (Turing Test, AI winters, modern compute/data), and the difference between symbolic/rule-based AI and probabilistic/data-driven AI.

**Case study:** Scholarship screening prototype comparing a transparent rule-based checker with a score/probability threshold.

**Tasks**
1. Timeline of at least five sourced AI milestones (including one AI winter and one modern compute/data milestone) — `task#01.docx`
2. Rule-based checker extended with two extra transparent conditions and four test cases — `task#02/task#02.py` and `task#02/task#02.docx`
3. Comparison of why passing a conversational test is not proof of general intelligence — `task#03.docx`

**Run**
```bash
cd "Lab#01/task#02"
python "task#02.py"
```

---

## Lab 2 — Intelligent Agents & the PEAS Framework

**Topic:** Agents, percepts, actions and rationality; PEAS specifications; environment classification (fully/partially observable, deterministic/stochastic); classical vs. LLM-based agents.

**Case study:** Smart classroom energy agent that observes temperature and occupancy and controls cooling.

**Tasks**
1. PEAS specifications for a delivery robot and an LLM-based student-support agent — `task01.docx`
2. Environment classification with justification — `task2.docx`
3. Stateful classroom agent that remembers the previous mode and avoids repeating identical commands — `task3/task3.ipynb`

**Run**
```bash
cd "Lab#02/task3"
jupyter notebook task3.ipynb
```

---

## Lab 3 — Uninformed Search: BFS, DFS, DLS, IDDFS & UCS

**Topic:** State-space formulation and uninformed search strategies, compared on completeness, optimality, time and space.

**Case study:** Emergency-exit graph where the fewest edges is not necessarily the lowest travel cost.

**Tasks**
1. BFS and DFS traced on the A–G graph — `task1/task1.docx`, `task1/task1.ipynb`
2. DLS / IDDFS (limits 1–4) and UCS on a weighted graph — `task2.ipynb`

**Run**
```bash
cd "Lab#03"
jupyter notebook task1/task1.ipynb
jupyter notebook task2.ipynb
```

---

## Lab 4 — Informed Search: Heuristics & A*

**Topic:** Heuristic evaluation functions and A* search, `f(n) = g(n) + h(n)`, admissibility and consistency, compared against uninformed search (UCS).

**Case study:** Low-cost route between campus buildings (S, A, B, C, G) using travel-time edges and heuristic estimates.

**Tasks**
1. Manual g/h/f calculations for the first three expansions — `task1.docx`
2. A* vs. UCS comparison on the same graph — `task2.docx`, `task2code.ipynb`
3. Overestimate experiment showing how an inadmissible heuristic affects optimality — `task3.docx`

**Run**
```bash
cd "Lab#04"
jupyter notebook task2code.ipynb
```

---

## Lab 5 — Adversarial Search: Minimax & Alpha-Beta Pruning

**Topic:** Game trees with alternating MAX/MIN layers, Minimax values, and alpha-beta pruning to reduce evaluated leaves without changing the decision.

**Case study:** Choosing the best move in a small two-player zero-sum game tree with known terminal scores.

**Tasks**
1. Manual Minimax trace of the supplied tree — `task1.docx`
2. Leaf-evaluation counter added to Minimax and alpha-beta — `task2.docx`, `code.ipynb`
3. Branch reordering and its effect on pruning — `task3.docx`

**Run**
```bash
cd "Lab#05"
jupyter notebook code.ipynb
```

---

## Lab 6 — NLP Fundamentals: Tokenization, Embeddings & Text Chunking

**Topic:** Tokenization, sentence embeddings with cosine similarity, and text chunking, combined into a traceable text-retrieval pipeline.

**Case study:** University help desk retrieval (synthetic handbook, fee, and IT-support data).

**Files**

| File | Purpose |
|------|---------|
| `lab6_search.py` | Shared retriever (TF-IDF and sentence-embedding backends) |
| `guided_embeddings.py` | Sentence embeddings and cosine similarity |
| `guided_chunks.py` | Word-window vs. sentence-aware chunking |
| `guided_chatbot.py` | Command-line FAQ chatbot |
| `guided_suggestions.py` | Related-question suggestions |
| `task1_tokens.py` | Task 1 — whitespace vs. word-like tokenization |
| `task2_chunks.py` | Task 2 — chunking with source offsets |
| `task2_semantic.py` | Task 2 — semantic retrieval vs. TF-IDF |

**Setup**
```bash
cd "Lab#06"
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
python -m pip install numpy scikit-learn sentence-transformers
```

**Run**
```bash
python task1_tokens.py
python task2_chunks.py
python task2_semantic.py
python guided_chatbot.py
python guided_chatbot.py --backend embedding
```

> The first embedding run downloads `sentence-transformers/all-MiniLM-L6-v2` (CPU only, no GPU or paid API needed).

---

## Requirements

- Python 3.10 or newer
- Jupyter Notebook (Labs 2–5): `pip install notebook`
- Lab 6: `numpy`, `scikit-learn`, `sentence-transformers`

## Notes

- All policies, thresholds, and datasets in these labs are synthetic teaching data, not real university policies.
- Virtual environments, model caches, and credentials are not included in the repository.

---

**Author:** Taimoor Ahmad | **Roll No.:** SU92-BSAIM-F25-054 | **Section:** BSAI-3A
