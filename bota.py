import discord
from discord.ext import commands
from discord import Color

bot = commands.Bot(command_prefix="#")
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name="Ticketbot")
    await bot.change_presence(activity=activity, status=discord.Status.do_not_disturb)


@bot.event
async def on_reaction_add(reaction,user):
  if user.id != 866732901953044483:
      guild = guildticket
      channelexists = discord.utils.get(guild.text_channels,name=user.name.lower().replace("#",""))
      if channelexists:
          None
      else:
          admin_role = discord.utils.get(guild.roles, name="Projektleiter")
          management_role = discord.utils.get(guild.roles, name="Management")
          tx_moderator_role = discord.utils.get(guild.roles, name="Tx Moderator")
          entwickler_role = discord.utils.get(guild.roles, name="Entwickler")
          entwicklungsleitung_role = discord.utils.get(guild.roles, name="Entwicklungsleitung")
          fraktionsleitung_role = discord.utils.get(guild.roles, name="Fraktionsleitung")
          supporter_role = discord.utils.get(guild.roles, name="Supporter")
          moderator_role = discord.utils.get(guild.roles, name="Moderator")
          teamleitung_role = discord.utils.get(guild.roles, name="Teamleitung")
          stv_projektleiter_role = discord.utils.get(guild.roles, name="Stv. Projektleiter")
          botrolle = discord.utils.get(guild.roles,id=866784378470531094)
          category = discord.utils.get(guild.categories, id=866407871130239016)
          if reaction.emoji == '🖤':
              overwrites = {
                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
              }
              channel = await guild.create_text_channel(name=f"{user.name}",category=category, overwrites=overwrites)
              await channel.set_permissions(user,read_messages=True,send_messages=True)
              await channel.send(f"<@{user.id}> - Donation\nStelle deine Frage, ein Teammitglied wird sich gleich um dich kümmern!") 
          elif reaction.emoji == '💚': 
              overwrites = {
                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  management_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  tx_moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  supporter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  entwickler_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  entwicklungsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  stv_projektleiter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  teamleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  fraktionsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
              }
              channel = await guild.create_text_channel(name=f"{user.name}",category=category, overwrites=overwrites)   
              await channel.set_permissions(user,read_messages=True,send_messages=True)
              await channel.send(f"<@{user.id}> - Bug Report\nStelle deine Frage, ein Teammitglied wird sich gleich um dich kümmern!")
          elif reaction.emoji == '💙': 
              overwrites = {
                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  management_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  tx_moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  supporter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  entwickler_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  entwicklungsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  stv_projektleiter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  teamleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  fraktionsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
              }
              channel = await guild.create_text_channel(name=f"{user.name}",category=category, overwrites=overwrites)  
              await channel.set_permissions(user,read_messages=True,send_messages=True)
              await channel.send(f"<@{user.id}> - Allgemeine Fragen\nStelle deine Frage, ein Teammitglied wird sich gleich um dich kümmern!")
          elif reaction.emoji == '💜': 
              overwrites = {
                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  stv_projektleiter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  teamleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
              }
              channel = await guild.create_text_channel(name=f"{user.name}",category=category, overwrites=overwrites) 
              await channel.set_permissions(user,read_messages=True,send_messages=True)
              await channel.send(f"<@{user.id}> - Team Beschwerde\nStelle deine Frage, ein Teammitglied wird sich gleich um dich kümmern!")
          elif reaction.emoji == '🤍': 
              overwrites = {
                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  management_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  tx_moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  supporter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  entwickler_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  entwicklungsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  stv_projektleiter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  teamleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  fraktionsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
              }
              channel = await guild.create_text_channel(name=f"{user.name}",category=category, overwrites=overwrites) 
              await channel.set_permissions(user,read_messages=True,send_messages=True)
              await channel.send(f"<@{user.id}> - Entbannungsantrag\nStelle deine Frage, ein Teammitglied wird sich gleich um dich kümmern!")
          elif reaction.emoji == '🤎':    
              overwrites = {
                  guild.default_role: discord.PermissionOverwrite(read_messages=False),
                  guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  management_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  admin_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  tx_moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  moderator_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  entwickler_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  entwicklungsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                  stv_projektleiter_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  teamleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True), 
                  fraktionsleitung_role: discord.PermissionOverwrite(read_messages=True, send_messages=True),
              }
              channel = await guild.create_text_channel(name=f"{user.name}",category=category, overwrites=overwrites)
              await channel.set_permissions(user,read_messages=True,send_messages=True)
              await channel.send(f"<@{user.id}> - Fraktionsanfrage\nStelle deine Frage, ein Teammitglied wird sich gleich um dich kümmern!")  


@bot.command()
async def ticket(ctx):
    global guildticket
    guildticket = ctx.guild
    embed = discord.Embed(
        colour=Color.red()
    )
    embed.set_author(name="⚡️ Tickets ⚡️")
    embed.add_field(name="TicketBot",value="Ticketsystem\n\nBenutzen Sie für ihr Passendes Thema das passende Ticket!\n\nEs ist verboten Tickets ohne Grund zu öffnen!\n\nBevor du ein Ticket öffnest Versuch dein Anliegen im Support oder auf Teamspeak zu klären.\n\n- Donation :black_heart:\n- Bug Report :green_heart:\n- Allgemeine Frage :blue_heart:\n- Team Beschwerde :purple_heart:\n- Entbannungsantrag :white_heart:\n- Fraktionsanfrage :brown_heart:")
    embed.set_footer(text=f"Angefordert von {ctx.author}")

    dontation = '🖤'
    bug_report = '💚'
    allgemeine_fragen = '💙'
    team_beschwerde = '💜'
    entbannungsanträge = '🤍'
    fraktionsanfrage = '🤎'
    message = await ctx.send(embed=embed)
    await message.add_reaction(dontation)
    await message.add_reaction(bug_report)
    await message.add_reaction(allgemeine_fragen)
    await message.add_reaction(team_beschwerde)
    await message.add_reaction(entbannungsanträge)
    await message.add_reaction(fraktionsanfrage)

bot.run("ODY2NzMyOTAxOTUzMDQ0NDgz.YPW16g.QzwRddtRKgG4Cbc92dVScp-fQIE")   
