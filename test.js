const fs = require("fs")
const PromiseBlue = require("bluebird")
PromiseBlue.promisifyAll(fs)

module.exports= {
    copyy: async()=>{
        aa= fs.existsSync("D:\\WKW3\\$ZBASE\\EXPORT\\vtesfam.txt")
        console.log("required existing : ", aa)

    },
}