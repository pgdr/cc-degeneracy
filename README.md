# FPT in P for c-closure, parameterized by degeneracy

We compute the c-closure of a graph parameterized by its degeneracy.

If the degeneracy is smaller than the c-closure, we compute the
c-closure, and output a witness in P-parameterized time $O(d^3 \cdot n)$.

In the case where the c-closure is smaller than the degeneracy, we fall
back to a quadratic time algorithm, $O(d \cdot n^2)$.

However, our analyses show that in general, degeneracy is in fact
smaller than the c-closure.

## Some experiments


| name              |     n |      m |   deg |   c-c |   time (ms) | smaller   |
|-------------------|-------|--------|-------|-------|-------------|-----------|
| `karate`          |    34 |     78 |     4 |     6 |         0.6 | d         |
| `adjnoun`         |   112 |    425 |     6 |    13 |         2.5 | d         |
| `celegans`        |   131 |    687 |     8 |    13 |         3.4 | d         |
| `arenasjazz`      |   198 |   2742 |    29 |    41 |        15.4 | d         |
| `*ca-netscience`  |   379 |    914 |     8 |     4 |         5.5 | **c (!)** |
| `dnc`             |   906 |  10429 |    74 |    79 |       117.8 | d         |
| `eu-emails`       |  1005 |  16064 |    34 |   161 |       288.3 | d         |
| `yeast`           |  1622 |   9070 |    40 |    59 |        53.9 | d         |
| `bible`           |  1773 |   9131 |    15 |    32 |        57.4 | d         |
| `ca-csphd`        |  1882 |   1740 |     2 |     2 |        17.1 | d         |
| `soc-hamsterster` |  2426 |  16630 |    24 |    76 |       181.8 | d         |
| `*power`          |  4941 |   6594 |     5 |     4 |        50.6 | **c (!)** |
| `facebook`        |  5524 |  94218 |    39 |   170 |      1622.1 | d         |
| `soc-advogato`    |  6551 |  39432 |    25 |   217 |       673.5 | d         |
| `bio-dmela`       |  7393 |  25569 |    11 |    71 |       210.9 | d         |
| `*ca-heph`        | 12008 | 118489 |   238 |    89 |      2253.6 | **c (!)** |
| `ca-astroph`      | 18772 | 198050 |    56 |    60 |      3008.8 | d         |
| `internet-as`     | 22963 |  48436 |    25 |   217 |       576.5 | d         |
| `enron-email`     | 36692 | 183831 |    43 |   186 |      4472.5 | d         |
| `soc-brightkite`  | 56739 | 212945 |    52 |   183 |      2931.1 | d         |

As can be seen, in these 20 networks, only 3 have $c < d$.

## Experiments: network-corpus

