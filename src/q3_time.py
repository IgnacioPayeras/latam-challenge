from typing import List, Tuple
import json
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    #Inicializa un contador para menciones de usuarios
    mention_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        data = [json.loads(line) for line in file]

    for tweet in data:
        #Obtiene los usuarios mencionados directamente en el tweet
        mentioned_users = tweet.get('mentionedUsers')
        if isinstance(mentioned_users, list):
            #Incrementa el contador de menciones para cada usuario mencionado
            for user in mentioned_users:
                mention_counts[user['username']] += 1

        #Verificamos si el tweet tiene citado
        quoted_tweet = tweet.get('quotedTweet')
        if quoted_tweet:
            #Obtiene los usuarios mencionados en el tweet citado
            quoted_mentioned_users = quoted_tweet.get('mentionedUsers')
            if isinstance(quoted_mentioned_users, list):
                #Incrementa el contador de menciones para cada usuario
                for user in quoted_mentioned_users:
                    mention_counts[user['username']] += 1

    #Obtenemos los 10 usuarios mas mencionados
    top_mentions = mention_counts.most_common(10)

    return top_mentions
