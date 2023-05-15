#!/usr/bin/env bash

g++ -std=c++17 -O3 c++closure.cpp && mv a.out c++closure

hyperfine --warmup=5 --output=./out.txt "zcat $1 | ./c++closure" "zcat $1 | pypy3 degeneracy.py"
