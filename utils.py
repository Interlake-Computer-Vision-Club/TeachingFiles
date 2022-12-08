import wikipedia as w, random as r, nltk, gensim.downloader as api, numpy as np

def find_summary(question, num_sentences=3, constant=0.5):
    
    glove_vectors = api.load('glove-twitter-25')
    
    vectorized_question = generate_vector(question, glove_vectors)
    
    most_relevant_article_name = r.choice(w.search(question, results=1))
    
    most_relevant_article_text = w.page(most_relevant_article_name, auto_suggest=False).content.split('==')[0]
    
    sentences = [sent for sent in nltk.sent_tokenize(most_relevant_article_text)]
    
    vectorized_sentences = [generate_vector(sent, glove_vectors) for sent in sentences]
    
    sentence_distances = [np.linalg.norm(vectorized_question - vec) for vec in vectorized_sentences]
    
    chosen_sent_indexes = []
    largest_sent_distance = max(sentence_distances)
    
    for i in range(num_sentences):
        best_sent_index = sentence_distances.index(min(sentence_distances))
        chosen_sent_indexes.append(best_sent_index)
        sentence_distances[best_sent_index] = largest_sent_distance
        
    ret = ''
    
    for ind in chosen_sent_indexes:
        for token in sentences[ind]:
            ret += token
    
    return most_relevant_article_name, ret

def generate_vector(sentence, model):
    
    nltk.download('stopwords')
    
    sentence = sentence.lower()
    
    split_text = nltk.word_tokenize(sentence)
    
    cleaned_text = []
    
    for token in split_text:
        if not token in set(nltk.corpus.stopwords.words('english')):
            cleaned_text.append(token)
    
    ret = np.zeros(25)
    
    count = 0
    
    for token in cleaned_text:
        
        try:    
            ret += model[token]
            count += 1
        except:
            pass
    
    return ret / count

article_name, text = find_summary('Who built the Taj Mahal?')

print("Article Name: ", article_name)
print(text)

#most_relevant_article_name = r.choice(w.search('egg', results=1))
    
#print(w.page(most_relevant_article_name, auto_suggest=False).content)
