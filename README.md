# weather-app

## Config app

Config must be defined in `instance/config.py`. Copy `instance/config.example.py` to `instance/config.py` and edit it.

## Installing dependencies

```sh
pip install -r requirements.txt
```

## Running app

To get app running run following command:
```sh
flask run
```

## Schema database

Following schema is necessary to get app working
```sql
CREATE TABLE public.history (
    id serial primary key,
    result jsonb NOT NULL,
    queried_at timestamp without time zone DEFAULT now()
);
```

## Artefacts

`Insomnia_2021-02-18.json` is the exported file from [Insomnia][insomnia] that I used to test the API.

## Dependencies

It was used 4 main libs that worth to be explained.

### [Flask][flask]

Flask is a micro-framework well-knowed between the python community for web development. I decided use it because of its simplicity.

### [SQLAlchemy][sqlalchemy]

SQLAlchemy is a library for SQL handling and offers great options for object relational mapping (ORM). I decided use it because of its API well documented.

### [Flask-SQLAlchemy][flask-sqlalchemy]

Flask-SQLAlchemy is a library maintened for the same team that support flask. I decided use it because the way that it integrate Flask and SQLAlchemy together it's simple but yet powerful.

### [Requests][requests]

To consume OpenWeatherMapAPI I used requests lib because of its simpler api than standard urllib3.


[flask]: https://flask.palletsprojects.com/en/1.1.x/
[sqlalchemy]: https://www.sqlalchemy.org/
[flask-sqlalchemy]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
[requests]: https://requests.readthedocs.io/en/master/
[insomnia]: https://insomnia.rest/
