from flask import render_template
from . import auth

@auth.app_errorhandler(404)
def _404(error):
    return render_template('./errors/404.html')

@auth.app_errorhandler(500)
def _500(error):
    return render_template('./errors/500.html')

@auth.app_errorhandler(400)
def _400(error):
    return render_template('./errors/400.html')
