from typing import Optional, List

from HeadFirstDesignPatterns.chapter_6.commands import Command, NoCommand


class SimpleRemoteControl(object):
    """
    Simple remote controller for testing
    """

    def __init__(self):
        self.slot: Optional[Command] = None

    def set_command(self, command: Command) -> None:
        self.slot = command

    def button_was_pressed(self) -> None:
        self.slot.execute()


class RemoteControl(object):
    """
    Remote control for commands executing
    """

    def __init__(self):
        self.on_commands: List[Command] = []
        self.off_commands: List[Command] = []

        no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()

    def __str__(self) -> str:
        result = '\n------ Remote Control ------\n'
        for i in range(len(self.on_commands)):
            on_command = self.on_commands[i].__class__.__name__
            off_command = self.off_commands[i].__class__.__name__
            result += '[slot {0}] {1:<30} {2:<30}\n'.format(i, on_command, off_command)
        return result


class RemoteControlWithUndo(object):
    """
    Remote control for command executing with ability to undo command
    """
    def __init__(self):
        self.on_commands: List[Command] = []
        self.off_commands: List[Command] = []

        no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)
        self.undo_command: Command = no_command

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self) -> None:
        self.undo_command.undo()

    def __str__(self) -> str:
        result = '\n------ Remote Control ------\n'
        for i in range(len(self.on_commands)):
            on_command = self.on_commands[i].__class__.__name__
            off_command = self.off_commands[i].__class__.__name__
            result += '[slot {0}] {1:<30} {2:<30}\n'.format(i, on_command, off_command)
        result += '[undo] {:<30}\n'.format(self.undo_command.__class__.__name__)
        return result
