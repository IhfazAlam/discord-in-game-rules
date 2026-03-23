import discord
from discord.ext import commands
from discord.ui import View, Select
import os

# ------------------- BOT SETUP -------------------
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Get Discord bot token from environment variable
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
        "11. Safezones\n⤷ Killing or shooting in safe zones will result in a warning.",
        "12. Bribery\n⤷ Bribery of any kind is not allowed.",
        "13. Border Violation\n⤷ Crossing borders without authorization may result in a warning or ban.",
        "14. Griefing\n⤷ Interfering with another player’s RP will result in a warning.",
        "15. Combat Logging\n⤷ Logging out during RP/combat will result in a warning or ban.",
        "16. Powergaming\n⤷ Forcing actions without consent will result in a warning.",
        "17. Metagaming\n⤷ Using out-of-character knowledge will result in a warning.",
        "18. Mass RDM\n⤷ Killing multiple players without RP reason is prohibited.",
        "19. Disruption of RP\n⤷ Off-topic behavior or trolling disrupts RP and may result in a warning.",
        "20. Prop Abuse\n⤷ Misusing in-game props may result in a warning or punishment."
    ],
    "21-30": [
        "21. Unauthorized Use of Admin Commands\n⤷ Using admin commands to gain advantage results in a ban.",
        "22. Border Control Violations\n⤷ Bypassing Border Control results in punishment.",
        "23. No Meta-Tactics\n⤷ Exploiting known tactics is prohibited.",
        "24. Respect for Roleplay Characters\n⤷ Disrespecting RP characters results in a warning.",
        "25. Weapon Abuse\n⤷ Using weapons outside RP rules results in a warning/ban.",
        "26. No Excessive OOC Chat\n⤷ Excessive OOC disrupts RP immersion.",
        "27. No Spamming\n⤷ Spamming messages/actions results in a warning/mute.",
        "28. Respect for Roleplay Boundaries\n⤷ Do not make others uncomfortable in RP.",
        "29. No Exploiting Bugs\n⤷ Exploiting bugs results in a ban.",
        "30. No Multiple Accounts\n⤷ Using multiple accounts to bypass bans results in permanent ban."
    ],
    "31-40": [
        "31. Bypassing Chat Filter\n⤷ Saying inappropriate words is prohibited.",
        "32. Bypassing Anti-AFK\n⤷ Bypassing anti-AFK may result in stat reset or ban.",
        "33. Roblox’s Terms of Service\n⤷ Violating TOS may result in permanent bans.",
        "34. Staff Impersonation\n⤷ Pretending to be staff is forbidden and results in a ban.",
        "35. Mini Modding\n⤷ Do not act as staff if you are not one.",
        "36. L-Tapping\n⤷ Leaving during active staff events is prohibited.",
        "37. Ro-Banging\n⤷ Using avatars to simulate suggestive actions is forbidden.",
        "38. Severe Ro-Banging\n⤷ Extreme suggestive acts will result in permanent ban.",
        "39. Radio Spamming\n⤷ Sending irrelevant messages on radio results in warning/mute.",
        "40. Firearm Abuse\n⤷ Using firearms in restricted areas without RP reason results in punishment."
    ]
}

# ------------------- SELECT MENU -------------------
class RuleSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="1-10 Game Rules", value="1-10", emoji="📕"),
            discord.SelectOption(label="11-20 Game Rules", value="11-20", emoji="📕"),
            discord.SelectOption(label="21-30 Game Rules", value="21-30", emoji="📕"),
            discord.SelectOption(label="31-40 Game Rules", value="31-40", emoji="📕"),
        ]
        super().__init__(
            placeholder="Press Here For Game Rules",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="rule_select_menu"
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        rule_text = "\n".join(rules[selected])

        embed = discord.Embed(
            title=f"📖 SRP | {selected} Rules",
            description=rule_text,
            color=discord.Color.blue()
        )

        # Ephemeral: only the user who clicked sees it
        await interaction.response.send_message(embed=embed, ephemeral=True)

class RuleView(View):
    def __init__(self):
        super().__init__(timeout=None)  # never expires
        self.add_item(RuleSelect())

# ------------------- POST RULES COMMAND -------------------
@bot.command()
async def ehingamerules(ctx):
    embed = discord.Embed(
        title="📖 SRP | SERIOUS ROLEPLAY — General In-Game Rules",
        description=(
            "Welcome to SRP | Serious Roleplay! To ensure a fun, fair, and immersive experience for all players, "
            "everyone must follow the server’s general in-game rules. These rules apply to all players regardless of role or rank.\n\n"
            "⚠️ Important Notices\n\n"
            "- Respect all players and staff. Harassment, racism, or toxic behavior will not be tolerated.\n"
            "- No exploiting glitches, bugs, or mechanics for unfair advantage.\n"
            "- No random deathmatch (RDM) or vehicle deathmatch (VDM). All kills must have RP reason.\n"
            "- Follow all roleplay rules, including department-specific rules.\n"
            "- Use appropriate language.\n"
            "- Staff decisions are final.\n\n"
            "🔄 Rule Updates\n"
            "Rules may be updated anytime. Ignorance is not an excuse."
        ),
        color=discord.Color.dark_blue()
    )

    embed.set_image(url="https://i.postimg.cc/prb2FRjQ/IN-GAME-RULES.png")

    view = RuleView()
    await ctx.send(embed=embed, view=view)

# ------------------- RUN BOT -------------------
bot.run(TOKEN)
