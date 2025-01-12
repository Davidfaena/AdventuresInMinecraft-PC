from MyAdventures.ExecuteComands.Execute import ejecutar_comando
import time


# Function that listen all the msg
def listener(mc):

    while True:
        msgs = mc.events.pollChatPosts()
        for msg in msgs:
            message_Parser(mc, msg)

        # Reducir la carga del bucle
        time.sleep(0.1)

# Función para filtrar y procesar mensajes
def filtrar_mensajes(mc):

    while True:
        mensajes = mc.events.pollChatPosts()
        list(map(lambda mensaje: message_Parser(mc, mensaje), mensajes))
        time.sleep(0.1)

# Aplicar programación funcional: Hacer que los mensajes de chat sean procesados
def message_Parser(mc, msg):
    """
    Función pura que procesa los mensajes y ejecuta comandos.
    """
    autor = msg.entityId
    content = msg.message.lower()

    if content.startswith("bot "):
        comand = content[4:]
        ejecutar_comando(mc, comand)

