args = process.argv.slice(2)

const fileAContent = fs.readFileSync(args[0], 'utf8')
const fileBContent = fs.readFileSync(args[1], 'utf8')

const concat = fileAContent + fileBContent
fileC = args[2]
fs.writeFileSync(fileC, concat)
