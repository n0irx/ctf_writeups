E = "101100000111011000000110101110011101100000001010111110010101101111101011110111010111001110101001011101001100001011000000010101111101101011111011010011000010100101110101001101001010010111010101111110101011011111011000000110110000001101100001011010111110110110000000101011100101010100101110100110000101011101111010111000110110000010101011101001011000100110101110110101001111101010111111010101000001101011011011010100010110101110110101011011111010100010110101101101101100001011010110111110101000011101011111001010100010110101101101101100000101010011111010100111110101011011011010111000010101000010101011100101011000101110100110000"
A = "10101101111" // a


// original function that create the token
function createToken(text) {
    let encrypted = "";
    for (let i = 0; i < text.length; i++) {
            encrypted += ((text[i].charCodeAt(0)-43+1337) >> 0).toString(2)
    }
    return encrypted
}

// try to reverse the function
function createTokenReverse(text) {
    let encrypted = "";
    for (let i = 0; i < text.length; i++) {
            encrypted += ((text[i].charCodeAt(0)-43+1337) >> 0)
    }
    return encrypted
}

// decode one character (binary) to char
function decode(text) {
    let decrypted = "";
    decrypted += (String.fromCharCode(parseInt(text, 2)+43-1337))
    return decrypted
}

// decode all the text
function decodeAll(text) {
    let tt = text.match(/.{1,11}/g); 
    let decrypted = "";
    for (const t of tt) {
        decrypted += decode(t)
    }
    return decrypted
}

console.log(createToken("a"))
console.log(createTokenReverse("a"))
console.log(decode(A))
console.log(decodeAll(E))