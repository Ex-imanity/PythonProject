# FastAPI Test Project

这是一个简单的 FastAPI 测试项目，用于测试 py-cov-service 覆盖率统计功能。

## 项目结构

```
PythonProject/
├── main.py              # FastAPI 应用主文件
├── requirements.txt      # Python 依赖
├── README.md            # 项目说明
└── .gitignore           # Git 忽略文件
```

## 功能特性

项目包含以下 API 接口：

- `GET /` - 根路径，返回欢迎信息
- `GET /health` - 健康检查接口
- `GET /users` - 获取用户列表
- `GET /users/{user_id}` - 根据ID获取用户
- `POST /users` - 创建新用户
- `GET /products` - 获取产品列表（支持分类筛选）
- `GET /products/{product_id}` - 根据ID获取产品
- `POST /orders` - 创建订单
- `GET /orders/{order_id}` - 根据ID获取订单
- `GET /stats` - 获取统计信息

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
# 方式1：直接运行
python main.py

# 方式2：使用 uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. 访问应用

- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/health
- 根路径：http://localhost:8000/

## API 示例

### 获取用户列表

```bash
curl http://localhost:8000/users
```

### 获取单个用户

```bash
curl http://localhost:8000/users/1
```

### 创建用户

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "David", "email": "david@example.com", "role": "user"}'
```

### 获取产品列表（按分类）

```bash
curl http://localhost:8000/products?category=electronics
```

## 测试覆盖率

此项目设计用于测试覆盖率统计功能，包含：

- 多个路由端点
- 条件分支逻辑（if/else）
- 循环处理（for 循环）
- 错误处理（404 响应）
- 数据计算函数

可以通过 py-cov-service 项目对此项目进行覆盖率统计测试。

## 许可证

MIT License

