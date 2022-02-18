#coding: utf-8 -*-
"""
Created on Mon Dec 28 18:24:55 2022

@author: Yannis VAULRY
"""
#python 3.9.7

#PROJET SDTS : BOT DISCORD EN UTILISANT discord.py

	#discord.py
	#deepl
	#neuralintents
	#discord-py-slash-command
	#Création du bot via le menu développeur(permet d'attribuer les droits au bot et d'obtenir un TOKEN pour ce dernier)

#Import des librairies
import discord
from neuralintents import GenericAssistant
import json
import deepl
import random
import requests
from math import *
from discord.ext import commands
from discord_slash import ButtonStyle, SlashCommand
from discord_slash.utils.manage_components import *

#Création de la variable bot en indiquant que les commandes destinées au bot commenceront par "!"
# intents=discord.Intents.all() -> pour permettre au bot de récupérer les membres des serveurs 
bot = commands.Bot(command_prefix = "!", description = "BoT SDTS", intents=discord.Intents.all())
#slash permet d'utiliser des boutons et des listes 
slash = SlashCommand(bot, sync_commands=True)
#Création et initialisation des variables de type liste
listeAlpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
listeAdmin = []
listeNbr = ['1','2','3','4','5','6','7','8','9','0']
listeCarac = ['/','@','*','+','-','?',';','!']
#Fonction de lancement pour le bot
def lancementBot():
	fin = False
	idBot = ""
	#id ou TOKEN est récupérable sur la page web developpeur de discord après avoir créé le bot
	idBot = str(input("Veuillez-renseigner l'id (TOKEN du bot) : "))

	while fin == False:
		retour = str(input("Qui peut avoir le droit admin (ex : TOTO#212)\nPour quitter utiliser le chiffre '0'\nRenseigner l'identifiant : "))
		if retour != "0":
			listeAdmin.append(retour)
			print (listeAdmin)
		else:
			fin = True
			try:
				bot.run(idBot)
			except:
				print("idBot non correct")
#Fonction IAchatBot utilise la librairie tensorflow et plus précisémment la librairie neuralintents, on se servira de cette fonction pour entrainer le bot avec une liste de données dse trouvant dans le fichier intents.json
def IAchatBot(message):
    retour = ""
    print(assistant.request(message))
    retour = assistant.request(message)
    return retour

assistant = GenericAssistant('intents.json', model_name="test_model")
assistant.train_model()
assistant.save_model()

                   
#S'active automatiquement lorsque le bot est connecté et visible sur discord
#async et await sont des coroutines utilisées par discord
@bot.event
async def on_ready():
    print("Bot pret")
#S'active automatiquement lorsque le bot est connecté .event fait partie des différents évènements de la librairie discord.py
@bot.event
async def on_connect():
   print("Bot connecté")

#S'active automatiquement lorsque le bot est déconnecté
@bot.event
async def on_disconnect():
   print("Bot déconnecté")

#La fonction aide affiche les différentes actions du bot lorsque l'utilisateur utilise le "!aide"
@bot.command()
async def aide(ctx):
    com = ""
    com = "!info\n!dire [expression]\n!traduireEN [expression]\n!traduireFR [expression]\n!traduireES [expression]\n!traduireDE [expression]\n!nettoyer [nombre de lignes]\n!stationsT [metros,buses,tramways] [nom du transport]\n!transport [metros,buses,tramways] [nom du transport] [position de départ]\n!chat [expression]\n!calculatrice\n!genererP [nombre de caractères]\n!ban [@TOTO#2121] [raison]\n!unban [utilisateur] [raison]\n!creerCV [nom]\n!creerCT [nom]\n!suppC [nom] "
  	#fonction send du contexte pour renvoyer un message dans le meme channel que le message envoyé par l'utilisateur
    await ctx.send(com)

