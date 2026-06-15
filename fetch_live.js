const fs = require('fs');
fetch('https://www.rahejasprimetwo.com/')
  .then(res => res.text())
  .then(text => {
    fs.writeFileSync('live.html', text);
    console.log("Fetched live.html");
  });
