from typing import List

from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon:Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):

        name_pokemon = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if name_pokemon:
            self.pokemons.remove(name_pokemon)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self):
        total_pokemon = ''.join([p.pokemon_details() for p in self.pokemons])
        return (f"Pokemon Trainer {self.name}\n"
                f"Pokemon count {len(self.pokemons)}\n"
                f"- {total_pokemon}")


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
