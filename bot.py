import discord
from discord.ext import commands
from discord.ui import View, Select
import os

# ------------------- BOT SETUP -------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Get Discord bot token from Railway environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Please set the DISCORD_BOT_TOKEN environment variable!")

# ------------------- RULES DATA -------------------
rules = {
    "1-10": [
        "1. RDM (Random Deathmatch)\n⤷ Killing a player without a valid roleplay reason will result in a warning.",
        "2. Staff RDM\n⤷ Killing or shooting staff members will result in a 7-day ban.",
        "3. New Life Rule (NLR)\n⤷ After respawning, you must roleplay as a new character and cannot return to your previous life.",
        "4. VDM (Vehicle Deathmatch)\n⤷ Damaging or destroying another player’s vehicle outside of roleplay will result in a warning.",
        "5. Cuff Rushing\n⤷ Cuffing a player without proper RP or without saying “-cuffs-” will result in a warning.",
        "6. Auto Jailing\n⤷ Jailing a criminal automatically without transporting them to the jail will result in a warning.",
        "7. Staff Disrespect\n⤷ Disrespecting staff or ignoring instructions will result in a warning.",
        "8. LTAP (Leaving to Avoid Punishment)\n⤷ Leaving the game to avoid a kick or ban will result in an immediate ban. Staff can enforce this even if you are offline.",
        "9. Failing Roleplay (FRP)\n⤷ Breaking roleplay or failing to participate properly in a scenario will result in a warning.",
        "10. Fear Roleplay (FRP)\n⤷ If held at gunpoint or kidnapped, you must comply and act according to the roleplay scenario, as your character’s life is in danger."
    ],
    "11-20": [
        "11. Safezones\n⤷ Killing or shooting in safe zones, such as Civilian Spawn, Police Station, Fire Department, and all active borders, will result in a warning.",
        "12. Bribery\n⤷ Bribery of any kind is not allowed. Perks or features cannot be obtained through bribes.",
        "13. Border Violation\n⤷ Crossing borders without proper authorization or ignoring the roleplay scenario will result in a warning or ban, depending on severity.",
        "14. Griefing\n⤷ Intentionally interfering with another player’s roleplay, such as blocking paths, destroying property, or provoking others, will result in a warning.",
        "15. Combat Logging\n⤷ Logging out during active roleplay or combat will result in a warning and may lead to a ban if repeated.",
        "16. Powergaming\n⤷ Forcing actions on other players without consent or ignoring realistic roleplay limits will result in a warning. Always respect the roleplay and fairness.",
        "17. Metagaming\n⤷ Using out-of-character knowledge to influence in-game decisions will result in a warning. Only in-game knowledge should be used for roleplay.",
        "18. Mass RDM (Random Deathmatch)\n⤷ Killing multiple players, cops, or admins without proper roleplay reasoning is prohibited and will result in an immediate ban.",
        "19. Disruption of RP\n⤷ Disrupting ongoing roleplay through off-topic behavior, spam, or trolling will result in a warning. Continued disruption may lead to further action.",
        "20. Prop Abuse\n⤷ Misusing in-game props to block areas, create obstacles, or exploit game mechanics will result in a warning and may lead to additional punishment."
    ],
    "21-30": [
        "21. Unauthorized Use of Admin Commands\n⤷ Players must not use admin commands or cheat tools to gain an unfair advantage. Violating this rule will result in an immediate ban.",
        "22. Border Control Violations\n⤷ Attempting to bypass or interfere with Border Control procedures, including smuggling or unauthorized access, will result in punishment depending on severity.",
        "23. No Meta-Tactics\n⤷ Exploiting known tactics, such as safe spots, bypassing border restrictions, or unfairly outsmarting others, is prohibited. Always respect the roleplay scenario and play fairly.",
        "24. Respect for Roleplay Characters\n⤷ Disrespecting or mocking other players’ roleplay characters, or engaging in discriminatory actions within roleplay, will result in a warning.",
        "25. Weapon Abuse\n⤷ Using weapons for non-roleplay activities, such as random shooting or unnecessary destruction, will result in a warning or temporary ban.",
        "26. No Excessive OOC (Out-of-Character) Chat\n⤷ Excessive OOC chat disrupts roleplay immersion. Use OOC chat sparingly and only when necessary for clarification.",
        "27. No Spamming\n⤷ Spamming messages, commands, or in-game actions is prohibited and will result in a warning or temporary mute.",
        "28. Respect for Roleplay Boundaries\n⤷ Do not engage in roleplay that makes others uncomfortable or crosses personal boundaries. If a player requests to stop a scenario, respect their decision immediately.",
        "29. No Exploiting Bugs\n⤷ Exploiting bugs or glitches to gain an advantage or disrupt gameplay is strictly prohibited and will result in an immediate ban.",
        "30. No Multiple Accounts\n⤷ Using multiple accounts to bypass bans, gain unfair advantages, or exploit the server will result in a permanent ban for all accounts involved."
    ],
    "31-40": [
        "31. Bypassing Chat Filter\n⤷ Bypassing the chat filter to say inappropriate or filtered words is not allowed. All communication must remain safe and appropriate for all players.",
        "32. Bypassing Anti-AFK\n⤷ Using tools, scripts, or any method to bypass the anti-AFK system is prohibited and may result in a stat reset or ban.",
        "33. Roblox’s Terms of Service\n⤷ All players must follow Roblox’s Terms of Service. Violations such as exploiting, sharing inappropriate content, or breaking community rules may result in permanent bans.",
        "34. Staff Impersonation\n⤷ Pretending to be a staff member or using similar usernames, tags, or behavior is strictly forbidden and will result in a ban.",
        "35. Mini Modding\n⤷ Do not act as staff if you are not one. Report rule-breakers to actual moderators instead of attempting to enforce rules yourself.",
        "36. L-Tapping\n⤷ Leaving the game while involved in an active staff scene or disciplinary process is prohibited and will result in a ban.",
        "37. Ro-Banging\n⤷ Using an avatar to simulate suggestive actions is strictly forbidden. This behavior will result in a permanent ban.",
        "38. Severe Ro-Banging\n⤷ Engaging in highly inappropriate or extreme suggestive acts using chat and avatar actions will lead to a permanent ban and be reported to Roblox moderation.",
        "39. Radio Spamming\n⤷ Spamming or sending irrelevant messages on the radio disrupts gameplay and will result in a warning or mute.",
        "40. Firearm Abuse\n⤷ Using firearms in restricted areas like the Parade Deck or against authorized/military personnel without roleplay reason will result in punishment."
    ]
}

