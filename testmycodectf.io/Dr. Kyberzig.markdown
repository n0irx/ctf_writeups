# Dr. Kyberzig

> You have lost your key to Dr. Kyberzig's software and he is refusing to help you since he believes that those who are foolish enough to lose their keys don't deserve to use his products. Dr. Kyberzig has suggested that you try to figure out what your key was. You can use his key validation service that is available here: https://dr-kyberzig-8b0e66b8.now.sh/

* Go to https://dr-kyberzig-8b0e66b8.now.sh/
* Use developer mode (chrome)
* Look for js/components/form.js

```javascript
validateKey(event) {
  const newValue = event.target.value.trim();
  if (newValue === "VERY SECRET KEY") {
    this.setState({
      valid: true
    });
  } else {
    this.setState({
      valid: false
    });
  }
}
```
* Verify key **VERY SECRET KEY**

**VERY SECRET KEY**