#!genererP permet de générer un mot de passe aléatoire, cette fonction prend un paramètre qui est nbrC qui correspond au nombre de caractères que le mot de passe doit avoir
@bot.command()
async def genererP(ctx, nbrC):
	# ctx.guild retourne une valeur uniquement si le message envoyé se trouve dans une guild 'serveur'
	if not ctx.guild:
		#si le paramètre nbrC est >= 6 on répartie la taille du mot de passe pour les majuscules, les minuscules, les caractères spéciaux et les chiffres
		if int(nbrC) >= 6:
			#On divise nbrC par 5 pour obtenir le nombre de majuscule, de chiffre et de caractère que le mot de passe doit obtenir
			nbrChiffre = ceil(int(nbrC)/5)
			nbrCaractere = ceil(int(nbrC)/5)
			nbrMajuscule = ceil(int(nbrC)/5)
			nbrMin = int(nbrC) - (nbrChiffre+nbrMajuscule+nbrCaractere)
			i=0
			pos = 0
			password  = [0] * int(nbrC)
			retour = ""
			while (i<int(nbrC)):
				#r permet de générer aléatoirement la position des différents caractères
				r = random.randint(0, 3)
				if (r == 1 and nbrChiffre >= 1):
					#r prend une nouvelle valeur, la valeur aléatoire est ensuite la position du caractère à utiliser dans la liste nommée listeNbr
					r = random.randint(0,len(listeNbr)-1)
					password[pos] = listeNbr[r]
					nbrChiffre = nbrChiffre - 1
					pos += 1
					i=i+1
				elif r == 2 and nbrCaractere >= 1:
					r = random.randint(0,len(listeCarac)-1)
					password[pos] = listeCarac[r]
					nbrCaractere = nbrCaractere - 1
					pos += 1
					i=i+1
				elif r == 3 and nbrMajuscule >= 1:
					r = random.randint(0,len(listeAlpha)-1)
					password[pos] = listeAlpha[r].upper()
					nbrMajuscule = nbrMajuscule - 1
					pos += 1
					i=i+1
				else:
		            
					if(nbrMin >= 1):
						r = random.randint(0,len(listeAlpha)-1)
						password[pos] = listeAlpha[r]
						nbrMin = nbrMin -1
						pos += 1
						i=i+1
			#.join permet de réunir les différents éléments de la liste
			retour = "Le mot de passe généré est : || "+ "".join(password)+ "||"
			print(password)
			await ctx.send(retour)
		else:
			retour = "Les mots de passe se génèrent sur 6 caractères minimums"
			await ctx.send(retour)
	else:
		await ctx.send("La fonction '!genrerP' fonctionne uniquement en message privé")
