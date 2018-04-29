Overthewire - Bandit Writeups
ssh -l bandit0 -p 2220 -L 1234:localhost:22 bandit.labs.overthewire.org

Lvl 0 	:
	** ssh 
	- login ssh
	- ssh -l bandit0 -p 2220 -L 1234:localhost:22 bandit.labs.overthewire.org
	- password : bandit0

Lvl 0-1	:
	** ssh
	- login using SSH
	- ls file
 	- you'll find readme file
	- cat readme
	- password : boJ9jbbUNNfktd78OOpsqOltutMc3MY1

Lvl 1-2	:
	** ls, cat, file, du, find
	- login ssh
	- cat the file name with ./- instead of just - (cat ./-)
	- password : CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Lvl 2-3	:
	**ls, cat, file, du, find
	- login ssh
	- ls
	- you will see spaced file name
	- you can use autocompletion or just type the space escaped "\ "
	- cat the file using that way
	- password : UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Lvl 3-4	:
	** ls, cd, cat, file, du, find
	- login using ssh
	- ls
	- cd to inhere directory
	- ls the file
	- find nothing? of course use -a to show HIDDEN file(s)
	- ls -a
	- cat .hidden file
	- password : pIwrPrtPN36QITSp3EQaw936yaFoFgAB

lvl 4-5	:
	** ls, cd, cat, file, du, find
	- login using ssh
	- cd to inhere
	- there will be many files
	- if you want, just cat it manually
	- or scan it with file command and you'll see the text file(cat ./*)
	- cat it
	- password : OkoReBOKuIDDepwhWk7jZC0RTdopnAYKh

lvl 5-6	:
	** ls, cd, cat, file, du, find
	- login using ssh
	- cd to inhere
	- there will be many folders
	- find in that directory with -size followed by the size (1033 bytes)
	- you will find a file, cat it
	- or just using simple command(find . -size 1033 -exec cat {} \;)
	- password : DXjZPULLxYr17uwoI01bNLQbtFemEgo7

lvl 6-7	:
	** ls, cd, cat, file, du, find, grep
	- login using ssh
	- find the file from the root and using -name and -group switches and cat
	- find / -user bandit7 -group bandit6 -size 33c 2>&1 -exec cat {} \; | grep -v "Permission denied" | grep -v "No such file or directory"
	- password : HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
	
lvl 7-8	:
	** ls, cd, cat, file, du, find, grep
	- login ssh
	- ls, you will find data.txt
	- there are bunch of words, so use grep to find the code near 'millionth' word
	- you got it
	- password : cvX2JJa4CFALtqS87jk27qwqGhBM9plV

lvl 8-9	:
	** grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
	- sort data.txt and pipe it to uniq and print just unique characters 
	- password : UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

lvl 9-10:
	** grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
	- there will be a bunch of words, use strings command and pipe it to grep and search for '='
	- truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

lvl 10-11:
	** grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd 
	- ls the file
	- there is a data.txt file, cat it
	- the text contain base64, just decode it using base64 -d
	- password : IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

lvl 11-12:
	** grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd
	- cat data.txt, you will get encrypted message
	- the message was encrypted by caesar cipher with 13 as key
	- 13 is special number because when yoou decrypt and encrypt will be the same way
	- cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
	- password : 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

lvl 12-13:
	** grep, sort, uniq, strings, base64, tr, tar, gzip, bzip2, xxd, mkdir, cp, mv
	- there will be a hexdump file, reverse it using xxd
	- you can check what the type of file is using file command
	- use gzip, bzip2, tar -xvf for extract chain zipped file
	- password : 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

lvl 13-14:
	** ssh, telnet, nc, openssl, s_client, nmap
	- use private key to connect to lvl14
	- use ssh -i(no need for password) key uname@host
	- 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

lvl 14-15:
	** ssh, telnet, nc, openssl, s_client, nmap
	- echo the last password and pipe it to nc command to localhost and port 30000
	- password : BfMYroe26WYalil77FoDi9qh59eK5xNr

lvl 15-16:
	** ssh, telnet, nc, openssl, s_client, nmap
	- login using openssl and s_client and connect to localhost with port 30001
	- use -ign_eof(see s_client man)
	- password : cluFn7wTiGryunymYOu4RcffSxQluehd

lvl 16-17:
	** 
	- use nmap for searching listened server
	- try all possible open port between 31000-32000
	- if the port give you a credential, and that's it
	- password : xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn

lvl 17-18:

kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
6vcSC74ROI95NqkKaeEC2ABVMDX9TyUr


ssh -l bandit0 -p 2220 -L 1234:localhost:22 bandit.labs.overthewire.org

