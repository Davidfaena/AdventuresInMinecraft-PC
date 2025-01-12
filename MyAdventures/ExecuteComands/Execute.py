from MyAdventures.FileMsg.SelectBot import SelectBot
import importlib


# Reflective function that let us call the differents bots
def apply_command(mc, comand):

    bot = SelectBot(mc, comand)  # Name of the bot to be called

    try:
        # Complet name from the module
        modulo_nombre = f"MyAdventures.Bots.{bot}"

        # Dinamic import of the module
        modulo = importlib.import_module(modulo_nombre)

        # Verifies if the module has a comun function name
        if hasattr(modulo, "main"):  # It is assumed that all the bots have the same function name
            comando_func = getattr(modulo, "main")

            if callable(comando_func): # Check if we can call that function
                mc.postToChat(f"Executing comand: {bot}")
                return comando_func(mc)  # Executes the main function of the bot
            else:
                mc.postToChat(f"<Bot>: Main function isn't executable {bot}.")
        else:
            mc.postToChat(f"<Bot>: Module {bot} dosent have a main function.")

    except ModuleNotFoundError:
        mc.postToChat(f"<Bot>: Módulo not found: {bot}.")
    except Exception as e:
        mc.postToChat(f"<Bot>: Error while executing {bot}: {str(e)}")

    return None


# Reflective function that let us call the differents bots
def ejecutar_coman2(mc, comand):

    bot = SelectBot(mc, comand)

    # Comprobamos si el comando existe en las funciones disponibles
    comando_func = globals().get(bot)
    mc.postToChat(comando_func)
    if callable(comando_func):
        return comando_func()
    else:
        mc.postToChat(f"<Bot>: Comand unknown: {comand}")
        return None
