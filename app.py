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
    res = instance.loadModelAndProcessPdfWithCount(str(q1),'./tmp/8dc4743c1966b0e/RESUME/data')
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
    # res = instance.loadModelAndProcessPdfWithCount(reqJson['context'],reqJson['inputpath'])
    res = instance.loadModelAndProcessPdfWithCount(reqJson['context'],'./tmp/8dc4743c1966b0e/RESUME/data')


    sortScore(res)
    print(res[0:int(reqJson['noOfMatches'])])
    return jsonify({"results":res[0:int(reqJson['noOfMatches'])]})

    


@app.route('/')
def form():
    return render_template('home.html')

# def downloadPDF():
#     from google.cloud import storage
#     from pathlib import Path
#     import base64
#     path_to_private_key = 'D:/fifth-compass-415612-76f634511b19.json'
#     client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)
#     bucket = storage.Bucket(client, 'hackathon1415')
#     str_folder_name_on_gcs = 'RESUME/data'

#     # Create the directory locally
#     Path(str_folder_name_on_gcs).mkdir(parents=True, exist_ok=True)

#     blobs = bucket.list_blobs(prefix=str_folder_name_on_gcs)
#     # print(len(list(blobs)))
#     blb = list(blobs)
#     for itr in range(200):
#         if not blb[itr].name.endswith('/'):
#             # This blob is not a directory!
#             print(f'Downloading file [{blb[itr].name}]')
#             # content = blb[itr].download_as_string()
#             blb[itr].download_to_filename(f'./{blb[itr].name}')
#             # data =base64.b64decode(content)
#             # data.decode('latin-1').translate()
    



if __name__ == '__main__':
    app.run(debug=True)
