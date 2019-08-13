from typing import Optional, Union


class TheaterLights(object):
    def __init__(self, description: str):
        self.description: str = description

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def dim(self, level: int) -> None:
        print(f'{self.description} dimming to {level} %')

    def __str__(self) -> str:
        return self.description


class Screen(object):
    def __init__(self, description: str):
        self.description: str = description

    def up(self) -> None:
        print(f'{self.description} going up')

    def down(self) -> None:
        print(f'{self.description} going down')

    def __str__(self) -> str:
        return self.description


class PopcornPopper(object):
    def __init__(self, description: str):
        self.description: str = description

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def pop(self) -> None:
        print(f'{self.description} popping popcorn!')

    def __str__(self) -> str:
        return self.description


class Tuner(object):
    def __init__(self, description: str, amplifier):
        self.description: str = description
        self.amplifier: Amplifier = amplifier
        self.frequency: float = 0

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def set_frequency(self, frequency: float) -> None:
        print(f'{self.description} setting frequency to {frequency}')
        self.frequency = frequency

    def set_am(self) -> None:
        print(f'{self.description} setting AM mode')

    def set_fm(self) -> None:
        print(f'{self.description} setting FM mode')

    def __str__(self) -> str:
        return self.description


class Projector(object):
    def __init__(self, description: str, dvd_player):
        self.description: str = description
        self.dvd_player: DVDPlayer = dvd_player

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def wide_screen_mode(self) -> None:
        print(f'{self.description} in wide-screen mode (16x9 aspect ratio)')

    def tv_mode(self) -> None:
        print(f'{self.description} in tv mode (4x3 aspect ratio)')

    def __str__(self) -> str:
        return self.description


class DVDPlayer(object):
    def __init__(self, description: str, amplifier):
        self.description: str = description
        self.amplifier: Amplifier = amplifier
        self.movie: Optional[str] = None
        self.current_track: int = 0

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def eject(self) -> None:
        self.movie = None
        print(f'{self.description} eject')

    def play(self, data: Union[int, str]) -> None:
        if type(data) == int:
            track: int = data
            if self.movie is None:
                print(f'{self.description} can\'t play track {track}, no DVD inserted!')
            else:
                self.current_track = track
                print(f'{self.description} playing track {track} of "{self.movie}"')
        if type(data) == str:
            movie: str = data
            self.movie = movie
            self.current_track = 0
            print(f'{self.description} playing "{movie}"')

    def stop(self) -> None:
        self.current_track = 0
        print(f'{self.description} stopped "{self.movie}"')

    def pause(self) -> None:
        print(f'{self.description} paused "{self.movie}"')

    def set_two_channel_audio(self) -> None:
        print(f'{self.description} set two channel audio')

    def set_surround_audio(self) -> None:
        print(f'{self.description} set surround audio')

    def __str__(self) -> str:
        return self.description


class CDPlayer(object):
    def __init__(self, description: str, amplifier):
        self.description: str = description
        self.amplifier: Amplifier = amplifier
        self.title: Optional[str] = None
        self.current_track: int = 0

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def eject(self) -> None:
        self.title = None
        print(f'{self.description} eject')

    def play(self, data: Union[str, int]) -> None:
        if type(data) == str:
            title: str = data
            self.title = title
            self.current_track = 0
            print(f'{self.description} playing "{title}"')
        if type(data) == int:
            track: int = data
            if self.title is None:
                print(f'{self.description} can\'t play track {track}, no CD inserted!')
            else:
                self.current_track = track
                print(f'{self.description} playing track {track} of "{self.title}"')

    def stop(self) -> None:
        self.current_track = 0
        print(f'{self.description} stopped')

    def pause(self) -> None:
        print(f'{self.description} paused "{self.title}"')

    def __str__(self) -> str:
        return self.description


class Amplifier(object):
    def __init__(self, description: str):
        self.description: str = description
        self.tuner: Optional[Tuner] = None
        self.dvd: Optional[DVDPlayer] = None
        self.cd: Optional[CDPlayer] = None

    def on(self) -> None:
        print(f'{self.description} on')

    def off(self) -> None:
        print(f'{self.description} off')

    def set_stereo_sound(self) -> None:
        print(f'{self.description} stereo mode on')

    def set_surround_sound(self) -> None:
        print(f'{self.description} surround sound on (5 speakers, 1 subwoofer)')

    def set_volume(self, level: int) -> None:
        if level >= 100:
            print(f'{self.description} setting volume to maximum')
        elif level <= 0:
            print(f'{self.description} mute volume')
        else:
            print(f'{self.description} setting volume to {level}')

    def set_tuner(self, tuner: Tuner) -> None:
        print(f'{self.description} setting tuner to {tuner}')
        self.tuner = tuner

    def set_dvd(self, dvd: DVDPlayer) -> None:
        print(f'{self.description} setting DVD player to {dvd}')
        self.dvd = dvd

    def set_cd(self, cd: CDPlayer) -> None:
        print(f'{self.description} setting DVD player to {cd}')
        self.cd = cd

    def __str__(self) -> str:
        return self.description
