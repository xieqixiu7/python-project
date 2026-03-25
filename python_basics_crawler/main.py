# python_basics_crawler/main.py
import requests

print("=== 开始执行 fetch_webpage ===")


def fetch_webpage():
    url = "https://httpbin.org/get"
    try:
        print(f"📡 正在请求: {url}")
        response = requests.get(url, timeout=5)
        print(f"📬 收到响应，状态码: {response.status_code}")

        if response.status_code == 200:
            print("✅ 成功获取数据!")
            print("📦 返回内容:")
            print(response.json())
        else:
            print(f"❌ 请求失败，状态码: {response.status_code}")
    except requests.exceptions.Timeout:
        print("⏰ 请求超时！请检查网络连接或服务器是否响应慢。")
    except requests.exceptions.ConnectionError:
        print("🔌 连接错误！可能是网络断开、DNS 错误或目标服务器拒绝连接。")
    except Exception as e:
        print(f"💥 发生未知异常: {type(e).__name__} - {e}")


if __name__ == "__main__":
    fetch_webpage()