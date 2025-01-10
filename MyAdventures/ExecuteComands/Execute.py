from MyAdventures.FileMsg.SelectBot import SelectBot
from MyAdventures.Bots import *
import importlib
import os

def ejecutar_comando(mc, comand):
    """
    Ejecuta el comando correspondiente de manera reflexiva.
    """
    bot = SelectBot(mc, comand)  # Seleccionar el nombre del bot (archivo Python)

    try:
        # Construir el nombre completo del módulo
        modulo_nombre = f"MyAdventures.Bots.{bot}"

        # Importar dinámicamente el módulo correspondiente
        modulo = importlib.import_module(modulo_nombre)

        # Verificar si el módulo tiene una función principal (puedes ajustar el nombre de la función)
        if hasattr(modulo, "main"):  # Se asume que cada archivo tiene una función `main`
            comando_func = getattr(modulo, "main")

            if callable(comando_func):
                mc.postToChat(f"Ejecutando comando: {bot}")
                return comando_func(mc)  # Ejecutar la función `main` del módulo
            else:
                mc.postToChat(f"<Bot>: La función `main` no es ejecutable en {bot}.")
        else:
            mc.postToChat(f"<Bot>: El módulo {bot} no tiene una función `main`.")

    except ModuleNotFoundError:
        mc.postToChat(f"<Bot>: Módulo no encontrado: {bot}.")
    except Exception as e:
        mc.postToChat(f"<Bot>: Error al ejecutar {bot}: {str(e)}")

    return None
# Función de dispatcher para ejecutar comandos de manera reflexiva
def ejecutar_comando2(mc, comand):
    """
    Ejecuta el comando correspondiente de manera reflexiva.
    """

    bot = SelectBot(mc, comand)

    # Comprobamos si el comando existe en las funciones disponibles
    comando_func = globals().get(bot)
    mc.postToChat(comando_func)
    if callable(comando_func):
        return comando_func()
    else:
        mc.postToChat(f"<Bot>: Comand unknown: {comand}")
        return None
