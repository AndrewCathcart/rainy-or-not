# rainy-or-not

## Description
This project is built using [Python3](https://www.python.org/download/releases/3.0/) & uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing dependencies.

It uses the openweathermap API to provide a tiny description of either the current weather at a location or the forecast for today

## Installation
`git clone "git@github.com:AndrewCathcart/rainy-or-not.git"`
`cd rainy-or-not`
`pipenv install` (or `pip install pipenv` followed by `pipenv install` if you don't already have pipenv)

`pipenv --py` should output the virtualenv python binary location, copy this

Navigate to weather.py
- On line 1 add the location you copied as a shebang, it should look something like this: `#!/Users/andrew.cathcart/.local/share/virtualenvs/rainy-or-not-kja58eca/bin/python`
- On line 13, change `"q": "newcastle,gb"` to the location you want information for. 
    - The format is city,iso3166countrycode
    - For example, to change the location to London, United Kingdom `"q": "London,GB"`

Create an account over at https://openweathermap.org/
- After you've done that you should receive a confirmation email with your API key in
- export this API key in your .zshrc or .bashrc file; `export OPENWEATHERMAP_API_KEY=1234567890`

`chmod +x weather.py`
`sudo cp weather.py /usr/local/bin`

## Usage
`weather.py` which will return the current weather description
or
`weather.py forecast` which will return a description of the forecast for the rest of the day

Alternatively you can alias these for ease of use. Add the below lines to your .zshrc or .bashrc file.
`alias weather="weather.py"`
`alias forecast="weather forecast"`
Then simply call `weather` or `forecast`

## To-do
Add support for passing in a location
