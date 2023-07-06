
from gameCode import effectsClass

class SpeedUpEffect(effectsClass.defaultEffect.Effect):

    def __init__(self, value=0, time=0):
        super().__init__(value, time)
        self.effectType = 'speedUp'

    def update(self, entity, dtime, TARGET_FPS):
        self.checkExist()
        if self.perfomance:
            entity.speed = entity.constantspeed * self.value
            
            if not self.periodicity:
                self.periodicity = dtime*TARGET_FPS/self.value

            self.delay += dtime
            if self.delay >= self.periodicity:
                self.perfomance -= self.periodicity*self.value
        else:
            entity.speed = entity.constantspeed
