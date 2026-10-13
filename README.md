# Flatiron Cars — Flask Car Routes

A small Flask app for the Flatiron Cars company. It has a welcome route and a
model route that tells you whether a car model is in the Flatiron fleet.

## Routes

| Method | Route      | Response |
|--------|------------|----------|
| GET    | `/`        | `Welcome to Flatiron Cars` |
| GET    | `/<model>` | `Flatiron {model} is in our fleet!` if the model exists, otherwise `No models called {model} exists in our catalog` |

Models in the fleet (`existing_models` in `server/app.py`):
`Beedle`, `Crossroads`, `M2`, `Panique`. Matching is case-sensitive.

## Installation

```bash
pipenv install
pipenv shell
```

## Usage

Start the development server:

```bash
python server/app.py
```

Then visit:

- http://localhost:5555/ → `Welcome to Flatiron Cars`
- http://localhost:5555/Beedle → `Flatiron Beedle is in our fleet!`
- http://localhost:5555/realCar → `No models called realCar exists in our catalog`

## Screenshot

<!-- Add a screenshot of the running app here, e.g. ![Flatiron Cars](screenshot.png) -->

## Running Tests

```bash
pytest
```

## Project Structure

```
server/
├── app.py              # Flask app and routes
└── testing/
    ├── conftest.py     # pytest test-name formatting
    └── app_test.py     # route tests
```

## Resources

- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Original lab repo](https://github.com/learn-co-curriculum/python-flask-car-routes-lab)

## License

See [LICENSE.md](LICENSE.md).
