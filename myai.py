from transformers import AutoTokenizer, AutoModel

# modelfile = "F:\ChatGLM2-6B\model-chatglm2-6b"
modelfile = "THUDM/chatglm2-6b"
tokenizer = AutoTokenizer.from_pretrained(modelfile, trust_remote_code=True)
model = AutoModel.from_pretrained(modelfile, trust_remote_code=True, device="cuda")

question = "从这段说明书中提取药品主要成份名，多种成份用';'分隔，不要输出辅料和解释相关语句"

text = """<div>
							本品为复方制剂，其组分为每粒含吲哚美辛75mg，呋喃唑酮100mg。
						</div>"""

model = model.eval()
response, history = model.chat(tokenizer, question + ":" + text, history=[])
print(response)
# response, history = model.chat(tokenizer, "晚上睡不着应该怎么办", history=history)
# print(response)
