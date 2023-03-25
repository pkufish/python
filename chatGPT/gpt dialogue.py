import openai
import time

# 使用 OpenAI API 密钥进行身份验证
# 设置 API Key，申请地址：https://platform.openai.com/account/api-keys
openai.api_key = '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'
# 设置组织，查看地址：https://platform.openai.com/account/org-settings
openai.organization = "org-ksQNRTJF3XweFCDhyOdbgLs3"

# 指定 GPT-3 模型和其配置
model_engine = "text-davinci-002"
prompt_text = ("Hello, I'm your assistant! What can I do for you today?\n"
               "User: Hey, I need some help with my math homework.\n"
               "Computer: Sure, what do you need help with?\n"
               )

print(prompt_text)

# 创建 OpenAI GPT-3 模型实例
def create_openai_instance(prompt_text):
    instance = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        max_tokens=120,
        n=1,
        stop=None,
        temperature=0.5,
    )["choices"][0]["text"].strip()
    return instance


# 进行对话的函数
def create_dialogue():
    for i in range(10):
        # 打印用户输入
        user_input = input("User: ")
        prompt_text = f"{prompt_text}User: {user_input}\nComputer: "
        # 从 OpenAI 获取模型响应并打印
        response = create_openai_instance(prompt_text)
        print("Computer:", response)
        # 修改 prompt_text 以便下一个对话回合
        prompt_text = f"{prompt_text}{response}\nUser: "
        time.sleep(1)
    return


if __name__ == "__main__":
    create_dialogue()

# 这段代码使用 OpenAI 的 GPT-3 模型生成了一个开场白，随后将进入一个循环，执行 10 次对话，每次输入用户的回复并将该回复发送给模型，模型返回响应并打印在控制台上。程序还添加了一个延迟时间，使对话不会过于快速地进行。您可以根据需要对提示文本进行调整，以便更好地适应您的用例。
