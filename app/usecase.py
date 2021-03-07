from fastapi import HTTPException
from models import PokemonIn, PokemonListDataIn

async def pokemon_data_builder(response):
    """
    Args: (pokemon_in).
    Return: pokemon_out_dict
    function to build the data to be delivered by the enpoint.
    """
    pokemon_in = PokemonIn(**response.json())
    pokemon_in_dict = pokemon_in.dict()
    pokemon_out_dict = pokemon_in.dict()

    for key, value in pokemon_out_dict.items():
        if isinstance(value, list) and key !='stats':
            pokemon_out_dict[key].clear()

            for value_dict in pokemon_in_dict[key]:
                for inner_k, inner_value  in value_dict.items():
                    if key == 'forms':
                        pokemon_out_dict[key].append(inner_value)
                    if key == 'abilities':
                        pokemon_out_dict[key].append(inner_value['name'])
                    if key == 'moves':
                        pokemon_out_dict[key].append(inner_value['name'])
                    if key == 'types':
                        pokemon_out_dict[key].append(inner_value['name'])

        if isinstance(value, dict):
            pokemon_out_dict[key].clear()
            pokemon_out_dict[key] = list(pokemon_out_dict[key])

            for value_dict, key_dict in pokemon_in_dict[key].items():
                if key == 'species':
                    pokemon_out_dict[key].append(key_dict)
                if key == 'sprites':
                    if key_dict is not None:
                        pokemon_out_dict[key].append(key_dict)

        if key == 'stats':
            pokemon_out_dict[key].clear()
            pokemon_out_dict[key] = dict(pokemon_out_dict[key])

            for value_dict in pokemon_in.stats:
                if value_dict.stat.name != 'hp':
                    pokemon_out_dict[key].update({value_dict.stat.name:value_dict.base_stat})

    return pokemon_out_dict

async def list_pokemon_data_builder(response, q, offset, limit):
    """
    Args: (response, q, offset, limit).
    Return: pokemons
    function to build the data to be delivered by the enpoint.
    """
    pokemon_data_in = PokemonListDataIn(**response.json())

    pokemons = {}

    data = await in_list_pokemon_data_builder(pokemon_data_in)

    pokemons["total"] = pokemon_data_in.count
    pokemons["limit"] = limit
    pokemons["offset"] = offset
    pokemons["data"] = []

    iterator = 0
    for values in data:
        if q in values['name']:
            pokemons["data"].append(data[iterator])
        iterator +=1

    if len(pokemons["data"]) == 0:
        raise HTTPException(status_code=404, detail="Pokemon name not found")

    pokemons["data"] = pokemons["data"][offset-1:limit+offset-1]

    return pokemons


async def in_list_pokemon_data_builder(pokemon_data_in):
    """
    Args: (pokemon_data_in).
    Return: data
    function to build a dict used in the list_pokemon_data_builder function.
    """
    data=[]
    total=0
    for count in pokemon_data_in.results:
        total +=1
        names = {
                'id' : total,
                'name' : count.name,
                'image' :
                'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{}.png'.format(total)
                }
        data.append(names)

    return data
