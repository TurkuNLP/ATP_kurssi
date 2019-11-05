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

### Extras:
* If Github does not show you the ipynb notebooks, you can display them at https://nbviewer.jupyter.org/
* Access server from Ubuntu/Mac machines: `ssh -X username@servername` 
* If `tr '[:upper:]' '[:lower:]'` does not properly convert unicode character (e.g. ä and ö), try replacing it with `awk '{print tolower($0)}'`

