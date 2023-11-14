import inquirer
import json


class Racas():
    def __init__(self):
        self.race = ""
        self.values_from_race = {}
        self.__races = [
            "Aggelus",
            "Anao",
            "Dahllan",
            "Elfo",
            "Goblin",
            "Golem",
            "Humano",
            "Hynne",
            "Kliren",
            "Lefou",
            "Medusa",
            "Minotauro",
            "Osteon",
            "Qareen",
            "Sereia/Tritao",
            "Silfide",
            "Aggelus",
            "Sulfure",
            "Trog",
        ]
        self.__ask_for_race()
        self.__set_values_from_race()
        self.race_attributes = self.values_from_race.get("attributes")
        self.race_abilities = self.values_from_race.get("abilities")
        self.race_size = self.values_from_race.get("size")
        self.displacement = self.values_from_race.get("displacement")

    def __ask_for_race(self):
        questions = [
            inquirer.List('raca',
                          message="Qual raça deseja escolher?",
                          choices=self.__races,
                          carousel=True,
                          ),
        ]
        answer = inquirer.prompt(questions)
        self.race = answer['raca'].lower()

    def __set_values_from_race(self):
        races_file = open("data/race.json", encoding="utf-8")
        json_races = json.load(races_file)
        specific_values = json_races.get(self.race)
        self.values_from_race = specific_values
