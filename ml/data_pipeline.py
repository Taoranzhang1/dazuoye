import pandas as pd
import numpy as np
import os

def create_sample_datasets():
    np.random.seed(42)
    users = [f'user_{i}' for i in range(1, 101)]
    movies = [f'movie_{i}' for i in range(1, 51)]
    
    data_v1 = []
    for user in users:
        for movie in np.random.choice(movies, size=10, replace=False):
            rating = np.random.randint(1, 6)
            data_v1.append({'user_id': user, 'movie_id': movie, 'rating': rating})
    
    df_v1 = pd.DataFrame(data_v1)
    os.makedirs('data/raw', exist_ok=True)
    df_v1.to_csv('data/raw/ratings_v1.csv', index=False)
    
    df_v2 = df_v1.copy()
    df_v2['timestamp'] = np.random.randint(1609459200, 1640995200, len(df_v2))
    df_v2 = df_v2[df_v2['rating'] >= 2]
    
    os.makedirs('data/processed', exist_ok=True)
    df_v2.to_csv('data/processed/ratings_v2.csv', index=False)
    
    print(f"数据集v1: {len(df_v1)} 条记录")
    print(f"数据集v2: {len(df_v2)} 条记录")
    
    return df_v1, df_v2

if __name__ == "__main__":
    create_sample_datasets()