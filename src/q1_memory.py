from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
import heapq
from dateutil.parser import parse

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Para contar la cantidad de tweets que hay por fecha
    date_counts = defaultdict(int)
    
    #Para contar la cantidad de tweets por usuario que tiene por fecha
    user_counts_by_date = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)

            #Extraemos la fecha
            date_str = tweet['date']

            #Extraemos el usuario
            username = tweet['user']['username']

            #Convertimos la fecha a formato date para evitar errores
            date = parse(date_str).date()
            date_counts[date] += 1
            user_counts_by_date[date][username] += 1

        #Encontramos las 10 fechas con mas tweets
        top_10_dates = heapq.nlargest(10, date_counts.items(), key=lambda x: x[1])

        result = []

        #Buscamos el usuario con más tweets en cada fecha
        for date, _ in top_10_dates:
            top_user = max(user_counts_by_date[date].items(), key=lambda x: x[1])[0]
            result.append((date, top_user))

        return result