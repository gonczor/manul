[![Build Status](https://travis-ci.org/gonczor/manul.svg?branch=master)](https://travis-ci.org/gonczor/manul)   [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# Manul

This is technology demonstrator using Flask to create restful web service with Angular on frontend. Apart from being cool it solves problem of providing data for intelligent home. Technologies used are listed below. I do not expect to know everything about them but I do expect contributors to be willing to learn at least some of the following:

1. [Flask](http://flask.pocoo.org/);
2. [AngularJS](https://angularjs.org/);
3. [Travis Continuous Integration](https://travis-ci.org/);
4. [Python virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv);
5. [Tests using python unittest](https://docs.python.org/3/library/unittest.html);
6. [Style checks using flake8](http://flake8.pycqa.org/en/latest/);
7. [npm for installing local packages](https://www.npmjs.com/);
8. [Grunt file watcher for automating frontend tasks](https://gruntjs.com/);
9. [CoffeeScript for more pleasant frontend programming](http://coffeescript.org/);
10. Docker (planned);
11. Karma frontend unittests (planned).


## Setup

1. Clone repo `$ git clone git@github.com:gonczor/manul.git`;
2. Install python virtual environment.
3. Create python virtual environment using `$ virtualenv venv -p python3`;
4. Download minified Angular and jQuery to `static/js` (you can use `get_js.sh` script for this);
5. Go to `static` folder to install frontend dependencies. Run `$ npm install` to install dependencies listed in `package.json` and `$ npm install -g grunt`. To compile coffeescripts once run `grunt`, to enable file watcher which will introduce all changes for you run `grunt watch`. Remember that you have to be in `static` folder. JavaScripts themselves are not added to git, only coffeescripts.
6. Before any changes, got to `setup` module and perform actions mentioned in `secret.py.txt`.
7. Run `python main.py createdb` to create database (it should be named `manul.db` as custom names are currently not supported) and `python main.py createsuperuser` to create admin user.
8. Introduce changes;
9. Test changes (see testing section for more details);

## Testing

Before you create a pull request please ensure that you changes pass tests. This means both unittests and style tests. Currently this is only implemented for python and PEP-8. To do this run:
```bash
$ python main.py test
$ flake8 --config=.flake8
```

## Structure

* api - backend for REST api serving data,
* core - core core for serving data for browsers, rendering templates and so on,
* db - database handling stuff (setup, models, migrations etc.)
* commands - useful bash scripts,
* static - css, js and coffeescripts,
* templates - html templates used by Flask,
* tests - backend unittests.

## Upgrade policy

There are very few things I hate more than carelessness while developing and technical debt is an excellent example. Therefore I want latest stable versions of packages in the project to be used. I do see, however, the need of stability and focus on other aspects of the project than having latest version of libraries for its own sake. Therefore, latest version is tracked regularly and create tickets for upgrades that should go together with normal flow.
