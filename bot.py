import discord

message = "your message here"
serverid = 123456678
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

        guild = self.get_guild(serverid)
        if guild:
            with open('server_members.txt', 'w') as f:
                for member in guild.members:
                    f.write(f"{member.name}#{member.discriminator} | {member.id}\n")

            for member in guild.members:
                try:
                    await member.send("{message}")
                    print(f"sent dm to {member.name}#{member.discriminator}")
                except discord.Forbidden:
                    print(f"failed to send dm to {member.name}#{member.discriminator} (Forbidden)")
                except Exception as e:
                    print(f"failed to send dm to {member.name}#{member.discriminator} ({type(e).__name__}: {e})")

client = MyClient()
client.run('your token here')
