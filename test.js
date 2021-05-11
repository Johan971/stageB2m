const fs = require("fs")
const PromiseBlue = require("bluebird")
PromiseBlue.promisifyAll(fs)

module.exports= {
    writeFile: async(filePath, toAppend)=>{
        await fs.writeFileAsync(filePath,toAppend)
    },

    appendFile: async(filePath, toAppend)=>{
        await fs.appendFileAsync(filePath,toAppend)
    },
}
