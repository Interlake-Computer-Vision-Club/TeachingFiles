from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

#home page of the application
@app.route('/')
def index():
    return render_template('index.html')

#return result
@app.route('/get_result')
def get_result():
    
    #image = request.args.get('image_upload', '')    
    
    return render_template('result.html').format('a', 'mouse')

if __name__ == '__main__':
    app.run()
    









































