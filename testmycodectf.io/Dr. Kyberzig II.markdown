# Dr. Kyberzig II

> *"Dr. Kyberzig is furious that you have cracked his key service! He has changed all of his keys and made a new validation service. Regain access. <https://dr-kyberzig-18op1re4f2491.now.sh/>""*


*  Go to <https://dr-kyberzig-18op1re4f2491.now.sh/>
*  Use developer mode (chrome)
*  Look for js/components/form.js

```javascript
render() {
    return (
      <Container>
        <Form>
          <Input
            prefix={
              <FontAwesomeIcon
                icon={faKey}
                style={{ color: "rgba(0,0,0,.25)" }}
              />
            }
            placeholder="Key"
            onChange={this.validateKey.bind(this)}
          />
        </Form>
        <ValidationMessage>
          {this.state.valid
            ? "Provided key is valid!"
            : "Provided key is not valid"}
        </ValidationMessage>
      </Container>
    );
  }
}
```

*  Look for validator.js in js/domain/validator.js

```javascript
    export default a => {
      return [
        (10)
          .toString(36)
          .toLowerCase()
          .split("")
          .map(function(s) {
            return String.fromCharCode(s.charCodeAt() + -13);
          })
          .join("") +
          (1148241)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(s) {
              return String.fromCharCode(s.charCodeAt() + -39);
            })
            .join("") +
          (function() {
            var u = Array.prototype.slice.call(arguments),
              S = u.shift();
            return u
              .reverse()
              .map(function(p, O) {
                return String.fromCharCode(p - S - 2 - O);
              })
              .join("");
          })(29, 102, 68, 118, 123, 102, 107, 63) +
          (1245)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(Q) {
              return String.fromCharCode(Q.charCodeAt() + -39);
            })
            .join("") +
          (16)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(B) {
              return String.fromCharCode(B.charCodeAt() + -71);
            })
            .join("") +
          (10)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(l) {
              return String.fromCharCode(l.charCodeAt() + -13);
            })
            .join("") +
          (1147)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(R) {
              return String.fromCharCode(R.charCodeAt() + -39);
            })
            .join("") +
          (16)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(B) {
              return String.fromCharCode(B.charCodeAt() + -71);
            })
            .join("") +
          (function() {
            var e = Array.prototype.slice.call(arguments),
              l = e.shift();
            return e
              .reverse()
              .map(function(F, D) {
                return String.fromCharCode(F - l - 16 - D);
              })
              .join("");
          })(27, 128, 109, 112) +
          (15)
            .toString(36)
            .toLowerCase()
            .split("")
            .map(function(L) {
              return String.fromCharCode(L.charCodeAt() + -13);
            })
            .join(""),
        a
      ].reduce(Object.is);
    };
```
*  You can identify the code, or just make a js file to check what's the code actually doing or see my drkyberzigsolver.js
*  You can use node.js to run the file
*  node drkeyberzigsolver.js

** THESE KEYS ARE TOO EASY **
