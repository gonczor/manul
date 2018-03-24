[![Build Status](https://travis-ci.org/gonczor/manul.svg?branch=master)](https://travis-ci.org/gonczor/manul)

# Manul

This is technology demonstrator using Flask to create restful web service with Angular on frontend. Apart from being cool it solves problem of providing data for intelligent home. Technologies used are listed below. I do not expect to know everything about them but I do expect contributors to be willing to learn:

1. [Flask](http://flask.pocoo.org/);
2. [AngularJS](https://angularjs.org/);
3. [Travis Continuous Integration](https://travis-ci.org/);
4. [Python virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv);
5. [Tests using python unittest](https://docs.python.org/3/library/unittest.html);
6. [Style checks using flake8](http://flake8.pycqa.org/en/latest/);
7. Docker (planned);
8. Karma frontend unittests (planned).


## Contributing

1. Clone repo `$ git clone git@github.com:gonczor/manul.git`;
2. Install python virtual environment.
3. Create python virtual environment using `$ virtualenv venv -p python3`;
4. Download minified Angular and jQuery to `static/js` (you can use `get_js.sh` script for this);
4. Introduce changes;
5. Test changes (see testing section for more details);

## Testing

Before you create a pull request please ensure that you changes pass tests. This means both unittests and style tests. Currently this is only implemented for python and PEP-8. To do this run:
```bash
$ python main.py test
$ flake8 --config=.flake8 .
```

## Structure

* api - backend for REST api serving data,
* app - core app for serving data for browsers, rendering templates and so on,
* helpers - useful bash scripts,
* static - css, js and coffeescripts,
* templates - html templates used by Flask,
* tests - backend unittests.
