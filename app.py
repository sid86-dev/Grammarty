import language_tool_python
from flask import Flask, request,render_template,redirect, make_response, jsonify

app = Flask(__name__)
 

def checkText(text):
    tool = language_tool_python.LanguageTool('en-US', config={ 'cacheSize': 1000, 'pipelineCaching': True })
    newText = tool.correct(text)
    return newText

@app.get("/")
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

    try:
        res = make_response(jsonify({"error": 'no-error','text':checkText(text)}), 200)
        return res
    except:
        res = make_response(jsonify({"error": 'Something went wrong, try again'}), 200)
        return res

        

if __name__ == "__main__":
    app.run(debug=True)
