from pydantic import BaseModel, HttpUrl
from typing import List, Dict, Optional

class Ability(BaseModel):
    name: str

class DataAbilities(BaseModel):
    ability: Ability

class Forms(BaseModel):
    name: str

class Move(BaseModel):
    name: str

class Moves(BaseModel):
    move: Move

class Species(BaseModel):
    name: str

class Sprites(BaseModel):
    back_default: Optional[HttpUrl] = None
    back_female: Optional[HttpUrl] = None
    back_shiny: Optional[HttpUrl] = None
    back_shiny_female: Optional[HttpUrl] = None
    front_default: Optional[HttpUrl] = None
    front_female: Optional[HttpUrl] = None
    front_shiny: Optional[HttpUrl] = None
    front_shiny_female: Optional[HttpUrl] = None

class Stat(BaseModel):
    name: str

class Stats(BaseModel):
    base_stat: int
    stat: Stat

class Type(BaseModel):
    name: str

class Types(BaseModel):
    type: Type

class PokemonIn(BaseModel):
    """
    BaseModel to valid the data from PokeAPI
    """
    abilities: List[DataAbilities]
    base_experience: int
    forms: List[Forms]
    height: int
    id: int
    location_area_encounters: HttpUrl
    moves: List[Moves]
    name: str
    order: int
    species: Species
    sprites: Sprites
    stats: List[Stats]
    types: List[Types]
    weight: int

class PokemonOut(BaseModel):
    """
    BaseModel for Endpoint response
    """
    abilities: List[str]
    base_experience: int
    forms: List[str]
    height: int
    id: int
    location_area_encounters: HttpUrl
    moves: List[str]
    name: str
    order: int
    species: List[str]
    sprites: List[HttpUrl]
    stats: Dict[str, int]
    types: List[str]
    weight: int

    class Config:
        schema_extra = {
            "example": {
        "abilities": [
            "hyper-cutter",
            "sand-veil",
            "immunity"
        ],
        "base_experience": 86,
        "forms": [
            "gligar"
        ],
        "height": 11,
        "id": 207,
        "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/207/encounters",
        "moves": [
            "guillotine",
            "razor-wind",
            "swords-dance",
            "cut",
            "wing-attack",
            "sand-attack",
            "headbutt",
            "double-edge",
            "poison-sting",
            "counter",
            "strength",
            "earthquake",
            "dig",
            "toxic",
            "agility",
            "quick-attack",
            "mimic",
            "screech",
            "double-team",
            "harden",
            "swift",
            "dream-eater",
            "rest",
            "rock-slide",
            "slash",
            "substitute",
            "thief",
            "snore",
            "curse",
            "protect",
            "feint-attack",
            "sludge-bomb",
            "detect",
            "sandstorm",
            "endure",
            "false-swipe",
            "swagger",
            "fury-cutter",
            "steel-wing",
            "attract",
            "sleep-talk",
            "return",
            "frustration",
            "baton-pass",
            "iron-tail",
            "metal-claw",
            "hidden-power",
            "rain-dance",
            "sunny-day",
            "rock-smash",
            "torment",
            "facade",
            "taunt",
            "brick-break",
            "knock-off",
            "secret-power",
            "rock-tomb",
            "sky-uppercut",
            "sand-tomb",
            "aerial-ace",
            "poison-tail",
            "roost",
            "natural-gift",
            "feint",
            "tailwind",
            "u-turn",
            "payback",
            "fling",
            "power-trick",
            "rock-polish",
            "poison-jab",
            "dark-pulse",
            "night-slash",
            "aqua-tail",
            "x-scissor",
            "earth-power",
            "rock-climb",
            "defog",
            "cross-poison",
            "stone-edge",
            "captivate",
            "stealth-rock",
            "bug-bite",
            "hone-claws",
            "venoshock",
            "round",
            "acrobatics",
            "struggle-bug",
            "bulldoze",
            "confide"
        ],
        "name": "gligar",
        "order": 289,
        "species": [
            "gligar"
        ],
        "sprites": [
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/female/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/female/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/female/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/207.png",
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/female/207.png"
        ],
        "stats": {
            "attack": 75,
            "defense": 105,
            "special-attack": 35,
            "special-defense": 65,
            "speed": 85
        },
        "types": [
            "ground",
            "flying"
        ],
        "weight": 648
        }
        }

class ListDataIn(BaseModel):
    name: str
    url: HttpUrl

class PokemonListDataIn(BaseModel):
    """
    BaseModel to valid the data from PokeAPI
    """
    count: int
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    results: List[ListDataIn]

class ListDataOut(BaseModel):
    id: int
    name: str
    image: HttpUrl

    class config:
        schema_extra = {
            "id": 1,
            "name": "bulbasaur",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
        }

class PokemonListDataOut(BaseModel):
    """
    BaseModel for Endpoint response
    """
    total: int
    limit: int
    offset: int
    data: List[ListDataOut]

    class config:
        schema_extra = {
    "total": 1118,
    "limit": 5,
    "offset": 5,
    "data": {
            "id": 1,
            "name": "bulbasaur",
            "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
        }
}
