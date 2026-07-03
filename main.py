import discord
from discord.ext import commands
import random
import time
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)
points = 0

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# qna = {
#     'what phenomenon of where the world is hotter than average, more disasters, and caused a greenhouse effect?' : 'climate change',
#     'Each one of trashes can cause massive trouble, but this one recycles by thousands of years later, what is it?' : 'plastic',
#     'True or false! is extreme weather linked to climate change?' : 'yes'


#     } await ctx.send("# Other questions :\n- Which is better? Eco friendly lights or LED lights?\n- What is the current sea level after 2025?")


# quiz, answer = random.choice(list(qna.items())) 
randomize = random.randint(1, 3)

@bot.command()
async def hello1(ctx):
    await ctx.send(f'Greetings! i am {bot.user}! Your personal AI-Climate Change assist! how may i help?')
    await ctx.send(f'> Type -help1 to know solutions!')
    await ctx.send(f'> Type -startquiz to play a pop of quiz with me!')
    await ctx.send('> Type -fact1 for facts!')
    await ctx.send('> Interested to talk with questions without games? type -questions!')

@bot.command()
async def help1(ctx):
    await ctx.send(f'Alot of recycling trashes, plastics,and other scraps of nothingness you could ever throw!')
    await ctx.send(f'But did you know there are other solutions that could be helpful too?')
    await ctx.send(f'Clean Energy Shifts! \n- Transition to Renewables: Replace coal, oil, and gas with solar, wind, and geothermal power.\n- Electrify Transportation: Switch to electric vehicles, trains, and public transit networks.\n- Upgrade Grid Efficiency: Build smart grids to distribute clean energy without power loss.')
    await ctx.send(f'> to continue, try typing -con1!')
    await ctx.send(f'> wanna play a pop quiz? try typing -startquiz, give it a try!')
    await ctx.send('> Interested to talk with questions without games? type -questions!')

@bot.command()
async def con1(ctx):
    await ctx.send(f'You see, struggles have been more constant lately, and we are sad to hear that\n people do not take action in such.')
    await ctx.send(f'But do not say you cannot do it! Out of your border of land, people are in need\n of your help, so take small solutions for now, like:')
    await ctx.send(f'💡Recycle your trashes : they have purpose to be beautiful as they are, they just need help of your hands, why not bother to make them like a fashion model? They can also be sold, both in a jackpot alright!')
    await ctx.send(f'💡Air-dry your clothes : dryers are just like hot airs, but just uses a massive amount of electricity, dry the clothes outside! You can chill out while drinking cold drinks for that hot air!')
    await ctx.send(f'💡Switch to LEDS : replace your lightbulbs with LED lights! they last longer than normal bulbs, but also can give massive aesthetic to a room! why not give it a try?')
    await ctx.send(f'💡Eat more plants, PLANTS! : they are good for you! Although tasteless, irritable texture.. They are just as good as eating a meat! But plants do have more variants! They are the most healthiest of them all.')
    await ctx.send(f'> to let the AI have a take on facts, try typing -fact1!')
    await ctx.send(f'> wanna play a pop quiz? try typing -startquiz, give it a try!')
    await ctx.send('> Interested to talk with questions without games? type -questions!')

