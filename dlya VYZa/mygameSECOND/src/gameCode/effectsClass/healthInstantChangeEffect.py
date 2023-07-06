
from gameCode import effectsClass

class HealthInstantChangeEffect(effectsClass.defaultEffect.Effect):

    def __init__(self, value=0, time=0):
        super().__init__(value, time)
        self.effectType = 'healthInstantChange'

    def update(self, entity, dtime, TARGET_FPS):
        self.checkExist()
        if self.perfomance:
            entity.health += self.value
            self.perfomance = 0