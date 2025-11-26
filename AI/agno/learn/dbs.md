# Agno Storage

Agno's storage layer provides a unified interface to persist essential data for your agents, regardless of the underlying database (e.g., SQL, Firestore).

It is designed to store:

-   **Sessions:** The state and history of agent, team, and workflow interactions.
-   **(User) Memories:** Information and conversational context specific to a user.
-   **Metrics:** Performance data and operational metrics from agent runs.
-   **Evaluation Runs:** The results and data from evaluation and testing sessions.
-   **(RAG) Knowledge:** Documents and content used for Retrieval-Augmented Generation.
