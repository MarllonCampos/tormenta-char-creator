import inquirer
from inquirer import errors
from pericias.periciapadrao import PericiaPadrao


class Pericias():
    def __init__(self,  expertise_quantity: int):

        self.expertise_quantity = expertise_quantity

    def __validate_max_expertise_choices(self, answers, current):
        if (len(current) != self.expertise_quantity):
            remaining_expertise = self.expertise_quantity - len(current)
            reason_message = f"+{remaining_expertise}"if remaining_expertise > 0 else remaining_expertise  # noqa

            reason = f"Você PRECISA selecionar {reason_message} pericias"  # noqa
            raise errors.ValidationError(
                "", reason=reason)
        return True

    def ask_for_expertise(self):
        message = f"Escolha {self.expertise_quantity} pericias"
        questions = [
            inquirer.Checkbox('pericias',
                              message=message,
                              choices=PericiaPadrao.DEFAULT_EXPERTISES,
                              carousel=True,
                              validate=self.__validate_max_expertise_choices
                              )
        ]
        answer = inquirer.prompt(questions)
        pericias = answer['pericias']
        return pericias
