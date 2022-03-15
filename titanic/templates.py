from context.models import Model
from context.domains import Dataset


class TitanicTemplates(object):
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()