#Calculatrice utilise la librairie slash de discord pour générer des boutons intéractifs
@bot.command()
async def calculatrice(ctx):
	#Si le message de l'utilisateur ne se trouve pas dans un serveur
	if not ctx.guild:
		#Création des différents boutons de la calculatrice
		#Chaque liste (buttons, buttons2...) peut contenir jusqu'a 5 boutons, on utilisera ces listes pour les affichées sur les différents lignes via create_actionrow()
	        buttons = [
	            
	            create_button(
	                style=ButtonStyle.blue,
	                label="7",
	                custom_id="7"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label="8",
	                custom_id="8"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label="9",
	                custom_id="9"
	                ),
	            create_button(
	                style=ButtonStyle.gray,
	                label="+",
	                custom_id="plus"
	                )
	          
	            ]
	        
	        buttons2 = [
	            create_button(
	                style=ButtonStyle.blue,
	                label="4",
	                custom_id="4"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label="5",
	                custom_id="5"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label="6",
	                custom_id="6"
	                ),
	            create_button(
	                style=ButtonStyle.gray,
	                label="-",
	                custom_id="moins"
	                )
	            ]
	        
	        buttons3 = [
	            create_button(
	                style=ButtonStyle.blue,
	                label="1",
	                custom_id="1"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label="2",
	                custom_id="2"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label="3",
	                custom_id="3"
	                ),
	            create_button(
	                style=ButtonStyle.gray,
	                label="*",
	                custom_id="fois"
	                )
	            ]
	        
	        
	        buttons4 = [
	            
	            create_button(
	                style=ButtonStyle.blue,
	                label="0",
	                custom_id="0"
	                ),
	            create_button(
	                style=ButtonStyle.blue,
	                label=".",
	                custom_id="."
	                ),
	            create_button(
	                style=ButtonStyle.danger,
	                label="=",
	                custom_id="egale"
	                ),
	            create_button(
	                style=ButtonStyle.grey,
	                label="/",
	                custom_id="div"
	                ),
	            create_button(
	                style=ButtonStyle.danger,
	                label="fin",
	                custom_id="fin"
	                )
	            
	            
	           
	           
	            ]
	        #Create_actionrow permet de générer la ligne comprenant la liste donnée en paramètre
	        action_row = create_actionrow(*buttons)
	        action_row2 = create_actionrow(*buttons2)
	        action_row3 = create_actionrow(*buttons3)
	        action_row4 = create_actionrow(*buttons4)
	        #Afficher les actionrow pour former la calculatrice, les actions rows sont transmis à la fonction send sous forme de composant
	        choix = await ctx.send("Calculatrice :",components = [action_row, action_row2,action_row3,action_row4])
	        #Variables
	        b = False
	        premierTour = True
	        nbr1 = 0
	        resultat = 0
	        expression = ""
	        aff = ""
	        p = False
	        


	        while (b == False):
	            #wait_for_component permet d'attendre que l'utilisateur utilise un des boutons 
	            bouton_ctrl = await wait_for_component(bot,components = [action_row, action_row2,action_row3,action_row4])
	        
	            if (bouton_ctrl.custom_id == "fin"):
	            		#edit_origin permet de modifier le texte de base généré lors de l'affichage de la calculatrice
	                    await bouton_ctrl.edit_origin(content ="Fin")
	                    b = True

	            else:
	                
	                if (bouton_ctrl.custom_id != "plus" and bouton_ctrl.custom_id != "moins" and bouton_ctrl.custom_id != "div" and bouton_ctrl.custom_id != "fois"):
	                                

	                    expression = expression + bouton_ctrl.custom_id
	                    print("exp",expression)
	                    await bouton_ctrl.edit_origin(content =expression)
	                    premierTour = False
	                
	                if  (premierTour == True) and (bouton_ctrl.custom_id == "plus" or bouton_ctrl.custom_id == "moins" or bouton_ctrl.custom_id == "div" or bouton_ctrl.custom_id == "fois"):
	                    await bouton_ctrl.edit_origin(content ="Non autorisé")
	                    




	                    #-------------------------------------------------------------------------


	                if (bouton_ctrl.custom_id == "plus" and premierTour == False):
	                    nbr1 = float(expression)
	                    print(nbr1)
	                    expression =""
	                    await bouton_ctrl.edit_origin(content ="+")

	                    while(p == False):


	                        bouton_ctrl = await wait_for_component(bot,components = [action_row, action_row2,action_row3,action_row4])
	                        if (bouton_ctrl.custom_id != "egale"):
	                        
	                            if (bouton_ctrl.custom_id == "plus" or bouton_ctrl.custom_id == "moins" or bouton_ctrl.custom_id == "div" or bouton_ctrl.custom_id == "fois" or bouton_ctrl.custom_id == "fin" ):
	                                await bouton_ctrl.edit_origin(content ="Non autorisé")
	                                
	                            else:
	                                expression = expression + bouton_ctrl.custom_id

	                                print("exp",expression)
	                                await bouton_ctrl.edit_origin(content =expression)
	                        else:
	                            p = True

	                    resultat = nbr1 + float(expression)
	                    aff = "resultat final : " + str(resultat)
	                    await bouton_ctrl.edit_origin(content = aff)

	                    expression = ""
	                    nbr1 = 0
	                    resultat = 0
	                    p = False
	                    premierTour = True
	                    #---------------------------------------------------------------------------------

	                if (bouton_ctrl.custom_id == "moins" and premierTour == False):
	                    nbr1 = float(expression)
	                    print(nbr1)
	                    expression =""
	                    await bouton_ctrl.edit_origin(content ="-")

	                    while(p == False):

	                        bouton_ctrl = await wait_for_component(bot,components = [action_row, action_row2,action_row3,action_row4])
	                        if (bouton_ctrl.custom_id != "egale"):
	                        
	                            if (bouton_ctrl.custom_id == "plus" or bouton_ctrl.custom_id == "moins" or bouton_ctrl.custom_id == "div" or bouton_ctrl.custom_id == "fois" or bouton_ctrl.custom_id == "fin" ):
	                                await bouton_ctrl.edit_origin(content ="Non autorisé")
	                                
	                            else:
	                                expression = expression + bouton_ctrl.custom_id

	                                print("exp",expression)
	                                await bouton_ctrl.edit_origin(content =expression)
	                        else:
	                            p = True

	                    resultat = nbr1 - float(expression)
	                    aff = "resultat final : " + str(resultat)
	                    await bouton_ctrl.edit_origin(content = aff)

	                    expression = ""
	                    nbr1 = 0
	                    resultat = 0
	                    p = False
	                    premierTour = True
	                    #--------------------------------------------------------------------------------

	                if (bouton_ctrl.custom_id == "fois" and premierTour == False):
	                    nbr1 = float(expression)
	                    print(nbr1)
	                    expression =""
	                    await bouton_ctrl.edit_origin(content ="*")

	                    while(p == False):

	                        bouton_ctrl = await wait_for_component(bot,components = [action_row, action_row2,action_row3,action_row4])
	                        if (bouton_ctrl.custom_id != "egale"):
	                        
	                            if (bouton_ctrl.custom_id == "plus" or bouton_ctrl.custom_id == "moins" or bouton_ctrl.custom_id == "div" or bouton_ctrl.custom_id == "fois" or bouton_ctrl.custom_id == "fin" ):
	                                await bouton_ctrl.edit_origin(content ="Non autorisé")
	                                
	                            else:
	                                expression = expression + bouton_ctrl.custom_id

	                                print("exp",expression)
	                                await bouton_ctrl.edit_origin(content =expression)
	                        else:
	                            p = True

	                    resultat = nbr1 * float(expression)
	                    aff = "resultat final : " + str(resultat)
	                    await bouton_ctrl.edit_origin(content = aff)

	                    expression = ""
	                    nbr1 = 0
	                    resultat = 0
	                    p = False
	                    premierTour = True

	                    #---------------------------------------------------------------------------------

	                if (bouton_ctrl.custom_id == "div" and premierTour == False):
	                    nbr1 = float(expression)
	                    print(nbr1)
	                    expression =""
	                    await bouton_ctrl.edit_origin(content ="/")

	                    while(p == False):

	                        bouton_ctrl = await wait_for_component(bot,components = [action_row, action_row2,action_row3,action_row4])
	                        if (bouton_ctrl.custom_id != "egale"):
	                        
	                            if (bouton_ctrl.custom_id == "plus" or bouton_ctrl.custom_id == "moins" or bouton_ctrl.custom_id == "div" or bouton_ctrl.custom_id == "fois" or bouton_ctrl.custom_id == "fin" ):
	                                await bouton_ctrl.edit_origin(content ="Non autorisé")
	                                
	                            else:
	                                expression = expression + bouton_ctrl.custom_id

	                                print("exp",expression)
	                                await bouton_ctrl.edit_origin(content =expression)
	                        else:
	                            p = True

	                    resultat = nbr1 / float(expression)
	                    aff = "resultat final : " + str(resultat)
	                    await bouton_ctrl.edit_origin(content = aff)

	                    expression = ""
	                    nbr1 = 0
	                    resultat = 0
	                    p = False
	                    premierTour = True
	else:
						await ctx.send("La fonction '!calculatrice' fonctionne uniquement en message privé")




