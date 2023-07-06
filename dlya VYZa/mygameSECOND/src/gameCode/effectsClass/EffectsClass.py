from gameCode import effectsClass

class Effects():

    def __init__(self):
        self.healthRegenEffect = effectsClass.healthRegenEffect.HealthRegenEffect()
        self.healthInstantChangeEffect = effectsClass.healthInstantChangeEffect.HealthInstantChangeEffect()
        self.staminaRegenEffect = effectsClass.staminaRegenEffect.StaminaRegenEffect()
        self.staminaInstantChangeEFfect = effectsClass.staminaInstantChangeEffect.StaminaInstantChangeEffect()
        self.bleedingEffect = effectsClass.bleedingEffect.BleedingEffect()
        self.bleedingStopEffect = effectsClass.bleedingStopEffect.BleedingStopEffect()

        self.effectsGroup = {
            'healthRegenEffect': self.healthRegenEffect,
            'healthInstantChangeEffect': self.healthInstantChangeEffect,
            'staminaRegenEffect': self.staminaRegenEffect,
            'staminaInstantChangeEffect': self.staminaInstantChangeEFfect,
            'bleedingEffect': self.bleedingEffect,
            'bleedingStopEffect': self.bleedingStopEffect,
        }

    def update(self, entity, dtime, TARGET_FPS):
        self.healthRegenEffect.update(entity, dtime, TARGET_FPS)
        self.healthInstantChangeEffect.update(entity, dtime, TARGET_FPS)
        self.staminaRegenEffect.update(entity, dtime, TARGET_FPS)
        self.staminaInstantChangeEFfect.update(entity, dtime, TARGET_FPS)
        self.bleedingEffect.update(entity, dtime, TARGET_FPS)
        self.bleedingStopEffect.update(entity, dtime, TARGET_FPS)


            

