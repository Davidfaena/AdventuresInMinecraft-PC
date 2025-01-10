from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random
import inspect

#Obrir servidor
# Ruta al archivo .bat
#ruta_bat = r"D:\TAP_2025\AdventuresInMinecraft-PC\StartServer.bat"

# Ejecutar el archivo .bat
#resultado = subprocess.run([ruta_bat], shell=True)

# Conexión al servidor de Minecraft
mc = Minecraft.create()

# Lista de insultos para el bot
insultos = [
    "¡Eres más lento que un creeper cansado!",
    "¡Tu casa parece hecha por un enderman ciego!",
    "¡Ni un aldeano querría comerciar contigo!",
    "¡El dragón del End se ríe de tus habilidades!",
    "¡Hasta un bloque de tierra tiene más estilo que tú!",
]

# Función para colocar TNT
def tnt_bot():
    # Obtener la posición del jugador
    pos = mc.player.getTilePos()

    # Coordenadas para colocar el TNT cerca del jugador
    x, y, z = pos.x + 2, pos.y, pos.z

    mc.setBlock(x, y, z, block.TNT)
    mc.postToChat("¡TNT colocada!")
    time.sleep(2)
    mc.setBlock(x, y+1, z, block.REDSTONE_BLOCK)
    mc.setBlock(x, y+1, z, block.AIR)

    mc.postToChat("¡TNT activada!")

# Función para insultar
def insult_bot():
    insulto = random.choice(insultos)
    mc.postToChat(f"<Bot>: {insulto}")

# Función para mostrar ayuda
def ayuda():
    mc.postToChat("<Bot>: Comandos disponibles:")
    mc.postToChat("  - bot tnt: Coloca y activa TNT cerca del jugador.")
    mc.postToChat("  - bot insultame: Recibe un insulto del bot.")
    mc.postToChat("  - bot ayuda: Muestra esta lista de comandos.")

# Función de dispatcher para ejecutar comandos de manera reflexiva
def ejecutar_comando(comando):
    """
    Ejecuta el comando correspondiente de manera reflexiva.
    """
    mc.postToChat(comando)
    # Comprobamos si el comando existe en las funciones disponibles
    comando_func = globals().get(comando)

    if callable(comando_func):
        return comando_func()
    else:
        mc.postToChat(f"<Bot>: Comando desconocido: {comando}")
        return None

# Función para escuchar los mensajes del chat
def escuchar_comandos():
    """
    Escucha el chat y ejecuta los comandos utilizando programación reflexiva.
    """
    while True:
        mensajes = mc.events.pollChatPosts()
        for mensaje in mensajes:
            autor = mensaje.entityId
            contenido = mensaje.message.lower()

            if contenido.startswith("bot "):
                comando = contenido[4:]  # Quitamos 'bot ' del inicio
                ejecutar_comando(comando)

        # Reducir la carga del bucle
        time.sleep(0.1)

# Aplicar programación funcional: Hacer que los mensajes de chat sean procesados
def procesar_mensaje(mensaje):
    """
    Función pura que procesa los mensajes y ejecuta comandos.
    """
    autor = mensaje.entityId
    contenido = mensaje.message.lower()

    if contenido.startswith("bot "):
        comando = contenido[4:]
        ejecutar_comando(comando)

# Función para filtrar y procesar mensajes
def filtrar_mensajes():
    """
    Recoge los mensajes, los filtra y los procesa con funciones puras.
    """
    mensajes = mc.events.pollChatPosts()
    list(map(procesar_mensaje, mensajes))

# Mensaje inicial
mc.postToChat("¡Bot activado! Escribe 'bot ayuda' para ver los comandos disponibles.")

# Iniciar la escucha de comandos
escuchar_comandos()
