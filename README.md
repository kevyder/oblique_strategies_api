# Oblique Strategies API

A FastAPI-based implementation of Brian Eno and Peter Schmidt's Oblique Strategies as a REST API.

## About

Oblique Strategies is a card-based method for promoting creativity jointly created by Brian Eno and Peter Schmidt. Each card offers a challenging constraint intended to help artists break creative blocks by encouraging lateral thinking.

This API provides programmatic access to the Oblique Strategies in multiple languages (currently English and Spanish).

## Features

- Get a random strategy
- List all available strategies
- Retrieve a specific strategy by ID
- Multi-language support (English and Spanish)

## Installation

The project requires Python 3.12 or higher.

```bash
# Clone the repository
git clone https://github.com/kevyder/oblique_strategies_api.git
cd oblique_strategies_api

# Install uv (if not already installed)
# Follow instructions at https://docs.astral.sh/uv/getting-started/installation/

# Create virtual environment and install dependencies
uv venv
uv sync
```

## Usage

### Running the API

```bash
uv run pywrangler dev
```

The API will be available at `http://localhost:8787`

### API Endpoints

#### Get a Random Strategy
```http
GET /random?lang=en
```
Query parameters:
- `lang`: Language code (`en` or `es`, defaults to `en`)

Response:
```json
{
    "id": 42,
    "strategy": "Emphasize repetitions"
}
```

#### List All Strategies
```http
GET /strategies?lang=en
```
Query parameters:
- `lang`: Language code (`en` or `es`, defaults to `en`)

Response:
```json
{
    "total": 114,
    "strategies": [
        {
            "id": 1,
            "strategy": "Abandon normal instruments"
        },
        // ...
    ]
}
```

#### Get Strategy by ID
```http
GET /strategy/1?lang=es
```
Query parameters:
- `lang`: Language code (`en` or `es`, defaults to `en`)

Response:
```json
{
    "id": 1,
    "strategy": "Abandona los instrumentos normales"
}
```

## Project Structure

```
oblique_strategies_api/
├── src/
│   ├── strategies/
│   │   ├── __init__.py
│   │   ├── base.py        # Base classes and interfaces
│   │   ├── data.py        # Strategy data
│   │   └── in_memory.py   # In-memory implementation
│   └── entry.py           # FastAPI application
├── pyproject.toml
└── README.md
```

## Credits

- Original Oblique Strategies created by Brian Eno and Peter Schmidt
- Spanish translations by the project maintainers

## License

This project is available under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

The Oblique Strategies content is intellectual property of Brian Eno and Peter Schmidt, used here for educational purposes. All rights to the original content belong to its creators.
