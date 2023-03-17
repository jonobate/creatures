import mido
import time

class MidiController:
    def __init__(self):
        self.outport = mido.open_output('IAC Driver creatures')

    def play_note(self, channel=0, note=60, velocity=64):
        msg = mido.Message('note_on', channel=channel, note=note, velocity=velocity)
        self.outport.send(msg)
        time.sleep(1)
        msg = mido.Message('note_off', channel=channel, note=note, velocity=velocity)
        self.outport.send(msg)

    def set_control(self, channel=0, control=0, value=127):
        msg = mido.Message('control_change', channel=channel, control=control, value=value)
        self.outport.send(msg)
        # print("Setting control signal %i to %i" % (control, value))
  
    def test_control(self, channel=0, control=0, value=None):
        if value != None:
            self.set_control(channel=channel, control=control, value=value)
        else:
            for value in range(128):
                self.set_control(channel=channel, control=control, value=value)

if __name__ == "__main__":
    my_controller = MidiController()
    #my_controller.test_control(control=5)
    # my_controller.set_control(channel=1, control=10, value=1)
    my_controller.play_note(channel=0, note=78)


# control 0 = ambient 1 volume
# control 1 = ambient 2 volume
# control 2 = music 1 volume
# control 3 = music 2 volume
# control 4 = music 3 volume
# control 5 = music 4 volume