We ran our algorithm on all the datasets from
[_network-corpus_](https://github.com/microgravitas/network-corpus/) and
the results are below.  We added a timeout on 600 seconds; 3 of 206 graphs timed out.


| name                                     |      n |       m |   deg |   c-c |   time (ms) | smaller   |
|------------------------------------------|--------|---------|-------|-------|-------------|-----------|
| `iscas89-s27`                            |      9 |       8 |     1 |     1 |         2.3 | d         |
| `wafa-padgett`                           |     15 |      27 |     3 |     3 |         2.9 | d         |
| `BioGrid-Human-Immunodeficiency-Virus-2` |     19 |      15 |     1 |     1 |         2.9 | d         |
| `wafa-hightech`                          |     21 |     159 |    12 |    16 |         4   | d         |
| `wafa-ceos`                              |     26 |      93 |     5 |     6 |         3.3 | d         |
| `BioGrid-Dictyostelium-Discoideum-Ax4`   |     27 |      20 |     1 |     1 |         2.9 | d         |
| `karate`                                 |     34 |      78 |     4 |     6 |         3.1 | d         |
| `windsurfers`                            |     43 |     336 |    11 |    16 |         4.9 | d         |
| `BioGrid-Glycine-Max`                    |     44 |      39 |     2 |     2 |         2.9 | d         |
| `wafa-eies`                              |     45 |     652 |    24 |    30 |         8.6 | d         |
| `bergen`                                 |     53 |     272 |     9 |    12 |         4.3 | d         |
| `iscas89-s208.1`                         |     61 |      67 |     2 |     2 |         3.1 | d         |
| `dolphins`                               |     62 |     159 |     4 |     4 |         5.7 | d         |
| `*trainbombing`                          |     64 |     243 |    10 |     8 |         4.2 | **c (!)** |
| `BioGrid-Emericella-Nidulans-Fgsc-A4`    |     64 |      62 |     2 |     2 |         3.3 | d         |
| `pollination-tenerife`                   |     68 |     129 |     4 |    10 |         3.5 | d         |
| `BioGrid-Cricetulus-Griseus`             |     69 |      57 |     1 |     1 |         3.8 | d         |
| `*Noordin-terror-relation`               |     70 |     251 |    11 |    10 |         4.4 | **c (!)** |
| `*mg_watchmen`                           |     76 |     201 |     7 |     5 |         3.7 | **c (!)** |
| `*lesmiserables`                         |     77 |     254 |     9 |     8 |         4.1 | **c (!)** |
| `mg_godfatherII`                         |     78 |     219 |     8 |     8 |         4   | d         |
| `iscas89-s298`                           |     92 |     131 |     2 |     5 |         3.6 | d         |
| `*mg_forrestgump`                        |     94 |     271 |     8 |     3 |         5.7 | **c (!)** |
| `win95pts`                               |     99 |     112 |     2 |     3 |         4.4 | d         |
| `iscas89-s641`                           |    100 |     144 |     3 |     6 |         3.8 | d         |
| `iscas89-s344`                           |    100 |     122 |     2 |     4 |         3.6 | d         |
| `movies`                                 |    101 |     192 |     3 |     5 |         4.7 | d         |
| `iscas89-s349`                           |    102 |     127 |     2 |     4 |         3.4 | d         |
| `polbooks`                               |    105 |     441 |     6 |    15 |         5.3 | d         |
| `*mg_casino`                             |    109 |     326 |     9 |     7 |         4.7 | **c (!)** |
| `word_adjacencies`                       |    112 |     425 |     6 |    13 |         5.3 | d         |
| `hypertext_2009`                         |    113 |    2196 |    28 |    53 |        33.2 | d         |
| `iscas89-s386`                           |    114 |     200 |     3 |    12 |         4   | d         |
| `StackOverflow-tags`                     |    115 |     245 |     6 |     6 |         5.8 | d         |
| `football`                               |    115 |     613 |     8 |     9 |         6.5 | d         |
| `iscas89-s382`                           |    116 |     168 |     2 |     4 |         4.5 | d         |
| `BioGrid-Human-Herpesvirus-5`            |    121 |     107 |     1 |     1 |         3.8 | d         |
| `iscas89-s400`                           |    121 |     182 |     2 |     4 |         3.5 | d         |
| `Noordin-terror-loc`                     |    127 |     190 |     3 |     6 |         4.5 | d         |
| `Noordin-terror-orgas`                   |    129 |     181 |     3 |    10 |         4.8 | d         |
| `iscas89-s420.1`                         |    129 |     145 |     2 |     2 |         4   | d         |
| `iscas89-s444`                           |    134 |     206 |     2 |     4 |         4.1 | d         |
| `BioGrid-Hepatitus-C-Virus`              |    136 |     134 |     1 |     1 |         3.8 | d         |
| `iscas89-s713`                           |    137 |     180 |     3 |     6 |         4.3 | d         |
| `capitalist`                             |    139 |    1071 |    19 |    34 |        11.3 | d         |
| `foodweb-otago`                          |    141 |     832 |    14 |    35 |        17.4 | d         |
| `american_revolution`                    |    141 |     160 |     3 |     9 |        15.6 | d         |
| `BioGrid-Canis-Familiaris`               |    143 |     125 |     2 |     2 |         3.8 | d         |
| `iscas89-s526n`                          |    159 |     268 |     3 |     8 |         4.2 | d         |
| `iscas89-s526`                           |    160 |     270 |     3 |     8 |         4.5 | d         |
| `iscas89-s510`                           |    172 |     251 |     2 |     2 |         4.5 | d         |
| `BioGrid-Human-Papillomavirus-16`        |    173 |     186 |     2 |    17 |         4.2 | d         |
| `BioGrid-Human-Herpesvirus-1`            |    178 |     208 |     3 |    10 |         4.3 | d         |
| `CoW-interstate`                         |    182 |     319 |     4 |    12 |         4.7 | d         |
| `jazz`                                   |    198 |    2742 |    29 |    41 |        29.6 | d         |
| `mousebrain`                             |    213 |   16089 |   111 |   178 |       954.7 | d         |
| `residence_hall`                         |    217 |    1839 |    11 |    17 |        29.3 | d         |
| `airlines`                               |    235 |    1297 |    13 |    42 |        11.3 | d         |
| `sp_data_school_day_2`                   |    238 |    5539 |    33 |    53 |       102.2 | d         |
| `iscas89-s820`                           |    239 |     480 |     3 |    15 |         5.7 | d         |
| `rhesusbrain`                            |    242 |    3054 |    19 |    37 |        38   | d         |
| `iscas89-s832`                           |    245 |     498 |     3 |    18 |         6.1 | d         |
| `BioGrid-Danio-Rerio`                    |    261 |     266 |     3 |     3 |         5   | d         |
| `iscas89-s838.1`                         |    265 |     301 |     2 |     2 |         5   | d         |
| `haggle`                                 |    274 |    2124 |    39 |    40 |        24.9 | d         |
| `celegans`                               |    297 |    2148 |    10 |    40 |        19.2 | d         |
| `BioGrid-Human-Herpesvirus-4`            |    323 |     326 |     2 |     5 |         5.6 | d         |
| `*hex`                                   |    331 |     930 |     3 |     2 |        26.3 | **c (!)** |
| `iscas89-s953`                           |    332 |     454 |     2 |     3 |         5.7 | d         |
| `autobahn`                               |    374 |     478 |     2 |     2 |         6.4 | d         |
| `photoviz_dynamic`                       |    376 |     610 |     4 |    12 |         8.1 | d         |
| `iscas89-s1196`                          |    377 |     537 |     2 |     2 |         6.4 | d         |
| `infectious`                             |    410 |    2765 |    17 |    22 |        21.8 | d         |
| `ia-infect-dublin`                       |    410 |    2765 |    17 |    22 |        22.8 | d         |
| `BioGrid-Gallus-Gallus`                  |    413 |     436 |     4 |    21 |         6.3 | d         |
| `iscas89-s1238`                          |    416 |     625 |     2 |     2 |         7   | d         |
| `iscas89-s1423`                          |    423 |     554 |     2 |     4 |         6.9 | d         |
| `ecoli-transcript`                       |    423 |     519 |     3 |    10 |         6.9 | d         |
| `*muenchen-bahn`                         |    447 |     578 |     2 |     1 |        13.7 | **c (!)** |
| `BioGrid-Bos-Taurus`                     |    454 |     424 |     3 |     6 |         6.4 | d         |
| `iscas89-s1488`                          |    463 |     779 |     3 |    10 |         8.2 | d         |
| `iscas89-s1494`                          |    473 |     796 |     3 |    10 |         8.3 | d         |
| `pigs`                                   |    492 |     592 |     2 |     6 |         7.3 | d         |
| `foodweb-caribbean`                      |    492 |    3313 |    13 |   154 |        54.9 | d         |
| `ratbrain`                               |    503 |   23030 |    67 |   126 |       492.7 | d         |
| `BioGrid-Human-Herpesvirus-8`            |    716 |     691 |     3 |     5 |         9   | d         |
| `codeminer`                              |    724 |    1015 |     4 |     6 |        10.3 | d         |
| `pollination-daphni`                     |    797 |    2933 |     9 |    44 |        29.9 | d         |
| `cpan-authors`                           |    839 |    2112 |     9 |    51 |        18.4 | d         |
| `columbia-social`                        |    863 |    7724 |    18 |    53 |        65.1 | d         |
| `columbia-mobility`                      |    863 |    4147 |     9 |    11 |        28.3 | d         |
| `unicode_languages`                      |    868 |    1255 |     4 |    18 |        23.1 | d         |
| `soc-wiki-Vote`                          |    889 |    2914 |     9 |    17 |        24.1 | d         |
| `link-pedigree`                          |    898 |    1125 |     2 |    13 |        11.5 | d         |
| `Opsahl-forum`                           |    899 |    7036 |    14 |    37 |        84.8 | d         |
| `EU-email-core`                          |    986 |   16064 |    34 |   161 |       362   | d         |
| `roget-thesaurus`                        |   1010 |    3648 |     6 |     7 |        26.9 | d         |
| `bn-mouse_retina_1`                      |   1076 |   90811 |   121 |   402 |     11342.9 | d         |
| `BioGrid-Candida-Albicans-Sc5314`        |   1121 |    1609 |     9 |    63 |        15.6 | d         |
| `ia-email-univ`                          |   1133 |    5451 |    11 |    18 |        43.3 | d         |
| `BioGrid-Human-Immunodeficiency-Virus-1` |   1138 |    1319 |     3 |    42 |        13.6 | d         |
| `euroroad`                               |   1174 |    1417 |     2 |     3 |        13.3 | d         |
| `BioGrid-Far-Western`                    |   1199 |    1089 |     3 |    10 |        13.5 | d         |
| `polblogs`                               |   1224 |   16715 |    36 |   129 |       414.1 | d         |
| `BioGrid-Escherichia-Coli-K12-Mg1655`    |   1273 |    1889 |     5 |    12 |        17.5 | d         |
| `web-google`                             |   1299 |    2773 |    17 |    17 |        23.9 | d         |
| `munin`                                  |   1324 |    1397 |     3 |    28 |        15.4 | d         |
| `iscas89-s5378`                          |   1411 |    1639 |     3 |     4 |        16.1 | d         |
| `*diseasome`                             |   1419 |    2738 |    11 |     8 |        21.9 | **c (!)** |
| `BioGrid-Dosage-Growth-Defect`           |   1447 |    2193 |     5 |    69 |        21.1 | d         |
| `*netscience`                            |   1461 |    2742 |    19 |     5 |        24.2 | **c (!)** |
| `chicago`                                |   1467 |    1298 |     1 |     1 |        16.8 | d         |
| `pollination-carlinville`                |   1500 |   15255 |    18 |    66 |       269.1 | d         |
| `bitcoin-otc-negative`                   |   1606 |    3259 |    16 |    38 |        32   | d         |
| `BioGrid-Fret`                           |   1700 |    2395 |    19 |    37 |        23.8 | d         |
| `BioGrid-Dosage-Lethality`               |   1776 |    2289 |     4 |    32 |        21.7 | d         |
| `bn-fly-drosophila_medulla_1`            |   1781 |    8911 |    18 |    41 |        97.6 | d         |
| `BioGrid-Affinity-Capture-Luminescence`  |   1840 |    2312 |     6 |    37 |        21.8 | d         |
| `DNC-emails`                             |   1866 |    4384 |    17 |    73 |        46.3 | d         |
| `wikipedia-norm`                         |   1881 |   15372 |    22 |   137 |       234.1 | d         |
| `exnet-water`                            |   1893 |    2416 |     2 |     2 |        21.5 | d         |
| `Opsahl-socnet`                          |   1899 |   13838 |    20 |   111 |       252.6 | d         |
| `Y2H_union`                              |   1966 |    2705 |     4 |    29 |        24.6 | d         |
| `iscas89-s9234`                          |   1985 |    2370 |     4 |     9 |        22.5 | d         |
| `NZ_legal`                               |   2141 |   15739 |    25 |   128 |       290.5 | d         |
| `BioGrid-Co-Crystal-Structure`           |   2291 |    2021 |     5 |     5 |        22.7 | d         |
| `Yeast`                                  |   2361 |    6646 |    10 |    21 |        55.6 | d         |
| `soc-hamsterster`                        |   2426 |   16630 |    24 |    76 |       188   | d         |
| `iscas89-s13207`                         |   2492 |    3406 |     4 |    30 |        31   | d         |
| `moreno_health`                          |   2539 |   10455 |     7 |    16 |        75.7 | d         |
| `minnesota`                              |   2642 |    3303 |     2 |     2 |        28.5 | d         |
| `ODLIS`                                  |   2900 |   16377 |    12 |    85 |       171.7 | d         |
| `openflights`                            |   2939 |   15677 |    28 |   110 |       203.4 | d         |
| `iscas89-s15850`                         |   3247 |    4004 |     4 |    15 |        35.1 | d         |
| `BioGrid-Dosage-Rescue`                  |   3380 |    6444 |     7 |    34 |        52.3 | d         |
| `BioGrid-Co-Localization`                |   3543 |    4452 |     6 |    24 |        40.5 | d         |
| `twittercrawl`                           |   3656 |  154824 |   142 |   506 |     23057.7 | d         |
| `BioGrid-Escherichia-Coli-K12-W3110`     |   4063 |  181620 |   156 |   441 |     63160.8 | d         |
| `*boards_gender_1m`                      |   4134 |   19993 |    25 |    19 |       142.5 | **c (!)** |
| `boards_gender_2m`                       |   4220 |    5598 |     4 |    20 |        49   | d         |
| `web-EPA`                                |   4271 |    8909 |     6 |    63 |        72.7 | d         |
| `BioGrid-Co-Purification`                |   4326 |    5970 |    12 |    70 |        56.8 | d         |
| `advogato`                               |   5155 |   39285 |    25 |   215 |       785.7 | d         |
| `soc-advogato`                           |   5167 |   39432 |    25 |   217 |       788   | d         |
| `bitcoin-otc-positive`                   |   5573 |   18591 |    20 |    91 |       228.4 | d         |
| `JUNG-javax`                             |   6120 |   50290 |    65 |   618 |      2293.7 | d         |
| `web-california`                         |   6175 |   15969 |    11 |    68 |       150.5 | d         |
| `reactome`                               |   6327 |  146160 |   176 |   445 |      7605.4 | d         |
| `BioGrid-Caenorhabditis-Elegans`         |   6394 |   23646 |    64 |    81 |       272.8 | d         |
| `JDK_dependency`                         |   6434 |   53658 |    65 |   706 |      2338.8 | d         |
| `as20000102`                             |   6474 |   12572 |    12 |    42 |       115.6 | d         |
| `zewail`                                 |   6651 |   54182 |    18 |    98 |       725.5 | d         |
| `ia-reality`                             |   6809 |    7680 |     5 |    18 |        70.9 | d         |
| `eva-corporate`                          |   7253 |    6711 |     3 |     6 |        66.5 | d         |
| `chess`                                  |   7301 |   55899 |    29 |    63 |      1005.1 | d         |
| `lederberg`                              |   8324 |   41532 |    15 |   174 |       451.3 | d         |
| `BioGrid-Biochemical-Activity`           |   8620 |   17746 |    11 |   181 |       203.6 | d         |
| `iscas89-s38584`                         |   9193 |   12573 |     4 |    12 |       116.2 | d         |
| `BioGrid-Drosophila-Melanogaster`        |   9330 |   60556 |    83 |   114 |       934.6 | d         |
| `iscas89-s38417`                         |   9500 |   10635 |     4 |    11 |       109.3 | d         |
| `movielens_1m`                           |   9746 | 1000209 |   221 |   nan |       nan   | nan       |
| `BioGrid-Arabidopsis-Thaliana-Columbia`  |  10417 |   47916 |    26 |   384 |      1179   | d         |
| `p2p-Gnutella04`                         |  10876 |   39994 |     7 |    28 |       354.3 | d         |
| `BioGrid-Co-Fractionation`               |  11017 |   56354 |    83 |    83 |       779.3 | d         |
| `AS-oregon-1`                            |  11174 |   23409 |    17 |    74 |       251.3 | d         |
| `AS-oregon-2`                            |  11461 |   32730 |    31 |   117 |       411.3 | d         |
| `*ca-HepPh`                              |  12006 |  118489 |   238 |    89 |      3534.1 | **c (!)** |
| `*iscas89-s35932`                        |  12515 |   15961 |     2 |     1 |      7680.6 | **c (!)** |
| `foldoc`                                 |  13356 |   91471 |    12 |    62 |       976.6 | d         |
| `BioGrid-Affinity-Capture-Rna`           |  13765 |   42815 |    54 |  1629 |      1875.1 | d         |
| `marvel`                                 |  19428 |   96662 |    18 |   744 |      2670.6 | d         |
| `BioGrid-Affinity-Capture-Western`       |  21028 |   64046 |    17 |    92 |      1202.1 | d         |
| `as-22july06`                            |  22963 |   48436 |    25 |   217 |       625.3 | d         |
| `edinburgh_associative_thesaurus`        |  23132 |  297094 |    34 |   204 |     14014.8 | d         |
| `ca-CondMat`                             |  23133 |   93439 |    25 |    26 |       887.6 | d         |
| `cora_citation`                          |  23166 |   89157 |    13 |    69 |       937   | d         |
| `soc-gplus`                              |  23628 |   39194 |    12 |   489 |       590.9 | d         |
| `google+`                                |  23628 |   39194 |    12 |   489 |       601.5 | d         |
| `BioGrid-Homo-Sapiens`                   |  24093 |  369767 |    71 |   801 |     38376.4 | d         |
| `cit-HepTh`                              |  27769 |  352285 |    37 |  1669 |     10689.3 | d         |
| `digg`                                   |  30398 |   85155 |     9 |    19 |      1015.4 | d         |
| `linux`                                  |  30834 |  213217 |    23 |  4835 |     23301.3 | d         |
| `BioGrid-Chemicals`                      |  33266 |   28093 |     1 |     1 |       341.5 | d         |
| `cit-HepPh`                              |  34546 |  420877 |    30 |   299 |      9849.7 | d         |
| `email-Enron`                            |  36692 |  183831 |    43 |   186 |      5181.2 | d         |
| `BioGrid-Affinity-Capture-Ms`            |  40495 |  321887 |    58 |   842 |     20702.2 | d         |
| `slashdot_threads`                       |  51083 |  116573 |    14 |    64 |      1786   | d         |
| `loc-brightkite_edges`                   |  58228 |  214078 |    52 |   183 |      3678.6 | d         |
| `facebook-links`                         |  63731 |  817090 |    52 |   232 |     35620.8 | d         |
| `BioGrid-All`                            |  75550 | 1316843 |   164 |  1791 |    436258.8 | d         |
| `soc-Epinions1`                          |  75879 |  405740 |    67 |   550 |     30828.6 | d         |
| `soc-Slashdot0811`                       |  77360 |  469180 |    54 |   617 |     23392.2 | d         |
| `NYClimateMarch2014`                     | 102378 |  327080 |    34 |  1036 |     15628.3 | d         |
| `livemocha`                              | 104103 | 2193083 |    92 |  1128 |    507575.7 | d         |
| `tv_tropes`                              | 152093 | 3232134 |   115 |   nan |       nan   | nan       |
| `gowalla`                                | 196591 |  950327 |    51 |  1131 |     32260.3 | d         |
| `bahamas`                                | 219856 |  246291 |     6 |    57 |      4042.2 | d         |
| `location`                               | 225486 |  293697 |     5 |   853 |      7144.2 | d         |
| `offshore`                               | 278877 |  505965 |    13 |  5697 |     23902.3 | d         |
| `dogster_friendships`                    | 426820 | 8543549 |   248 |   nan |       nan   | nan       |
| `Cannes2013`                             | 438089 |  835892 |    27 |  3167 |     23658.4 | d         |
| `actor_movies`                           | 511463 | 1470404 |    14 |   216 |     28196.5 | d         |
| `paradise`                               | 542102 |  794545 |    23 |  4241 |     17401.1 | d         |
| `panama`                                 | 556686 |  702437 |    62 |  1947 |     13334.7 | d         |
| `countries`                              | 592414 |  624402 |     6 | 11047 |     32231.1 | d         |
| `teams`                                  | 935591 | 1366466 |     9 |   350 |     38635.5 | d         |

In this larger dataset, 13 of 206 networks have $c < d$, whereas in 188, we have $c \geq d$.

This means that $188/206 \approx 0.91 = 91\%$ are solved completely by _Case 1_.