@bot.command()
async def startquiz(ctx):
    await ctx.send(f'Seems like you are in for a quiz! I will let you choose numbers of 1-3\n and YOU will have to answer the question correctly!')
    await ctx.send(f'Pick a number from 1-5!\n> to type and choose the quiz, type -quiz (the number you chose between 1-3)')
    

    @bot.command()
    async def quiz(ctx, number:int):
        global points
        questions = ['what phenomenon of where the world is hotter than average, more disasters, and caused a greenhouse effect?', 'Each one of trashes can cause massive trouble, but this one recycles by thousands of years later, what is it?', 'True or false! is extreme weather linked to climate change?', 'Which gas contributes the most?', "what effect that causes gases that trap heat in Earth's atmosphere, warming the planet?"]
        answers = ['climate change', 'plastic', 'yes', 'carbon dioxide', 'greenhouse effect']
        question = questions[number-1]
        answer = answers[number-1]
        await ctx.send(question)

        def check(message):
            return (
                message.author == ctx.author
                and message.channel == ctx.channel
            )

        try:
            msg = await bot.wait_for("message", check=check, timeout=10)

            if msg.content.lower() == answer.lower():
                points += 1
                await ctx.send("✅ Correct!")
                await ctx.send(f'Points : {points}')
                if points == 5:
                    await ctx.send('Way to go pal! Do you wanna continue or end the quiz?')
                    await ctx.send('> to end, just type -endquiz!')
            else:
                await ctx.send(f"❌ Incorrect. The correct answer is **{answer}**")
            return
        except asyncio.TimeoutError:
            await ctx.send(f"⏰ Time's up! The answer is **{answer}**")

    @bot.command()
    async def endquiz(ctx):
        await ctx.send("Alright! Seems like you've got yourself a bit of a knowledge! I'm more of a simple bot, if you need anything, just let me know!")

@bot.command()
async def questions(ctx):
    await ctx.send("Oh? Asking questions i see! Here are the questions that are available for you to pick:\n- What is Climate change?\n- How to dispose trash?\n- What simple steps are there to help reduce climate change?\n- How to tell which trashes are organic or inorganic?\n- Is it worth it to recycle trashes?\n> type a number to let me answer the question! ex. 'one, two, three, etc.'")
    
    @bot.command()
    async def one(ctx):
        await ctx.send("Climate change refers to the long-term, significant shifts in global or regional weather patterns and average temperatures. While natural cycles have influenced Earth's climate historically, human activities—primarily the burning of fossil fuels like coal, oil, and gas—have been the primary driver since the 1800s.\n# How It Works\n- The Greenhouse Effect: When we burn fossil fuels or clear forests, we release greenhouse gases—such as carbon dioxide and methane—into the atmosphere. These gases act like a thermal blanket, trapping the sun's heat and warming the Earth's surface.\n- Global Warming: This continuous accumulation of heat-trapping gases is the direct cause of long-term global warming, which fundamentally alters local and global climates.")
        await ctx.send("2. How to dispose trash?\n3. What simple steps are there to help reduce climate change?\n4. How to tell which trashes are organic or inorganic?\n5. Is it worth it to recycle trash?")

    @bot.command()
    async def two(ctx):
        await ctx.send("To dispose of trash properly, you must segregate your waste at the source, bag it securely, and utilize your municipality's designated collection systems. Taking the time to separate your items ensures that recyclables stay out of landfills and hazardous materials do not pollute local ecosystems.")
        await ctx.send("1. What is Climate change\n3. What simple steps are there to help reduce climate change?\n4. How to tell which trashes are organic or inorganic?\n5. Is it worth it to recycle trash?")
    
    @bot.command()
    async def three(ctx):
        await ctx.send("Reducing climate change is highly achievable through daily adjustments to how you travel, eat, and consume energy. Simple, impactful actions include walking or using public transit to limit vehicle emissions, eating more plant-based meals, washing laundry in cold water, and shopping second-hand to reduce manufacturing waste.\n- Optimize Travel: Plan carpools or find local routes using public transportation mapping. You can check local options provided by Google Maps.\n- Reduce Household Energy: Switch to energy-efficient appliances and LED lighting to instantly cut your electricity use. Learn more about which upgrades make a difference with the U.S. EPA Energy Star Program.\n- Shop Responsibly: Fight fast fashion and mass consumerism by buying pre-owned goods or supporting sustainable brands.")
        await ctx.send("1. What is Climate change?\n2. How to dispose trash?\n4. How to tell which trashes are organic or inorganic?\n5. Is it worth it to recycle trash?")
    
    @bot.command()
    async def four(ctx):
        await ctx.send("Here is how you can easily identify and sort them:\n# 🌿 Organic Waste (Biodegradable)\nThese items originate from plants and animals. They rot naturally and can be turned into compost.\n- Food Scraps: Vegetable peels, fruit rinds, eggshells, tea leaves, coffee grounds, and leftover food.\n- Yard Waste: Dry leaves, grass clippings, and small twigs.\n- How to spot: They generally smell when they go bad, attract insects, and get soft or mushy over time.")
        await ctx.send("# 🏭 Inorganic Waste (Non-Biodegradable)\nThese items are typically human-made, synthetic, or non-living minerals. They do not rot and can cause pollution if left in landfills.\n- Plastics: Plastic bottles, grocery bags, straws, food packaging, and Styrofoam.Metals: Aluminum cans, aluminum foil, and old nails.\n- Glass: Broken windows, drinking glasses, and glass bottles.\n- Paper & Cardboard: Although they come from trees, once they are processed industrially, they are treated as inorganic waste in everyday sorting.\n- How to spot: They hold their shape, can be washed or wiped down, and do not break down in water or soil.")
        await ctx.send("1. What is Climate change?\n2. How to dispose trash?\n3. What simple steps are there to reduce climate change?\n5. Is it worth it to recycle trash?")

    @bot.command()
    async def five(ctx):   
        await ctx.send("Yes, recycling is absolutely worth it, but its effectiveness depends heavily on the material and avoiding contamination. While not a silver bullet, doing your part diverts waste from landfills and reduces the need to extract fresh, raw resources\n# How to Make Your Recycling 'Worth It'\nTo ensure your recycling actually gets processed instead of becoming 'wish-cycling' that contaminates an entire batch, follow these best practices:\n- Check local guidelines: Local municipalities vary widely on what they accept. Always check with your local waste management or government office to see exactly what materials (and plastic numbers) are accepted in your area.\n- Keep it clean: Give containers a quick rinse to remove food or liquid residue. Contaminated items can ruin whole batches of recyclables.Remove caps: Take caps and lids off plastic bottles before tossing them in the bin.\n- Keep out plastic bags: Traditional plastic grocery bags usually jam sorting machinery. Instead, collect them and drop them off at designated grocery or pharmacy collection bins.") 
        await ctx.send("# The Golden Rule: Reduce and Reuse\nWhile recycling is a crucial step, the most effective way to manage waste is to prevent it from being created in the first place. Prioritize reducing consumption, reusing items, and choosing products with less packaging.")
        await ctx.send("1. What is Climate change?\n2. How to dispose trash?\n3. What simple steps are there to help reduce climate change?\n4. How to tell which trashes are organic or inorganic?")

