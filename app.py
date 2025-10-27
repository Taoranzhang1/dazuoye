import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def main():
    app_name = os.getenv("APP_NAME", "Python应用")
    greeting = os.getenv("GREETING", "你好")

    print(f"{app_name}已启动")

    name = input("请输入您的姓名: ")

    if name.strip():
        print(f"{greeting}, {name}!")
    else:
        print(f"{greeting}!")

@app.route('/')
def hello():
    return jsonify({
        'message': '电影推荐系统 - DevOps & MLOps项目',
        'status': '运行中'
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/model-info')
def model_info():
    return jsonify({
        'project': '电影推荐系统',
        'mlops_status': '完整实现',
        'models_trained': {
            'baseline': {
                'dataset': 'v1 (1000条记录)',
                'performance': {'RMSE': 1.4519, 'MAE': 1.2234}
            },
            'improved': {
                'dataset': 'v2 (793条记录)',
                'performance': {'RMSE': 1.0588, 'MAE': 0.8829},
                'improvement': 'RMSE提升27%'
            }
        }
    })

@app.route('/mlops-status')
def mlops_status():
    return jsonify({
        'data_versioning': {
            'status': '完成',
            'tool': 'DVC',
            'versions': ['v1 - 原始数据', 'v2 - 清洗数据']
        },
        'experiment_tracking': {
            'status': '完成',
            'tool': 'MLflow',
            'experiments': ['baseline模型', 'improved模型']
        }
    })

if __name__ == "__main__":
    main()