import discord



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        elif message.content.startswith('!bot'):
            await message.channel.send("You rang?")


        #crafting recipes for carpenter

        elif message.content.startswith('?maplelumber'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/f3ffcf2c8fd/')

        elif message.content.startswith('?mapleclogs'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/f79d553086b/')

        elif message.content.startswith('?mapleshortbow'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/4fbbbf5cd11/')

        elif message.content.startswith('?boneharpoon'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/f1a6a67f7a1/')

        elif message.content.startswith('?amateursgrindingwheel'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/946a06b23dd/')

        elif message.content.startswith('?maplepattens'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/b12e9f23b1c/')

        elif message.content.startswith('?amateursspinningwheel'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/d88afdd7cd0/')

        elif message.content.startswith('?squaremapleshield'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/af000818eca/')

        elif message.content.startswith('?bronzespear'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/1843a5c9e5e/')

        elif message.content.startswith('?maplecane'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/37e9712ff53/')

        elif message.content.startswith('?maplebow'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/dcbdb02ffdf/')

        elif message.content.startswith('?maplecrook'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/f6d73fdd68f/')

        elif message.content.startswith('?maplefishingrod'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/25ca5ef4b0b/')

        elif message.content.startswith('?plumedmapleshortbow'):
            await message.channel.send('https://na.finalfantasyxiv.com/lodestone/playguide/db/recipe/e2d060122ba/')



client = MyClient()
client.run('NTk2NDg4MDcxNDg3MjkxNDIz.Xlr2vQ.0mHdODqBt-wwsEDARa6pdGtcLfI')