import nltk

nltk.download('punkt')

def get_sentences_from_paragraph(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    sentences_dict = {i: sentence for i, sentence in enumerate(sentences)}
    return sentences_dict
