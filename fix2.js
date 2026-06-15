const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

// Fix rupee symbol encoding issue (? instead of ₹)
content = content.replace(/\? 1\.58 Cr Onwards<\/td>/g, '₹ 1.58 Cr Onwards</td>');
content = content.replace(/₹ 1\.58Cr\+/g, '₹1.58Cr+');

// Fix the meta description rupee
content = content.replace(/₹,11\.58Cr\+/g, '₹1.58Cr+');
content = content.replace(/,1 1\.58 Cr\*/g, '₹ 1.58 Cr*');

// Make sure Rachana name is correct in chatbot
content = content.replace(/Shreya Shetty /g, 'Shreya Shetty ');

fs.writeFileSync('index.html', content, 'utf8');
console.log('Fixed encoding issues');
