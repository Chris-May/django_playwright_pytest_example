import pytest


def pytest_addoption(parser):
    """Looks for the `runplaywright` argument"""
    parser.addoption(
        '--runplaywright',
        action='store_true',
        default=False,
        help='run playwright tests',
    )


def pytest_configure(config):
    """Auto-add the slow mark to the config at runtime"""
    config.addinivalue_line('markers', 'playwright: mark test as slow to run')


def pytest_collection_modifyitems(config, items):
    """This skips the tests if runslow is not present"""
    if config.getoption('--runplaywright'):
        # --runplaywright given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason='need --runplaywright option to run')
    for item in items:
        if 'playwright' in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture()
def test_server(page, live_server):
    page.goto(live_server.url)
    return page
