#!/usr/bin/env node

const express= require("express")
const bodyParser= require("body-parser")
const http = require("http")
const path= require("path")
const open = require('open')
const cp = require("child_process")
const fs = require("fs")
const nodemailer = require('nodemailer')
const PromiseBlue = require("bluebird")
PromiseBlue.promisifyAll(fs)
PromiseBlue.promisifyAll(cp)


const prompt = require('prompt')

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
year=String(year).slice(1)
let hours = dateObject.getHours()
let minutes = dateObject.getMinutes()
let seconds = dateObject.getSeconds()
console.log("date", `${date}/${month}/${year} at ${hours}h${minutes}:${seconds}`)
let Jour=`${year}${month}${date}` //yyMMdd
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

//Fonctions
const deleteFileIfExist= async(pathFile)=>{
	fs.unlink(pathFile,e=>{})
	
}
const createFolderIfNotExist= async(pathFile)=>{
	if (!fs.existsSync(pathFile)){
		await fs.mkdirAsync(pathFile)
	}
}

const copy1File=  async function(sourcePath, destFolder, fileDest, action="copy"){
	try{
		// console.log("on est là")
		let destPath=path.join(destFolder,fileDest)
		// console.log("eeeeeee",sourcePath)
		// let Aa=fs.existsSync(String(sourcePath))
		// console.log(Aa)
		
		if (fs.existsSync(String(destFolder))){

			await fs.appendFileAsync(cheminLogFile,`Dossier ${destFolder} trouvé. \n`)
			if (String(action).toUpperCase()=="MOVE"){
				await fs.copyFileAsync(sourcePath,destPath)
				await fs.unlinkAsync(sourcePath)
			}else
			{	
				await fs.copyFile(sourcePath,destPath, e=>{})
			}

			
		}
		else{

			console.log("Dossier de destination absent.")
			fs.appendFileAsync(cheminLogFile,"Dossier de destination absent tentatice de création.\n")
			await createFolderIfNotExist(destPath)
		}
		
		// await fs.copyFileAsync(sourcePath,destPath)
		// let files = await fs.readdirAsync(String(destFolder))

		// console.log("ee",files)

	}
	catch(err){
		fs.appendFileAsync(cheminLogFile,`Erreur copie fichier : ${sourcePath} vers ${destPath}`)
		throw err
	}
}

//=============================================================================



const main= async() =>{

	try{
		if(!fs.existsSync("C:\\Gestion")){
			await createFolderIfNotExist("C:\\Gestion")
			await createFolderIfNotExist("C:\\Gestion\\Lbm")
			await createFolderIfNotExist("C:\\Gestion\\Meti")
			await createFolderIfNotExist("C:\\Gestion\\Lbm\\Export")
			await createFolderIfNotExist("C:\\Gestion\\Lbm\\Import")
			await createFolderIfNotExist("C:\\Gestion\\Lbm\\Export\\Log")
			await createFolderIfNotExist("C:\\Gestion\\Lbm\\Export\\Archives")
		}

		if(fs.existsSync(cheminLogFile)){
			await fs.unlinkAsync(cheminLogFile)
			await fs.writeFileAsync(cheminLogFile, `${date}/${month}/${year} at ${hours}h${minutes}:${seconds}. \n`)
		
			await fs.appendFileAsync(cheminLogFile,`Dossier de log ${cheminLogFile} écrasé.\n`)

		}
		
		
		
	}catch(e){throw e}
	
	// Fermeture kwisatz
	a= await cp.execAsync('tasklist /fi "IMAGENAME eq kwisatz.exe"')
	if (String(a.slice(0,11))!="Information"){ //Si kwisatz n'est pas déja fermé
		cp.execAsync('taskkill /F /IM kwisatz.exe')
	}
	
	try{
		await deleteFileIfExist(pathKVenteFam)
		await deleteFileIfExist(pathKVente)
		await deleteFileIfExist(pathKRegl)

		await deleteFileIfExist(pathGVente)
		await deleteFileIfExist(pathGRegl)
	}catch(e){}
	
	try{
		await fs.accessAsync(pathFichiersArchive,fs.constants.F_OK)
		
	}catch(e){
		try{
			await fs.mkdirAsync(pathFichiersArchive)
		}catch(er){
			throw(er)
		}
		
	}

	try{
		 
		await cp.execAsync("D:\\WKW3\\kwisatz.exe -DZBASE -a120 -p99")
		let KVTE= await fs.access(pathKVente,e=>{throw e})
		let KREG= await fs.access(pathKRegl,e=>{throw e})
		let KVTEF= await fs.access(pathKVenteFam,e=>{throw e})
		await fs.appendFileAsync(cheminLogFile, `Fichiers générés trouvés dans le dossier.\n`)
		
	}
	catch(e){
		try{
			await fs.appendFileAsync(cheminLogFile, `Erreur : fichiers générés introuvables.\nErreur:${e}\n`)
		
		}catch(er){
			throw er
		}
		
	}


	try{
		//Copie repo gestion
		await copy1File(pathKVente,pathExportGest,VteArt)
		await copy1File(pathKVenteFam,pathExportGest,Vtesfam)
		await copy1File(pathKRegl,pathExportGest,Regl)
		await fs.appendFileAsync(cheminLogFile,`Exportation des fichiers créés vers ${pathExportGest} effectuée.\n`)
		//Copie archivage
		await copy1File(pathKVente,pathFichiersArchive,BkVteArt)
		await copy1File(pathKRegl,pathFichiersArchive,BkRegl)
		await copy1File(pathKVenteFam,pathFichiersArchive,BkVtesfam)
		await fs.appendFileAsync(cheminLogFile,`Exportation des fichiers créés vers ${pathFichiersArchive} effectuée.\n`)

	}
	catch(e){
		try{
			await fs.appendFileAsync(cheminLogFile,`Erreur : Exportation des fichiers créés compromise.\nErreur:${e}\n`)
		}catch(er){
			throw er
		}
	}

	try{
	var transporter = nodemailer.createTransport({
	  service: 'orange',
	  host: serveur,
	  port:587,
	  auth: {
	    user: expediteur,
	    pass: 'tr2xhcli'
	  }
	})

	var mailOptions = {
	  from: expediteur,
	  to: destinataire,
	  subject: 'OK Exportation Fichiers CheminGVTE et CheminGREG',
	  text: 'Exportations terminées et normalement OK.'
	}

	transporter.sendMail(mailOptions, function(error, info){
	  if (error) {
	    console.log(error)
	  } else {
	  	fs.appendFileAsync(cheminLogFile,`Email bien envoyé.\n`)
	    console.log('Email sent: ' + info.response)
	  }
	})
	}catch(e){
		throw e
	}
}
	
main()
// open('http://localhost:8080',{wait: true}) //ouvre interface
process.on('uncaughtException', ()=>{serverHttps.close()})
process.on('exit', ()=>{serverHttps.close()})