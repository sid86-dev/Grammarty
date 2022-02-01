from gingerit.gingerit import GingerIt

from flask import Flask, request,render_template,redirect, make_response, jsonify
import json

app = Flask(__name__)
 

def checkText(text):
    parser = GingerIt()
    newText = parser.parse(text)
    return newText

@app.route("/")
def sent():
    if request.method == "GET":
        return render_template("index.html")
    else:
        
        if not request.form["SENT"]:
            return redirect("/")


  
 
@app.post("/sent_correct")
def sent_correct():
    # get data from frontend
    data = request.get_json()
    text = data["text"]
    print(text)

    try:
        print(checkText(text))
        res = make_response(jsonify({"error": 'no-error','text':checkText(text)}), 200)
        return res
    except:
        res = make_response(jsonify({"error": 'Something went wrong, try again'}), 200)
        return res

        

if __name__ == "__main__":
    # app.run(debug=True)
    print(checkText("hi this are tree"))