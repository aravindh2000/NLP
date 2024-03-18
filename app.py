from flask import Flask, request, jsonify, render_template
import DataPreProcessor
import spacy

app = Flask(__name__)

def sortScore(data) :
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]['score'] < data[j + 1]['score']:
                data[j], data[j + 1] = data[j + 1], data[j]
                 



@app.route("/predict",methods=['POST'])
def predict():
    q1 = request.form.get("val")
    
    instance = DataPreProcessor.DataPreProcessor(spacy=spacy)
    res = instance.loadModelAndProcessPdfWithCount(str(q1),'./RESUME/data')
    sortScore(res)
    
    # print(res[0:int(request.form.get("count"))])
    op = res[0:int(request.form.get("count"))]
    
    col = []
    for ind in op:
        col.append([ind['id'],ind['path'],ind['score']])
    # return jsonify({"results":res[0:int(reqJson['noOfMatches'])]})

    return render_template('home.html',result=col)

@app.route("/predictCall",methods=['POST'])
def predictCall():
    reqJson = request.get_json()
    
    instance = DataPreProcessor.DataPreProcessor(spacy=spacy)
    res = instance.loadModelAndProcessPdfWithCount(reqJson['context'],reqJson['inputpath'])
    sortScore(res)
    print(res[0:int(reqJson['noOfMatches'])])
    return jsonify({"results":res[0:int(reqJson['noOfMatches'])]})

    


@app.route('/')
def form():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
