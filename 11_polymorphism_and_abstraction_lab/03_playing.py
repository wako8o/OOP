def start_playing(get_guitar):
    return get_guitar.play()

class Guitar:

    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))
