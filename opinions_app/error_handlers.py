from flask import render_template

from . import app, db


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
