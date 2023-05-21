class Band:

    def __init__(self, name=""):
        self.name = name
        self.members = []

    def __str__(self):
        members_str = ', '.join(str(member) for member in self.members)
        return "{} ({})".format(self.name, members_str)

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.members.append(musician)

    def play(self):
        if not self.members:
            return f"{self.name} has no members!"
        band_playing = f"{self.name} is playing:"
        for musician in self.members:
            band_playing += f" {musician.play()}"
        return band_playing
