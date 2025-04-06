import time
import sys

def typewriter_effect(line, char_delay=0.14):
    """Menampilkan teks dengan efek mengetik lambat per karakter."""
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print()  # Pindah baris setelah selesai satu line

def verse():
    """Lirik Bat Country - Avenged Sevenfold ."""
    lyrics = [
        "So sorry you're not here",
        "I've been sane too long, my vision's so unclear",
        "Now take a trip with me",
        "But don't be surprised when things aren't what they seem",
        "I've known it from the start",
        "All these good ideas will tear your brain apart",
        "Scared, but you can follow me",
        "I'm too weird to live, but much too rare to die"
    ]

    for line in lyrics:
        typewriter_effect(line, char_delay=0.14)
        time.sleep(2.3)  # jeda antar baris, cocok buat tempo mellow

if __name__ == "__main__":
    verse()