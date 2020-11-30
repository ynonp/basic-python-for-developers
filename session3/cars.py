from __future__ import annotations

class Car:
    def __init__(self, color: str, *, speed: float):
        self.color = color
        self.speed = speed

    # this also works
#    def faster_than(self, other: 'Car'):
#        return self.speed > other.speed


    def faster_than(self, other: Car):
        return self.speed > other.speed


c1 = Car('yellow', speed=69)
c2 = Car('red', speed=50)
#c1.speed_up()

if c1.faster_than(c2):
    print(f"the yellow car won")