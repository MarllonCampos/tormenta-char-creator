import inquirer
from inquirer import errors
DEFAULT_ATTRIBUTE_CHOICES = ['Força',
                             'Destreza',
                             'Constituição',
                             'Inteligência',
                             'Sabedoria',
                             'Carisma']
DEFAULT_POINTS = {
    "-2": 2,
    "-1": 1,
    "0": 0,
    "1": -1,
    "2": -2,
    "3": -4,
    "4": -7
}


DEFAULT_TOTAL_POINTS = 10


class Atributos():
    def __init__(self,
                 choices: list[str] = DEFAULT_ATTRIBUTE_CHOICES,
                 points: dict[str:int] = DEFAULT_POINTS,
                 totalPoints: int = DEFAULT_TOTAL_POINTS):
        self.attributes = {
            "FOR": 0,
            "DES": 0,
            "CON": 0,
            "INT": 0,
            "SAB": 0,
            "CAR": 0,
        }
        self._choices = choices.copy()
        self._points = points
        self._total_points = totalPoints
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
            self.__ask_for_attribute()
            self.__assign_points_to_an_attribute()

    def correct_name_attribute(self, value: str):
        return value.upper()[0:3]

    def change_attribute(self, attribute: str, mod: int):
        formatted_attribute = self.correct_name_attribute(attribute)
        self.attributes[formatted_attribute] += mod

    def __ask_for_attribute(self):
        questions = [
            inquirer.List('atributo',
                          message="Qual atributo deseja atribuir pontos?",
                          choices=self.choices,
                          carousel=True
                          ),
        ]
        answer = inquirer.prompt(questions)
        attribute = answer['atributo']
        formatted_attribute = self.correct_name_attribute(attribute)
        self.__selected_attribute = formatted_attribute
        self.choices.remove(attribute)

    def __assign_points_to_an_attribute(self):
        keyPoints = self.points.keys()
        point_message = f"Qual ponto deseja atribuir?\
          Restantes: {self.total_points} |"
        point = 1
        if len(keyPoints) != 1:
            questions = [
                inquirer.List('ponto',
                              message=point_message,
                              choices=keyPoints,
                              carousel=True,
                              validate=self.__validate_valid_points
                              )
            ]
            answer = inquirer.prompt(questions)
            point = answer['ponto']
        modifier_on_object = int(point)
        point_on_object = self.points[str(modifier_on_object)]
        self.change_attribute(
            attribute=self.__selected_attribute, mod=modifier_on_object)
        self.total_points += point_on_object

    def __validate_valid_points(self, answers, current):
        point_value_on_object = int(self.points[str(current)])
        if self.total_points + point_value_on_object < 0:
            raise errors.ValidationError(
                "",
                reason=f"O ponto que foi atribuido é mais custoso {point_value_on_object} do que o total de pontos: {self.total_points}")  # noqa: E501
        return True
