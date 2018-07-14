# bandit 0-1

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

**password : bandit0**

```bash
cat readme
```

**output: boJ9jbbUNNfktd78OOpsqOltutMc3MY1**

# bandit 1-2

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```
> password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

there is file called - ( a special character )

```bash
cat ./-
```
**output: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**

# bandit 2-3

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```
**password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**

using escape sequence (\) to use space in terminal

```bash
cat spaces\ in\ this\ filename
```
**output: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**

# bandit 3-4

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```
**password : UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**

```bash
cd inhere
ls -la
cat .hidden
```
**output: pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

# bandit 4-5

```bash
ssh bandit4@bandit.labs.overthewire.org -p 2220
```
**password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

```bash
cd inhere
for f in ./-file*; do cat ${f}; echo '\n'; done
```
**output: koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

# bandit 5-6

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```
**password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

```bash
cd inhere
cat $(find . -readable -type f -size 1033c)
```
**output: DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

# bandit 6-7

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```
**password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

```bash
cat $(find / -user bandit7 -group bandit6 -size 33c 2>/dev/null)
```
**output: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**

# bandit 7-8

```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```
**password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**

```bash
cat data.txt | grep millionth
```

**output: cvX2JJa4CFALtqS87jk27qwqGhBM9plV**


# bandit 8-9

```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```
**password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV**

```bash
sort data.txt  | uniq -u
```

**output: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**

# bandit 9-10

```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
```
**password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**

```bash
cat data.txt  | strings | grep =
```

**output: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**


# bandit 10-11

```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```
**password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**

```bash
cat data.txt | base64 -d
```

**output: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**

# bandit 11-12

```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
```
**password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**

```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
**output: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**

# bandit 12-13

```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```
**password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**

```bash
cat data.txt | base64 -d
```

**output: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**

# bandit 10-11

```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```
**password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**

```bash
cat data.txt | base64 -d
```

**output: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**