#La fonction !dire permet au bot de répéter le message que l'utilisateur a écrit
@bot.command()
async def dire(ctx, *texte):
    
    await ctx.send(" ".join(texte))
#Les différentes fonctions traduire utilise l'API de deepl, cette API est disponible sur python
@bot.command()
async def traduireEN(ctx, *message):
	print(message)
	message = " ".join(message)
	message = message.replace("'", ' ')
	#deepl.translator() permet d'initialiser la connexion avec deepl, le paramètre de cette fonction est le TOKEN
	translator = deepl.Translator("3574d2a4-ce63-a220-edb5-a336302ba645:fx")
	#translate_text() permet de commencer la traduction, on précise le message a traduire ainsi que la langue de retour pour ce message
	traduction = translator.translate_text(message, target_lang="EN-US")
	print(traduction)
	await ctx.send(traduction)
    
@bot.command()
async def traduireES(ctx, *message):
	message = " ".join(message)
	message = message.replace("'", ' ')
	translator = deepl.Translator("3574d2a4-ce63-a220-edb5-a336302ba645:fx")
	traduction = translator.translate_text(message, target_lang="ES") # -> ESPAGNOL
	print(traduction)
	await ctx.send(traduction)
    
@bot.command()
async def traduireDE(ctx, *message):
	message = " ".join(message)
	message = message.replace("'", ' ')
	translator = deepl.Translator("3574d2a4-ce63-a220-edb5-a336302ba645:fx")
	traduction = translator.translate_text(message, target_lang="DE") # -> ALLEMAND
	print(traduction)
	await ctx.send(traduction)
    
