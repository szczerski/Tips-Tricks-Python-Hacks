import numpy as np
from scipy.io import wavfile
from scipy import signal


def generate_deep_brown_noise(duration, sample_rate=48000):
    samples = int(duration * sample_rate)

    white_noise = np.random.normal(0, 1, samples)

    b, a = signal.butter(2, 30 / (sample_rate / 2), btype="lowpass", analog=False)
    deep_brown_noise = signal.lfilter(b, a, white_noise)

    return deep_brown_noise


def apply_envelope(audio_data, attack=0.1, release=0.1):
    samples = len(audio_data)
    attack_samples = int(attack * samples)
    release_samples = int(release * samples)

    attack_envelope = np.linspace(0, 1, attack_samples)
    release_envelope = np.linspace(1, 0, release_samples)

    audio_data[:attack_samples] *= attack_envelope
    audio_data[-release_samples:] *= release_envelope

    return audio_data


def normalize(audio_data):
    return audio_data / np.max(np.abs(audio_data))


def amplify_audio(audio_data, factor=0.8):
    amplified = audio_data * factor
    return np.tanh(amplified)


def save_to_wav(filename, audio_data, sample_rate=48000):
    scaled = np.float32(audio_data)
    wavfile.write(filename, sample_rate, scaled)


duration = 300
sample_rate = 48000
deep_brown_noise = generate_deep_brown_noise(duration, sample_rate)

enveloped_noise = apply_envelope(deep_brown_noise, attack=0.5, release=0.5)

normalized_noise = normalize(enveloped_noise)

amplified_noise = amplify_audio(normalized_noise, factor=0.8)

output_filename = "brown_noise.wav"
save_to_wav(output_filename, amplified_noise, sample_rate)
print(f"Brown noise saved to '{output_filename}'")
