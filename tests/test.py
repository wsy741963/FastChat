import openai

# to get proper authentication, make sure to use a valid key that's listed in
# the --api-keys flag. if no flag value is provided, the `api_key` will be ignored.
openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"

model = "vicuna-7b-v1.5"

# prompt = "Once upon a time"
# completion = openai.Completion.create(model=model, prompt=prompt, max_tokens=64)
# print(prompt + completion.choices[0].text)

completion = openai.ChatCompletion.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": """从以下文字中提取药品主要成份名，复方药成份名用';'分隔，输出结果不带辅料、化学名和解释语句：\n
           <p>本品主要成份为氧氟沙星。-9-氟-2，3-二氢-3-甲基-10-（4-甲基-1-哌嗪基）-7-氧代-7h-吡啶并[1，2，3，-de]-[1，4]苯并噁嗪-6-羧酸。</p>
""",
        }
    ],
)
print(completion.choices[0].message.content)
