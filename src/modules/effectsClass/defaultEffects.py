
class Effects():

    def __init__(self, owner):
        self.instanthealthheal = 0
        self.instantstaminaheal = 0
        
        self.healthregeneration = 0 #надо сделать механику эффектов. Ну класс такой, что при накладывании на энтити (self.effects = Effects(), self.effects render and etc)
        self.healthregenerationtime = 0
        self.healthregenerationdelay = 0
        #есть определенные значения регена, времени регена и тд в привязанном к игроку классе эффектов. Мы передаем предметом в него новые значение и в при достижении 
        #конкретного времени значения обнуляются, а эффект спадает. Также сделать ИНТЕРФЕЙС 
        self.staminaregeneration = 0
        self.staminaregenerationtime = 0
        self.staminaregenerationdelay = 0

        self.speedup = 0
        self.speeduptime = 0
        self.speedupdelay = 0

        self.periodicity = 2

    def update(self, owner, dtime, TARGET_FPS):
        if self.instanthealthheal:
            owner.health, self.instanthealthheal = owner.health + self.instanthealthheal, 0
        if self.instantstaminaheal:
            owner.stamina, self.instantstaminaheal = owner.stamina + self.instantstaminaheal, 0

        if self.healthregeneration:
            self.healthregenerationdelay += dtime
            if self.healthregenerationdelay >= dtime*TARGET_FPS/self.periodicity:
                self.healthregenerationtime - self.healthregenerationdelay
                self.healthregenerationdelay = 0
                owner.health += self.healthregeneration

        if self.staminaregeneration:
            self.staminaregenerationdelay += dtime
            if self.staminaregenerationdelay >= dtime*TARGET_FPS/self.periodicity:
                self.staminaregenerationtime - self.staminaregenerationdelay
                self.staminaregenerationdelay = 0
                owner.stamina += self.staminaregeneration

            

