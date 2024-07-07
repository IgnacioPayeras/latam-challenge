from typing import List, Tuple
import json
from collections import Counter
import re

def extract_emojis(text):
    #Seteamos un patrón de expresiones regulares de emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F" 
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    #Retornamos los los emojis encontrados en el JSON
    return emoji_pattern.findall(text)

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                tweet = json.loads(line)
                #Si está el campo content en el JSON
                if 'content' in tweet:
                    content = tweet['content']

                    #Extraemos los emojis del content
                    emojis = extract_emojis(content)

                    #Actualizamos el contador
                    emoji_counter.update(emojis)
            except json.JSONDecodeError:
                continue
    
    #Obtenemos los 10 emojis más comunes
    top_emojis = emoji_counter.most_common(10)
    return top_emojis