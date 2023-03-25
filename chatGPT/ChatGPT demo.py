# 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
# org-ksQNRTJF3XweFCDhyOdbgLs3
#1
import openai

# 设置 API Key，申请地址：https://platform.openai.com/account/api-keys
openai.api_key = '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'
# 设置组织，查看地址：https://platform.openai.com/account/org-settings
openai.organization = "org-ksQNRTJF3XweFCDhyOdbgLs3"

# print(openai.Model.list())

# 请求模型
model_engine = "gpt-3.5-turbo"  # text-davinci-002  gpt-3.5-turbo
# 输入内容
prompt = input("欢迎使用chatGPT 佐才demo，请输入对话的内容\n")
# 调用接口
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message.content)
print(completion)

# import os
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Who won the world series in 2020?"},
#         {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         {"role": "user", "content": "Where was it played?"}
#     ]
# )
#
# print(completion.choices[0].message)
#


# completions = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )
#
#
