
class Instrument:
    def play(self, accessory, other=None):
        raise NotImplementedError('Cannot play these')


class SnareDrum(Instrument):
    def play(self, accessory, other=None):
        if isinstance(accessory, Stick):
            return 'POC!'
        if isinstance(accessory, Brushes):
            return 'SHHHH!'
        raise NotImplementedError('Cannot play these')


class Cymbal(Instrument):
    def play(self, accessory, other):
        if isinstance(accessory, Brushes) and isinstance(other, Stick):
            return 'FRCCCHHT!'
        raise NotImplementedError('Cannot play these')


class Stick(Instrument): pass
class Brushes(Instrument): pass


def play(instrument, accessory, other=None):
    return instrument.play(accessory, other)


print(play(SnareDrum(), Stick()))
print(play(SnareDrum(), Brushes()))
print(play(Cymbal(), Brushes(), Stick()))
