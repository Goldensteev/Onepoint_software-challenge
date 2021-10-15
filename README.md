# onepoint python tech test
---

This repo contains 3 folders one for each excerise

### Caesar
A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. For example, assume the input plain text is the following

the file `casear.py` contains the caesar_cipher function

`python ./caesar.py` will output : `uijt jt b uftu!!! ju xpslt!? apjolt`

shift = 1 : *this is a test!!! it works!? zoinks* -> *uijt jt b uftu!!! ju xpslt!? apjolt*

---

### Logparse

program will parse the given log file and print out a report giving how long the device was ON and the timestamp of any ERR conditions.

`python ./logparse.py logfile.log` 

will output :
```
Device was ON for 2 days, 0:00:09
ERR condition logged on 2021/07/11 11:18:56
ERR condition logged on 2021/07/12 04:11:58
```

---

### sudokusolve

Given a string in SDM format, sudokusolve will find and return the solution for the sudoku puzzle in the string. If a sudoku is unsolvable it will return the string `Unsolvable`

`python .\sudokusolve.py 530070000600195000098000060800060003400803001700020006060000280000419005000080079`

will output :
```
Solution:
534678912672195348198342567859761423426853791713924856961537284287419635345286179
```

`python .\sudokusolve.py 020400080000000006800007100200500090095000000040030000000041007002800040000060300`

will output :
```
Unsolvable
```