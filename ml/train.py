import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from datetime import datetime

def train_model(model_version="baseline"):
    mlflow.set_experiment("MovieRecommendation")
    
    with mlflow.start_run(run_name=f"{model_version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"):
        data_version = 'v1' if model_version == 'baseline' else 'v2'
        data_path = f'data/{"raw" if data_version == "v1" else "processed"}/ratings_{data_version}.csv'
        df = pd.read_csv(data_path)
        
        user_stats = df.groupby('user_id')['rating'].agg(['mean', 'count']).reset_index()
        user_stats.columns = ['user_id', 'user_mean', 'user_count']
        
        movie_stats = df.groupby('movie_id')['rating'].agg(['mean', 'count']).reset_index()
        movie_stats.columns = ['movie_id', 'movie_mean', 'movie_count']
        
        df = df.merge(user_stats, on='user_id')
        df = df.merge(movie_stats, on='movie_id')
        
        df['user_id_encoded'] = pd.factorize(df['user_id'])[0]
        df['movie_id_encoded'] = pd.factorize(df['movie_id'])[0]
        
        features = ['user_id_encoded', 'movie_id_encoded', 'user_mean', 'movie_mean']
        X = df[features]
        y = df['rating']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # 硬编码参数
        if model_version == "baseline":
            n_estimators = 50
            max_depth = 10
        else:
            n_estimators = 100
            max_depth = 20
        
        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        # MLflow记录
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("data_version", data_version)
        mlflow.log_metrics({
            "mse": mse, 
            "mae": mae, 
            "rmse": np.sqrt(mse)
        })
        mlflow.sklearn.log_model(model, "model")
        
        print(f"{model_version}模型训练完成!")
        print(f"数据集: {data_version}, 记录数: {len(df)}")
        print(f"MSE: {mse:.4f}, MAE: {mae:.4f}, RMSE: {np.sqrt(mse):.4f}")
        
        return model

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', choices=['baseline', 'improved'], default='baseline')
    args = parser.parse_args()
    train_model(args.version)