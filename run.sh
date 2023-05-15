#!/usr/bin/env bash

echo "name,n,m,d,c,t,s,x" > run.log
for f in ../network-corpus/networks/*gz
do
    echo $f
    date
    echo -n $f >> run.log
    echo -n "," >> run.log
    timeout 120s zcat $f | pypy3 degeneracy.py >> run.log
done


# g++ -std=c++17 -O3 c++closure.cpp && mv a.out c++closure

# hyperfine --warmup=5 --output=./out.txt "zcat $1 | ./c++closure" "zcat $1 | pypy3 degeneracy.py"
