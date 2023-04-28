#!/usr/bin/env bash

for dataset in karate power yeast bible dnc internet-as facebook
do
    date
    echo $dataset
    pypy3 ccdeg.py $dataset.csv
    pypy3 cc.py $dataset.csv
    date
    echo "/$dataset"
    echo
    echo
done
