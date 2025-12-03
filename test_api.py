"""
简单的 API 测试脚本
用于测试各个接口是否正常工作
"""
import requests
import json

BASE_URL = "http://localhost:8000"


def test_root():
    """测试根路径"""
    response = requests.get(f"{BASE_URL}/")
    print(f"GET / - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_health():
    """测试健康检查"""
    response = requests.get(f"{BASE_URL}/health")
    print(f"GET /health - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_users():
    """测试获取用户列表"""
    response = requests.get(f"{BASE_URL}/users")
    print(f"GET /users - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_user():
    """测试获取单个用户"""
    response = requests.get(f"{BASE_URL}/users/1")
    print(f"GET /users/1 - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_create_user():
    """测试创建用户"""
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "role": "user"
    }
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    print(f"POST /users - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_products():
    """测试获取产品列表"""
    response = requests.get(f"{BASE_URL}/products")
    print(f"GET /products - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_products_by_category():
    """测试按分类获取产品"""
    response = requests.get(f"{BASE_URL}/products?category=electronics")
    print(f"GET /products?category=electronics - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_product():
    """测试获取单个产品"""
    response = requests.get(f"{BASE_URL}/products/1")
    print(f"GET /products/1 - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_create_order():
    """测试创建订单"""
    order_data = {
        "user_id": 1,
        "products": [
            {"id": 1, "price": 99.99, "quantity": 2},
            {"id": 3, "price": 49.99, "quantity": 1}
        ]
    }
    response = requests.post(f"{BASE_URL}/orders", json=order_data)
    print(f"POST /orders - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_order():
    """测试获取订单"""
    response = requests.get(f"{BASE_URL}/orders/1001")
    print(f"GET /orders/1001 - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_get_stats():
    """测试获取统计信息"""
    response = requests.get(f"{BASE_URL}/stats")
    print(f"GET /stats - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


def test_404():
    """测试404错误处理"""
    response = requests.get(f"{BASE_URL}/users/999")
    print(f"GET /users/999 - Status: {response.status_code}")
    print(f"Response: {response.json()}\n")


if __name__ == "__main__":
    print("=" * 50)
    print("FastAPI Test Project - API 测试")
    print("=" * 50)
    print()
    
    try:
        test_root()
        test_health()
        test_get_users()
        test_get_user()
        test_create_user()
        test_get_products()
        test_get_products_by_category()
        test_get_product()
        test_create_order()
        test_get_order()
        test_get_stats()
        test_404()
        
        print("=" * 50)
        print("所有测试完成！")
        print("=" * 50)
    except requests.exceptions.ConnectionError:
        print("错误：无法连接到服务器，请确保 FastAPI 应用正在运行")
        print("运行命令：python main.py 或 uvicorn main:app --reload")
    except Exception as e:
        print(f"测试过程中出现错误：{str(e)}")

