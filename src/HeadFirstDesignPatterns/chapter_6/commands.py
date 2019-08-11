import abc
from typing import Optional, List

from HeadFirstDesignPatterns.chapter_6.devices import Light, Stereo, GarageDoor, CeilingFan, TV, HotTub


class Command(metaclass=abc.ABCMeta):
    """
    Command interface
    """

    @abc.abstractmethod
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class MacroCommand(Command):
    """
    Macro command for multiple command sets
    """

    def __init__(self, commands: List[Command]):
        self.commands: List[Command] = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()

    def undo(self) -> None:
        for command in self.commands:
            command.undo()


class NoCommand(Command):
    """
    No command used as None for the command
    """

    def execute(self) -> None:
        pass


class LightOnCommand(Command):
    """
    Light on command
    """

    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightOffCommand(Command):
    """
    Light off command
    """

    def __init__(self, light: Light):
        self.light: Light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()


class StereoOnWithCDCommand(Command):
    """
    Start stereo with CD command
    """

    def __init__(self, stereo: Stereo):
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(80)

    def undo(self) -> None:
        self.stereo.off()


class StereoOnWithDVDCommand(Command):
    """
    Start stereo with DVD command
    """

    def __init__(self, stereo: Stereo):
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_dvd()
        self.stereo.set_volume(80)

    def undo(self) -> None:
        self.stereo.off()


class StereoOffCommand(Command):
    """
    Stereo turn off command
    """

    def __init__(self, stereo: Stereo):
        self.stereo: Stereo = stereo

    def execute(self) -> None:
        self.stereo.off()

    def undo(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(80)


class GarageDoorUpCommand(Command):
    """
    Garage door up command
    """

    def __init__(self, door: GarageDoor):
        self.door: GarageDoor = door

    def execute(self) -> None:
        self.door.up()

    def undo(self) -> None:
        self.door.down()


class GarageDoorDownCommand(Command):
    """
    Garage door down command
    """

    def __init__(self, door: GarageDoor):
        self.door: GarageDoor = door

    def execute(self) -> None:
        self.door.down()

    def undo(self) -> None:
        self.door.up()


class CeilingFanCommand(Command, metaclass=abc.ABCMeta):
    """
    Abstract command class for ceiling fan
    """

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan: CeilingFan = ceiling_fan
        self.previous_speed: Optional[int] = None

    @abc.abstractmethod
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        if self.previous_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.previous_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.previous_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.previous_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanHighCommand(CeilingFanCommand):
    """
    Turn on ceiling fan on high speed command
    """

    def __init__(self, ceiling_fan: CeilingFan):
        super().__init__(ceiling_fan)

    def execute(self) -> None:
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()


class CeilingFanMediumCommand(CeilingFanCommand):
    """
    Turn on ceiling fan on medium speed command
    """

    def __init__(self, ceiling_fan: CeilingFan):
        super().__init__(ceiling_fan)

    def execute(self) -> None:
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()


class CeilingFanLowCommand(CeilingFanCommand):
    """
    Turn on ceiling fan on low speed command
    """

    def __init__(self, ceiling_fan: CeilingFan):
        super().__init__(ceiling_fan)

    def execute(self) -> None:
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.low()


class CeilingFanOffCommand(CeilingFanCommand):
    """
    Turn off ceiling fan command
    """

    def __init__(self, ceiling_fan: CeilingFan):
        super().__init__(ceiling_fan)

    def execute(self) -> None:
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()


class TVOnCommand(Command):
    """
    Turn on TV command
    """

    def __init__(self, tv: TV):
        self.tv: TV = tv

    def execute(self) -> None:
        self.tv.on()
        self.tv.set_input_channel()

    def undo(self) -> None:
        self.tv.off()


class TVOffCommand(Command):
    """
    Turn off TV command
    """

    def __init__(self, tv: TV):
        self.tv: TV = tv

    def execute(self) -> None:
        self.tv.off()

    def undo(self) -> None:
        self.tv.on()


class HotTubOnCommand(Command):
    """
    Turn on hot tub command
    """

    def __init__(self, hot_tub: HotTub):
        self.hot_tub: HotTub = hot_tub

    def execute(self) -> None:
        self.hot_tub.on()
        self.hot_tub.temperature = 104
        self.hot_tub.bubbles_on()

    def undo(self) -> None:
        self.hot_tub.temperature = 98
        self.hot_tub.off()


class HotTubOffCommand(Command):
    """
    Turn off hot tub command
    """

    def __init__(self, hot_tub: HotTub):
        self.hot_tub: HotTub = hot_tub

    def execute(self) -> None:
        self.hot_tub.temperature = 98
        self.hot_tub.off()

    def undo(self) -> None:
        self.hot_tub.on()
        self.hot_tub.temperature = 104
        self.hot_tub.bubbles_on()
