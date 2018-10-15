# KKLT0030 Automaattinen tekstiprosessointi

### 2018 Exams
1. ja 2. tenttikerta järjestetään viimeisellä opetusviikolla (vk 43) normaalien luentojen aikana. Huom! Aloitetaan tentit heti tasalta, eli maanantaina tasan klo 10.00 ja torstaina tasan kello 12.00.

**1. tentti** maanantaina 22.10. klo 10.00-12.00 A252

**2. tentti** torstaina 25.10. klo 12.00-14.00 A252

**3. tentti** ilmoitetaan myöhemmin, jos sinulla on tarve 3. tenttikerralle (et pääse 1. ja 2. tenttiin tai haluat tulla uusimaan tentin), ota yhteyttä jmnybl@utu.fi ennen kurssin päättymistä tai heti 1. ja 2. tenttikertojen tulosten tultua

### 1. lecture
* General course information
* ssh / connecting to a server
* Getting familiar with unix environment
* Commands: ls, cd, echo, cat, less, different text editors
* materials: [Unix_1.ipynb](Unix_1.ipynb)

### 2. lecture
* Creating, moving, renaming or deleting files and directories
* Reading manuals
* Switches (e.g. `ls -lh`, `wc -l`)
* Searching words from text files with `egrep` and counting lines or words with `wc`
* Commands: mkdir, cp, mv, rmdir, rm, man, clear, head, tail, egrep, wc
* materials: [Unix_1.ipynb](Unix_1.ipynb), [Unix_2.ipynb](Unix_2.ipynb)

### 3. lecture
* Redirecting output to a file
* Pipes
* Commands: `>`, `|`
* materials: [Unix_2.ipynb](Unix_2.ipynb)

### 4. lecture
* Counting word frequency lists
* Selecting random lines from a file
* Compressing text
* Commands: sort, uniq, tr, gzip, shuf
* materials: [Unix_3.ipynb](Unix_3.ipynb)

### 5. lecture
* Search with regular expressions
* Commands: egrep
* materials: [Unix_4.ipynb](Unix_4.ipynb)

### 6. lecture
* Search and replace
* Commands: perl -pe 's/old/new/g'
* materials: [Unix_5.ipynb](Unix_5.ipynb)

### 7. lecture
* Recap

### 8. lecture
* Bash scripts
* File permissions
* Commands: `chmod u+x script.sh`
* materials: [Unix_6.ipynb](Unix_6.ipynb)

### 9. lecture
* Processing syntax analyzed files on command line (conllu)
* Commands: `cut`
* materials: [Unix_7.ipynb](Unix_7.ipynb)

### 10. lecture
* Scripts for processing syntax analyzed files
* materials: [Unix_8.ipynb](Unix_8.ipynb)

### 11. and 12. lecture
* Bash for loops
* For loop over all .txt files in a directory: `for x in directory/*.txt ; do echo $x ; done`
* For loop over numeric range: `for x in {1..10} ; do echo $x ; done`
* For loop over list of strings: `for x in en fi sv ; do echo $x ; done` or `languages="en fi sv" ; for x in $languages ; do echo $x ; done`
* Recap
* materials: [Unix_9.ipynb](Unix_9.ipynb)

### 13. and 14. lecture
* EXAMS!

### Extras:
* Access server from Ubuntu/Mac machines: `ssh -X username@servername` 
* If `tr '[:upper:]' '[:lower:]'` does not properly convert unicode character (e.g. ä and ö), try replacing it with `awk '{print tolower($0)}'`

