import inquirer


class Divindades():
    def __init__(self):
        self.divinity = ""
        self.__divinities = [
            "Aharadak",
            "Allihanna",
            "Arsenal",
            "Azgher",
            "Hyninn",
            "Kallyadranoch",
            "Khalmyr",
            "Lena",
            "Lin-Wu",
            "Megalokk",
            "Marah",
            "Nimb",
            "Oceano",
            "Sszzaas",
            "Tanna-Toh",
            "Tenebra",
            "Thwor",
            "Thyatis",
            "Valkaria",
            "Wynna",
        ]
        self.__askForDivinity()

    def __askForDivinity(self):
        questions = [
            inquirer.List('divinity',
                          message="Qual divindade deseja escolher?",
                          choices=self.__divinities,
                          carousel=True
                          )
        ]
        answer = inquirer.prompt(questions)
        self.divinity = answer['divinity'].lower()
