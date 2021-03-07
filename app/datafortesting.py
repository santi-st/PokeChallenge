
test_main_get_pokemon_by_name_bad_input_js = {
  "detail": [
    {
      "loc": [
        "query",
        "offset"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    },
    {
      "loc": [
        "query",
        "limit"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}

test_main_get_pokemon_by_name_ok_js = {
  "abilities": [
    "limber",
    "imposter"
  ],
  "base_experience": 101,
  "forms": [
    "ditto"
  ],
  "height": 3,
  "id": 132,
  "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/132/encounters",
  "moves": [
    "transform"
  ],
  "name": "ditto",
  "order": 203,
  "species": [
    "ditto"
  ],
  "sprites": [
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png",
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/132.png",
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png"
  ],
  "stats": {
    "attack": 48,
    "defense": 48,
    "special-attack": 48,
    "special-defense": 48,
    "speed": 48
  },
  "types": [
    "normal"
  ],
  "weight": 40
}

test_main_get_pokemon_list_ok_js = {
    "total": 1118,
  "limit": 5,
  "offset": 5,
  "data": [
    {
      "id": 107,
      "name": "hitmonchan",
      "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/107.png"
    },
    {
      "id": 113,
      "name": "chansey",
      "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png"
    },
    {
      "id": 308,
      "name": "medicham",
      "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/308.png"
    },
    {
      "id": 390,
      "name": "chimchar",
      "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/390.png"
    },
    {
      "id": 441,
      "name": "chatot",
      "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/441.png"
    }
  ]
}

test_main_get_pokemon_list_bad_input_js = {    
  "detail": [
    {
      "loc": [
        "query",
        "q"
      ],
      "msg": "ensure this value has at least 3 characters",
      "type": "value_error.any_str.min_length",
      "ctx": {
        "limit_value": 3
      }
    },
    {
      "loc": [
        "query",
        "offset"
      ],
      "msg": "ensure this value is greater than or equal to 1",
      "type": "value_error.number.not_ge",
      "ctx": {
        "limit_value": 1
      }
    },
    {
      "loc": [
        "query",
        "limit"
      ],
      "msg": "ensure this value is greater than or equal to 1",
      "type": "value_error.number.not_ge",
      "ctx": {
        "limit_value": 1
      }
    }
  ]
}
