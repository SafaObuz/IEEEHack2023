import openai
from flask import Flask, redirect, render_template, request, url_for


## Im testing merging. Adding this comment to merge.


app = Flask(__name__)
openai.api_key = "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"

def generate_prompt(input):
    return """{}
    This is the user's response and answer to these questions.
    How would you recommend reducing their emissions?
    """.format(input.capitalize())

@app.route("/")
def index():
    output = ""
    return render_template("index.html", output=output)

@app.route("/thisIsTheNameOfRedirect", methods=("GET", "POST"))
def question():
    if request.method == "POST": 
        variableQ1 = request.form.get("Do you eat meat?")
        variableQ2 = request.form.get("Do you use public transport?")
        variableQ3 =request.form.get("monthly_electric_bill")
        if variableQ1.lower() in ["yes", "y", "1", "true"]:
           eat_meat="I eat meat"
        else:
            eat_meat="I dont meat"
        # add more vars here

        fString = f'{eat_meat} Do you use public transport? {variableQ2}. My monthly electric bill is {variableQ3}$ per month'

        response = openai.Completion.create(
             model="text-davinci-003",
             prompt=generate_prompt(fString),
             temperature=1,
              max_tokens=500
        )
        
        output = response.choices[0].text
        
        return render_template("index.html", output=output)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)