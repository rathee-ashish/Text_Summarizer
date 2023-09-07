from flask import Flask,render_template,request
from text_summary import summarizer

app = Flask(__name__)

@app.route("/" , methods=['GET','POST'])
def index():
    summary=""
    doc=""
    if request.method == 'POST':
        text=request.form['inputText']
        if text !="":
            summary,doc =summarizer(text)
            return render_template("index.html",summary=summary,doc=doc)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)