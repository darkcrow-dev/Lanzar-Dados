import random

class Dados:
    def __init__(self):
        self.dadoDibujos = {
            1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"),

            2: ("┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘"),

            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),

            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),

            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),

            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")

            }

        print("Bienvenido/a al simulador de lanzamiento de dados\n")
        self.palabras = "Desea lanzar los dados? Si/No: "

    def jugar(self):
        opcionUsuario = input(self.palabras).upper()
        if(opcionUsuario == "SI"):
            return self.tirarDados()
        elif(opcionUsuario == "NO"):
            return print("Simulador finalizado")
        else:
            print("Elija una opcion valida\n")
            return self.jugar()

    def tirarDados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"\nValores de dados lanzados \nDado 1: {dado1} \nDado 2: {dado2}")
        print("\n".join(self.dadoDibujos[dado1]))
        print("\n".join(self.dadoDibujos[dado2]))
        self.palabras = "\nDesea volver a lanzar los dados? Si/No: "
        return self.jugar()

Dados().jugar()
