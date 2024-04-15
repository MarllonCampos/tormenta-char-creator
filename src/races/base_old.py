class BaseRace():

    def __init__(self):
        self._displacement = 0
        self._size = ""
        self._attributes = None
        self._remove_attributes = None
        self._except_attributes = None
        self._any_attribute = None
        print(__name__)

    @property
    def displacement(self):
        return self._displacement

    @displacement.setter
    def displacement(self, value):
        self._displacement = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    @property
    def any_attribute(self):
        return self._any_attribute

    @any_attribute.setter
    def any_attribute(self, value):
        self._any_attribute = value

    @property
    def remove_attributes(self):
        return self._remove_attributes

    @remove_attributes.setter
    def remove_attributes(self, value):
        self._remove_attributes = value

    @property
    def except_attributes(self):
        return self._except_attributes

    @except_attributes.setter
    def except_attributes(self, value):
        self._except_attributes = value

    def any_attribute_choices(self, except_attributes):
        default_choices = [('Força', "FOR"),
                           ('Destreza', "DES"),
                           ('Constituição', "CON"),
                           ('Inteligência', 'INT'),
                           ('Sabedoria', 'SAB'),
                           ('Carisma', 'CAR')]

        if (except_attributes is None):
            return default_choices

        filtered_choices = []
        for choice in default_choices:
            if choice[1] not in except_attributes:
                filtered_choices.append(choice)

        return filtered_choices
