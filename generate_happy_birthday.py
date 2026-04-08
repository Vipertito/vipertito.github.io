import math
import wave
import struct

sample_rate = 44100
notes = [
    ('G4', 0.5), ('G4', 0.5), ('A4', 1.0), ('G4', 1.0), ('C5', 1.0), ('B4', 2.0),
    ('G4', 0.5), ('G4', 0.5), ('A4', 1.0), ('G4', 1.0), ('D5', 1.0), ('C5', 2.0),
    ('G4', 0.5), ('G4', 0.5), ('G5', 1.0), ('E5', 1.0), ('C5', 1.0), ('B4', 1.0), ('A4', 1.0),
    ('F5', 0.5), ('F5', 0.5), ('E5', 1.0), ('C5', 1.0), ('D5', 1.0), ('C5', 2.0),
]
frequencies = {
    'C5': 523.25,
    'D5': 587.33,
    'E5': 659.25,
    'F5': 698.46,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88,
    'G5': 783.99,
}
volume = 0.3
samples = []
for name, duration in notes:
    freq = frequencies[name]
    nframes = int(sample_rate * duration)
    for i in range(nframes):
        t = i / sample_rate
        sample = volume * math.sin(2 * math.pi * freq * t)
        samples.append(int(sample * 32767))

with wave.open('happy-birthday.wav', 'w') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(struct.pack('<h', s) for s in samples))

print('created happy-birthday.wav')
