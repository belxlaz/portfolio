# Mabel Lazzarin

http://mabel.ml

## Installing

Depends on Python 3.6 and NodeJS.

```console
pipenv install
npm install
```

## Preparing the environment

1. Preparing yor environment variables: copy `.env.sample` as `.env` and adjust your settings
2. Activate the environment: `pipienv shell`
3. Build the assets: `flask assets build`

## Running the application

```console
flask run
```

## Tests

```console
nosetests
```