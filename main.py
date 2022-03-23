from nextcord import Member, Embed, Color, ActivityType, Activity, Intents, Status
from nextcord.ext import commands
from config import Owner_IDS, Token
print ("hello grim!")

bot = commands.Bot(command_prefix="ä", help_command=None, owner_ids=Owner_IDS, activity=Activity(type=ActivityType.watching, name="eZaR's status UwU"), intents=Intents.all())

@bot.event
async def on_ready():
    print("watching eZaR :D")

@bot.event
async def on_error():
    pass


@bot.event
async def on_presence_update(before: Member, after: Member):
    if after.guild.id == 922364228365582356:
        if after.id == 906816722676371496:
            status_channel = after.guild.get_channel(911196897631424573)

            if not after.status in [Status.dnd, Status.idle, Status.online]:
                offline_embed = Embed(color=Color.red(), description="<:eZaR_offline:924988220062711859> eZaR is offline! Please wait while we solve the issue.", title="Offline moment lol")
                await status_channel.send(content="<@&911199514675802142>", embed=offline_embed)
            elif after.status == Status.online:
                now_online_embed = Embed(color=Color.green(), description="<:eZaR_online:911562297695141888> eZaR is back online! Applogies for the offline time.", title="Online yey")
                await status_channel.send(content="<@&911199514675802142>", embed=now_online_embed)
                print(after.status)

bot.run(Token)
