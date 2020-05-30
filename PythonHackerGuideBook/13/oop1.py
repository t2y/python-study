
class Instrument:
    def play(self, accessory):
        raise NotImplementedError('Cannot play these')


class SnareDrum(Instrument):
    def play(self, accessory):
        if isinstance(accessory, Stick):
            return 'POC!'
        if isinstance(accessory, Brushes):
            return 'SHHHH!'
        raise NotImplementedError('Cannot play these')


class Cymbal(Instrument):
    def play(self, accessory):
        if isinstance(accessory, Brushes):
            return 'FRCCCHHT!'
        raise NotImplementedError('Cannot play these')


class Stick(Instrument): pass
class Brushes(Instrument): pass


def play(instrument, accessory):
    return instrument.play(accessory)


print(play(SnareDrum(), Stick()))
print(play(SnareDrum(), Brushes()))
print(play(Cymbal(), Stick()))
#print(play(Stick(), Stick()))
