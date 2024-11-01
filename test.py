from dotenv import load_dotenv
import os
from openai import OpenAI


def load_api_key():
    """
    从.env文件加载API密钥
    """
    load_dotenv()  # 加载.env文件
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("未找到 OPENAI_API_KEY。请确保在.env文件中设置了OPENAI_API_KEY。")
    return api_key


def chat_with_gpt(messages, model="gpt-3.5-turbo"):
    """
    与ChatGPT进行对话
    :param messages: 消息列表
    :param model: 使用的模型
    :return: AI的回复
    """
    try:
        # 创建客户端
        client = OpenAI(api_key=load_api_key())

        # 发送请求
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"发生错误：{str(e)}")
        if "authentication" in str(e).lower():
            print("API密钥验证错误，请检查.env文件中的OPENAI_API_KEY是否正确")
        return None


def main():
    try:
        # 创建对话消息
        messages = [
            {"role": "user", "content": "你好，请介绍一下自己。"}
        ]

        # 发送请求
        response = chat_with_gpt(messages)
        if response:
            print("AI回复:", response)

    except Exception as e:
        print(f"发生错误：{str(e)}")


if __name__ == "__main__":
    main()