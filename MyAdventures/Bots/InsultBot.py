import random

# List with some mineSpanish slurs
slurs = [
    "¡Eres más lento que un creeper cansado!",
    "¡Tu casa parece hecha por un enderman ciego!",
    "¡Ni un aldeano querría comerciar contigo!",
    "¡El dragón del End se ríe de tus habilidades!",
    "¡Hasta un bloque de tierra tiene más estilo que tú!",
]


# Function that activate slurs
def main(mc):
    slur = random.choice(slurs)
    mc.postToChat(f"<Bot>: {slur}")