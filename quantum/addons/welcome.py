from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.get_channel(
            1199288009003106405
        )  # Replace with the actual channel ID
        if channel:
            await channel.send(f"```Hello {member.mention}! Welcome to the server.```")
            await channel.send(f"```مرحبة {member.mention}! .أهلاً بكم بشبكة خضر نت```")


def setup(bot):
    bot.add_cog(Welcome(bot))
