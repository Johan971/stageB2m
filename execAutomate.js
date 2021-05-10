const {exec} = require("child_process")

module.exports= {
    genTicketsVente: async()=>{
        exec("D:\\WKW3\\kwisatz.exe -DZBASE -a120 -p99", (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`)
                return
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`)
                return
            }
            if (stdout.length>0){
                console.log(`stdout: ${stdout}`)
            }
            
        })
        
    },
}



