from flask import Flask ,request,render_template
import pickle
import os 
app=Flask(__name__)
model=pickle.load(open('classificationModel.sav','rb'))   
FLOWER_FOLDER = os.path.join('static', 'flower_photo')
# FLOWER_FOLDER = os.path('static')
app.config['UPLOAD_FOLDER'] = FLOWER_FOLDER

@app.route("/")
def home():
    result=''
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Iris.jpeg')
    print(f"full_filename is: {full_filename}")
    return render_template("index.html",**locals())
    # return render_template("index.html",**locals())

@app.route("/predict",methods=["POST","GET"])
def predict():
    sepal_length=float(request.form['sepal_length'])
    sepal_width=float(request.form['sepal_width'])
    petal_length=float(request.form['petal_length'])
    petal_width=float(request.form['petal_width'])
    result=model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Iris.jpeg')
    print(f"full_filename is: {full_filename}")
    return render_template("index.html",**locals(), UserImage = full_filename)
    # return render_template("index.html",**locals())

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)