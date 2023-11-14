from atributos import Atributos, DEFAULT_ATTRIBUTE_CHOICES

from racas.racas import Racas
from classes import Classes
import inquirer
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
# from classes import Classes
# from origens import Origens
# from divindades import Divindades


class Personagem:
    def __init__(self):
        self.nome = ""
        self.pericias = []
        self.poderes = []
        self.equipamentos = []
        self.magias = []
        self._atributos = Atributos()
        self._raca = Racas()

        self.add_attributes_from_race()
        # self.classe = Classes()
        # self.origem = Origens()
        # self.divindade = Divindades()

        # print(self._atributos.attributes)
        print(self._atributos.attributes)
        # print(self._raca.raceSize)

    @property
    def raca(self):
        return self._raca.race

    @property
    def atributos(self):
        return self._atributos.attributes

    def add_attributes_from_race(self):
        choices = []
        for attribute in self._raca.race_attributes:
            attribute_name: str = attribute.get("attribute")
            attribute_modifier: int = attribute.get("mod")
            except_attribute = attribute.get("except")
            choices = self.__filter_attributes_from_race(
                except_attribute=except_attribute) if len(choices) == 0 else choices  # noqa: #501
            if attribute_name.upper() != "ANY":
                self._atributos.change_attribute(
                    attribute=attribute_name, mod=attribute_modifier)
            else:
                cls()
                question = [
                    inquirer.List("atributo",
                                  message=f"Escolha um dos atributos, sera aumentado em {attribute_modifier}",  # noqa: #501
                                  choices=choices,
                                  carousel=True)
                ]
                answer = inquirer.prompt(questions=question)
                attribute = answer['atributo']
                formatted_attribute = self._atributos.correct_name_attribute(
                    attribute)
                choices.remove(attribute)
                self._atributos.change_attribute(
                    attribute=formatted_attribute, mod=attribute_modifier)

    def __filter_attributes_from_race(self, except_attribute,
                                      choice_list=DEFAULT_ATTRIBUTE_CHOICES):
        if except_attribute is None:
            return DEFAULT_ATTRIBUTE_CHOICES.copy()
        new_attribute_choices = []
        for attribute in DEFAULT_ATTRIBUTE_CHOICES:
            correct_name_attribute = self._atributos.correct_name_attribute(
                attribute)
            if correct_name_attribute != except_attribute:
                new_attribute_choices.append(attribute)
        return new_attribute_choices
