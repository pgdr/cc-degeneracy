# FPT in P for c-closure, parameterized by degeneracy

We compute the c-closure of a graph parameterized by its degeneracy.

If the degeneracy is smaller than the c-closure, we compute the
c-closure, and output a witness in P-parameterized time $O(d^3 \cdot
n)$.

In the case where the c-closure is smaller than the degeneracy, we fall
back to a quadratic time algorithm, $O(n^2 \cdot d^2)$.  (TODO:Check)

However, our analyses show that in general, degeneracy is in fact
smaller than the c-closure.
