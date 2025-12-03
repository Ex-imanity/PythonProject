"""
FastAPI 测试项目
用于测试 py-cov-service 覆盖率统计功能
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List, Dict, Optional
import random

app = FastAPI(
    title="FastAPI Test Project",
    description="用于测试覆盖率统计的简单 FastAPI 项目",
    version="1.0.0"
)


@app.get("/")
async def root():
    """根路径"""
    return {"message": "Welcome to FastAPI Test Project", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    """健康检查接口"""
    return {"status": "healthy", "service": "fastapi-test"}


@app.get("/users")
async def get_users():
    """获取用户列表"""
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    ]
    return {"users": users, "total": len(users)}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """根据ID获取用户"""
    users = {
        1: {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin"},
        2: {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "user"},
        3: {"id": 3, "name": "Charlie", "email": "charlie@example.com", "role": "user"},
    }
    
    if user_id not in users:
        return JSONResponse(
            status_code=404,
            content={"error": "User not found", "user_id": user_id}
        )
    
    return users[user_id]


@app.post("/users")
async def create_user(user_data: Dict):
    """创建新用户"""
    user_id = random.randint(100, 999)
    new_user = {
        "id": user_id,
        "name": user_data.get("name", "Unknown"),
        "email": user_data.get("email", ""),
        "role": user_data.get("role", "user")
    }
    return JSONResponse(
        status_code=201,
        content={"message": "User created", "user": new_user}
    )


@app.get("/products")
async def get_products(category: Optional[str] = None):
    """获取产品列表，支持按分类筛选"""
    products = [
        {"id": 1, "name": "Product A", "category": "electronics", "price": 99.99},
        {"id": 2, "name": "Product B", "category": "electronics", "price": 149.99},
        {"id": 3, "name": "Product C", "category": "clothing", "price": 49.99},
        {"id": 4, "name": "Product D", "category": "clothing", "price": 79.99},
    ]
    
    if category:
        filtered_products = [p for p in products if p["category"] == category]
        return {"products": filtered_products, "category": category, "total": len(filtered_products)}
    
    return {"products": products, "total": len(products)}


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """根据ID获取产品"""
    products = {
        1: {"id": 1, "name": "Product A", "category": "electronics", "price": 99.99, "stock": 10},
        2: {"id": 2, "name": "Product B", "category": "electronics", "price": 149.99, "stock": 5},
        3: {"id": 3, "name": "Product C", "category": "clothing", "price": 49.99, "stock": 20},
        4: {"id": 4, "name": "Product D", "category": "clothing", "price": 79.99, "stock": 15},
    }
    
    if product_id not in products:
        return JSONResponse(
            status_code=404,
            content={"error": "Product not found", "product_id": product_id}
        )
    
    return products[product_id]


@app.post("/orders")
async def create_order(order_data: Dict):
    """创建订单"""
    order_id = random.randint(1000, 9999)
    order = {
        "id": order_id,
        "user_id": order_data.get("user_id"),
        "products": order_data.get("products", []),
        "total": calculate_order_total(order_data.get("products", [])),
        "status": "pending"
    }
    return JSONResponse(
        status_code=201,
        content={"message": "Order created", "order": order}
    )


def calculate_order_total(products: List[Dict]) -> float:
    """计算订单总价"""
    total = 0.0
    for product in products:
        price = product.get("price", 0.0)
        quantity = product.get("quantity", 1)
        total += price * quantity
    return round(total, 2)


@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    """根据ID获取订单"""
    orders = {
        1001: {"id": 1001, "user_id": 1, "products": [{"id": 1, "quantity": 2}], "total": 199.98, "status": "completed"},
        1002: {"id": 1002, "user_id": 2, "products": [{"id": 3, "quantity": 1}], "total": 49.99, "status": "pending"},
    }
    
    if order_id not in orders:
        return JSONResponse(
            status_code=404,
            content={"error": "Order not found", "order_id": order_id}
        )
    
    return orders[order_id]


@app.get("/stats")
async def get_stats():
    """获取统计信息"""
    stats = {
        "total_users": 3,
        "total_products": 4,
        "total_orders": 2,
        "revenue": 249.97
    }
    return stats


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

