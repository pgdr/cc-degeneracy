#!/usr/bin/env bash

for dataset in karate power yeast bible dnc internet-as facebook
do
    date
    echo $dataset
    hyperfine -L alg cc,ccdeg -L dataset $dataset "pypy3 {alg}.py {dataset}.csv"
    date
    echo "/$dataset"
    echo
    echo
done
