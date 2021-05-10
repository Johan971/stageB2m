#!/usr/bin/env node

const express= require("express")
const bodyParser= require("body-parser")
const http = require("http")
const path= require("path")
const open = require('open')
const cp = require("child_process")
const fs = require("fs")
const PromiseBlue = require("bluebird")
PromiseBlue.promisifyAll(fs)
PromiseBlue.promisifyAll(cp)



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
let pathExportGest="C:\\Gestion\\Lbm\\export"
let logFolder = pathExportGest+"\\log" //CheminBaseArticle

let cheminLogFile = `${logFolder}\\${logFile}`

//=== Noms des fichiers archives
let VteArt = "vteart.txt"
let Vtesfam = "vtesfam.txt"
let Regl = "regl.txt"
let BkVteArt =` Vteart-${Jour}.txt`
let BkVtesfam = `Vtesfam-${Jour}.txt`
let BkRegl = `Regl-${Jour}.txt`

// Paths fichiers exports et archives
let dossierBaseClient$= "$ZBASE" //Besoin pour la gestion de fichiers
let dossierBaseClient= "ZBASE" //Besoin pour les commandes

let disqueInstallationKwisatz= "D"
let pathBaseExportKw = `${disqueInstallationKwisatz}:\\WKW3\\${dossierBaseClient$}\\EXPORT`
let pathFichiersArchive=pathBaseExportKw + "\\Archives"
// let pathKVente = pathBaseExportKw + "\\VTE*.*"
// let pathKRegl = pathBaseExportKw + "\\REG*.*"
// let pathGVente = pathExportGest + "\\VTE*.*"
// let pathGRegl = pathExportGest + "\\REG*.*"
let pathKVente = pathBaseExportKw + `\\${VteArt}`
let pathKRegl = pathBaseExportKw + `\\${Regl}`
let pathKVenteFam=pathBaseExportKw +`\\${Vtesfam}`
let pathGVente = pathExportGest + "\\VTE*.*"
let pathGRegl = pathExportGest + "\\REG*.*"
//==============================================================================

// TODO COMMENCER le programme (un jour pour refaire l'ancien et peut etre commencer interface)


const copy1File=  async function(sourcePath, destFolder, fileDest, action="copy"){
	try{
		// console.log("on est là")
		let destPath=path.join(destFolder,fileDest)
		// console.log("eeeeeee",sourcePath)

		
		if (fs.existsSync(String(destFolder))){

			await fs.writeFileAsync(cheminLogFile,"Dossier trouvé. \n")
			if (String(action).toUpperCase()=="MOVE"){
				await fs.copyFileAsync(sourcePath,destPath)
				await fs.unlinkAsync(sourcePath)
			}else
			{
				fs.copyFileAsync(sourcePath,destPath)
			}

			
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

const main= async() =>{
	try{
		if(fs.existsSync(cheminLogFile)){
			// console.log("hi")
			await fs.unlinkAsync(cheminLogFile)
			await fs.appendFileAsync(cheminLogFile,`Dossier de log ${cheminLogFile} écrasé.\n`)
		}
		
		await fs.appendFileAsync(cheminLogFile, `\n${date}/${month}/${year} at ${hours}h${minutes}:${seconds}. \n`)
		
	}catch(e){throw e}
	
	// Fermeture kwisatz
	a= await cp.execAsync('tasklist /fi "IMAGENAME eq kwisatz.exe"')
	if (String(a.slice(0,11))!="Information"){ //Si kwisatz n'est pas déja fermé
		cp.execAsync('taskkill /F /IM kwisatz.exe')
	}
	// console.log("aaa", a)
	try{
		
		await fs.unlinkAsync(pathKVente)
		await fs.unlinkAsync(pathKRegl)
		await fs.unlinkAsync(pathGVente)
		await fs.unlinkAsync(pathGRegl)
		
	}catch(e){}
	
	try{
		await fs.accessAsync(pathFichiersArchive,fs.constants.F_OK)
		
	}catch(e){
		await fs.mkdirAsync(pathFichiersArchive) //ok
	}
	
	try{
		await require("./execAutomate.js").genTicketsVente()
		
		// await fs.access("D:\\WKW3\\$ZBASE\\EXPORT\\regl.txt", e=>{})
		let KVTE= await fs.access(pathKVente,e=>{throw e})
		let KREG= await fs.access(pathKRegl,e=>{throw e})
		let KVTEF= await fs.access(pathKVenteFam,e=>{throw e})
		await fs.appendFileAsync(cheminLogFile, `fichiers générés trouvés dans le dossier\n`)
		
	}
	catch(e){
		await fs.appendFileAsync(cheminLogFile, `Erreur : fichiers générés introuvables\n`)
		throw e
	}
}
	
	
main()



// open('http://localhost:8080',{wait: true}) //ouvre interface
process.on('uncaughtException', ()=>{serverHttps.close()})
process.on('exit', ()=>{serverHttps.close()})