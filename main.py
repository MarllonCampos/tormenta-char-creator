from personagem import Personagem


class Main():
    def __init__(self):
        print("All Working Fine")
        personagem = Personagem()
        # classe = Classes()
        # origem = Origens()
        # questionForDivinity = [inquirer.Confirm("divinity",
        #                 message="Deseja escolher alguma divindade?",
        #                 default=True
        #             )]
        # chooseDivinity = inquirer.prompt(questionForDivinity)
        # print(chooseDivinity['divinity'])
        # divindade = Divindades()
        # print(atributo.attributes)
        print(personagem.atributos)
        print(personagem.raca)


run = Main()
