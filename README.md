# ChiPia
 This is a discord bot made to scrap Songsterr in order to get the music sheet of the song of your choice (on your choice instrument).
 
 How it works?
 This script uses the public Songsterr API to make a call with the given song name/artist name/instrument of your choice as parameters that returns the latest version of the first arrangements that matches your parameters (usually in Guitar Pro format/.gp5); afterwards the file is converted using the MuseScore API into another format: for example .png in order to be able to easily acess and see the Music Sheet straight in the Discord chat
 
 How to use?
 1. log in using the Discord Developer Portal and grab your Bot's latest Discord Token
 2. replace the Discord Token with your working current key in the .env
 3. run main.py
 4. add the bot to your target server
 [OPTIONAL: configure the bot (change which server the bot can read/send messages to or the parameters to call the bot)]
 5. give a querry to the bot (e.g. !song2 Nothing else matters - Metallica - Guitar)
 6. enjoy the sheet music!
