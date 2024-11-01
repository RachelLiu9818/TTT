import os
from dotenv import load_dotenv
import openai

# 加载 .env 文件
load_dotenv()

# 设置 OpenAI API 密钥
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # 测试 API 调用
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用正确的模型名称
        messages=[
            {"role": "user", "content": "请给我讲个笑话。"}
        ]
    )
    # 输出返回的消息
    print(response.choices[0].message['content'])

except openai.error.OpenAIError as e:
    print(f"发生错误：{e}")

