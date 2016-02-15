from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    # TODO: This is an opportunity for upgrade; this is a poor session factory
    session_factory = SignedCookieSessionFactory('secret')
    config.set_session_factory(session_factory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('start', '/api/start')
    config.add_route('place_ship', '/api/place_ship')
    config.add_route('shoot', '/api/shoot')
    config.scan()
    return config.make_wsgi_app()
