# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
# IMPORT THE OS MODULE.
import os
#WEBSCRAPING
import requests
#JSON
import json
#DOWNLOADPACKAGE
import urllib.request
#LibrariePDF2IMG
import pdf2image
#tempFile
import tempfile
from pdf2image import convert_from_path, convert_from_bytes

S = requests.Session()
# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv
# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()
# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=discord.Intents.all())
#client = commands.Bot(commands_prefix=)
# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
#WEBSCRAPING THINGS
URL = "http://www.songsterr.com/a/wa/bestMatchForQueryString"
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("ChiPia is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content[0] == "!":
		if message.content[1:6] == "song ":
			#for i in len(message.content):
			#	if message.content[i] == "-":
			#		songName = message.content[1:i-1]
			#		songArtist = message.content[i+1:]
			s=message.content[6:].split('-')
			songName = s[0].strip()
			songArtist = s[1].strip()
			instr = s[2].strip()
			PARAMS = {'s': songName, 'a': songArtist, 'inst': instr}
			R = S.get(url=URL, params=PARAMS)
			await message.channel.send(R.url)
		if message.content[1:7] == "song2 ":
			s = message.content[6:].split('-')
			songName = s[0].strip()
			songArtist = s[1].strip()
			instr = s[2].strip()
			PARAMS = {'s': songName, 'a': songArtist, 'inst': instr}
			R = S.get(url=URL, params=PARAMS)
			songId = R.url
			for chr in songId[::-1]:
				if chr.isdigit():
					temp = songId.index(chr)
			print(str(songId[temp:-2]))
			songId = songId[temp:-2]
			URL2 = "https://www.songsterr.com/api/meta/" + songId + "/revisions"
			URLCont = S.get(url=URL2).content
			y = json.loads(URLCont.decode())
			i = 0
			links = []
			while i < len(y):
				print(y[i]['source'])
				links.append(y[i]['source'])
				i += 1
			#await message.channel.send('\n'.join(links))
			careGP=0
			if links[0][-1]=="4":
				careGP=4
			elif links[0][-1]=="5":
				careGP=5
			urllib.request.urlretrieve(links[0],songId+".gp"+str(careGP))
			os.system('cmd /c "MuseScore4.exe -o '+songId+'.pdf '+songId+'.gp"'+str(careGP)+'"')
			#await message.channel.send(file=discord.File(songId+".pdf"))
			with tempfile.TemporaryDirectory() as path:
				images_from_path = convert_from_path(songId+".pdf", poppler_path=r'C:\Program Files (x86)\Release-23.08.0-0\poppler-23.08.0\Library\bin')
			images_from_path[0].save(songId+".jpeg")
			await message.channel.send(file=discord.File(songId + ".jpeg"))
		if message.content[1:] == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
			await message.channel.send("hey dirtbag")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)