from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--record_path",
        default='.',
        action="store"
    )

@fixture()
def record_path(request):
    return request.config.getoption("--record_path")