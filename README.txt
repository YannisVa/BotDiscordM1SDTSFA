PROJET BOT DISCORD EN UTILISANT LA LIBRAIRIE PYTHON discord.py
Auteur : Vaulry Yannis

Dans le cadre de ma formation en master 1 OIVM parcours Système distribué et data science 
et plus précisément dans le cadre du cours : conception et analyse d’algorithmes (CAA),
j’ai pour but de réaliser un bot en utilisant l’API (application programming interface) discord.py.

-------------------------------------------------------------    |
DERNIERE UNTILISATION DU PROGRAMME : 17/02/2022                  | 
ATTENTION : DISCORD PREVOIT LA FIN DE discord.py pour AVRIL 2022.|
https://www.lemondedupc.fr/article/92-la-fin-de-discord-py       | 
-------------------------------------------------------------    | 
Utilisable sur :

-Windows 10
-Debian 10 ou 11
-MAC OS

-------------------------------------------------------------

Prérequis : 

-Python3 version : 3.7.9 https://www.python.org/downloads/release/python-397/
-pip pour installer les différentes librairies (Voir le document PrerequisBotSDTS)
-Token du bot (Voir le document PrerequisBotSDTS)
-1,5 go de mémoire disponible pour les différentes les librairies
-PC plus ou moins puissant et compatible avec TENSORFLOW (si ce n'est pas le cas le fichier DiscordBotDiscordSNI.py est disponible)
-FACULTATIF : TOKEN DEEPL

-------------------------------------------------------------

Installation via pip des librairies (Windows) : 

py3 -m pip install -U discord.py
py3 -m pip install -U deepl
py3 -m pip install -U neuralintents
py3 -m pip install -U discord-slash
py3 -m pip install -U discord-py-slash-command


	OU


py -m pip install discord.py
py -m pip install deepl
py -m pip install neuralintents
py -m pip install discord-slash
py -m pip install discord-py-slash-command


Tensoflow s'installe automatiquement avec neuralintents mais il peut etre nécéssaire de l'installer séparemment :
py -m pip install -U tensorflow

Installation via pip des librairies (Debian ou MACOS -> UNIX) : 

python3 -m pip install -U discord.py
python3 -m pip install -U deepl
python3 -m pip install -U neuralintents
python3 -m pip install -U discord-slash
python3 -m pip install -U discord-py-slash-command

Tensoflow s'installe automatiquement avec neuralintents mais il peut etre nécéssaire de l'installer séparemment :
python3 -m pip install -U tensorflow

-------------------------------------------------------------

Activation de nltk (librairie utilisé par neuralintents) : 
Pour ce faire il faut lancer python dans le cmd (Windows) via la commande : py3
Pour le lancement de python dans le terminal (Système UNIX), il faut utiliser : python3

Il faudra ensuite renseigner ceci : 

 >>> import nltk
 >>> nltk.download('omw-1.4')

Une fois cela il faut sortir de python en utilisant CTRL + Z + ENTRER

Pour exécuter le fichier "ProjetBotDiscord.py", il faut utiliser le terminal ou le CMD (selon l'OS).
Se trouver dans le meme répertoire que le fichier et vérifier que ce fichier est bien accompagné du fichier "intents.json"
Pour executer le py avec Windows : py ProjetBotDiscord.py
Avec Unix : python3 ProjetBotDiscord.py

Si l'installation de neuralintents ne fonctionne pas alors il est possible d'utiliser le fichier "ProjetDiscordSNI.py".

Le fichier PDF RapportVaulryYannis, ce fichier contient toutes les explications du fonctionnement du projet.
