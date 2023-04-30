import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"

def generate_prompt(variableQ1, variableQ2, variableQ3):
    return f"{variableQ1.capitalize()} Do you use public transport? {variableQ2}. My monthly electric bill is {variableQ3}$ per month. Based on your responses, here are some ways you can reduce your carbon footprint: Also, respond according to how much power they use. If they use little power (less than 1000) then do not recommend much power saving. If they use a lot of power (1000000) then aggressively tell them to be energy efficient."

@app.route("/")
def index():
    output = ""
    return render_template("index.html", output=output)

@app.route("/thisIsTheNameOfRedirect", methods=("GET", "POST"))
def question():
    if request.method == "POST": 
        variableQ1 = request.form.get("Do you eat meat?")
        variableQ2 = request.form.get("Do you use public transport?")
        variableQ3 = request.form.get("monthly_electric_bill")

        # Convert variableQ1 to boolean for easier processing
        eat_meat = variableQ1.lower() == "yes"

        # Generate prompt based on user's carbon footprint
        prompt = generate_prompt(variableQ1, variableQ2, variableQ3)

        # Generate response using GPT-3
        response = openai.Completion.create(
             model="text-davinci-003",
             prompt=prompt,
             temperature=0,
             max_tokens=500
        )
        
        output = response.choices[0].text
        
        return render_template("index.html", output=output)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
