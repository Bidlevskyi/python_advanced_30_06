#!/usr/local/bin python3.8
'''Без использования библиотек, создать класс для представления 
информации о времени. Ваш класс должен иметь
возможности установки времени и изменения его отдельных полей (час, минута,
секунда) с проверкой допустимости вводимых значений. В случае недопустимых
значений полей нужно установить максимально допустимое значение.
Создать методы изменения времени на заданное количество часов, минут и секунд.
'''

class Time:
    def __init__(self, h=0, m=0, s=0):
        if h > 23:
            self._hours = 23
        else:
            self._hours = h
        if m > 59:
            self._minutes = 59
        else: 
            self._minutes = m
        if s > 59:
            self._seconds = 59
        else:
            self._seconds = s

    @property
    def hours(self):
        return self._hours
    
    @property
    def minutes(self):
        return self._minutes
    
    @property
    def seconds(self):
        return self.seconds

    @hours.setter
    def hours(self, value):
        if value > 23:
            self._hours = 23
        else:
            self._hours = value

    @minutes.setter
    def minutes(self, value):
        if value > 59:
            self._minutes = 59
        else:
            self._minutes = value

    @seconds.setter
    def seconds(self, value):
        if value > 23:
            self._seconds = 23
        else:
            self._seconds = value

    def __repr__(self):
        return f"Time('{self._hours}'-'{self._minutes}'-'{self._seconds}')"

    def __str__(self):
        return f"Time: {self._hours}-{self._minutes}-{self._seconds}"
        
    def shift_hours(self, value):
        self._hours = (self._hours + value) % 24

    def shift_minutes(self, value):
        if (self._minutes + value) > 59:
            sh_hours = (self._minutes + value) // 60
            self.shift_hours(sh_hours)
            self._minutes = (self._minutes + value) % 60
        else:
            self._minutes = (self._minutes + value)
    
    def shift_seconds(self, value):
        if (self._seconds + value) > 59:
            shi_hours = (self._seconds + value) // 3600
            shi_minutes = ((self._seconds + value) % 3600) // 60
            self.shift_hours(shi_hours)
            self.shift_minutes(shi_minutes)
            self._seconds = ((self._seconds + value) % 3600) % 60
