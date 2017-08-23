from puppetboard.app import app
#app.config.from_object('puppetboard.default_settings')
app.config.from_envvar('PUPPETBOARD_SETTINGS', silent=False)
app.secret_key = app.config['SECRET_KEY']
app.run(app.config['DEV_LISTEN_HOST'], app.config['DEV_LISTEN_PORT'])
