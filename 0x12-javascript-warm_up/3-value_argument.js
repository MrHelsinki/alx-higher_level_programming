const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('No arguments');
} else {
  console.log(`${argv[2]}`);
}
