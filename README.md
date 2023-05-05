# FPT in P for c-closure, parameterized by degeneracy

We compute the c-closure of a graph parameterized by its degeneracy.

If the degeneracy is smaller than the c-closure, we compute the
c-closure, and output a witness in P-parameterized time $O(d^3 \cdot n)$.

In the case where the c-closure is smaller than the degeneracy, we fall
back to a quadratic time algorithm, $O(d \cdot n^2)$.

However, our analyses show that in general, degeneracy is in fact
smaller than the c-closure.

## Some experiments

We ran our algorithm on all the datasets from
[_network-corpus_](https://github.com/microgravitas/network-corpus/) and
some from the folder `dataset` in this repository, the results are
below.  We note that 3 of 229 graphs used more than 25 minutes, while
180 graphs were solved in less than a second (in Python).

Only 5 of 229 graphs used more than a minute, and they all had degeneracy smaller than c-closure:

* `BioGrid-All`  $n=75550, m=1316843, d=164, c=1791$  **6 min**
* `livemocha`  $n=104103, m=2193083, d=92, c=1128$   **7 min**
* `tv_tropes`  $n=152093, m=3232134, d=115, c=2654$   **25 min**
* `movielens_1m` $n=9746, m=1000209, d=221, c=2355$     **37 min**
* `dogster_friendships` $n=426820, m=8543549, d=248, c=32803$  **1 h 49 min**


### Analysis

| name                                     |      n |       m |   deg |   c-c |    time ms | smaller |
|------------------------------------------|--------|---------|-------|-------|------------|---------|
| `iscas89-s27`                            |      9 |       8 |     1 |     1 |      1.3   | d       |
| `wafa-padgett`                           |     15 |      27 |     3 |     3 |      1.4   | d       |
| `BioGrid-Human-Immunodeficiency-Virus-2` |     19 |      15 |     1 |     1 |      2.6   | d       |
| `wafa-hightech`                          |     21 |     159 |    12 |    16 |      2     | d       |
| `wafa-ceos`                              |     26 |      93 |     5 |     6 |      1.6   | d       |
| `BioGrid-Dictyostelium-Discoideum-Ax4`   |     27 |      20 |     1 |     1 |      2.4   | d       |
| `seventh-graders`                        |     29 |     250 |    13 |    17 |      2.7   | d       |
| `karate`                                 |     34 |      78 |     4 |     6 |      1.9   | d       |
| `karate`                                 |     34 |      78 |     4 |     6 |      1.9   | d       |
| `windsurfers`                            |     43 |     336 |    11 |    16 |      2.5   | d       |
| `BioGrid-Glycine-Max`                    |     44 |      39 |     2 |     2 |      3.4   | d       |
| `wafa-eies`                              |     45 |     652 |    24 |    30 |      3.8   | d       |
| `bergen`                                 |     53 |     272 |     9 |    12 |      4     | d       |
| `iscas89-s208.1`                         |     61 |      67 |     2 |     2 |      1.8   | d       |
| `dolphins`                               |     62 |     159 |     4 |     4 |     40.6   | d       |
| `BioGrid-Emericella-Nidulans-Fgsc-A4`    |     64 |      62 |     2 |     2 |      3.2   | d       |
| *`train_bombing`                         |     64 |     243 |    10 |     8 |      4     | **c_!** |
| `pollination-tenerife`                   |     68 |     129 |     4 |    10 |      2     | d       |
| `BioGrid-Cricetulus-Griseus`             |     69 |      57 |     1 |     1 |      2.8   | d       |
| *`Noordin-terror-relation`               |     70 |     251 |    11 |    10 |      2.1   | **c_!** |
| *`mg_watchmen`                           |     76 |     201 |     7 |     5 |      2.3   | **c_!** |
| *`lesmiserables`                         |     77 |     254 |     9 |     8 |      2.6   | **c_!** |
| `mg_godfatherII`                         |     78 |     219 |     8 |     8 |      2.2   | d       |
| `iscas89-s298`                           |     92 |     131 |     2 |     5 |      2     | d       |
| *`mg_forrestgump`                        |     94 |     271 |     8 |     3 |      2.7   | **c_!** |
| `win95pts`                               |     99 |     112 |     2 |     3 |      2     | d       |
| `iscas89-s344`                           |    100 |     122 |     2 |     4 |      2     | d       |
| `iscas89-s641`                           |    100 |     144 |     3 |     6 |      2.1   | d       |
| `movies`                                 |    101 |     192 |     3 |     5 |      4.2   | d       |
| `iscas89-s349`                           |    102 |     127 |     2 |     4 |      2.1   | d       |
| `polbooks`                               |    105 |     441 |     6 |    15 |      2.9   | d       |
| *`mg_casino`                             |    109 |     326 |     9 |     7 |      3     | **c_!** |
| `adjnoun`                                |    112 |     425 |     6 |    13 |      3.9   | d       |
| `word_adjacencies`                       |    112 |     425 |     6 |    13 |      3.4   | d       |
| `hypertext_2009`                         |    113 |    2196 |    28 |    53 |     19.5   | d       |
| `iscas89-s386`                           |    114 |     200 |     3 |    12 |      2.5   | d       |
| `football`                               |    115 |     613 |     8 |     9 |      4     | d       |
| `StackOverflow-tags`                     |    115 |     245 |     6 |     6 |      2.4   | d       |
| `iscas89-s382`                           |    116 |     168 |     2 |     4 |      2.6   | d       |
| `iscas89-s400`                           |    121 |     182 |     2 |     4 |      2.3   | d       |
| `BioGrid-Human-Herpesvirus-5`            |    121 |     107 |     1 |     1 |      3.3   | d       |
| `Noordin-terror-loc`                     |    127 |     190 |     3 |     6 |      2.2   | d       |
| `iscas89-s420.1`                         |    129 |     145 |     2 |     2 |      2.3   | d       |
| `Noordin-terror-orgas`                   |    129 |     181 |     3 |    10 |      2.1   | d       |
| `celegans`                               |    131 |     687 |     8 |    13 |      4.3   | d       |
| `iscas89-s444`                           |    134 |     206 |     2 |     4 |      2.7   | d       |
| `BioGrid-Hepatitus-C-Virus`              |    136 |     134 |     1 |     1 |      3.6   | d       |
| `iscas89-s713`                           |    137 |     180 |     3 |     6 |      2.4   | d       |
| `capitalist`                             |    139 |    1071 |    19 |    34 |      8.1   | d       |
| `american_revolution`                    |    141 |     160 |     3 |     9 |     11.4   | d       |
| `foodweb-otago`                          |    141 |     832 |    14 |    35 |      8.1   | d       |
| `BioGrid-Canis-Familiaris`               |    143 |     125 |     2 |     2 |      3.8   | d       |
| `iscas89-s526n`                          |    159 |     268 |     3 |     8 |      2.8   | d       |
| `iscas89-s526`                           |    160 |     270 |     3 |     8 |      2.9   | d       |
| `iscas89-s510`                           |    172 |     251 |     2 |     2 |      2.8   | d       |
| `BioGrid-Human-Papillomavirus-16`        |    173 |     186 |     2 |    17 |      4.3   | d       |
| `BioGrid-Human-Herpesvirus-1`            |    178 |     208 |     3 |    10 |      6.2   | d       |
| `CoW-interstate`                         |    182 |     319 |     4 |    12 |      7.2   | d       |
| `jazz`                                   |    198 |    2742 |    29 |    41 |     15.9   | d       |
| `arenasjazz`                             |    198 |    2742 |    29 |    41 |     15.6   | d       |
| `mousebrain`                             |    213 |   16089 |   111 |   178 |    577.8   | d       |
| `residence_hall`                         |    217 |    1839 |    11 |    17 |     10.4   | d       |
| `airlines`                               |    235 |    1297 |    13 |    42 |      8.9   | d       |
| `sp_data_school_day_2`                   |    238 |    5539 |    33 |    53 |     61     | d       |
| `iscas89-s820`                           |    239 |     480 |     3 |    15 |      3.9   | d       |
| `rhesusbrain`                            |    242 |    3054 |    19 |    37 |     23.1   | d       |
| `iscas89-s832`                           |    245 |     498 |     3 |    18 |      4.1   | d       |
| `BioGrid-Danio-Rerio`                    |    261 |     266 |     3 |     3 |      4.2   | d       |
| `iscas89-s838.1`                         |    265 |     301 |     2 |     2 |      3.3   | d       |
| `haggle`                                 |    274 |    2124 |    39 |    40 |     12.9   | d       |
| `celegans`                               |    297 |    2148 |    10 |    40 |     14.1   | d       |
| `BioGrid-Human-Herpesvirus-4`            |    323 |     326 |     2 |     5 |      5.4   | d       |
| *`hex`                                   |    331 |     930 |     3 |     2 |     24.1   | **c_!** |
| `iscas89-s953`                           |    332 |     454 |     2 |     3 |      4.1   | d       |
| `autobahn`                               |    374 |     478 |     2 |     2 |      5.9   | d       |
| `photoviz_dynamic`                       |    376 |     610 |     4 |    12 |      6.5   | d       |
| `iscas89-s1196`                          |    377 |     537 |     2 |     2 |      4.7   | d       |
| *`ca-netscience`                         |    379 |     914 |     8 |     4 |      6.5   | **c_!** |
| `ia-infect-dublin`                       |    410 |    2765 |    17 |    22 |     14.8   | d       |
| `infectious`                             |    410 |    2765 |    17 |    22 |     14.4   | d       |
| `BioGrid-Gallus-Gallus`                  |    413 |     436 |     4 |    21 |      5.9   | d       |
| `iscas89-s1238`                          |    416 |     625 |     2 |     2 |      5.7   | d       |
| `iscas89-s1423`                          |    423 |     554 |     2 |     4 |      5.1   | d       |
| `ecoli-transcript`                       |    423 |     519 |     3 |    10 |      5.8   | d       |
| *`muenchen-bahn`                         |    447 |     578 |     2 |     1 |     11.4   | **c_!** |
| `BioGrid-Bos-Taurus`                     |    454 |     424 |     3 |     6 |      6.2   | d       |
| `iscas89-s1488`                          |    463 |     779 |     3 |    10 |      6.2   | d       |
| `iscas89-s1494`                          |    473 |     796 |     3 |    10 |      6.2   | d       |
| `foodweb-caribbean`                      |    492 |    3313 |    13 |   154 |     42.3   | d       |
| `pigs`                                   |    492 |     592 |     2 |     6 |      5     | d       |
| `ratbrain`                               |    503 |   23030 |    67 |   126 |    191.9   | d       |
| `BioGrid-Human-Herpesvirus-8`            |    716 |     691 |     3 |     5 |      8.1   | d       |
| `codeminer`                              |    724 |    1015 |     4 |     6 |      9.8   | d       |
| `pollination-daphni`                     |    797 |    2933 |     9 |    44 |     22.7   | d       |
| `cpan-authors`                           |    839 |    2112 |     9 |    51 |     15.4   | d       |
| `columbia-mobility`                      |    863 |    4147 |     9 |    11 |     21.9   | d       |
| `columbia-social`                        |    863 |    7724 |    18 |    53 |     43.3   | d       |
| `unicode_languages`                      |    868 |    1255 |     4 |    18 |      9.9   | d       |
| `soc-wiki-Vote`                          |    889 |    2914 |     9 |    17 |     17.4   | d       |
| `link-pedigree`                          |    898 |    1125 |     2 |    13 |      9.2   | d       |
| `Opsahl-forum`                           |    899 |    7036 |    14 |    37 |     62.3   | d       |
| `dnc`                                    |    906 |   10429 |    74 |    79 |     85.4   | d       |
| `EU-email-core`                          |    986 |   16064 |    34 |   161 |    256.5   | d       |
| `eu-emails`                              |   1005 |   16064 |    34 |   161 |    275.9   | d       |
| `roget-thesaurus`                        |   1010 |    3648 |     6 |     7 |     20.8   | d       |
| `bn-mouse_retina_1`                      |   1076 |   90811 |   121 |   402 |   8592.4   | d       |
| `BioGrid-Candida-Albicans-Sc5314`        |   1121 |    1609 |     9 |    63 |     14.4   | d       |
| `ia-email-univ`                          |   1133 |    5451 |    11 |    18 |     32.2   | d       |
| `BioGrid-Human-Immunodeficiency-Virus-1` |   1138 |    1319 |     3 |    42 |     13     | d       |
| `euroroad`                               |   1174 |    1417 |     2 |     3 |     11.7   | d       |
| `BioGrid-Far-Western`                    |   1199 |    1089 |     3 |    10 |     29.8   | d       |
| `polblogs`                               |   1224 |   16715 |    36 |   129 |    302.6   | d       |
| `BioGrid-Escherichia-Coli-K12-Mg1655`    |   1273 |    1889 |     5 |    12 |     15.3   | d       |
| `web-google`                             |   1299 |    2773 |    17 |    17 |     18.3   | d       |
| `munin`                                  |   1324 |    1397 |     3 |    28 |     11.7   | d       |
| `iscas89-s5378`                          |   1411 |    1639 |     3 |     4 |     13.9   | d       |
| *`diseasome`                             |   1419 |    2738 |    11 |     8 |     19.7   | **c_!** |
| `BioGrid-Dosage-Growth-Defect`           |   1447 |    2193 |     5 |    69 |     19.2   | d       |
| *`netscience`                            |   1461 |    2742 |    19 |     5 |     18.5   | **c_!** |
| `chicago`                                |   1467 |    1298 |     1 |     1 |     14.6   | d       |
| `pollination-carlinville`                |   1500 |   15255 |    18 |    66 |    199.5   | d       |
| `bitcoin-otc-negative`                   |   1606 |    3259 |    16 |    38 |     27.7   | d       |
| `yeast`                                  |   1622 |    9070 |    40 |    59 |     51.5   | d       |
| `BioGrid-Fret`                           |   1700 |    2395 |    19 |    37 |     20.8   | d       |
| `bible`                                  |   1773 |    9131 |    15 |    32 |     56.5   | d       |
| `BioGrid-Dosage-Lethality`               |   1776 |    2289 |     4 |    32 |     20     | d       |
| `bn-fly-drosophila_medulla_1`            |   1781 |    8911 |    18 |    41 |     75.3   | d       |
| `BioGrid-Affinity-Capture-Luminescence`  |   1840 |    2312 |     6 |    37 |     20.6   | d       |
| `DNC-emails`                             |   1866 |    4384 |    17 |    73 |     32.9   | d       |
| `wikipedia-norm`                         |   1881 |   15372 |    22 |   137 |    193.2   | d       |
| `ca-csphd`                               |   1882 |    1740 |     2 |     2 |     17.2   | d       |
| `exnet-water`                            |   1893 |    2416 |     2 |     2 |     18.5   | d       |
| `Opsahl-socnet`                          |   1899 |   13838 |    20 |   111 |    195.8   | d       |
| `Y2H_union`                              |   1966 |    2705 |     4 |    29 |     21.5   | d       |
| `iscas89-s9234`                          |   1985 |    2370 |     4 |     9 |     33.1   | d       |
| `NZ_legal`                               |   2141 |   15739 |    25 |   128 |    216     | d       |
| `BioGrid-Co-Crystal-Structure`           |   2291 |    2021 |     5 |     5 |     21.3   | d       |
| `Yeast`                                  |   2361 |    6646 |    10 |    21 |     45.5   | d       |
| `soc-hamsterster`                        |   2426 |   16630 |    24 |    76 |    129     | d       |
| `soc-hamsterster`                        |   2426 |   16630 |    24 |    76 |    165     | d       |
| `iscas89-s13207`                         |   2492 |    3406 |     4 |    30 |     25.9   | d       |
| `moreno_health`                          |   2539 |   10455 |     7 |    16 |     57.8   | d       |
| `minnesota`                              |   2642 |    3303 |     2 |     2 |     23.8   | d       |
| `ODLIS`                                  |   2900 |   16377 |    12 |    85 |    273.3   | d       |
| `openflights`                            |   2939 |   15677 |    28 |   110 |    140.9   | d       |
| `iscas89-s15850`                         |   3247 |    4004 |     4 |    15 |     32.6   | d       |
| `BioGrid-Dosage-Rescue`                  |   3380 |    6444 |     7 |    34 |     68.1   | d       |
| `BioGrid-Co-Localization`                |   3543 |    4452 |     6 |    24 |     35.2   | d       |
| `twittercrawl`                           |   3656 |  154824 |   142 |   506 |  18892.4   | d       |
| `BioGrid-Escherichia-Coli-K12-W3110`     |   4063 |  181620 |   156 |   441 |  54881.1   | d       |
| *`boards_gender_1m`                      |   4134 |   19993 |    25 |    19 |    124.4   | **c_!** |
| `boards_gender_2m`                       |   4220 |    5598 |     4 |    20 |     44.9   | d       |
| `web-EPA`                                |   4271 |    8909 |     6 |    63 |     59     | d       |
| `BioGrid-Co-Purification`                |   4326 |    5970 |    12 |    70 |     51.4   | d       |
| *`power`                                 |   4941 |    6594 |     5 |     4 |     47.8   | **c_!** |
| `advogato`                               |   5155 |   39285 |    25 |   215 |    629.7   | d       |
| `soc-advogato`                           |   5167 |   39432 |    25 |   217 |    651.4   | d       |
| *`ca-GrQc`                               |   5242 |   14484 |    43 |    42 |    111.1   | **c_!** |
| `facebook`                               |   5524 |   94218 |    39 |   170 |   1668.9   | d       |
| `bitcoin-otc-positive`                   |   5573 |   18591 |    20 |    91 |    291.2   | d       |
| `JUNG-javax`                             |   6120 |   50290 |    65 |   618 |   1976.6   | d       |
| `web-california`                         |   6175 |   15969 |    11 |    68 |   1499.2   | d       |
| `reactome`                               |   6327 |  146160 |   176 |   445 |   4830.9   | d       |
| `BioGrid-Caenorhabditis-Elegans`         |   6394 |   23646 |    64 |    81 |    210.2   | d       |
| `JDK_dependency`                         |   6434 |   53658 |    65 |   706 |   2022.4   | d       |
| `as20000102`                             |   6474 |   12572 |    12 |    42 |     97.3   | d       |
| `soc-advogato`                           |   6551 |   39432 |    25 |   217 |    657.7   | d       |
| `zewail`                                 |   6651 |   54182 |    18 |    98 |    555     | d       |
| `ia-reality`                             |   6809 |    7680 |     5 |    18 |     61.8   | d       |
| `wiki-Vote`                              |   7115 |  100762 |    53 |   440 |   6053.6   | d       |
| `eva-corporate`                          |   7253 |    6711 |     3 |     6 |    146.2   | d       |
| `chess`                                  |   7301 |   55899 |    29 |    63 |    779     | d       |
| `bio-dmela`                              |   7393 |   25569 |    11 |    71 |    212.2   | d       |
| `lederberg`                              |   8324 |   41532 |    15 |   174 |    368.5   | d       |
| `BioGrid-Biochemical-Activity`           |   8620 |   17746 |    11 |   181 |    169.1   | d       |
| `iscas89-s38584`                         |   9193 |   12573 |     4 |    12 |     99.7   | d       |
| `BioGrid-Drosophila-Melanogaster`        |   9330 |   60556 |    83 |   114 |    657.5   | d       |
| `iscas89-s38417`                         |   9500 |   10635 |     4 |    11 |    463.1   | d       |
| `movielens_1m`                           |   9746 | 1000209 |   221 |  2355 |2268845.0   | d       |
| `BioGrid-Arabidopsis-Thaliana-Columbia`  |  10417 |   47916 |    26 |   384 |   1363.6   | d       |
| `p2p-Gnutella04`                         |  10876 |   39994 |     7 |    28 |    279.7   | d       |
| `BioGrid-Co-Fractionation`               |  11017 |   56354 |    83 |    83 |    521.7   | d       |
| `AS-oregon-1`                            |  11174 |   23409 |    17 |    74 |    217.2   | d       |
| `AS-oregon-2`                            |  11461 |   32730 |    31 |   117 |    326.8   | d       |
| *`ca-HepPh`                              |  12006 |  118489 |   238 |    89 |   1744.2   | **c_!** |
| *`iscas89-s35932`                        |  12515 |   15961 |     2 |     1 |   7429.4   | **c_!** |
| `foldoc`                                 |  13356 |   91471 |    12 |    62 |    664.2   | d       |
| `BioGrid-Affinity-Capture-Rna`           |  13765 |   42815 |    54 |  1629 |   1639.8   | d       |
| `ca-astroph`                             |  18772 |  198050 |    56 |    60 |   3208.8   | d       |
| `marvel`                                 |  19428 |   96662 |    18 |   744 |   2372.6   | d       |
| `BioGrid-Affinity-Capture-Western`       |  21028 |   64046 |    17 |    92 |    633     | d       |
| `as-22july06`                            |  22963 |   48436 |    25 |   217 |    528.5   | d       |
| `internet-as`                            |  22963 |   48436 |    25 |   217 |    586.9   | d       |
| `edinburgh_associative_thesaurus`        |  23132 |  297094 |    34 |   204 |  10993.2   | d       |
| `ca-CondMat`                             |  23133 |   93439 |    25 |    26 |    711.1   | d       |
| `cora_citation`                          |  23166 |   89157 |    13 |    69 |    840.3   | d       |
| `google+`                                |  23628 |   39194 |    12 |   489 |    815.9   | d       |
| `soc-gplus`                              |  23628 |   39194 |    12 |   489 |    689.6   | d       |
| `BioGrid-Homo-Sapiens`                   |  24093 |  369767 |    71 |   801 |  32416.4   | d       |
| `cit-HepTh`                              |  27769 |  352285 |    37 |  1669 |   8872.6   | d       |
| `digg`                                   |  30398 |   85155 |     9 |    19 |    802.1   | d       |
| `linux`                                  |  30834 |  213217 |    23 |  4835 |  22206.2   | d       |
| `BioGrid-Chemicals`                      |  33266 |   28093 |     1 |     1 |    348.4   | d       |
| `cit-HepPh`                              |  34546 |  420877 |    30 |   299 |   7410.7   | d       |
| `email-Enron`                            |  36692 |  183831 |    43 |   186 |   6788.4   | d       |
| `enron-email`                            |  36692 |  183831 |    43 |   186 |   4385.1   | d       |
| `BioGrid-Affinity-Capture-Ms`            |  40495 |  321887 |    58 |   842 |  17018.7   | d       |
| `slashdot_threads`                       |  51083 |  116573 |    14 |    64 |   1928.5   | d       |
| `soc-brightkite`                         |  56739 |  212945 |    52 |   183 |   2911     | d       |
| `loc-brightkite_edges`                   |  58228 |  214078 |    52 |   183 |   2915     | d       |
| `facebook-links`                         |  63731 |  817090 |    52 |   232 |  27457.2   | d       |
| `BioGrid-All`                            |  75550 | 1316843 |   164 |  1791 | 386464     | d       |
| `soc-Epinions1`                          |  75879 |  405740 |    67 |   550 |  26139     | d       |
| `soc-Slashdot0811`                       |  77360 |  469180 |    54 |   617 |  19902.3   | d       |
| `NYClimateMarch2014`                     | 102378 |  327080 |    34 |  1036 |  14087.6   | d       |
| `livemocha`                              | 104103 | 2193083 |    92 |  1128 | 464815     | d       |
| `tv_tropes`                              | 152093 | 3232134 |   115 |  2654 |1514352.9   | d       |
| `gowalla`                                | 196591 |  950327 |    51 |  1131 |  26795.7   | d       |
| `bahamas`                                | 219856 |  246291 |     6 |    57 |   4386     | d       |
| `location`                               | 225486 |  293697 |     5 |   853 |   7442.8   | d       |
| `offshore`                               | 278877 |  505965 |    13 |  5697 |  22075.1   | d       |
| `dogster_friendships`                    | 426820 | 8543549 |   248 | 32803 |6566609.0   | d       |
| `Cannes2013`                             | 438089 |  835892 |    27 |  3167 |  21601.1   | d       |
| `actor_movies`                           | 511463 | 1470404 |    14 |   216 |  23240.4   | d       |
| `paradise`                               | 542102 |  794545 |    23 |  4241 |  16142.9   | d       |
| `panama`                                 | 556686 |  702437 |    62 |  1947 |  12712.9   | d       |
| `countries`                              | 592414 |  624402 |     6 | 11047 |  28089.4   | d       |
| `teams`                                  | 935591 | 1366466 |     9 |   350 |  36653.5   | d       |

In this larger dataset, 17 of 229 networks have $c < d$, whereas in 212, we have $c \geq d$.

This means that $212/229 \approx 0.926 = 92.6\%$ are solved completely by _Case 1_.
