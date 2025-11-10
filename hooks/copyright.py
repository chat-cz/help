import datetime
def on_config(config, **kwargs):
    config.copyright = f"© {datetime.datetime.now().year}, Chat.cz"
