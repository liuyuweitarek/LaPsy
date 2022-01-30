from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--record_path",
        action="store"
    )

@fixture()
def recordPath(request):
    return request.config.getoption("--record_path")