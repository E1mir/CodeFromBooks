from HeadFirstDesignPatterns.chapter_7.facade.devices import Amplifier, Tuner, DVDPlayer, CDPlayer, Projector, Screen, \
    TheaterLights, PopcornPopper


class HomeTheaterFacade(object):
    def __init__(self,
                 amplifier: Amplifier,
                 tuner: Tuner,
                 dvd: DVDPlayer,
                 cd: CDPlayer,
                 projector: Projector,
                 screen: Screen,
                 lights: TheaterLights,
                 popper: PopcornPopper):
        self.amplifier: Amplifier = amplifier
        self.tuner: Tuner = tuner
        self.dvd: DVDPlayer = dvd
        self.cd: CDPlayer = cd
        self.projector: Projector = projector
        self.screen: Screen = screen
        self.lights: TheaterLights = lights
        self.popper: PopcornPopper = popper

    def watch_movie(self, movie: str):
        print('Get ready to watch a movie...')
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amplifier.on()
        self.amplifier.set_dvd(self.dvd)
        self.amplifier.set_surround_sound()
        self.amplifier.set_volume(50)
        self.dvd.on()
        self.dvd.play(movie)

    def end_movie(self):
        print('Shutting movie theater down...')
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

    def listen_to_cd(self, title: str):
        print('Get ready fo an audio-pile experience')
        self.lights.on()
        self.amplifier.on()
        self.amplifier.set_volume(50)
        self.amplifier.set_cd(self.cd)
        self.amplifier.set_stereo_sound()
        self.cd.on()
        self.cd.play(title)

    def end_cd(self):
        print('Shutting down CD...')
        self.amplifier.off()
        self.amplifier.set_cd(self.cd)
        self.cd.eject()
        self.cd.off()

    def listen_to_radio(self, frequency: float):
        print('Tuning in the airways...')
        self.tuner.on()
        self.tuner.set_frequency(frequency)
        self.amplifier.on()
        self.amplifier.set_volume(50)
        self.amplifier.set_tuner(self.tuner)

    def end_radio(self):
        print('Shutting down the tuner...')
        self.tuner.off()
        self.amplifier.off()
