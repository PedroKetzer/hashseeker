# hashseeker
Assigment for week 8 of Desec Pentest Profissional course

Execution: hashseeker.py hash.txt wordlist.txt

Phase 1 (in python): Reads the wordlist and outputs the hashes in md5file, then in base64 and lastly, in sha1sum, after that executes the lineseeker.sh, passing the arg.sys 1 and 2

Phase 2 (in bash): Reads the outputed sha1file, find if the hash exists in the wordlist, then outputs the line number and the equivalent in the wordlist
