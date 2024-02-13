#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument')
} else {
  process.argv.forEach((val) => {
    console.log(`${val}`)
  })
}