@bot.command()
async def traduireFR(ctx, *message):
	message = " ".join(message)
	message = message.replace("'", ' ')				
	translator = deepl.Translator("3574d2a4-ce63-a220-edb5-a336302ba645:fx")
	traduction = translator.translate_text(message, target_lang="FR") # -> FRANCAIS
	print(traduction)
	await ctx.send(traduction)

#Nettoyer permet de nettoyer une ou plusieurs lignes dans le salon ou l'utilisateur admin se trouve   
@bot.command()
async def nettoyer(ctx, nombre : int):
	if ctx.guild:
		#si l'utilisateur fait partie de la liste Admin générée lors de l'appele de la fonction lancementBot() alors on supprime les lignes demandées par ce dernier
		if str(ctx.message.author) in listeAdmin:
			messages = await ctx.channel.history(limit = nombre).flatten()
			for messages in messages:
				await messages.delete()
		else:
			await ctx.send("'!nettoyer' est utilisable uniquement par les profils Admin")

	else:
		messages = await ctx.channel.history(limit = nombre).flatten()
		for messages in messages:
			await messages.delete()
#Récupérer le nom des différentes stations pour une ligne de transport donnée
@bot.command()
async def stationsT(ctx, typeTrans, numTrans):
	r = ""
	nom = ""
	requete = "https://api-ratp.pierre-grimaud.fr/v4/stations/" + typeTrans + "/" + numTrans + "?way=A"
	#Récupération des valeurs de retours de la requete
	retour = requests.get(requete)
	#Conversion de la variable de type String en json
	contenu = retour.json()
	#Récupération des différents éléments de contenu (json)
	for i in range(1,25):
		nom = contenu["result"]["stations"][i]["name"]
		r = r + nom + "\n"
	if (retour != ""):
		await ctx.send(r) 
	else:
		retour = "Les paramètres ne sont pas corrects"
		await ctx.send(r)


#Transport est une fonction qui utilise l'API RATP, pour utiliser cette API on utilise des requetes HTTPS
@bot.command()
async def transport(ctx, typeTrans, numTrans, *depart):
	#%20 permet de renplacer les différents espaces de la variable depart pour y mettre %20 (cela est nécéssaire pour la requete HTTPS)
	depart = "%20".join(depart)
	#On prend en compte les ' et / pour éviter des problèmes de transmission lors de la requete HTTPS
	depart = depart.replace("'", '\'')
	depart = depart.replace("/", ' ')		
	#Requete envoyé à l'API
	requete = "https://api-ratp.pierre-grimaud.fr/v4/schedules/" + typeTrans + "/" + numTrans + "/" + depart + "/A%2BR"
	#Récupération des valeurs de retours de la requete
	retour = requests.get(requete)
	#Conversion de la variable de type String en json
	contenu = retour.json()
	#Récupération des différents éléments de contenu (json)
	if contenu["result"]["schedules"][0]["message"] != "Schedules unavailable": 
		directionA = contenu["result"]["schedules"][0]["destination"]
		directionB = contenu["result"]["schedules"][2]["destination"]
		tempsA = contenu["result"]["schedules"][0]["message"]
		tempsB = contenu["result"]["schedules"][2]["message"]
		#r correspond a la valeur de retour renvoyé à l'utilisateur
		r = "Prochain pour aller à : '"+ directionA + "' est dans '" + tempsA + "'\nProchain pour aller à : '" + directionB + "' est  dans '" + tempsB + "'"
		await ctx.send(r)
	else:
		await ctx.send("Les paramètres ne sont pas corrects")
#Chat est la fonction pour discuter avec le bot sans demander au bot d'executer des actions. Utilisation de la fonction IAchatBot qui utilise neuralintents
@bot.command()
async def chat(ctx, *message):
    message = " ".join(message)
    retour = ""
    retour = IAchatBot(message)
    await ctx.send(retour)

