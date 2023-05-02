# FPT in P for c-closure, parameterized by degeneracy

We compute the c-closure of a graph parameterized by its degeneracy.

If the degeneracy is smaller than the c-closure, we compute the
c-closure, and output a witness in P-parameterized time $O(d^3 \cdot n)$.

In the case where the c-closure is smaller than the degeneracy, we fall
back to a quadratic time algorithm, $O(n^2 \cdot d)$.

However, our analyses show that in general, degeneracy is in fact
smaller than the c-closure.

## Some experiments

| name                |     n |      m |   deg |   c-c | time (ms) | smaller   |
|---------------------|-------|--------|-------|-------|-----------|-----------|
| karate.csv          |    34 |     78 |     4 |     6 |       0.6 | d         |
| adjnoun.csv         |   112 |    425 |     6 |    13 |       2.5 | d         |
| celegans.csv        |   131 |    687 |     8 |    13 |       3.4 | d         |
| arenasjazz.csv      |   198 |   2742 |    29 |    41 |      15.4 | d         |
| ca-netscience.csv   |   379 |    914 |     8 |     4 |       5.5 | c         |
| dnc.csv             |   906 |  10429 |    74 |    79 |     121.1 | d         |
| eu-emails.csv       |  1005 |  16064 |    34 |   161 |     289.1 | d         |
| yeast.csv           |  1622 |   9070 |    40 |    59 |      54.3 | d         |
| bible.csv           |  1773 |   9131 |    15 |    32 |      57.4 | d         |
| ca-csphd.csv        |  1882 |   1740 |     2 |     2 |      17.1 | d         |
| soc-hamsterster.csv |  2426 |  16630 |    24 |    76 |     185.4 | d         |
| power.csv           |  4941 |   6594 |     5 |     4 |      50.7 | c         |
| facebook.csv        |  5524 |  94218 |    39 |   170 |    1639.1 | d         |
| soc-advogato.csv    |  6551 |  39432 |    25 |   217 |     683.2 | d         |
| bio-dmela.csv       |  7393 |  25569 |    11 |    71 |     210.9 | d         |
| ca-heph.csv         | 12008 | 118489 |   238 |    89 |    2269   | c         |
| ca-astroph.csv      | 18772 | 198050 |    56 |    60 |    3068   | d         |
| internet-as.csv     | 22963 |  48436 |    25 |   217 |     584.8 | d         |
| enron-email.csv     | 36692 | 183831 |    43 |   186 |    4492.5 | d         |
| soc-brightkite.csv  | 56739 | 212945 |    52 |   183 |    2979.6 | d         |

As can be seen, in these 20 networks, only 3 have $c < d$.
