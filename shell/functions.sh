#!/bin/bash
# Misc. functions and their uses

# how many days till a deadline?
dcd() {
    deadline=$(date -j -f "%Y-%m-%d" "2069-07-20" "+%s") # Apollo 11 centennial
    today=$(date +%s)
    let day_count_down="($deadline-$today)/(60*60*24)"
    echo $day_count_down
}

export -f dcd
