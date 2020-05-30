import functools

class SnareDrum: pass
class Cymbal: pass
class Stick: pass
class Brushes: pass


@functools.singledispatch
def play(instrument, accessory):
    raise NotImplementedError('Cannot play these')


@play.register(SnareDrum)
def _(instrument, accessory):
    if isinstance(accessory, Stick):
        return 'POC!'
    if isinstance(accessory, Brushes):
        return 'SHHHH!'
    raise NotImplementedError('Cannot play these')


@play.register(Cymbal)
def _(instrument, accessory):
    if isinstance(accessory, Brushes):
        return 'FRCCCHHT!'
    raise NotImplementedError('Cannot play these')


print(play(SnareDrum(), Stick()))
print(play(SnareDrum(), Brushes()))
print(play(Cymbal(), Stick()))
print(play(SnareDrum, Cymbal()))
