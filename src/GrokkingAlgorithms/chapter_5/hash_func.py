class Voter(object):
    voters = dict()

    def __init__(self, name):
        self.name = name

    def vote(self):
        name = self.name
        if self.voters.get(name):
            print('{} has already voted!'.format(name))
        else:
            print('Let {} to vote!'.format(name))
            self.voters[name] = True


if __name__ == '__main__':
    v = Voter('Jimmy')
    v.vote()
    v2 = Voter('Tommy')
    v2.vote()
    v3 = Voter('Tommy')
    v3.vote()
