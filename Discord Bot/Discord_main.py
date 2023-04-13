import discord
from discord.ext import commands
from discord.ui import Button, View, Select
from Firebasefile import *
import os
from keep_alive import keep_alive



bot = discord.Bot(command_prefix="!", intents = discord.Intents.all())

def embed_creation(num):
    if num == 0:
        return None
    if num==1:    
        embed = discord.Embed(
                    title="Premium Format",
                    colour=discord.Colour.orange()
                )
    elif num==2:
        embed = discord.Embed(
                    title="V Premium Format",
                    colour=discord.Colour.orange()
                )
    elif num==3:
        embed = discord.Embed(
                    title="Standard Format",
                    colour=discord.Colour.orange()
                )
    return embed
embed_challenge = embed_creation(0)

def create_name(namestring):
    newname = ""
    for i in namestring:
        if i=="#":
            continue
        else:
            newname += i
    return newname
    
l1 = []
choice = 0
@bot.event
async def on_ready():
    print("Online")


@bot.slash_command(guild_ids=[1011222494797123587, 765922497672642601], description="Leaderboards")
async def vgleaderboard(ctx):
    view = LeaderBoard()
    await ctx.respond(view=view)

class LeaderBoard(View):
    @discord.ui.select(placeholder="Choose a Format",
        options=[
        discord.SelectOption(label="Premium Format"),
        discord.SelectOption(label="V Premium Format"),
        discord.SelectOption(label="Standard Format")
    ])
    async def select_callback(self, select, interaction):
        if select.values[0] == "Premium Format":
            embed = leaderboards(1)
        elif select.values[0] == "V Premium Format":
            embed = leaderboards(2)
        elif select.values[0] == "Standard Format":
            embed = leaderboards(3)
        await interaction.response.send_message(embed = embed)

@bot.slash_command(guild_ids=[1011222494797123587, 765922497672642601], description="Register for Rank Fights")
async def register(ctx):
    name = str(ctx.author)
    newname = create_name(name)
    registerping = Register(name=newname,premwinstat=1200,vpremwinstat=1200,standardwinstat=1200)
    check = registerping.registration_check()
    embed = discord.Embed(
        title="Registeration",
        description="Registered",
        colour=discord.Colour.orange()
    )
    if check is True:
        embed = discord.Embed(
            title="Registeration",
            description="Already Registered",
            colour=discord.Colour.orange()
        )
        await ctx.respond(embed=embed)
    else:
        registerping.registration_embed()
        await ctx.respond(embed=embed)


class MatchDecide(View):
    @discord.ui.select(placeholder="Outcome",
                         options = [
                         discord.SelectOption(label="Player 1 Wins"),
                         discord.SelectOption(label="Player 2 wins"),
                         ])
    
    async def select_callback(self, select, interaction):
        if interaction.user not in l1:
            await interaction.response.send_message("Stay Out of this", ephemeral = True)
        else:
            
            if select.values[0]=="Player 1 Wins":
                select.disabled = True
                name = str(l1[0])
                name2 = str(l1[2])
                newname = create_name(name)
                newname2 = create_name(name2)
                win_up = Wins(newname)
                win_up2 = Wins(newname2)
                if l1[1] == 1:
                    win_up.premium_list()
                    win_up2.premium_lose()    
                elif l1[1] == 2:
                    val2 = trophy2.last_vpremium_trophy()
                    win_up.vpremium_list()
                    win_up2.vpremium_lose()
                elif l1[1] == 3:
                    val2 = trophy2.last_standard_trophy()
                    win_up.standard_list()
                    win_up2.standard_lose()
                embed_win = discord.Embed(
                    title = name + " wins",
                    description="Stats updated",
                    colour=discord.Colour.orange()
                )
                await interaction.response.edit_message(embed = embed_win, view = self)

            elif select.values[0] == "Player 2 wins":
                select.disabled = True
                name = str(l1[2])
                name2 = str(l1[0])
                newname = create_name(name)
                newname2 = create_name(name2)
                win_up = Wins(newname)
                win_up2 = Wins(newname2)
                if l1[1] == 1:
                    win_up.premium_list()
                    win_up2.premium_lose()    
                elif l1[1] == 2:
                    win_up.vpremium_list()
                    win_up2.vpremium_lose()
                elif l1[1] == 3:
                    win_up.standard_list()
                    win_up2.standard_lose()
                embed_win = discord.Embed(
                    title = name + " wins",
                    description="Stats updated"
                )
                await interaction.response.edit_message(embed = embed_win, view = self)
            
                
            

class ChallengeAccept(View):
    @discord.ui.button(label="Accept", style = discord.ButtonStyle.green, emoji="⚔️")
    async def button_callback(self, button, interaction):
        if interaction.user in l1:
            await interaction.response.send_message("Bruh are you dumb!", ephemeral = True)
        else:    
            l1.append(interaction.user)
            name = str(interaction.user)
            newname = create_name(name)
            trophy = Trophy(newname)
            view = MatchDecide()
            if l1[-2] == 1:    
                wins = trophy.last_premium_trophy()
            elif l1[-2] == 2:
                wins = trophy.last_vpremium_trophy()
            elif l1[-2] == 3:
                wins = trophy.last_standard_trophy()
            embed_challenge.add_field(
                        name = "Player 2 \n" +name,
                        value = "🏆" + str(wins)
                    )
            await interaction.response.edit_message(embed = embed_challenge, view = view)
        
class VanguardFormatView(View):
    @discord.ui.select(placeholder="Choose a Format",
                         options = [
                         discord.SelectOption(label="Premium Format"),
                         discord.SelectOption(label="V Premium Format"),
                         discord.SelectOption(label="Standard Format")
                         ])
    async def select_callback(self, select, interaction):
        view = ChallengeAccept()
        l1.append(interaction.user)
        name = str(interaction.user)
        newname = create_name(name)
        trophy = Trophy(newname)
        global embed_challenge
        if select.values[0]=="Premium Format":
            embed_challenge = embed_creation(1)
            wins = trophy.last_premium_trophy() 
            l1.append(1)
        elif select.values[0]=="V Premium Format":
            embed_challenge = embed_creation(2)
            wins = trophy.last_vpremium_trophy()
            l1.append(2)
        elif select.values[0]=="Standard Format":
            embed_challenge = embed_creation(3)
            wins = trophy.last_standard_trophy()
            l1.append(3)
        embed_challenge.add_field(
                name = "Player 1 \n" + name,
                value = "🏆" + str(wins)
            )
        await interaction.response.edit_message(embed = embed_challenge,view = view)
        
            
@bot.slash_command(guild_ids=[1011222494797123587, 765922497672642601], description="Register for Rank Fights")
async def cardfight(ctx):
    global l1
    view = VanguardFormatView()
    embed1 = discord.Embed(
                title="Format Selection",
                colour= discord.Colour.orange()
    )
    await ctx.respond(embed = embed1,view = view)


bot.run("MTAxMTY1MTQ4ODMxOTI3NTA2OQ.GI2PQk.RaIcrWy8XujWbQ9y0Zv8J9RmBSVXG35PE6HrWo")