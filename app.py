import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def index():
    output = ""
    return render_template("index.html", output=output)

@app.route("/thisIsTheNameOfRedirect", methods=("GET", "POST"))
def question():
    if request.method == "POST": 
        variableQ1 = request.form.get("Do you eat meat?")
        variableQ2 = request.form.get("Do you use public transport?")
        # add more vars here

        fString = f'Do you eat meat? {variableQ1} Do you use public transport? {variableQ2}'

        response = openai.Completion.create(
             model="text-davinci-003",
             prompt=generate_prompt(fString),
             temperature=0.6,
        )
        
        output = response.choices[0].text
        
        return render_template("index.html", output=output)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


def generate_prompt(input):
    return """{}
    This is the user's response and answer to these questions.
    How would you reccomend reduce their emmissions
    
    """.format(
        input.capitalize()
    )

#the brackets above put the user response into the code and gpt fills the rest.
#this is generation. 