# Django Playwright and Pytest example

This repo was inspired by my conversation [on Mastodon](https://fosstodon.org/@christophb/109992813033443934) 
about how I had recently started testing a UI with Django, Playwright, and Pytest.

## Setup script

This repo includes a `demo_setup.py` file. Running that file will set up a virtual 
environment and install the python dependencies.

You will also need to install the Playwright dependencies. If you haven't done so, the first time you run Playwright tests, it'll ask you to run `playwright install`.

## Playwright tests are skipped by default

When I code, I run my quick tests. Testing with Playwright takes longer, so I configure pytest to skip every test marked with `pytest.mark.playwright` unless the `--runplaywright` argument is present.

This allows me to run all my quick tests whenever I want, and then when I'm ready, I can run all tests to make sure it all works.

If you want to change that behavior, edit the `tests/conftest.py` file.

To run the tests in this project from the paojrct root, run `pytest tests --runplaywright`.


## Helpful fixture

There is one fixture, `test_server` in the `tests/conftest.py` file that returns a `playwright.page` instance that has loaded the root page of a server spun up for the test session.
