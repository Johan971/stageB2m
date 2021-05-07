#!/usr/bin/env node

const express= require("express")
const bodyParser= require("body-parser")
const http = require("http")
const path= require("path")
const open = require('open')
const { exec } = require("child_process")
const fs = require("fs")
const PromiseBlue = require("bluebird")
PromiseBlue.promisifyAll(fs)




const app=express()


app.use(bodyParser.urlencoded({extended:true}))
app.use(bodyParser.json())

app.get("/",[
	async( req, res, next)=>{
		// console.log(path.join(__dirname, "./interface.html"))
		res.sendFile(path.join(__dirname, "./interface.html"))
	},
	])

const serverHttps= http.createServer(app)

serverHttps.listen(8080,()=>{
	console.log("server running at http://localhost:8080/")
})



// Infos expédition mail
let expediteur = "travail.client@orange.fr"
let destinataire = "jm-dom.gp@wanadoo.fr"
let name = "travail.client"
let serveur = "smtp.orange.fr"
// password = ConvertTo-SecureString -string "tr2xhcli" -AsPlainText -Force

//=== Définition des chemins de base pour les fichiers et les log
let dateObject= new Date()
let date = ("0" + dateObject.getDate()).slice(-2)
let month = ("0" + (dateObject.getMonth() + 1)).slice(-2)
let year = dateObject.getYear()
let hours = dateObject.getHours()
let minutes = dateObject.getMinutes()
let seconds = dateObject.getSeconds()
// console.log("date", `${date}/${month}/${year} at ${hours}h${minutes}:${seconds}`)
let Jour=`${String(year).slice(1)}${month}${date}` //yyMMdd
// console.log(Jour)
let logFile = `ExportVteLog-${Jour}.rtf`
let logFolder = "C:\\Gestion\\Lbm\\export\\log" //CheminBaseArticle
let cheminLogFile = `${logFolder}\\${logFile}`

//=== Noms des fichiers archives
VteArt = "Vteart.txt"
Vtesfam = "Vtesfam.txt"
Regl = "Regl.txt"
BkVteArt =` Vteart-${Jour}.txt`
BkVtesfam = `Vtesfam-${Jour}.txt`
BkRegl = `Regl-${Jour}.txt`

//==============================================================================

// TODO COMMENCER le programme (un jour pour refaire l'ancien et peut etre commencer interface)


const copy1File=  async function(sourcePath, destFolder, fileDest, action="copy"){
	try{
		// console.log("on est là")
		let destPath=path.join(destFolder,fileDest)
		console.log(destPath)

		
		if (fs.existsSync(String(destFolder))){

			await fs.writeFileAsync(cheminLogFile,"Dossier trouvé\n")
			if (String(action).toUpperCase()=="MOVE"){
				await fs.copyFileAsync(sourcePath,destPath)
				await fs.unlinkAsync(sourcePath)
			}else
			{
				
				fs.copyFileAsync(sourcePath,destPath,err=>{
					console.log(err)
				})
				
				
			}

			console.log("ok")
		}
		else{

			console.log("Dossier de destination absent : création")
			fs.writeFileAsync(cheminLogFile,"Dossier de destination absent : création\n")
			if (!fs.existsSync("C:\\Gestion")){
				await fs.mkdirAsync("C:\\Gestion")
			}
			if(!fs.existsSync("C:\\Gestion\\Lbm")){
				await fs.mkdirAsync("C:\\Gestion\\Lbm")
			}
			if(!fs.existsSync("C:\\Gestion\\Meti")){
				await fs.mkdirAsync("C:\\Gestion\\Meti")
			}
			if(!fs.existsSync("C:\\Gestion\\Lbm")){
				await fs.mkdirAsync("C:\\Gestion\\Lbm")
			}
			if(!fs.existsSync("C:\\Gestion\\Lbm\\Export")){
				await fs.mkdirAsync("C:\\Gestion\\Lbm\\Export")
			}
			if(!fs.existsSync("C:\\Gestion\\Lbm\\Import")){
				await fs.mkdirAsync("C:\\Gestion\\Lbm\\Import")
			}
			if(!fs.existsSync("C:\\Gestion\\Lbm\\Export\\Log")){
				await fs.mkdirAsync("C:\\Gestion\\Lbm\\Export\\Log")
			}
			if(!fs.existsSync("C:\\Gestion\\Lbm\\Export\\Archives")){
				await fs.mkdirAsync("C:\\Gestion\\Lbm\\Export\\Archives")
			}
		}
		
		// await fs.copyFileAsync(sourcePath,destPath)
		// let files = await fs.readdirAsync(String(destFolder))

		// console.log("ee",files)

	}
	catch(err){
		throw err
	}
}

copy1File("pathSource",logFolder,"fileDest","action")

// exec("D:\\WKW3\\kwisatz.exe -p1 -t", (error, stdout, stderr) => {
//     if (error) {
//         console.log(`error: ${error.message}`)
//         return
//     }
//     if (stderr) {
//         console.log(`stderr: ${stderr}`)
//         return
//     }
//     if (stdout.length>0){
//     	console.log(`stdout: ${stdout}`)
//     }
    
// })

// open('http://localhost:8080',{wait: true}) //ouvre interface
process.on('uncaughtException', ()=>{serverHttps.close()})
process.on('exit', ()=>{serverHttps.close()})