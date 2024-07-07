from typing import List, Tuple
from datetime import datetime
from dateutil.parser import parse
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Leemos el JSON
    df = pd.read_json(file_path, lines=True)
    
    #Convertir la columna date a formato date por si no está en ese formato
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        df['date'] = pd.to_datetime(df['date']).dt.date
    else:
        df['date'] = df['date'].dt.date
    
    #Se calcula la cantidad de tweets por fecha y se seleccionan las top 10 con más tweets
    date_counts = df['date'].value_counts().nlargest(10)
    
    result = []
    for date in date_counts.index:
        #Se obtienen los tweets con la fecha que se está iterando
        df_filtered = df[df['date'] == date]

        #Encuentra el usuario con más tweets
        top_user = df_filtered['user'].apply(lambda x: x['username']).value_counts().idxmax()
        result.append((date, top_user))
    
    return result