# ------------------- SELECT MENU -------------------
class RuleSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="1-10 Game Rules", value="1-10", emoji="📕),
            discord.SelectOption(label="11-20 Game Rules", value="11-20", emoji="📕),
            discord.SelectOption(label="21-30 Game Rules", value="21-30", emoji="📕),
            discord.SelectOption(label="31-40 Game Rules", value="31-40", emoji="📕),
        ]
        super().__init__(placeholder="Press Here For Game Rules", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        rule_text = "\n".join(rules[selected])
        embed = discord.Embed(
            title=f"📖 SRP | {selected} Rules",
            description=rule_text,
            color=discord.Color.blue()
        )
        # ✅ Respond properly to the interaction
        await interaction.response.send_message(embed=embed, ephemeral=True)

class RuleView(View):
    def __init__(self):
        super().__init__()
        self.add_item(RuleSelect())

# ------------------- POST RULES COMMAND -------------------
@bot.command()
async def ehingamerules(ctx):
    embed = discord.Embed(
        title="📖 SRP | SERIOUS ROLEPLAY — General In-Game Rules",
        description=(
            "Welcome to SRP | Serious Roleplay! To ensure a fun, fair, and immersive experience for all players, "
            "everyone must follow the server’s general in-game rules. These rules apply to all players regardless of role or rank and cover behavior, gameplay, and fair roleplay standards.\n\n"
            "⚠️ Important Notices\n\n"
            "Respect all players and staff. Harassment, racism, discrimination, or toxic behavior will not be tolerated.\n"
            "No exploiting glitches, bugs, or game mechanics for unfair advantage.\n"
            "Do not engage in random deathmatch (RDM) or random vehicle deathmatch (VDM). All kills must have a valid RP reason.\n"
            "Follow all roleplay rules, including those specific to your department or role.\n"
            "Use appropriate language and content in all chat and voice channels.\n"
            "Staff decisions are final. Appeals may be made, but all players must respect rulings in the meantime.\n\n"
            "🔄 Rule Updates\n"
            "Rules may be updated at any time. You are responsible for staying informed of current policies. Ignorance of the rules is not an acceptable excuse."
        ),

        


        
        color=discord.Color.dark_blue()
    )

    # Add the image at the bottom (above the dropdown)
    embed.set_image(url="https://i.postimg.cc/prb2FRjQ/IN-GAME-RULES.png")

    # Add the dropdown menu
    view = RuleView()
    await ctx.send(embed=embed, view=view)

    

# ------------------- RUN BOT -------------------
bot.run(TOKEN)
