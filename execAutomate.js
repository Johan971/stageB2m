const cp = require("child_process")
const fs = require("fs")
const PromiseBlue = require("bluebird")
PromiseBlue.promisifyAll(fs)
PromiseBlue.promisifyAll(cp)


module.exports= {
    genTicketsVente: async()=>{
        await cp.execAsync("D:\\WKW3\\kwisatz.exe -DZBASE -a120 -p99") 
    },
}



