## lil-corona 
Prerequisites discord.py, BeautifulSoup and requests.

A python bot that provides live Coronavirus to your Discord server.

1.) Download the .py file in the desired directory.

2.) Edit the TOKEN in parameter ```client.run('')``` to match your bots, specifically.

3.) Navigate to where you've put the .py file via cli and execute

4.) In the text channel of your choice envoke virus stats via the ```$summon``` command.


# Optional 
You can put the following code underneath  ```client = discord.Client()``` (line 8) to have the groundwork for an embed.

Simply edit the fields to contain your data, then on line 52 put your embed title in ```content=""```

If you don't want an embed then simply delete line 10-12 and remove line 52.
