import inquirer
from inquirer import errors
from inquirer.themes import BlueComposure
from utils import cls

DEFAULT_ATTRIBUTE_CHOICES = [('Força', "FOR"),
                             ('Destreza', "DES"),
                             ('Constituição', "CON"),
                             ('Inteligência', "INT"),
                             ('Sabedoria', "SAB"),
                             ('Carisma', "CAR")]
DEFAULT_POINTS = [
    ("-2", 2),
    ("-1", 1),
    ("0", 0),
    ("1", -1),
    ("2", -2),
    ("3", -4),
    ("4", -7)
]

DEFAULT_MODIFIER_POINTS = {
    "2": -2,
    "1": -1,
    "0": 0,
    "-1": 1,
    "-2": 2,
    "-4": 3,
    "-7": 4
}


DEFAULT_TOTAL_POINTS = 10


class Atributos():
    def __init__(self):
        self.attributes = {
            "FOR": 0,
            "DES": 0,
            "CON": 0,
            "INT": 0,
            "SAB": 0,
            "CAR": 0,
        }
        self._choices = DEFAULT_ATTRIBUTE_CHOICES.copy()
        self._points = DEFAULT_POINTS.copy()
        self._total_points = DEFAULT_TOTAL_POINTS
        self.__selected_attribute = ""
        self.assign_points()

    @property
    def choices(self):
        return self._choices

    @choices.setter
    def choices(self, value):
        self._choices = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def total_points(self):
        return self._total_points

    @total_points.setter
    def total_points(self, value):
        self._total_points = value

    def assign_points(self):
        while self.total_points > 0 and self.choices:
            cls()
            print(f"Atributos ja atribuidos {self.attributes}")
            self.__ask_for_attribute()
            self.__assign_points_to_an_attribute()

    def change_attribute(self, attribute: str, mod: int):
        formatted_attribute = attribute
        self.attributes[formatted_attribute] += mod

    def __remove_attribute_from_choice(self, attribute: str):
        for index, choice in enumerate(self.choices):
            if choice[1] == attribute:
                self.choices.remove(self.choices[index])

    def __ask_for_attribute(self):
        questions = [
            inquirer.List('atributo',
                          message="Qual atributo deseja atribuir pontos?",
                          choices=self.choices,
                          carousel=True
                          ),
        ]
        answer = inquirer.prompt(questions, theme=BlueComposure())
        attribute = answer['atributo']
        self.__selected_attribute = attribute
        self.__remove_attribute_from_choice(attribute=attribute)

    def __assign_points_to_an_attribute(self):
        point_message = f"Qual ponto deseja atribuir?\
          Restantes: {self.total_points} |"
        questions = [
            inquirer.List('ponto',
                          message=point_message,
                          choices=self.points,
                          carousel=True,
                          validate=self.__validate_valid_points,

                          )
        ]
        answer = inquirer.prompt(questions)
        point = answer['ponto']
        losing_total_points = int(point)
        earning_modifier_points = DEFAULT_MODIFIER_POINTS.get(
            str(losing_total_points))

        self.change_attribute(
            attribute=self.__selected_attribute, mod=earning_modifier_points)
        self.total_points += losing_total_points

    def __validate_valid_points(self, answers, current):
        if self.total_points + current < 0:
            raise errors.ValidationError(
                "",
                reason=f"O ponto que foi atribuido é mais custoso {current} do que o total de pontos: {self.total_points}")  # noqa: E501
        return True
