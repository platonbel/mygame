
class Effect():

    def __init__(self, value=0, time=0):
        self.effectType = 'default'

        self.value = value
        self.time = time
        self.perfomance = self.value*self.time
        self.periodicity = 0
        self.delay = 0

    def setStats(self, value, time):
        self.value = value
        self.time = time
        self.perfomance = self.value*self.time if self.value*self.time >= 0 else 0

    def checkExist(self):
        if not self.perfomance:
            self.value = 0
            self.time = 0
            self.delay = 0