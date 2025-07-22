from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_minutes(transcript):
    prompt = f"Below is a transcript of a city council meeting. Write professional meeting minutes with summary, discussion points, takeaways, and action items.\n\n{transcript}"
    model_id = "mistralai/Mistral-7B-Instruct-v0.2"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=1024)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)