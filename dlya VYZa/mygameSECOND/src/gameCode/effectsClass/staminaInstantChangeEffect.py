
from gameCode import effectsClass

class StaminaInstantChangeEffect(effectsClass.defaultEffect.Effect):

    def __init__(self, value=0, time=0):
        super().__init__(value, time)
        self.effectType = 'staminaInstantChange'

    def update(self, entity, dtime, TARGET_FPS):
        self.checkExist()
        if self.perfomance:
            entity.stamina += self.value
            self.perfomance = 0