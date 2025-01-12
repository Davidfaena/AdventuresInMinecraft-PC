from mcpi.minecraft import Minecraft
from MyAdventures.FileMsg.MsgParser import listener, filter_message


# Opens a conection to the minecraft server
mc = Minecraft.create()


# Initial message
mc.postToChat("¡Active bot! write 'bot ajuda' to see all active bots.")

# Proceeds to listen the chat log
filter_message(mc)