# yueheuhehehehehehehe slesai yeuhehe

@bot.command()
async def fact1(ctx):
    await ctx.send(f'Seems like you are interested for facts! here are some of them :\n💡Greenhouse Effect: Gases like carbon dioxide (CO2) and methane act like a blanket around the Earth. They let sunlight in but trap heat from escaping back into space.\n💡Carbon Levels: CO2 in the atmosphere sits at its highest concentrations in human history, largely due to industrial processes, transportation, and electricity generation.')
    await ctx.send('💡 Deforestation: Forests naturally absorb CO2; destroying them releases stored carbon and removes a vital planetary cooling mechanism.\n💡Ice Loss & Sea Levels: The planet is losing over 1 trillion tons of ice annually, contributing to rising sea levels that threaten global coastlines.\n💡Extreme Weather: Warmer temperatures cause moisture to evaporate faster, resulting in more intense heatwaves, longer droughts, and heavier, more frequent storms and floods.')
    await ctx.send('> wanna play a pop quiz? try typing -startquiz, give it a try!')
    await ctx.send('> Interested to talk with questions without games? type -questions!')

bot.run('MTUxNTMzMTU3OTI5ODQ1MTQ1Ng.GBwPss.GtfnuNhMJbeX83jnRXe63tcmKxcY27aFETxRNw')
