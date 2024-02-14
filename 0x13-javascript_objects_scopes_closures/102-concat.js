args = process.argv.slice(2);

let content = '';
content.concat(fs.readFileSync(process.argv[2]));

content = content.concat(fs.readFileSync(args[0]));
content = content.concat(fs.readFileSync(args[1]));
fileC = args[2];
fs.writeFileSync(fileC, content);
