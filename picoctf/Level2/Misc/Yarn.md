# Yarn

* If we try to strings the yarn, we couldnt find anything.
* The hints said about length
* Strings command use 4 byte to identify string (the default)
* Use (-number) flag to controll how many bytes we want

```bash
strings yarn -3
```

* we can see there is a distributed 3 bytes chars that build "Submit_me_for_I_am_the_flag" strings
