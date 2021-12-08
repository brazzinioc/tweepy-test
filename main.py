
from authentication import auth
import tweepy
from settings import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, OWNER_ACCOUNT


def get_principal_tweets(api, query, quantity):
    """Obtiene los tweets principales

    Args:
        api (Object): Instancia de Tweepy API.
        query (String): Query para filtrar los tweets. Referencia https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/overview/standard-operators
        quantity (Int): Cantidad de tweets que se obtendrá
    """
    tweets = []
    try:

        if api is not None and query is not None and len(query) > 0 and quantity > 0:
            for tweet in tweepy.Cursor(api.search, q=query, result_type='recent', timeout=999999).items(quantity):
                    if hasattr(tweet, 'in_reply_to_status_id_str') and tweet.in_reply_to_status_id_str is None:
                        tweet_data = { 'id': tweet.id_str, 'text': tweet.text.replace('\n', ''), 'author': tweet.author.screen_name}
                        tweets.append(tweet_data)

    except tweepy.TweepError as e:
        print(f'Ocurrió un error inesperado, al obtener los tweet principales. {e}')

    return tweets


def get_replies_tweet(api, tweet_id, tweet_author, quantity):
    """Obtiene los comentarios de un tweet principal

    Args:
        api (Object): Instancia de Tweepy API
        tweet_id (String): Id del tweet principal
        tweet_author (String): Nombre del autor del tweet principal
        quantity (Int): Cantidad de tweets que se obtendrá
    """
    replies = []

    try:

        for tweet in tweepy.Cursor(api.search, q='to:' + tweet_author + ' filter:replies AND -filter:retweets', timeout=999999).items(quantity):
            if hasattr(tweet, 'in_reply_to_status_id_str') and tweet.in_reply_to_status_id_str == tweet_id:
                reply_data = { 'id': tweet.id_str, 'text': tweet.text.replace('\n',''), 'author': tweet.author.screen_name}
                replies.append(reply_data)

    except tweepy.TweepError as e:
        print(f'Ocurrió un error inesperado, al obtener los comentarios de un tweet. {e}')        

    return replies


def run(auth):
    auth = auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, OWNER_ACCOUNT)
    if auth['status'] == 'success':
        api = auth['data']
        
        principal_tweets = get_principal_tweets(api, 'SE HIZO JUSTICIA -filter:retweets AND -filter:replies', 500)

        if len(principal_tweets) > 0:
            for t in principal_tweets:
                print('Tweet principal: \n----------------')
                id_principal = t['id']
                text_principal = t['text']
                author_principal = t['author']

                print(f'Id: {id_principal} \nTexto: {text_principal} \nAutor:{author_principal}')


                replies = get_replies_tweet(api, id_principal, author_principal, 30)

                if len(replies) > 0:
                    print('\n')
                    for r in replies:
                        print('\t Comentario: \n\t---------------')
                        id_reply = r['id']
                        text_reply = r['text']
                        author_reply = r['author']
                        print(f'\tId: {id_reply} \n\tTexto: {text_reply} \n\tAutor:{author_reply}')
                        print('\n')
                else:
                    print("No posee comentarios.")

                print('\n\n')


if __name__ == "__main__":
    run(auth)
