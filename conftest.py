import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.logIn(username="administrator", password="1904")
    else:
        if not fixture.is_vallid():
            fixture = Application()
            fixture.session.logIn(username="administrator", password="1904")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logOut()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture



# @pytest.fixture
# def app(request):
#     global fixture
#     if fixture is None:
#         fixture = Application()
#     else:
#         if fixture.is_vallid():
#             fixture = Application()
#     fixture.session.ensure_logIn(username="administrator", password="1904")
#     return fixture
#
#
# @pytest.fixture(scope="session", autouse=True)
# def stop(request):
#     def fin():
#         fixture.session.ensure_logOut()
#         fixture.destroy()
#     request.addfinalizer(fin)
    # return fixture
