# KKLT0030 Automaattinen tekstiprosessointi

### 2019 Exams

**1. tentti** torstaina 12.12, luentoaikana

**2. tentti** tiistaina 17.12, luentoaikana

**3. tentti** ilmoitetaan myöhemmin, jos sinulla on tarve 3. tenttikerralle (et pääse 1. ja 2. tenttiin tai haluat tulla uusimaan tentin), ota yhteyttä mavela@utu.fi ennen kurssin päättymistä tai heti 1. ja 2. tenttikertojen tulosten tultua

### 1. lecture
* General course information
* ssh / connecting to a server
* Getting familiar with unix environment
* Commands: ls, cd, echo, cat, less, different text editors
* materials: [Unix_1.ipynb](Unix_1.ipynb)

### 2. lecture
* Searching and counting: egrep, wc, tail, head
* Pipes and flags (vivut)
* Directing output to a file with > and >>
* materials: Unix_2.ipynb

### 3. lecture
* More on searching and counting
* Frequency lists with sort and uniq
* materials: Unix_2.ipynb, Unix_3.ipynb

### 4. lecture
* More on frequency lists with sort and uniq
* tr, shuf and gzip
* materials: Unix_3.ipynb, beginning of Unix_4.ipynb

### 5. lecture
* Recap on frequency lists and tr
* Regular expressions
* materials: Unix_4.ipynb

### 6. lecture
* More on regular expressions
* materials: Unix_4.ipynb

### 7. lecture
* Recap on regex
* perl -pe 's///g' -komento
* skriptit
* materials: Unix_4.ipynb, Unix_5.ipynb, Unix_6.ipynb

### HUOM! TORSTAI 21.11 LUENTO ON PERUTTU! 
### Korvaavina tehtävinä seuraavat:
* Unix_6.ipynb tehtävät 10 ja 11
* Unix_5.ipynb tehtävä 9

### 7. lecture
* Recap on scripts and perl -pe 's///g'
* Materials Unix_5.ipynb, Unix_6.ipynb  

### 8. lecture
* The command cut
* Syntax analyzed files, the conll format
* Analyzing and grepping conllu files
* Materials Unix_7.ipynb

### HUOM! 3.12 ja 5.12 ei ole ohjattuja luentoja, vaan ne korvataan tehtävillä. Tehtävien tekeminen yhdessä on kuitenkin kannattavaa! Suosittelen luentoaikana Sammioon menemistä, yhdessä mahdolliset ongelmat saa helpommin ratkottua!
### TEHTÄVÄT: 
* Unix_7.ipynb: Tehtävät 13,14
* Unix_8.ipynb: Tehtävät 15,16,17,18


### Extras:
* If Github does not show you the ipynb notebooks, you can display them at https://nbviewer.jupyter.org/
* Access server from Ubuntu/Mac machines: `ssh -X username@servername` 
* If `tr '[:upper:]' '[:lower:]'` does not properly convert unicode character (e.g. ä and ö), try replacing it with `awk '{print tolower($0)}'`

