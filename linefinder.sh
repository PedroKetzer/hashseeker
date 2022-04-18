#!/bin/bash
echo "Seeking hash line number"

#variables
hash=$(cat $1)
password=$(cat $2)

linenum="$(grep -n $hash sha1file | head -n 1 | cut -d ":" -f 1)"
location="$(sed -n -e "$linenum"p $2)"

if [[ $linenum ]]; then
    echo "Found a hash in the line" $linenum
else 
    echo "Hash doesn't exist in this wordlist"
fi

echo "The password in the list is $location"