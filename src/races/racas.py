# import json
import re

import inquirer

from races import nome_racas
from utils import cls


class Racas():
    def __init__(self):
        cls()
        self.race_name = ""
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
            "Sulfure",
            "Silfide",
            "Trog",
        ]
        self.__ask_for_race()
        self.race = nome_racas.NomeRacas.race_class(self.race_name)

        # self.__set_values_from_race()
        # self.race_attributes = self.values_from_race.get("attributes")
        # self.race_abilities = self.values_from_race.get("abilities")
        # self.race_size = self.values_from_race.get("size")
        # self.displacement = self.values_from_race.get("displacement")

    def __clean_race(self, race):
        return re.sub('\W', '', race)

    def __ask_for_race(self):
        questions = [
            inquirer.List('raca',
                          message="Qual raça deseja escolher?",
                          choices=self.__races,
                          carousel=True,
                          ),
        ]
        answer = inquirer.prompt(questions)

        self.race_name = self.__clean_race(answer['raca'].lower())

    # def __set_values_from_race(self):
    #     races_file = open("data/race.json", encoding="utf-8")
    #     json_races = json.load(races_file)
    #     specific_values = json_races.get(self.__clean_race(self.race))
    #     self.values_from_race = specific_values
