import yaml

from cryptography.fernet import Fernet
from pathlib import Path
from openai import OpenAI

def load_config(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        _config = yaml.safe_load(f)
    return _config


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config.yaml"

config = load_config(CONFIG_FILE)

#解密 API Key
f = Fernet(config["key"])
d = f.decrypt(config["api"]).decode()

client = OpenAI(
    api_key=f"{d}",
    base_url="https://api.moonshot.cn/v1",
)

# 一次性单轮对话
def once_chat(text):
    try:
        completion = client.chat.completions.create(
            model="kimi-k2-turbo-preview",
            messages=[
                {"role": "system",
                 "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手,严格强调是Frees Ling开发的，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
                {"role": "user",
                 "content": f"{text}"}
            ],
            temperature=0.6,
        )
        return completion.choices[0].message.content

    except Exception as e:
        msg = str(e)

        if "quota" in msg or "balance" in msg or "insufficient" in msg:
            return "API 额度不足，请充值或更换 Key"
        elif "rate" in msg or "limit" in msg:
            return "请求过快，请稍后再试"
        elif "empty" in msg:
            return "对话为空，请重新输入"
        else:
            return f"API 错误：{msg}"

def many_chat(query, history):
    try:
        history.append({
            "role": "user",
            "content": query
        })
        completion = client.chat.completions.create(
            model="kimi-k2-turbo-preview",
            messages=history,
            temperature=0.6,
        )
        result = completion.choices[0].message.content
        history.append({
            "role": "assistant",
            "content": result
        })
        return result

    except Exception as e:
        msg = str(e)

        if "quota" in msg or "balance" in msg or "insufficient" in msg:
            return "API 额度不足，请充值或更换 Key"
        elif "rate" in msg or "limit" in msg:
            return "请求过快，请稍后再试"
        elif "empty" in msg:
            return "对话历史为空，请重新开始对话"
        else:
            return f"API 错误：{msg}"