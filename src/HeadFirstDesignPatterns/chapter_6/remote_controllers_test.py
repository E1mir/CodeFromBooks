from typing import List

from HeadFirstDesignPatterns.chapter_6.commands import (
    LightOnCommand,
    LightOffCommand,
    GarageDoorUpCommand,
    GarageDoorDownCommand,
    StereoOnWithCDCommand,
    StereoOffCommand,
    CeilingFanHighCommand,
    StereoOnWithDVDCommand,
    TVOnCommand,
    TVOffCommand,
    HotTubOnCommand, HotTubOffCommand, MacroCommand, Command)
from HeadFirstDesignPatterns.chapter_6.devices import (
    Light,
    CeilingFan,
    GarageDoor,
    Stereo,
    TV,
    HotTub
)
from HeadFirstDesignPatterns.chapter_6.remote_controllers import (
    SimpleRemoteControl,
    RemoteControl,
    RemoteControlWithUndo
)


def test_simple_remote_controller() -> None:
    remote = SimpleRemoteControl()
    light = Light('Kitchen')
    light_on = LightOnCommand(light)
    remote.set_command(light_on)
    remote.button_was_pressed()


def remote_control_test() -> None:
    remote_control = RemoteControl()
    # Define devices
    living_room_light = Light('Living Room')
    kitchen_light = Light('Kitchen')
    ceiling_fan = CeilingFan('Living Room')
    garage_door = GarageDoor('Garden')
    stereo = Stereo('Living Room')

    # Define commands
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    ceiling_fan_on = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanHighCommand(ceiling_fan)
    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)
    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    # Configure remote control
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on_with_cd, stereo_off)
    remote_control.set_command(4, garage_door_up, garage_door_down)

    print(remote_control)
    # imitation of button pressing
    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)
    remote_control.on_button_was_pushed(4)
    remote_control.off_button_was_pushed(4)


def remote_control_test_simple_undo() -> None:
    remote_control = RemoteControlWithUndo()

    living_room_light = Light('Living Room')

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()


def macro_command_test() -> None:
    remote_control = RemoteControlWithUndo()
    # define devices
    light = Light('Living room')
    tv = TV('Living room')
    stereo = Stereo('Living room')
    hot_tub = HotTub()
    # define commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    stereo_on = StereoOnWithDVDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)
    tv_on = TVOnCommand(tv)
    tv_off = TVOffCommand(tv)
    hot_tub_on = HotTubOnCommand(hot_tub)
    hot_tub_off = HotTubOffCommand(hot_tub)

    party_on: List[Command] = [light_on, stereo_on, tv_on, hot_tub_on]
    party_off: List[Command] = [light_off, stereo_off, tv_off, hot_tub_off]

    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    remote_control.set_command(0, party_on_macro, party_off_macro)

    print(remote_control)
    print('--- Pushing Macro On ---')
    remote_control.on_button_was_pushed(0)
    print('--- Pushing Macro Off ---')
    remote_control.off_button_was_pushed(0)
    print('--- Undo Macro ---')
    remote_control.undo_button_was_pushed()


def title(text: str, line_length: int = 30) -> None:
    print('\n' + '-' * line_length, text.upper(), '-' * line_length + '\n')


if __name__ == '__main__':
    title('Simple remote controller testing')
    test_simple_remote_controller()
    title('Remote controller testing')
    remote_control_test()
    title('Undo testing')
    remote_control_test_simple_undo()
    title('Macro command testing')
    macro_command_test()
