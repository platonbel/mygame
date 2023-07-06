
from gameCode import effectsClass

class BleedingStopEffect(effectsClass.defaultEffect.Effect):

    def __init__(self, value=0, time=0):
        super().__init__(value, time)
        self.effectType = 'bleedingStop'

    def update(self, entity, dtime, TARGET_FPS):
        self.checkExist()
        if self.perfomance:

            if not self.periodicity:
                self.periodicity = dtime*TARGET_FPS/self.value

            self.delay += dtime
            if self.delay >= self.periodicity:
                entity.effects.effectsGroup['bleeding'].setStats(
                    value=(entity.effects.effectsGroup['bleeding'].value), time=(entity.effects.effectsGroup['bleeding'].time-self.periodicity*self.value)
                )
                self.perfomance -= self.periodicity*self.value
                self.delay = 0