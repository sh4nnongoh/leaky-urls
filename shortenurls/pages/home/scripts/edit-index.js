const fs = require('fs')

const pathArray = __dirname.split('/')
const projectName = pathArray[pathArray.length-2]

const index = fs.readFileSync('build/index.html').toString()

const updatedIndex = index
  .replace('/static/js/',`/static/${projectName}/static/js/`)
  .replace('/static/css/',`/static/${projectName}/static/css/`)
  .replace('/static/media/',`/static/${projectName}/static/media/`)

fs.writeFileSync('build/index.html', updatedIndex)
