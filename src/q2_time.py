from typing import List, Tuple
import re
import json
from collections import Counter

def extract_emojis(text):
    #Seteamos un patrón de expresiones regulares de los emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    #Devuelve los emojis encontrados en el JSON
    return emoji_pattern.findall(text)

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    #Contador de los emojis
    emoji_counter = Counter()

    #Tamaño del lote de 10.000 lineas
    batch_size = 10000

    with open(file_path, 'r', encoding='utf-8') as file:
        buffer = []
        for line in file:
            buffer.append(line)
            #Si el tamaño del buffer alcanza el tamaño del lote, procesa el lote 
            if len(buffer) >= batch_size:
                process_batch(buffer, emoji_counter)
                #Se vacía el buffer para el próximo lote
                buffer = []

        #Se procesan las líneas restantes en el buffer
        if buffer:
            process_batch(buffer, emoji_counter)  # Procesa cualquier línea restante

    #Obtiene los 10 emojis más comunes
    top_emojis = emoji_counter.most_common(10)
    return top_emojis

def process_batch(buffer: List[str], emoji_counter: Counter):
    for line in buffer:
        try:
            tweet = json.loads(line)
            #Verificamos si el tweet contiene la clave 'content'
            if 'content' in tweet:
                content = tweet['content']

                #Extrae los emojis del contenido
                emojis = extract_emojis(content)
                
                #Actualiza el contador de emojis
                emoji_counter.update(emojis)
        except json.JSONDecodeError:
            continue