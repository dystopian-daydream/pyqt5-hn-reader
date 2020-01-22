#!/bin/bash

redecho() { echo -e "\e[0;32m$1\e[0m" ; }
grnecho() { echo -e "\e[92m$1\e[0m" ; }
grnprnt() { printf "\e[32m$1\e[0m" ; }
success() { grnprnt "\xE2\x9C\x94 " && echo "$1"  ; }
divider() { printf "=%.0s"  $(seq 1 80) ; }
section() { echo && divider && echo && redecho "$1" && divider && echo ; }