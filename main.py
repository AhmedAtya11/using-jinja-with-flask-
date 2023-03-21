import requests
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/guess/<name>')
def guess(name):
    name_parameters={"name": name}
    response_agify=requests.get(f"https://api.agify.io",params=name_parameters)
    response_genderize=requests.get(f"https://api.genderize.io",params=name_parameters)
    age_response=response_agify.json()["age"]
    gender_response=response_genderize.json()["gender"]
    return render_template ("index.html",personal_name=name,age=age_response,gender=gender_response)


@app.route('/blog')
def blog():
    my_list=[num for num in range(10)]
    return render_template ("index2.html",all_nums=my_list)


if __name__=="__main__":
    app.run(debug=True)

