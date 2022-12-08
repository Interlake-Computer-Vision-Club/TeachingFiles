from flask import Flask, render_template, request
import wikipedia as w, utils

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

#home page of the application
@app.route('/')
def index():
    return render_template('index.html')

#return result
@app.route('/get_result')
def get_result():
    
    question = request.args.get('question', '')
    
    most_relevant_article = w.search(question, results=1)[0]
    
    article_name, summary = utils.find_summary(question)
    
    answer = 'Response summarized from the article: {}\n\n'.format(article_name) + summary
    
    return render_template('result.html').format(question, answer)

if __name__ == '__main__':
    app.run()
    









































