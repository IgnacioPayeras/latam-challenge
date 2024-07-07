from typing import List, Tuple
import json
import heapq
from collections import defaultdict

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    #Inicializamos para contar las menciones de los usuarios
    mention_counts = defaultdict(int)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)

            #Obtenemos los usuarios mencionados directamente en el tweet
            mentioned_users = tweet.get('mentionedUsers')
            if mentioned_users:
                #Incrementamos el contador para cada usuario mencionado
                for user in mentioned_users:
                    mention_counts[user['username']] += 1

            #Verifica si tweet tiene tweet citado
            quoted_tweet = tweet.get('quotedTweet')
            if quoted_tweet:
                #Obtiene usuarios mencionados en el tweet
                quoted_mentioned_users = quoted_tweet.get('mentionedUsers')
                if quoted_mentioned_users:
                    #Incrementa el contador de menciones para el usuario mencionado en el tweet
                    for user in quoted_mentioned_users:
                        mention_counts[user['username']] += 1

    #Obtenemos los 10 usuarios más mencionados
    top_mentions = heapq.nlargest(10, mention_counts.items(), key=lambda x: x[1])

    return top_mentions