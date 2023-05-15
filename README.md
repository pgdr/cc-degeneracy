# FPT in P for c-closure, parameterized by degeneracy

We compute the c-closure of a graph parameterized by its degeneracy.

If the degeneracy is smaller than the c-closure, we compute the
c-closure, and output a witness in P-parameterized time $O(d^3 \cdot n)$.

In the case where the c-closure is smaller than the degeneracy, we fall
back to a quadratic time algorithm, $O(d \cdot n^2)$.

However, our analyses show that in general, degeneracy is in fact
smaller than the c-closure.

In fact, the best known algorithm for computing the c-closure is in
$O(c\cdot n^\omega)$ time, where $\omega$ is the matrix multiplication
constant.  This means that if $d \in O(n^{0.37})$, then this algorithm
is faster than the best known algorithm.  In the case where degeneracy
is smaller than the c-closure, as we see below it is in most cases, the
$O(d^3 \cdot n)$ is much faster than $O(c \cdot n^\omega)$ for all our
dataset.


## Some experiments

We ran our algorithm on all the datasets from
[_network-corpus_](https://github.com/microgravitas/network-corpus/), the results are
below.  We note that only 6 of 216 graphs used more than 5 seconds, while
195 graphs were solved in less than a second (in Python).

Only 2 of 216 graphs used more than 30 seconds

* `dogster_friendships.txt.gz` (48 sec) ($n=426821, m=8546581, d=249, c=32804$)
* `livemocha` (53 sec) ($n=104104, m=2193083, d=92, c=1129$)


In this dataset, 9 / 216 networks have $c < d$, whereas in 207, we have $c \geq d$.

This means that $207/216 \approx 0.95833... > 95.8\%$ are solved completely by _Case 1_.


### Analysis

| name                                     |       n |       m |   deg |   c-c | time (ms) | smaller   |
|------------------------------------------|---------|---------|-------|-------|-----------|-----------|
| `iscas89-s27`                            |       9 |       8 |     1 |     2 |       0.2 | d         |
| `wafa-padgett`                           |      15 |      27 |     3 |     4 |       0.2 | d         |
| `BioGrid-Human-Immunodeficiency-Virus-2` |      19 |      15 |     1 |     2 |       0.2 | d         |
| `wafa-hightech`                          |      22 |     159 |    12 |    17 |       0.7 | d         |
| `wafa-ceos`                              |      26 |      93 |     5 |     7 |       0.3 | d         |
| `BioGrid-Dictyostelium-Discoideum-Ax4`   |      27 |      20 |     1 |     2 |       0.2 | d         |
| `seventh-graders`                        |      29 |     376 |    20 |    18 |       3.6 | c         |
| `karate`                                 |      34 |      78 |     4 |     7 |       0.3 | d         |
| `windsurfers`                            |      43 |     336 |    11 |    17 |       3.8 | d         |
| `BioGrid-Glycine-Max`                    |      44 |      39 |     2 |     3 |       0.2 | d         |
| `wafa-eies`                              |      45 |     652 |    24 |    31 |       8.8 | d         |
| `dutch-textiles`                         |      48 |     134 |     7 |    12 |       0.3 | d         |
| `bergen`                                 |      53 |     272 |     9 |    13 |       0.9 | d         |
| `iscas89-s208.1`                         |      61 |      67 |     2 |     3 |       0.3 | d         |
| `dolphins`                               |      62 |     159 |     4 |     5 |       0.5 | d         |
| `BioGrid-Emericella-Nidulans-Fgsc-A4`    |      64 |      62 |     2 |     3 |       0.3 | d         |
| `train_bombing`                          |      64 |     243 |    10 |     9 |       1.4 | c         |
| `pollination-tenerife`                   |      68 |     129 |     4 |    11 |       0.4 | d         |
| `BioGrid-Cricetulus-Griseus`             |      69 |      57 |     1 |     2 |       0.3 | d         |
| `Noordin-terror-relation`                |      70 |     251 |    11 |    11 |       1   | d         |
| `mg_watchmen`                            |      76 |     201 |     7 |     6 |       0.7 | c         |
| `lesmiserables`                          |      77 |     254 |     9 |     9 |       0.8 | d         |
| `mg_godfatherII`                         |      78 |     219 |     8 |     9 |       0.6 | d         |
| `iscas89-s298`                           |      92 |     131 |     2 |     6 |       0.4 | d         |
| `mg_forrestgump`                         |      94 |     271 |     8 |     4 |       1.7 | c         |
| `win95pts`                               |      99 |     112 |     2 |     4 |       0.3 | d         |
| `iscas89-s344`                           |     100 |     122 |     2 |     5 |       0.3 | d         |
| `iscas89-s641`                           |     100 |     144 |     3 |     7 |       0.4 | d         |
| `movies`                                 |     101 |     192 |     3 |     6 |       0.5 | d         |
| `iscas89-s349`                           |     102 |     127 |     2 |     5 |       0.4 | d         |
| `polbooks`                               |     105 |     441 |     6 |    16 |       1   | d         |
| `mg_casino`                              |     109 |     326 |     9 |     8 |       0.9 | c         |
| `word_adjacencies`                       |     112 |     425 |     6 |    14 |       1   | d         |
| `iscas89-s386`                           |     114 |     200 |     3 |    13 |       0.5 | d         |
| `hypertext_2009`                         |     114 |    2196 |    28 |    54 |      16.8 | d         |
| `StackOverflow-tags`                     |     115 |     245 |     6 |     7 |       0.6 | d         |
| `football`                               |     115 |     613 |     8 |    10 |       5   | d         |
| `iscas89-s382`                           |     116 |     168 |     2 |     5 |       0.5 | d         |
| `BioGrid-Human-Herpesvirus-5`            |     121 |     107 |     1 |     2 |       0.4 | d         |
| `iscas89-s400`                           |     121 |     182 |     2 |     5 |       0.6 | d         |
| `Noordin-terror-loc`                     |     127 |     190 |     3 |     7 |       0.5 | d         |
| `iscas89-s420.1`                         |     129 |     145 |     2 |     3 |       0.4 | d         |
| `Noordin-terror-orgas`                   |     129 |     181 |     3 |    11 |       0.5 | d         |
| `iscas89-s444`                           |     134 |     206 |     2 |     5 |       0.5 | d         |
| `BioGrid-Hepatitus-C-Virus`              |     136 |     134 |     1 |     2 |       0.4 | d         |
| `iscas89-s713`                           |     137 |     180 |     3 |     7 |       0.5 | d         |
| `capitalist`                             |     139 |    1071 |    19 |    35 |      11   | d         |
| `american_revolution`                    |     141 |     160 |     3 |    10 |       0.4 | d         |
| `foodweb-otago`                          |     141 |     832 |    14 |    36 |       3.2 | d         |
| `BioGrid-Canis-Familiaris`               |     143 |     125 |     2 |     3 |       0.4 | d         |
| `iscas89-s526n`                          |     159 |     268 |     3 |     9 |       0.6 | d         |
| `iscas89-s526`                           |     160 |     270 |     3 |     9 |       0.6 | d         |
| `iscas89-s510`                           |     172 |     251 |     2 |     3 |       0.6 | d         |
| `BioGrid-Human-Papillomavirus-16`        |     173 |     186 |     2 |    18 |       0.5 | d         |
| `BioGrid-Human-Herpesvirus-1`            |     178 |     208 |     3 |    11 |       0.5 | d         |
| `CoW-interstate`                         |     182 |     319 |     4 |    13 |       0.7 | d         |
| `jazz`                                   |     199 |    2742 |    29 |    42 |      17.5 | d         |
| `mousebrain`                             |     213 |   16089 |   111 |   179 |      37.5 | d         |
| `residence_hall`                         |     218 |    1839 |    11 |    18 |      18.6 | d         |
| `airlines`                               |     235 |    1297 |    13 |    43 |       8   | d         |
| `sp_data_school_day_2`                   |     238 |    5539 |    33 |    54 |      36.2 | d         |
| `iscas89-s820`                           |     239 |     480 |     3 |    16 |       1.1 | d         |
| `rhesusbrain`                            |     242 |    3054 |    19 |    38 |      23.4 | d         |
| `iscas89-s832`                           |     245 |     498 |     3 |    19 |       1.2 | d         |
| `BioGrid-Danio-Rerio`                    |     261 |     266 |     3 |     4 |       0.6 | d         |
| `iscas89-s838.1`                         |     265 |     301 |     2 |     3 |       0.7 | d         |
| `haggle`                                 |     275 |    2124 |    39 |    41 |       6.6 | d         |
| `celegans`                               |     297 |    2148 |    10 |    41 |       8.6 | d         |
| `BioGrid-Human-Herpesvirus-4`            |     323 |     326 |     2 |     6 |       0.7 | d         |
| `hex`                                    |     331 |     930 |     3 |     3 |      27.2 | d         |
| `iscas89-s953`                           |     332 |     454 |     2 |     4 |       1   | d         |
| `autobahn`                               |     374 |     478 |     2 |     3 |       1   | d         |
| `photoviz_dynamic`                       |     376 |     610 |     4 |    13 |       1.1 | d         |
| `iscas89-s1196`                          |     377 |     537 |     2 |     3 |       1.2 | d         |
| `ia-infect-dublin`                       |     411 |    2765 |    17 |    23 |      16.9 | d         |
| `infectious`                             |     411 |    2765 |    17 |    23 |      17.5 | d         |
| `BioGrid-Gallus-Gallus`                  |     413 |     436 |     4 |    22 |       1   | d         |
| `iscas89-s1238`                          |     416 |     625 |     2 |     3 |       1.3 | d         |
| `iscas89-s1423`                          |     423 |     554 |     2 |     5 |       1.1 | d         |
| `ecoli-transcript`                       |     424 |     578 |     3 |    11 |       1.1 | d         |
| `muenchen-bahn`                          |     447 |     578 |     2 |     2 |      11.7 | d         |
| `BioGrid-Bos-Taurus`                     |     454 |     424 |     3 |     7 |       0.9 | d         |
| `iscas89-s1488`                          |     463 |     779 |     3 |    11 |       2   | d         |
| `iscas89-s1494`                          |     473 |     796 |     3 |    11 |       1.7 | d         |
| `pigs`                                   |     492 |     592 |     2 |     7 |       1.1 | d         |
| `foodweb-caribbean`                      |     492 |    3313 |    13 |   155 |      10.8 | d         |
| `ratbrain`                               |     503 |   23030 |    67 |   127 |      37.9 | d         |
| `BioGrid-Human-Herpesvirus-8`            |     716 |     691 |     3 |     6 |       1.4 | d         |
| `codeminer`                              |     724 |    1015 |     4 |     7 |       1.8 | d         |
| `pollination-daphni`                     |     797 |    2933 |     9 |    45 |      15.3 | d         |
| `cpan-authors`                           |     839 |    2112 |     9 |    52 |      11.1 | d         |
| `columbia-mobility`                      |     864 |    4147 |     9 |    12 |      17.9 | d         |
| `columbia-social`                        |     864 |    7724 |    18 |    54 |      25.5 | d         |
| `unicode_languages`                      |     868 |    1255 |     4 |    19 |       3.7 | d         |
| `soc-wiki-Vote`                          |     890 |    2914 |     9 |    18 |      15.2 | d         |
| `link-pedigree`                          |     898 |    1125 |     2 |    14 |       3.1 | d         |
| `Opsahl-forum`                           |     899 |    7036 |    14 |    38 |      32.4 | d         |
| `pollination-uk`                         |     984 |   16712 |    35 |   202 |      23.9 | d         |
| `EU-email-core`                          |     986 |   16064 |    34 |   162 |      29.1 | d         |
| `roget-thesaurus`                        |    1010 |    3648 |     6 |     8 |      21.2 | d         |
| `bn-mouse_retina_1`                      |    1076 |   90811 |   121 |   403 |     869.1 | d         |
| `BioGrid-Candida-Albicans-Sc5314`        |    1121 |    1609 |     9 |    64 |       5   | d         |
| `ia-email-univ`                          |    1134 |    5451 |    11 |    19 |      28.7 | d         |
| `BioGrid-Human-Immunodeficiency-Virus-1` |    1138 |    1319 |     3 |    43 |       5   | d         |
| `euroroad`                               |    1174 |    1417 |     2 |     4 |       4.1 | d         |
| `BioGrid-Far-Western`                    |    1199 |    1089 |     3 |    11 |       4.2 | d         |
| `polblogs`                               |    1224 |   16715 |    36 |   130 |      49.4 | d         |
| `BioGrid-Escherichia-Coli-K12-Mg1655`    |    1273 |    1889 |     5 |    13 |       7.1 | d         |
| `web-google`                             |    1299 |    2773 |    17 |    18 |      17.4 | d         |
| `munin`                                  |    1324 |    1397 |     3 |    29 |       4.2 | d         |
| `iscas89-s5378`                          |    1411 |    1639 |     3 |     5 |       5.3 | d         |
| `diseasome`                              |    1419 |    2738 |    11 |     9 |      16.1 | c         |
| `BioGrid-Dosage-Growth-Defect`           |    1447 |    2193 |     5 |    70 |       7   | d         |
| `netscience`                             |    1461 |    2742 |    19 |     6 |      28.4 | c         |
| `chicago`                                |    1468 |    1298 |     1 |     2 |       6.5 | d         |
| `pollination-carlinville`                |    1500 |   15255 |    18 |    67 |      45.3 | d         |
| `bitcoin-otc-negative`                   |    1606 |    3259 |    16 |    39 |      15   | d         |
| `BioGrid-Fret`                           |    1700 |    2395 |    19 |    38 |      17.4 | d         |
| `BioGrid-Dosage-Lethality`               |    1776 |    2289 |     4 |    33 |       6.9 | d         |
| `bn-fly-drosophila_medulla_1`            |    1781 |    8911 |    18 |    42 |      39.8 | d         |
| `BioGrid-Affinity-Capture-Luminescence`  |    1840 |    2312 |     6 |    38 |       5.5 | d         |
| `DNC-emails`                             |    1866 |    4384 |    17 |    74 |      19.7 | d         |
| `wikipedia-norm`                         |    1881 |   15372 |    22 |   138 |      47.6 | d         |
| `exnet-water`                            |    1893 |    2416 |     2 |     3 |       7.1 | d         |
| `Opsahl-socnet`                          |    1899 |   13838 |    20 |   112 |      44   | d         |
| `Y2H_union`                              |    1966 |    2705 |     4 |    30 |       7   | d         |
| `iscas89-s9234`                          |    1985 |    2370 |     4 |    10 |       7.1 | d         |
| `NZ_legal`                               |    2141 |   15739 |    25 |   129 |      44.1 | d         |
| `BioGrid-Co-Crystal-Structure`           |    2291 |    2021 |     5 |     6 |       6.6 | d         |
| `Yeast`                                  |    2362 |    7182 |    10 |    22 |      27.3 | d         |
| `soc-hamsterster`                        |    2426 |   16630 |    24 |    77 |      39.8 | d         |
| `iscas89-s13207`                         |    2492 |    3406 |     4 |    31 |       8.4 | d         |
| `moreno_health`                          |    2539 |   10455 |     7 |    17 |      20.5 | d         |
| `minnesota`                              |    2642 |    3303 |     2 |     3 |       8.3 | d         |
| `ODLIS`                                  |    2900 |   16377 |    12 |    86 |      40.8 | d         |
| `openflights`                            |    2940 |   15677 |    28 |   111 |      33.1 | d         |
| `iscas89-s15850`                         |    3247 |    4004 |     4 |    16 |       9.1 | d         |
| `BioGrid-Dosage-Rescue`                  |    3380 |    6444 |     7 |    35 |      15.4 | d         |
| `BioGrid-Co-Localization`                |    3543 |    4452 |     6 |    25 |      13.7 | d         |
| `twittercrawl`                           |    3656 |  154824 |   142 |   507 |     641.6 | d         |
| `BioGrid-Escherichia-Coli-K12-W3110`     |    4063 |  181620 |   156 |   442 |    3634.4 | d         |
| `boards_gender_1m`                       |    4134 |   19993 |    25 |    20 |      34.3 | c         |
| `boards_gender_2m`                       |    4220 |    5598 |     4 |    21 |      12.2 | d         |
| `web-EPA`                                |    4271 |    8909 |     6 |    64 |      16   | d         |
| `BioGrid-Co-Purification`                |    4326 |    5970 |    12 |    71 |      19.4 | d         |
| `ingredients`                            |    4372 |  591463 |   462 |   836 |    3424.3 | d         |
| `advogato`                               |    5155 |   39285 |    25 |   216 |      51   | d         |
| `soc-advogato`                           |    5167 |   39432 |    25 |   218 |      51.7 | d         |
| `ca-GrQc`                                |    5242 |   14484 |    43 |    43 |      39.2 | d         |
| `bitcoin-otc-positive`                   |    5573 |   18591 |    20 |    92 |      43.9 | d         |
| `JUNG-javax`                             |    6120 |   50290 |    65 |   619 |      38.9 | d         |
| `web-california`                         |    6175 |   15969 |    11 |    69 |      23.5 | d         |
| `reactome`                               |    6328 |  147547 |   176 |   446 |     101.6 | d         |
| `BioGrid-Caenorhabditis-Elegans`         |    6394 |   23646 |    64 |    82 |      42.4 | d         |
| `JDK_dependency`                         |    6435 |   53658 |    65 |   707 |      41.8 | d         |
| `as20000102`                             |    6474 |   12572 |    12 |    43 |      26.7 | d         |
| `zewail`                                 |    6651 |   54182 |    18 |    99 |      48.7 | d         |
| `ia-reality`                             |    6810 |    7680 |     5 |    19 |       8.9 | d         |
| `wiki-vote`                              |    7115 |  100762 |    53 |   441 |     126.1 | d         |
| `eva-corporate`                          |    7253 |    6711 |     3 |     7 |       9   | d         |
| `chess`                                  |    7301 |   55899 |    29 |    64 |     259.8 | d         |
| `lederberg`                              |    8324 |   41532 |    15 |   175 |      51.1 | d         |
| `BioGrid-Biochemical-Activity`           |    8620 |   17746 |    11 |   182 |      33.1 | d         |
| `iscas89-s38584`                         |    9193 |   12573 |     4 |    13 |      11.5 | d         |
| `BioGrid-Drosophila-Melanogaster`        |    9330 |   60556 |    83 |   115 |      73.8 | d         |
| `iscas89-s38417`                         |    9500 |   10635 |     4 |    12 |      14.2 | d         |
| `movielens_1m`                           |    9746 | 1000209 |   221 |  2356 |   12513.7 | d         |
| `BioGrid-Arabidopsis-Thaliana-Columbia`  |   10417 |   47916 |    26 |   385 |      37   | d         |
| `p2p-Gnutella04`                         |   10876 |   39994 |     7 |    29 |      32.1 | d         |
| `BioGrid-Co-Fractionation`               |   11017 |   56354 |    83 |    84 |      68.6 | d         |
| `AS-oregon-1`                            |   11174 |   23409 |    17 |    75 |      42.8 | d         |
| `AS-oregon-2`                            |   11461 |   32730 |    31 |   118 |      54.6 | d         |
| `ca-HepPh`                               |   12006 |  118489 |   238 |    90 |     436.8 | c         |
| `ukroad`                                 |   12378 |   15641 |     3 |     5 |      11.2 | d         |
| `iscas89-s35932`                         |   12515 |   15961 |     2 |     2 |    2799.9 | d         |
| `foldoc`                                 |   13357 |   91471 |    12 |    63 |      65.1 | d         |
| `BioGrid-Affinity-Capture-Rna`           |   13765 |   42815 |    54 |  1630 |     230   | d         |
| `escorts`                                |   16730 |   39044 |    11 |    69 |      51.6 | d         |
| `marvel`                                 |   19429 |   96662 |    18 |   745 |     204.2 | d         |
| `BioGrid-Affinity-Capture-Western`       |   21028 |   64046 |    17 |    93 |      80.8 | d         |
| `as-22july06`                            |   22963 |   48436 |    25 |   218 |      85   | d         |
| `edinburgh_associative_thesaurus`        |   23132 |  297094 |    34 |   205 |    1175.4 | d         |
| `ca-CondMat`                             |   23133 |   93439 |    25 |    27 |      81.6 | d         |
| `cora_citation`                          |   23167 |   89157 |    13 |    70 |      49.8 | d         |
| `soc-gplus`                              |   23628 |   39194 |    12 |   490 |      97.6 | d         |
| `google+`                                |   23629 |   39194 |    12 |   490 |      97   | d         |
| `BioGrid-Homo-Sapiens`                   |   24093 |  369767 |    71 |   802 |    1667.5 | d         |
| `cit-HepTh`                              |   27769 |  352285 |    37 |  1670 |     249.3 | d         |
| `digg`                                   |   30399 |   86312 |    10 |    20 |     139.7 | d         |
| `linux`                                  |   30834 |  213217 |    23 |  4836 |    3946.5 | d         |
| `BioGrid-Chemicals`                      |   33266 |   28093 |     1 |     2 |      18.7 | d         |
| `cit-HepPh`                              |   34546 |  420877 |    30 |   300 |     198.6 | d         |
| `email-Enron`                            |   36692 |  183831 |    43 |   187 |     752.2 | d         |
| `BioGrid-Affinity-Capture-Ms`            |   40495 |  321887 |    58 |   843 |     580.6 | d         |
| `slashdot_threads`                       |   51084 |  117378 |    15 |    65 |     212.4 | d         |
| `deezer`                                 |   54573 |  498202 |    21 |    83 |     400.2 | d         |
| `loc-brightkite_edges`                   |   58228 |  214078 |    52 |   184 |     213.7 | d         |
| `facebook-links`                         |   63731 |  817090 |    52 |   233 |    1705.6 | d         |
| `BioGrid-All`                            |   75550 | 1316843 |   164 |  1792 |    1738.1 | d         |
| `soc-Epinions1`                          |   75879 |  405740 |    67 |   551 |    1301.5 | d         |
| `soc-Slashdot0811`                       |   77360 |  469180 |    54 |   618 |     832.4 | d         |
| `NYClimateMarch2014`                     |  102378 |  327080 |    34 |  1037 |    2548.4 | d         |
| `livemocha`                              |  104104 | 2193083 |    92 |  1129 |   52801.5 | d         |
| `tv_tropes`                              |  152093 | 3232134 |   115 |  2655 |   25491.8 | d         |
| `gowalla`                                |  196591 |  950327 |    51 |  1132 |    1258.8 | d         |
| `bahamas`                                |  219856 |  246291 |     6 |    58 |     145.9 | d         |
| `location`                               |  225486 |  293697 |     5 |   854 |     486.3 | d         |
| `offshore`                               |  278877 |  505965 |    13 |  5698 |     479.2 | d         |
| `dogster_friendships`                    |  426821 | 8546581 |   249 | 32804 |   48807.8 | d         |
| `Cannes2013`                             |  438089 |  835892 |    27 |  3168 |    2523.8 | d         |
| `actor_movies`                           |  511463 | 1470404 |    14 |   217 |    1036.9 | d         |
| `paradise`                               |  542102 |  794545 |    23 |  4242 |    1317.1 | d         |
| `panama`                                 |  556686 |  702437 |    62 |  1948 |     699.5 | d         |
| `countries`                              |  592414 |  624402 |     6 | 11048 |    9415.9 | d         |
| `teams`                                  |  935591 | 1366466 |     9 |   351 |    6893.1 | d         |
| `mag_geology_coauthor`                   | 2852295 | 4448428 |    13 |   193 |    3205.6 | d         |
