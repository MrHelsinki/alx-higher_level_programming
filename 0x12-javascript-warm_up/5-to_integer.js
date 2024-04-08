const { argv } = require('process');

if (!isNaN(argv[2])) {
  const num = parseInt(argv[2]);
  console.log(num);
} else {
  console.log('Not a number');
}
