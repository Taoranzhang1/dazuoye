import os
from dotenv import load_dotenv

load_dotenv()


def main():
    app_name = os.getenv("APP_NAME", "Python应用")
    greeting = os.getenv("GREETING", "你好")

    print(f"{app_name}已启动")

    name = input("请输入您的姓名: ")

    if name.strip():
        print(f"{greeting}, {name}!")
    else:
        print(f"{greeting}!")


if __name__ == "__main__":
    main()
