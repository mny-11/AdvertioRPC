import discord

token = input("Enter your bot token: ").strip()

while True:
    try:
        num_buttons = int(input("How many buttons? (1-4): "))
        if 1 <= num_buttons <= 4:
            break
        else:
            print("Please choose between 1 and 4 buttons.")
    except ValueError:
        print("Invalid number, try again.")

buttons_data = []
for i in range(num_buttons):
    name = input(f"Enter name for button {i+1}: ").strip()
    link = input(f"Enter URL for button {i+1}: ").strip()
    buttons_data.append({"label": name, "url": link})

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} (ID: {client.user.id})")

    # Set rich presence activity with buttons
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="AdvertBot 🚀",
        buttons=buttons_data
    )
    await client.change_presence(activity=activity)

    print("Rich Presence with buttons is now active!")

client.run(token)
