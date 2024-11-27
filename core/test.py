import os
from openai import OpenAI
import httpx
import logging

# 获取环境变量
base_url = os.environ.get('LLM_API_BASE', "").strip()  # 去除可能的空格

# 检查环境变量是否设置
if not base_url:
    raise ValueError("LLM_API_BASE must be set")

# 打印调试信息
print(f"Base URL: {base_url} (Type: {type(base_url)})")

# 设置日志级别
logging.basicConfig(level=logging.DEBUG)

# 创建一个自定义的 HTTPX 客户端
httpx_client = httpx.Client()

# 初始化 OpenAI 客户端
client = OpenAI(base_url=base_url, http_client=httpx_client)

try:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        model="qwen2.5-coder-14b-instruct"
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")