from . import web


@web.route('test')
def test():
    return 'welcome to api/v1/web/test test'