class Image:
    def __init__(self, filename):
        self._filename = filename

    def load_image_from_disk(self):
        print("loading " + self._filename)

    def display_image(self):
        print("display " + self._filename)

    @property
    def filename(self):
        return self._filename


class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxy_state = None

    @property
    def subject(self):
        return self._subject

    @property
    def proxy_state(self):
        return self._proxy_state

    @proxy_state.setter
    def proxy_state(self, state: int):
        self._proxy_state = state


class ProxyImage(Proxy):
    def display_image(self):
        if self.proxy_state is None:
            self.subject.load_image_from_disk()
            self.proxy_state = 1
        print("display " + self.subject.filename)


def main():
    proxy_image1 = ProxyImage(Image("HiRes_10Mb_Photo1"))
    proxy_image2 = ProxyImage(Image("HiRes_10Mb_Photo2"))

    proxy_image1.display_image()  # loading necessary
    proxy_image1.display_image()  # loading unnecessary
    proxy_image2.display_image()  # loading necessary
    proxy_image2.display_image()  # loading unnecessary
    proxy_image1.display_image()  # loading unnecessary


if __name__ == '__main__':
    main()
