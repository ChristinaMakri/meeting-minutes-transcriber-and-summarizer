from keybert import KeyBERT

def extract_topics(text, num_topics=5):
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_topics)
    return [kw for kw, _ in keywords]