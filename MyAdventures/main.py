from mcpi.minecraft import Minecraft
from MyAdventures.FileMsg.MsgParser import listener, filtrar_mensajes



# Opens a conection to the minecraft server
mc = Minecraft.create()


# Initial message
mc.postToChat("¡Active bot! write 'bot ajuda' to see all active bots.")

# Proceeds to listen the chat log
filtrar_mensajes(mc)
