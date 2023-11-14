import inquirer


class Origens():
    def __init__(self):
        self.origin = ""
        self.__origens = [
            "Amigo Dos Animais",
            "Amnesico",
            "Aristocrata",
            "Artesao",
            "Artista",
            "Assistente De Laboratorio",
            "Batedor",
            "Capanga",
            "Charlatao",
            "Circense",
            "Criminoso",
            "Curandeiro",
            "Eremita",
            "Escravo",
            "Estudioso",
            "Fazendeiro",
            "Forasteiro",
            "Gladiador",
            "Guarda",
            "Herdeiro",
            "Heroi Campones",
            "Marujo",
            "Mateiro",
            "Membro De Guilda",
            "Mercador",
            "Minerador",
            "Nomade",
            "Pivete",
            "Refugiado",
            "Seguidor",
            "Selvagem",
            "Soldado",
            "Taverneiro",
            "Trabalhador",
        ]
        self.__askForOrigin()

    def __askForOrigin(self):
        questions = [
            inquirer.List('origin',
                          message="Qual origem deseja escolher?",
                          choices=self.__origens,
                          carousel=True
                          )
        ]
        answer = inquirer.prompt(questions)
        self.origin = answer['origin'].lower()
