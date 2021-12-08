
import tweepy
from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, OWNER_ACCOUNT

def auth(consumer_key, consumer_secret, access_token, access_token_secret, owner_account):
    """Autenticación con la API de Twitter

    Args:
        consumer_key (String): Key de la App creado en https://developer.twitter.com/
        consumer_secret (String): Secret de la App creado en https://developer.twitter.com/
        access_token (String): Token de la App creado en https://developer.twitter.com/
        access_token_secret (String): Token secret de la App creado en https://developer.twitter.com/
    """
    try:

        if consumer_key is not None and consumer_secret is not None and access_token is not None and access_token_secret is not None:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            owner = api.me().name
            if owner == owner_account:
                return { 'status': 'success', 'data': api, 'message': f'Autenticación exitosa. Bienvenido desarrollador(a) {owner}' }
        else:
            return { 'status': 'error', 'data': '', 'message': 'Error!. No puede enviar credenciales vacíos.'}

    except tweepy.TweepError as e:
        return { 'status': 'error', 'data': '', 'message': f'Ocurrió un error inesperado. {e}'}


if __name__ == "__main__":
    print(auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, OWNER_ACCOUNT))