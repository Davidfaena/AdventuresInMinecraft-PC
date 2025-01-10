from mcpi.minecraft import Minecraft
from MyAdventures.FileMsg.MsgParser import listener

#Server initialization
# Path to .bat file
#path_bat = r"D:\TAP_2025\AdventuresInMinecraft-PC\StartServer.bat"

# Execute .bat file
#res = subprocess.run([path_bat], shell=True)

# Conexión al servidor de Minecraft
mc = Minecraft.create()


# Initial message
mc.postToChat("¡Active bot! write 'bot ajuda' to see all active bots.")

# Iniciar la escucha de comandos
listener(mc)
