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
[_network-corpus_](https://github.com/microgravitas/network-corpus/) and
some from the folder `dataset` in this repository, the results are
below.  We note that 3 of 229 graphs used more than 25 minutes, while
180 graphs were solved in less than a second (in Python).

Only 5 of 229 graphs used more than a minute, and they all had degeneracy smaller than c-closure:

* `BioGrid-All` **6 min** ($n=75550, m=1316843, d=164, c=1791$)
* `livemocha` **7 min** ($n=104103, m=2193083, d=92, c=1128$)
* `tv_tropes` **25 min** ($n=152093, m=3232134, d=115, c=2654$)
* `movielens_1m` **37 min** ($n=9746, m=1000209, d=221, c=2355$)
* `dogster_friendships` **1 h 49 min** ($n=426820, m=8543549, d=248, c=32803$)


In this dataset, 17 of 229 networks have $c < d$, whereas in 212, we have $c \geq d$.

This means that $212/229 \approx 0.926 = 92.6\%$ are solved completely by _Case 1_.


### Analysis

| name                                            |       n |       m |   deg |   c-c |   time (ms) | smaller   |
|-------------------------------------------------|---------|---------|-------|-------|-------------|-----------|
| `iscas89-s27.txt.gz`                            |       9 |       8 |     1 |     1 |         0.1 | d         |
| `wafa-padgett.txt.gz`                           |      15 |      27 |     3 |     3 |         0.1 | d         |
| `BioGrid-Human-Immunodeficiency-Virus-2.txt.gz` |      19 |      15 |     1 |     1 |         0.1 | d         |
| `wafa-hightech.txt.gz`                          |      21 |     159 |    12 |    16 |         0.3 | d         |
| `wafa-ceos.txt.gz`                              |      26 |      93 |     5 |     6 |         0.2 | d         |
| `BioGrid-Dictyostelium-Discoideum-Ax4.txt.gz`   |      27 |      20 |     1 |     1 |         0.1 | d         |
| `seventh-graders.csv`                           |      29 |     250 |    13 |    17 |         0.6 | d         |
| `karate.txt.gz`                                 |      34 |      78 |     4 |     6 |         0.2 | d         |
| `windsurfers.txt.gz`                            |      43 |     336 |    11 |    16 |         0.8 | d         |
| `BioGrid-Glycine-Max.txt.gz`                    |      44 |      39 |     2 |     2 |         0.2 | d         |
| `wafa-eies.txt.gz`                              |      45 |     652 |    24 |    30 |         1.5 | d         |
| `dutch-textiles.txt.gz`                         |      48 |      88 |     4 |    11 |         0.2 | d         |
| `bergen.txt.gz`                                 |      53 |     272 |     9 |    12 |         0.6 | d         |
| `iscas89-s208.1.txt.gz`                         |      61 |      67 |     2 |     2 |         0.2 | d         |
| `dolphins.txt.gz`                               |      62 |     159 |     4 |     4 |         0.4 | d         |
| `BioGrid-Emericella-Nidulans-Fgsc-A4.txt.gz`    |      64 |      62 |     2 |     2 |         0.2 | d         |
| *`train_bombing.txt.gz`                         |      64 |     243 |    10 |     8 |         0.7 | **c !**   |
| `pollination-tenerife.txt.gz`                   |      68 |     129 |     4 |    10 |         0.4 | d         |
| `BioGrid-Cricetulus-Griseus.txt.gz`             |      69 |      57 |     1 |     1 |         0.3 | d         |
| *`Noordin-terror-relation.txt.gz`               |      70 |     251 |    11 |    10 |         0.6 | **c !**   |
| *`mg_watchmen.txt.gz`                           |      76 |     201 |     7 |     5 |         0.5 | **c !**   |
| *`lesmiserables.txt.gz`                         |      77 |     254 |     9 |     8 |         0.6 | **c !**   |
| `mg_godfatherII.txt.gz`                         |      78 |     219 |     8 |     8 |         0.5 | d         |
| `iscas89-s298.txt.gz`                           |      92 |     131 |     2 |     5 |         0.4 | d         |
| *`mg_forrestgump.txt.gz`                        |      94 |     271 |     8 |     3 |         0.9 | **c !**   |
| `win95pts.txt.gz`                               |      99 |     112 |     2 |     3 |         0.4 | d         |
| `iscas89-s344.txt.gz`                           |     100 |     122 |     2 |     4 |         0.4 | d         |
| `iscas89-s641.txt.gz`                           |     100 |     144 |     3 |     6 |         0.5 | d         |
| `movies.txt.gz`                                 |     101 |     192 |     3 |     5 |         0.5 | d         |
| `iscas89-s349.txt.gz`                           |     102 |     127 |     2 |     4 |         0.4 | d         |
| `polbooks.txt.gz`                               |     105 |     441 |     6 |    15 |         1   | d         |
| *`mg_casino.txt.gz`                             |     109 |     326 |     9 |     7 |         0.8 | **c !**   |
| `word_adjacencies.txt.gz`                       |     112 |     425 |     6 |    13 |         1   | d         |
| `hypertext_2009.txt.gz`                         |     113 |    2196 |    28 |    53 |        14.4 | d         |
| `iscas89-s386.txt.gz`                           |     114 |     200 |     3 |    12 |         0.5 | d         |
| `StackOverflow-tags.txt.gz`                     |     115 |     245 |     6 |     6 |         0.7 | d         |
| `football.txt.gz`                               |     115 |     613 |     8 |     9 |         1.5 | d         |
| `iscas89-s382.txt.gz`                           |     116 |     168 |     2 |     4 |         0.5 | d         |
| `BioGrid-Human-Herpesvirus-5.txt.gz`            |     121 |     107 |     1 |     1 |         0.4 | d         |
| `iscas89-s400.txt.gz`                           |     121 |     182 |     2 |     4 |         0.5 | d         |
| `Noordin-terror-loc.txt.gz`                     |     127 |     190 |     3 |     6 |         0.6 | d         |
| `iscas89-s420.1.txt.gz`                         |     129 |     145 |     2 |     2 |         0.5 | d         |
| `Noordin-terror-orgas.txt.gz`                   |     129 |     181 |     3 |    10 |         0.6 | d         |
| `celegans.csv`                                  |     131 |     687 |     8 |    13 |         1.8 | d         |
| `iscas89-s444.txt.gz`                           |     134 |     206 |     2 |     4 |         0.6 | d         |
| `BioGrid-Hepatitus-C-Virus.txt.gz`              |     136 |     134 |     1 |     1 |         0.5 | d         |
| `iscas89-s713.txt.gz`                           |     137 |     180 |     3 |     6 |         0.6 | d         |
| `capitalist.txt.gz`                             |     139 |    1071 |    19 |    34 |         2.7 | d         |
| `american_revolution.txt.gz`                    |     141 |     160 |     3 |     9 |         0.6 | d         |
| `foodweb-otago.txt.gz`                          |     141 |     832 |    14 |    35 |         4.8 | d         |
| `BioGrid-Canis-Familiaris.txt.gz`               |     143 |     125 |     2 |     2 |         0.5 | d         |
| `iscas89-s526n.txt.gz`                          |     159 |     268 |     3 |     8 |         0.8 | d         |
| `iscas89-s526.txt.gz`                           |     160 |     270 |     3 |     8 |         0.7 | d         |
| `iscas89-s510.txt.gz`                           |     172 |     251 |     2 |     2 |         0.8 | d         |
| `BioGrid-Human-Papillomavirus-16.txt.gz`        |     173 |     186 |     2 |    17 |         0.6 | d         |
| `BioGrid-Human-Herpesvirus-1.txt.gz`            |     178 |     208 |     3 |    10 |         0.7 | d         |
| `CoW-interstate.txt.gz`                         |     182 |     319 |     4 |    12 |         1.2 | d         |
| `jazz.txt.gz`                                   |     198 |    2742 |    29 |    41 |        10.1 | d         |
| `mousebrain.txt.gz`                             |     213 |   16089 |   111 |   178 |       540.3 | d         |
| `residence_hall.txt.gz`                         |     217 |    1839 |    11 |    17 |         5.7 | d         |
| `airlines.txt.gz`                               |     235 |    1297 |    13 |    42 |         3.3 | d         |
| `sp_data_school_day_2.txt.gz`                   |     238 |    5539 |    33 |    53 |        51   | d         |
| `iscas89-s820.txt.gz`                           |     239 |     480 |     3 |    15 |         1.6 | d         |
| `rhesusbrain.txt.gz`                            |     242 |    3054 |    19 |    37 |        16.8 | d         |
| `iscas89-s832.txt.gz`                           |     245 |     498 |     3 |    18 |         1.3 | d         |
| `BioGrid-Danio-Rerio.txt.gz`                    |     261 |     266 |     3 |     3 |         1   | d         |
| `iscas89-s838.1.txt.gz`                         |     265 |     301 |     2 |     2 |         1   | d         |
| `haggle.txt.gz`                                 |     274 |    2124 |    39 |    40 |         5.5 | d         |
| `celegans.txt.gz`                               |     297 |    2148 |    10 |    40 |         7.4 | d         |
| `BioGrid-Human-Herpesvirus-4.txt.gz`            |     323 |     326 |     2 |     5 |         1.2 | d         |
| *`hex.txt.gz`                                   |     331 |     930 |     3 |     2 |        20.3 | **c !**   |
| `iscas89-s953.txt.gz`                           |     332 |     454 |     2 |     3 |         1.4 | d         |
| `autobahn.txt.gz`                               |     374 |     478 |     2 |     2 |         1.6 | d         |
| `photoviz_dynamic.txt.gz`                       |     376 |     610 |     4 |    12 |         2   | d         |
| `iscas89-s1196.txt.gz`                          |     377 |     537 |     2 |     2 |         1.7 | d         |
| *`ca-netscience.csv`                            |     379 |     914 |     8 |     4 |         2.6 | **c !**   |
| `ia-infect-dublin.txt.gz`                       |     410 |    2765 |    17 |    22 |         8.1 | d         |
| `infectious.txt.gz`                             |     410 |    2765 |    17 |    22 |         7.7 | d         |
| `BioGrid-Gallus-Gallus.txt.gz`                  |     413 |     436 |     4 |    21 |         1.7 | d         |
| `iscas89-s1238.txt.gz`                          |     416 |     625 |     2 |     2 |         1.9 | d         |
| `ecoli-transcript.txt.gz`                       |     423 |     519 |     3 |    10 |         1.8 | d         |
| `iscas89-s1423.txt.gz`                          |     423 |     554 |     2 |     4 |         1.9 | d         |
| *`muenchen-bahn.txt.gz`                         |     447 |     578 |     2 |     1 |         8.4 | **c !**   |
| `BioGrid-Bos-Taurus.txt.gz`                     |     454 |     424 |     3 |     6 |         1.7 | d         |
| `iscas89-s1488.txt.gz`                          |     463 |     779 |     3 |    10 |         2.5 | d         |
| `iscas89-s1494.txt.gz`                          |     473 |     796 |     3 |    10 |         2.4 | d         |
| `pigs.txt.gz`                                   |     492 |     592 |     2 |     6 |         2   | d         |
| `foodweb-caribbean.txt.gz`                      |     492 |    3313 |    13 |   154 |        34.2 | d         |
| `ratbrain.txt.gz`                               |     503 |   23030 |    67 |   126 |       128.5 | d         |
| `BioGrid-Human-Herpesvirus-8.txt.gz`            |     716 |     691 |     3 |     5 |         2.8 | d         |
| `codeminer.txt.gz`                              |     724 |    1015 |     4 |     6 |         3.3 | d         |
| `pollination-daphni.txt.gz`                     |     797 |    2933 |     9 |    44 |        14   | d         |
| `cpan-authors.txt.gz`                           |     839 |    2112 |     9 |    51 |         7.1 | d         |
| `columbia-mobility.txt.gz`                      |     863 |    4147 |     9 |    11 |         9.7 | d         |
| `columbia-social.txt.gz`                        |     863 |    7724 |    18 |    53 |        23.1 | d         |
| `unicode_languages.txt.gz`                      |     868 |    1255 |     4 |    18 |         4.2 | d         |
| `soc-wiki-Vote.txt.gz`                          |     889 |    2914 |     9 |    17 |         9   | d         |
| `link-pedigree.txt.gz`                          |     898 |    1125 |     2 |    13 |         3.8 | d         |
| `Opsahl-forum.txt.gz`                           |     899 |    7036 |    14 |    37 |        49.1 | d         |
| `dnc.csv`                                       |     906 |   10429 |    74 |    79 |        61.3 | d         |
| `pollination-uk.txt.gz`                         |     984 |   16712 |    35 |   201 |       741.3 | d         |
| `EU-email-core.txt.gz`                          |     986 |   16064 |    34 |   161 |       223.6 | d         |
| `roget-thesaurus.txt.gz`                        |    1010 |    3648 |     6 |     7 |        10.6 | d         |
| `bn-mouse_retina_1.txt.gz`                      |    1076 |   90811 |   121 |   402 |      8374.2 | d         |
| `BioGrid-Candida-Albicans-Sc5314.txt.gz`        |    1121 |    1609 |     9 |    63 |         5.6 | d         |
| `ia-email-univ.txt.gz`                          |    1133 |    5451 |    11 |    18 |        18.7 | d         |
| `BioGrid-Human-Immunodeficiency-Virus-1.txt.gz` |    1138 |    1319 |     3 |    42 |         4.9 | d         |
| `euroroad.txt.gz`                               |    1174 |    1417 |     2 |     3 |         5.5 | d         |
| `BioGrid-Far-Western.txt.gz`                    |    1199 |    1089 |     3 |    10 |         4.9 | d         |
| `polblogs.txt.gz`                               |    1224 |   16715 |    36 |   129 |       269.5 | d         |
| `BioGrid-Escherichia-Coli-K12-Mg1655.txt.gz`    |    1273 |    1889 |     5 |    12 |         6.7 | d         |
| `web-google.txt.gz`                             |    1299 |    2773 |    17 |    17 |         8.3 | d         |
| `munin.txt.gz`                                  |    1324 |    1397 |     3 |    28 |         6.2 | d         |
| `iscas89-s5378.txt.gz`                          |    1411 |    1639 |     3 |     4 |         6.2 | d         |
| *`diseasome.txt.gz`                             |    1419 |    2738 |    11 |     8 |         8.7 | **c !**   |
| `BioGrid-Dosage-Growth-Defect.txt.gz`           |    1447 |    2193 |     5 |    69 |         8.7 | d         |
| *`netscience.txt.gz`                            |    1461 |    2742 |    19 |     5 |        10.4 | **c !**   |
| `chicago.txt.gz`                                |    1467 |    1298 |     1 |     1 |         5.7 | d         |
| `pollination-carlinville.txt.gz`                |    1500 |   15255 |    18 |    66 |       167.5 | d         |
| `bitcoin-otc-negative.txt.gz`                   |    1606 |    3259 |    16 |    38 |        14.7 | d         |
| `yeast.csv`                                     |    1622 |    9070 |    40 |    59 |        33.2 | d         |
| `BioGrid-Fret.txt.gz`                           |    1700 |    2395 |    19 |    37 |         9.4 | d         |
| `bible.csv`                                     |    1773 |    9131 |    15 |    32 |        32.9 | d         |
| `BioGrid-Dosage-Lethality.txt.gz`               |    1776 |    2289 |     4 |    32 |         8.6 | d         |
| `bn-fly-drosophila_medulla_1.txt.gz`            |    1781 |    8911 |    18 |    41 |        49.2 | d         |
| `BioGrid-Affinity-Capture-Luminescence.txt.gz`  |    1840 |    2312 |     6 |    37 |         8.8 | d         |
| `DNC-emails.txt.gz`                             |    1866 |    4384 |    17 |    73 |        16.5 | d         |
| `wikipedia-norm.txt.gz`                         |    1881 |   15372 |    22 |   137 |       138.2 | d         |
| `ca-csphd.csv`                                  |    1882 |    1740 |     2 |     2 |         8.6 | d         |
| `exnet-water.txt.gz`                            |    1893 |    2416 |     2 |     2 |         8.7 | d         |
| `Opsahl-socnet.txt.gz`                          |    1899 |   13838 |    20 |   111 |       178.9 | d         |
| `Y2H_union.txt.gz`                              |    1966 |    2705 |     4 |    29 |        10   | d         |
| `iscas89-s9234.txt.gz`                          |    1985 |    2370 |     4 |     9 |         8.7 | d         |
| `NZ_legal.txt.gz`                               |    2141 |   15739 |    25 |   128 |       176.8 | d         |
| `BioGrid-Co-Crystal-Structure.txt.gz`           |    2291 |    2021 |     5 |     5 |         9.2 | d         |
| `Yeast.txt.gz`                                  |    2361 |    6646 |    10 |    21 |        23   | d         |
| `soc-hamsterster.txt.gz`                        |    2426 |   16630 |    24 |    76 |        93.8 | d         |
| `iscas89-s13207.txt.gz`                         |    2492 |    3406 |     4 |    30 |        12.5 | d         |
| `moreno_health.txt.gz`                          |    2539 |   10455 |     7 |    16 |        33.6 | d         |
| `minnesota.txt.gz`                              |    2642 |    3303 |     2 |     2 |        13.4 | d         |
| `ODLIS.txt.gz`                                  |    2900 |   16377 |    12 |    85 |        96.6 | d         |
| `openflights.txt.gz`                            |    2939 |   15677 |    28 |   110 |       139.5 | d         |
| `iscas89-s15850.txt.gz`                         |    3247 |    4004 |     4 |    15 |        15.2 | d         |
| `BioGrid-Dosage-Rescue.txt.gz`                  |    3380 |    6444 |     7 |    34 |        22.8 | d         |
| `BioGrid-Co-Localization.txt.gz`                |    3543 |    4452 |     6 |    24 |        17.7 | d         |
| `twittercrawl.txt.gz`                           |    3656 |  154824 |   142 |   506 |     18880   | d         |
| `BioGrid-Escherichia-Coli-K12-W3110.txt.gz`     |    4063 |  181620 |   156 |   441 |     54345.7 | d         |
| *`boards_gender_1m.txt.gz`                      |    4134 |   19993 |    25 |    19 |        79.2 | **c !**   |
| `boards_gender_2m.txt.gz`                       |    4220 |    5598 |     4 |    20 |        21.2 | d         |
| `web-EPA.txt.gz`                                |    4271 |    8909 |     6 |    63 |        32.3 | d         |
| `BioGrid-Co-Purification.txt.gz`                |    4326 |    5970 |    12 |    70 |        44.5 | d         |
| `ingredients.txt.gz`                            |    4372 |  430460 |   295 |   835 |     73038.5 | d         |
| *`power.csv`                                    |    4941 |    6594 |     5 |     4 |        25.9 | **c !**   |
| `advogato.txt.gz`                               |    5155 |   39285 |    25 |   215 |       498.9 | d         |
| `soc-advogato.txt.gz`                           |    5167 |   39432 |    25 |   217 |       515.7 | d         |
| *`ca-GrQc.csv`                                  |    5242 |   14484 |    43 |    42 |        59.6 | **c !**   |
| `facebook.csv`                                  |    5524 |   94218 |    39 |   170 |      1279.7 | d         |
| `bitcoin-otc-positive.txt.gz`                   |    5573 |   18591 |    20 |    91 |       120.7 | d         |
| `JUNG-javax.txt.gz`                             |    6120 |   50290 |    65 |   618 |      1691.9 | d         |
| `web-california.txt.gz`                         |    6175 |   15969 |    11 |    68 |        72.9 | d         |
| `reactome.txt.gz`                               |    6327 |  146160 |   176 |   445 |      4548.4 | d         |
| `BioGrid-Caenorhabditis-Elegans.txt.gz`         |    6394 |   23646 |    64 |    81 |       116.8 | d         |
| `JDK_dependency.txt.gz`                         |    6434 |   53658 |    65 |   706 |      1702.5 | d         |
| `as20000102.txt.gz`                             |    6474 |   12572 |    12 |    42 |        43.6 | d         |
| `zewail.txt.gz`                                 |    6651 |   54182 |    18 |    98 |       391.2 | d         |
| `ia-reality.txt.gz`                             |    6809 |    7680 |     5 |    18 |        30.6 | d         |
| `wiki-Vote.csv`                                 |    7115 |  100762 |    53 |   440 |      5637.3 | d         |
| `eva-corporate.txt.gz`                          |    7253 |    6711 |     3 |     6 |        52.3 | d         |
| `chess.txt.gz`                                  |    7301 |   55899 |    29 |    63 |       628.4 | d         |
| `bio-dmela.csv`                                 |    7393 |   25569 |    11 |    71 |       124.9 | d         |
| `lederberg.txt.gz`                              |    8324 |   41532 |    15 |   174 |       230.1 | d         |
| `BioGrid-Biochemical-Activity.txt.gz`           |    8620 |   17746 |    11 |   181 |       104.9 | d         |
| `iscas89-s38584.txt.gz`                         |    9193 |   12573 |     4 |    12 |        50.8 | d         |
| `BioGrid-Drosophila-Melanogaster.txt.gz`        |    9330 |   60556 |    83 |   114 |       505.6 | d         |
| `iscas89-s38417.txt.gz`                         |    9500 |   10635 |     4 |    11 |        60.5 | d         |
| `BioGrid-Arabidopsis-Thaliana-Columbia.txt.gz`  |   10417 |   47916 |    26 |   384 |       842.5 | d         |
| `p2p-Gnutella04.txt.gz`                         |   10876 |   39994 |     7 |    28 |       181.4 | d         |
| `BioGrid-Co-Fractionation.txt.gz`               |   11017 |   56354 |    83 |    83 |       356.8 | d         |
| `AS-oregon-1.txt.gz`                            |   11174 |   23409 |    17 |    74 |       103.7 | d         |
| `AS-oregon-2.txt.gz`                            |   11461 |   32730 |    31 |   117 |       190   | d         |
| *`ca-HepPh.txt.gz`                              |   12006 |  118489 |   238 |    89 |      1436.9 | **c !**   |
| `ukroad.txt.gz`                                 |   12378 |   15641 |     3 |     4 |        65.8 | d         |
| *`iscas89-s35932.txt.gz`                        |   12515 |   15961 |     2 |     1 |      7107   | **c !**   |
| `foldoc.txt.gz`                                 |   13356 |   91471 |    12 |    62 |       692.3 | d         |
| `BioGrid-Affinity-Capture-Rna.txt.gz`           |   13765 |   42815 |    54 |  1629 |      1346.2 | d         |
| `escorts.txt.gz`                                |   16730 |   39044 |    11 |    68 |       296.6 | d         |
| `ca-astroph.csv`                                |   18772 |  198050 |    56 |    60 |      2159   | d         |
| `marvel.txt.gz`                                 |   19428 |   96662 |    18 |   744 |      2054.8 | d         |
| `BioGrid-Affinity-Capture-Western.txt.gz`       |   21028 |   64046 |    17 |    92 |       411.4 | d         |
| `as-22july06.txt.gz`                            |   22963 |   48436 |    25 |   217 |       291.1 | d         |
| `edinburgh_associative_thesaurus.txt.gz`        |   23132 |  297094 |    34 |   204 |     10011.6 | d         |
| `ca-CondMat.txt.gz`                             |   23133 |   93439 |    25 |    26 |       400.5 | d         |
| `cora_citation.txt.gz`                          |   23166 |   89157 |    13 |    69 |       452   | d         |
| `google+.txt.gz`                                |   23628 |   39194 |    12 |   489 |       333.6 | d         |
| `soc-gplus.txt.gz`                              |   23628 |   39194 |    12 |   489 |       337.6 | d         |
| `BioGrid-Homo-Sapiens.txt.gz`                   |   24093 |  369767 |    71 |   801 |     30879.9 | d         |
| `cit-HepTh.txt.gz`                              |   27769 |  352285 |    37 |  1669 |      7574.2 | d         |
| `digg.txt.gz`                                   |   30398 |   85155 |     9 |    19 |       660.4 | d         |
| `linux.txt.gz`                                  |   30834 |  213217 |    23 |  4835 |     20399.7 | d         |
| `BioGrid-Chemicals.txt.gz`                      |   33266 |   28093 |     1 |     1 |       168.6 | d         |
| `cit-HepPh.txt.gz`                              |   34546 |  420877 |    30 |   299 |      5934.3 | d         |
| `email-Enron.txt.gz`                            |   36692 |  183831 |    43 |   186 |      3401.9 | d         |
| `BioGrid-Affinity-Capture-Ms.txt.gz`            |   40495 |  321887 |    58 |   842 |     14957.6 | d         |
| `slashdot_threads.txt.gz`                       |   51083 |  116573 |    14 |    64 |      1054   | d         |
| `deezer.txt.gz`                                 |   54573 |  498202 |    21 |    82 |      5433   | d         |
| `loc-brightkite_edges.txt.gz`                   |   58228 |  214078 |    52 |   183 |      2002.2 | d         |
| `facebook-links.txt.gz`                         |   63731 |  817090 |    52 |   232 |     23999.7 | d         |
| `soc-Epinions1.txt.gz`                          |   75879 |  405740 |    67 |   550 |     26000.2 | d         |
| `soc-Slashdot0811.txt.gz`                       |   77360 |  469180 |    54 |   617 |     18022.7 | d         |
| `NYClimateMarch2014.txt.gz`                     |  102378 |  327080 |    34 |  1036 |     11087.1 | d         |
| `gowalla.txt.gz`                                |  196591 |  950327 |    51 |  1131 |     20574.4 | d         |
| `bahamas.txt.gz`                                |  219856 |  246291 |     6 |    57 |      1954.2 | d         |
| `location.txt.gz`                               |  225486 |  293697 |     5 |   853 |      3212.2 | d         |
| `offshore.txt.gz`                               |  278877 |  505965 |    13 |  5697 |     15387.7 | d         |
| `Cannes2013.txt.gz`                             |  438089 |  835892 |    27 |  3167 |     14272   | d         |
| `actor_movies.txt.gz`                           |  511463 | 1470404 |    14 |   216 |     14672.1 | d         |
| `paradise.txt.gz`                               |  542102 |  794545 |    23 |  4241 |     10838.4 | d         |
| `panama.txt.gz`                                 |  556686 |  702437 |    62 |  1947 |      7294.5 | d         |
| `countries.txt.gz`                              |  592414 |  624402 |     6 | 11047 |     15818.4 | d         |
| `teams.txt.gz`                                  |  935591 | 1366466 |     9 |   350 |     24349.7 | d         |
| `mag_geology_coauthor.txt.gz`                   | 2852295 | 4448428 |    13 |   192 |     53662.4 | d         |
