from web.factory import get_web

def before_all(context):
    web = get_web(context.config.userdata['browser'])
    context.web = web