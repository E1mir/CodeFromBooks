from typing import Optional


class Light(object):
    """
    Light
    """

    def __init__(self, location: str = ''):
        self.location: str = location

    def on(self) -> None:
        print(f'{self.location} light is on')

    def off(self) -> None:
        print(f'{self.location} light is off')


class GarageDoor(object):
    """
    Garage door
    """

    def __init__(self, location: str = ''):
        self.location = location

    def up(self) -> None:
        print(f'{self.location} garage Door is Up')

    def down(self) -> None:
        print(f'{self.location} garage Door is Down')

    def stop(self) -> None:
        print(f'{self.location} garage Door is Stopped')

    def light_on(self) -> None:
        print(f'{self.location} garage light is on')

    def light_off(self) -> None:
        print(f'{self.location} garage light is off')


class CeilingFan(object):
    """
    Ceiling fan
    """

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    OFF = 0

    def __init__(self, location: str = ''):
        self.location = location
        self.level: Optional[int] = None

    def high(self) -> None:
        self.level = self.HIGH
        print(f'{self.location} ceiling fan is on high')

    def medium(self) -> None:
        self.level = self.MEDIUM
        print(f'{self.location} ceiling fan is on medium')

    def low(self) -> None:
        self.level = self.LOW
        print(f'{self.location} ceiling fan is on low')

    def off(self) -> None:
        self.level = 0
        print(f'{self.location} ceiling fan is off')

    def get_speed(self) -> int:
        return self.level


class HotTub(object):
    """
    Hot tub
    """

    def __init__(self):
        self._on: Optional[bool] = None
        self._temperature: int = 0

    def on(self) -> None:
        self._on = True

    def off(self) -> None:
        self._on = False

    def bubbles_on(self) -> None:
        if self._on:
            print(f'Hot tub is bubbling!')

    def bubbles_off(self) -> None:
        if self._on:
            print(f'Hot tub is not bubbling!')

    def jets_on(self) -> None:
        if self._on:
            print('Hot tub jets are on')

    def jets_off(self) -> None:
        if self._on:
            print('Hot tub jets are off')

    def heat(self) -> None:
        self._temperature = 105
        print('Hot tub is heating to a steaming 105 degrees')

    def cool(self) -> None:
        self._temperature = 98
        print('Hot tub is cooling to 98 degrees')

    @property
    def temperature(self) -> int:
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: int) -> None:
        if temperature > self.temperature:
            print(f'Hot tub is heating to a steaming {temperature} degrees')
        else:
            print(f'Hot tub is cooling to {temperature} degrees')
        self._temperature = temperature


class Stereo(object):
    """
    Stereo
    """

    def __init__(self, location: str = ''):
        self.location: str = location

    def on(self) -> None:
        print(f'{self.location} stereo is on')

    def off(self) -> None:
        print(f'{self.location} stereo is off')

    def set_cd(self) -> None:
        print(f'{self.location} stereo is set for CD input')

    def set_dvd(self) -> None:
        print(f'{self.location} stereo is set for DVD input')

    def set_radio(self) -> None:
        print(f'{self.location} stereo is set for Radio')

    def set_volume(self, volume: int) -> None:
        if volume < 0:
            volume = 0
        elif volume > 100:
            volume = 100

        print(f'{self.location} stereo volume set to {volume}')


class TV(object):
    """
    Television
    """

    def __init__(self, location: str = ''):
        self.location: str = location
        self.channel: Optional[int] = None

    def on(self) -> None:
        print(f'{self.location} TV is on')

    def off(self) -> None:
        print(f'{self.location} TV is off')

    def set_input_channel(self) -> None:
        self.channel = 3
        print('Channel is set for VCR')
