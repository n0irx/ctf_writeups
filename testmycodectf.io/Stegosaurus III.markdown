#StegosaurusIII

> Something is not quite as it should be in this image. Can you find it? http://sec-mooc-1.cs.helsinki.fi/stegosaurus/rwer3/03/stegosaurus03.jpg

1. strings stegosaurus04.jpg
2. **TWFraW5nIFRoaW5ncyBhIGJpdCBoYXJkZXIgaW4gb3JkZXIgdG8gZmluZCB0aGUgZmxhZyB3aGljaCBpcyBGbGFne1Nob3VsZE5vdEJlVG9vSGFyZH0=**
3. echo "TWFraW5nIFRoaW5ncyBhIGJpdCBoYXJkZXIgaW4gb3JkZXIgdG8gZmluZCB0aGUgZmxhZyB3aGljaCBpcyBGbGFne1Nob3VsZE5vdEJlVG9vSGFyZH0=" | base64 -d
4. Making Things a bit harder in order to find the flag which is Flag{ShouldNotBeTooHard}


> Flag{ShouldNotBeTooHard}
