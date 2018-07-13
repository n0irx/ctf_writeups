code_in ="SYNTPrfneVfPbbyOhgAbgFrpher"

for alphabet in range(1, 27):
    plain_code = "" 
    for letter in code_in:
        plain_code += chr(ord(letter) + alphabet)
    print(plain_code)



