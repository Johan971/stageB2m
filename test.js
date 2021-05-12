const express= require("express")
const bodyParser= require("body-parser")
const http = require("http")
const open = require('open')
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
open('http://localhost:8080',{wait: true}) //ouvre interface
process.on('uncaughtException', ()=>{serverHttps.close()})
process.on('exit', ()=>{serverHttps.close()})
