const fs = require("fs-extra");

const pathArray = __dirname.split('/')

const source = [
  ...pathArray.slice(0,pathArray.length-1),
].join('/')

console.log('Copying files for ', source)

const destination = (type) => [
  ...pathArray.slice(0,pathArray.length-3),
  type,
  pathArray[pathArray.length-2]
].join('/')
  
console.log('destination ', destination('static'))
fs.copySync(`${source}/build/`, destination('static'))

console.log('destination ', destination(`${destination('templates')}/index.html`))
fs.copyFileSync(`${source}/build/index.html`, `${destination('templates')}/index.html`)
