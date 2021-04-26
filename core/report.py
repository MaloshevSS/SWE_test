class Data:
    def __init__(self, data):
        self.data = data


class Step:
    num: int
    text: str
    data = []

    def __init__(self, num: int, text: str):
        self.num = num
        self.text = text

    def add_data(self, data: Data):
        self.data.append(data)


class Report:
    id: str  # id from test rails
    currentStep: int = 0  # current step of report
    steps = {}

    def __init__(self, id: str):
        self.id = id

    def step(self, text: str):
        self.currentStep = self.currentStep + 1
        self.steps.update({self.currentStep: Step(self.currentStep, text)})

        return self

    def current_step(self) -> Step:
        return self.steps.get(self.currentStep)

    def add_data(self, data):
        self.current_step().add_data(Data(data))
