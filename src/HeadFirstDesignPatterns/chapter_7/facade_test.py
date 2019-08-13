from HeadFirstDesignPatterns.chapter_7.facade.devices import Amplifier, Tuner, DVDPlayer, CDPlayer, Projector, TheaterLights, \
    Screen, PopcornPopper
from HeadFirstDesignPatterns.chapter_7.facade.facade import HomeTheaterFacade

if __name__ == '__main__':
    amplifier: Amplifier = Amplifier("Top-O-Line Amplifier")
    tuner: Tuner = Tuner("Top-O-Line AM/FM Tuner", amplifier)
    dvd_player: DVDPlayer = DVDPlayer("Top-O-Line DVD Player", amplifier)
    cd_player: CDPlayer = CDPlayer("Top-O-Line CD Player", amplifier)
    projector: Projector = Projector("Top-O-Line Projector", dvd_player)
    lights: TheaterLights = TheaterLights("Theater Ceiling Lights")
    screen: Screen = Screen("Theater Screen")
    popper: PopcornPopper = PopcornPopper("Popcorn Popper")

    theaterFacade: HomeTheaterFacade = HomeTheaterFacade(
        amplifier,
        tuner,
        dvd_player,
        cd_player,
        projector,
        screen,
        lights,
        popper
    )

    theaterFacade.watch_movie('Avengers Endgame')
    print('-' * 50)
    theaterFacade.end_movie()
