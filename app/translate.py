import json
import requests
from flask_babel import _
from app import current_app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = current_app.config['MS_TRANSLATOR_KEY']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}-{}'.format(
        auth, text, source_language, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
