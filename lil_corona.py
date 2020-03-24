# bot.py
import discord
from datetime import datetime
from bs4 import BeautifulSoup
import requests

client = discord.Client()

embed = discord.Embed(title="", colour=discord.Colour(0xd0021b), url="", timestamp= datetime.utcfromtimestamp(1585021097))
embed.set_thumbnail(url="")
embed.set_footer(text="", icon_url="")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="Awaiting summon...")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$summon'):
        page_link = 'https://www.worldometers.info/coronavirus/'
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        number_set = page_content.find_all('div', class_='maincounter-number')

        total_cases = number_set[0].get_text()
        deaths = number_set[1].get_text()
        recovered = number_set[2].get_text()

        new_lst = []
        str_lst = [total_cases, deaths, recovered]
        for element in str_lst:
          element = element.strip()
          element = element.replace(',','')
          element = int(element)
          new_lst.append(element)

        total_cases = new_lst[0]
        deaths = new_lst[1]
        recovered = new_lst[2]

        death_ratio = (deaths/total_cases)*100
        death_ratio = ("{:.1f}".format(death_ratio))
        recovery_rate = (recovered/total_cases)*100
        recovery_rate = ("{:.1f}".format(recovery_rate))
        still_sick = (total_cases - deaths - recovered)
        await message.channel.send(content="", embed=embed)
        await message.channel.send(" *Total cases*: " + str(total_cases) + '\n')
        await message.channel.send(" *Deaths*: " + str(deaths) + '\n')
        await message.channel.send(" *Recovered*: " + str(recovered) + '\n')
        await message.channel.send(" *Still infected*: " + str(still_sick)+'\n'+'\n')
        await message.channel.send(" *Death* : " + str(death_ratio) +"% \n")
        await message.channel.send(" *Recovery*: " + str(recovery_rate) +"% \n")

client.run('')
