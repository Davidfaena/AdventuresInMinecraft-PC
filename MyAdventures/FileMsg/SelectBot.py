
def SelectBot(mc, comando):

    match comando:
        case "tnt":
            return "TNTBot"
        case "insultame":
            return "InsultBot"
        case "ajuda":
            return "AjudaBot"
        case _:
            mc.postToChat(f"<Bot>: Comand unknown: {comando}")