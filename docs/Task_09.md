# Task 9: Eigenvalues and Eigenvectors

## B. Input Values and Mathematical Operations
* **Input values:** A `4x4` symmetric adjacency matrix `A` representing connections between four network nodes (`A, B, C, D`), where `1` means connected and `0` means not connected.
* **Math performed:** Computes all eigenvalues and eigenvectors of `A` using `np.linalg.eig(A)`. It locates the largest (dominant) real eigenvalue, extracts its corresponding eigenvector, takes the absolute values, and divides by the sum (`dominant_vector / dominant_vector.sum()`) to normalize the centrality scores so they add up to `1.0`. It also verifies the fundamental eigenvalue equation $Av = \lambda v$[cite: 14, 15].

## C. Parameter Change and Impact
* **Change:** Added a direct connection between Node A and Node D by changing `A[0, 3]` and `A[3, 0]` from `0.` to `1.`.
* **Result:** Every node now has the exact same number of connections (3 each). As a result, the dominant eigenvalue increases from `2.5616` to `3.0`, and all four nodes end up with identical importance scores of `0.2500` (25% each) because no single node is more central than the others.

## D. Meaning of Output in Words
The output prints the dominant eigenvalue (which measures the overall connectivity strength of the network) followed by each node's importance score[cite: 14, 15]. Nodes `B` and `C` get higher scores (`0.2812` each) than `A` and `D` (`0.2188` each) because `B` and `C` have more direct links and sit at the center of the network. The tiny verification error (near `0`) proves that $Av = \lambda v$ holds true. No graph is generated for this task.

## E. New Related Case: Study Group Note-Sharing Influence
* **Scenario:** Identifying which student is the most central "hub" in a 5-person university study circle based on who shares notes and revises with whom.
* **Assumptions:** 
  * Connections are two-way (undirected `5x5` adjacency matrix).
  * Being connected to other well-connected students boosts your influence score more than just having one isolated friend.
* **Output & Interpretation:** **Kevin** gets the highest influence score (~`28.9%`) because he links directly to all four classmates, including **Brian** (`11.6%`), who only talks to Kevin. **Emmanuel** ranks second (~`24.8%`) due to strong ties with Kevin, Sarah, and Faith. If Kevin misses class, note distribution across the group slows down the most.