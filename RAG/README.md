
```mermaid

subgraph RAG pipeline
    A1[1. Load Source Data]
    A2[Vector Store]
    A3[2. Query]
    A4[3. Retrieve 'most similar']

    A1 -->|Load, Transform, Embed| A2
    A3 -->|Query, Transform, Embed| A2
    A2 -->|Retrieve 'most similar'| A4
end

```