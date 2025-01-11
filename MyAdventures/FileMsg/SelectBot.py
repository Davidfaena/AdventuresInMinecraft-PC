def SelectBot(mc, comand):

    # Dictionary that contains the names and the bots
    comands = {
        "tnt": "TNTBot",
        "insultame": "InsultBot",
        "ajuda": "AjudaBot",
        "tortuga": "TortugaBot"
    }

    # Search for the correct bot
    bot = comands.get(comand)

    if bot:
        return bot
    else:
        mc.postToChat(f"<Bot>: Comand unknown: {comand}")
        return None