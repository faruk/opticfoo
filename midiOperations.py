import re
import mido

class MidiOperations:

    def __init__(self, vrc):
        self.vrc = vrc
        
        # Value read pattern
        self.control_pattern = re.compile('control_change channel=([\d]+) control=([\d]+) value=([\d]+) time=([\d]+)')
        self.note_on_pattern = re.compile('note_on channel=([\d]+) note=([\d]+) velocity=([\d]+) time=([\d]+)')
        self.note_off_pattern = re.compile('note_off channel=([\d]+) note=([\d]+) velocity=([\d]+) time=([\d]+)')

        mido.open_input('Oxygen 49 MIDI 1', callback=self.process_msg)

    def process_msg(self, msg):
        control_result = self.control_pattern.search(msg.__str__())
        note_on_result = self.note_on_pattern.search(msg.__str__())
        note_off_result = self.note_off_pattern.search(msg.__str__())
        
        if control_result == None and note_on_result == None and note_off_result == None:
            return # exit here

        if control_result != None:
            self.control_func(int(control_result.group(1)),
                              int(control_result.group(2)),
                              int(control_result.group(3)),
                              int(control_result.group(4)))

        if note_on_result != None:
            self.note_on_func(int(note_on_result.group(1)),
                              int(note_on_result.group(2)),
                              int(note_on_result.group(3)),
                              int(note_on_result.group(4)))

        if note_off_result != None:
            self.note_off_func(int(note_off_result.group(1)),
                              int(note_off_result.group(2)),
                              int(note_off_result.group(3)),
                              int(note_off_result.group(4)))

    def control_func(self, channel, control, value, time):
        self.vrc.activeVisual.receive_midi_control(channel, control, value, time)

    def note_on_func(self, channel, note, velocity, time):
        self.vrc.activeVisual.receive_midi_note_on(channel, note, velocity, time)

    def note_off_func(self, channel, note, velocity, time):
        self.vrc.activeVisual.receive_midi_note_off(channel, note, velocity, time)
