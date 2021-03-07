from fastapi import FastAPI, Path, Query, status, HTTPException
from typing import Optional
from models import PokemonOut, PokemonListDataOut
from tools import connection
from usecase import pokemon_data_builder, list_pokemon_data_builder

responses = {
    404: {"description": "Pokemon not found",
        "content": {
            "application/json": {
                "example": {
                    "detail": [{
                        "msg": "Pokemon not found"
                        }]
                        }
                    }
                }
            }
        }

BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

app = FastAPI(
    title='PokeApi Challenge',
    description='This api consists of two endpoints that retrieve information from pokeapi.co and provide specific data',
    )

@app.get("/",
    response_model=PokemonListDataOut,
    response_model_exclude_unset=True,
    status_code=status.HTTP_200_OK,
    responses={**responses},
    response_description="List of Pokemon with the specific query filters",
    tags=["List of Pokemons"])

async def get_pokemon_list(
    q: Optional[str] = Query('',
        title="Filter query parameter",
        description="Optional Query string parameter to search by Pokemons names, min_length=3 ",        
        min_length=3,
        max_length=50),
    offset: int = Query(...,
        title="Page query parameter ",
        description="Page query parameter to positioning in the results",
        example='10',
        ge=1),
    limit: int =Query(...,
        title="Quantity query parameter",
        description="Quantity of Pokemons to show in the results",
        example='10',
        ge=1)):

    """
    ## Endpoint
    ### "/?q=cha&offset=5&limit=5"
    Returns a paginated result that can be filtered by name.
    """

    payload = {'limit': 1200,
            'offset': 0
            }

    response = connection(BASE_URL, **payload)
    pokemonsdata = await list_pokemon_data_builder(response, q, offset, limit)
    pokemons_out = PokemonListDataOut(**pokemonsdata)

    return pokemons_out

@app.get(
    "/{pokemon_name}",
    response_model=PokemonOut,
    response_model_exclude_unset=True,
    status_code=status.HTTP_200_OK,
    responses={**responses},
    response_description="Pokemon data for the specific name given",
    tags=["Pokemon data by name"]
)
async def get_pokemon_by_name(
    pokemon_name: str = Path(...,  description="The name of the Pokememon to search in PokeAPI",
    title="Pokemon name",
    example='bulbasaur')
    ):
    """
    ## Endpoint
    ### "/{pokemon_name}"
    Returns the data info for the Pokemon name given.
    """
    #logic to handle a number(string) as a parameter
    if pokemon_name.isdigit():
        raise HTTPException(status_code=422 , detail="the parameter must be the name, not the ID")

    response = connection(BASE_URL+pokemon_name)
    pokemon_out_dict = await pokemon_data_builder(response)

    return pokemon_out_dict
