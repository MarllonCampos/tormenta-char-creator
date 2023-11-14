import inquirer


class Classes():
    def __init__(self):
        self.characterClass = ""

        self.classes = [
            "Arcanista",
            "Barbaro",
            "Bardo",
            "Bucaneiro",
            "Cacador",
            "Cavaleiro",
            "Clerigo",
            "Druida",
            "Guerreiro",
            "Inventor",
            "Ladino",
            "Lutador",
            "Nobre",
            "Paladino",
        ]
        self.__askForClasses()

    def __askForClasses(self):
        questions = [
            inquirer.List('classe',
                          message="Qual classe deseja escolher?",
                          choices=self.classes,
                          carousel=True,
                          ),
        ]
        answer = inquirer.prompt(questions)
        self.classe = answer['classe'].lower()
