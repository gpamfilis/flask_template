from . import mobile


@mobile.route('test')
def test():
    return 'welcome to api/v1/mobile/test test'