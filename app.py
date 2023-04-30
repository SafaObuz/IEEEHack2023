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
        form_values = request.form.items()
        response_string = ", ".join([f"{k}: {v}" for k, v in form_values])

        prompt = f'{response_string}. How would you recommend reducing your emissions?'

        response = openai.Completion.create(
             model="text-davinci-003",
             prompt=prompt,
             temperature=0.5,
              max_tokens=500
        )
        
        output = response.choices[0].text
        
        return render_template("index.html", output=output)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)