#CreerCT permet de créer des salons de type texte si l'utilisateur se trouve dans un serveur et si l'utilisateur est un admin
@bot.command()
async def creerCT(ctx, *nom, reason = None):
	if ctx.guild and str(ctx.message.author) in listeAdmin:
		nom = " ".join(nom)
		channel = await ctx.guild.create_text_channel(nom)
	else:
		await ctx.send("'!creerCT' est utilisable uniquement lorsque le bot se trouve dans un serveur et est utilisable uniquement par les profils Admin")
#CreerCV permet de créer des salons vocaux si l'utilisateur se trouve dans un serveur et si l'utilisateur est un admin
@bot.command()
async def creerCV(ctx, *nom, reason = None):
	print (ctx.message.author)
	if ctx.guild and str(ctx.message.author) in listeAdmin:
		nom = " ".join(nom)
		channel = await ctx.guild.create_voice_channel(nom)
	else:
		await ctx.send("'!creerCV' est utilisable uniquement lorsque le bot se trouve dans un serveur et est utilisable uniquement par les profils Admin")
#SuppC permet de supprimer des salons si l'utilisateur se trouve dans un serveur et si l'utilisateur est un admin
@bot.command()
async def suppC(ctx, *nom, reason = None):
	if ctx.guild and str(ctx.message.author) in listeAdmin:
		nom = " ".join(nom)
		channel = discord.utils.get(ctx.guild.channels, name=nom)
		if channel is not None:
			await channel.delete()
		else:
			await ctx.send("Le channel n'existe pas")
	else:
		await ctx.send("'!suppC' est utilisable uniquement lorsque le bot se trouve dans un serveur et est utilisable uniquement par les profils Admin")
#Info utilise les attributs de guild pour retourner à l'utilisateur le nombre de salons vocaux, des salons de type texte et le nombre de membres
@bot.command()
async def info(ctx):
	if ctx.guild:
		channelT = 0
		channelV = 0
		membre =  0
		for guild in bot.guilds:
			for channel in guild.voice_channels:
				channelV += 1
			for channel in guild.text_channels:
				channelT += 1	
			for member in guild.members:
				membre += 1
			membre = membre -1
		if channelV > 1:
			retour = "Il y'a " + str(channelV) + " salons vocaux\n"
		else:
			retour = "Il y'a " + str(channelV) + " salon vocal\n"

		if channelT > 1:
			retour = retour + "Il y'a " + str(channelT) + " salons de type texte\n"
		else:
			retour =  retour + "Il y'a " + str(channelT) + " salon de type texte\n"

		if membre > 1:
			retour =  retour + "Il y'a " + str(membre) + " membres dans le serveur : " + guild.name
		else:
			retour =  retour + "Il y'a " + str(membre) + " membre dans le serveur : " + guild.name

		await ctx.send(retour)
	else:
		await ctx.send("'!info' est utilisable uniquement lorsque le bot se trouve dans un serveur")
#ban es utilisé pour bannir (expulser) un utilisateur. Pour cela il est nécéssaire lors de l'appel de la fonction de donner le nom de l'utilisateur a bannir sous la forme de @TOTO#1222
#Il faut aussi donner la raison du bannissement

@bot.command()
async def ban(ctx, user : discord.User, *reason):
    if ctx.guild and str(ctx.message.author) in listeAdmin:
        reason = " ".join(reason)
        await ctx.guild.ban(user, reason = reason)
        await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")
    else:
    	await ctx.send("Vous n'avez pas les droits")
    	
#Unban permet de débannir un utilisateur en donnant une raison
@bot.command()
async def unban(ctx, user, *reason):
        if ctx.guild and str(ctx.message.author) in listeAdmin:
                    reason = " ".join(reason)
                    userName, userId = user.split("#")
                    bannedUsers = await ctx.guild.bans()
                    for i in bannedUsers:
                                if i.user.name == userName and i.user.discriminator == userId:
                                    await ctx.guild.unban(i.user, reason = reason)
                                    await ctx.send(f"{user} à été unban.")
                                    return
                    #Ici on sait que lutilisateur na pas ete trouvé
                    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")
        else:
        	await ctx.send("Vous n'avez pas les droits")


#Appel de la fonction pour lancer le bot    
lancementBot()