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

        print(response_string)

        prompt = f'''
        {response_string}
        Given these responses, how should this person reduce their CO2 emmissions?
        Use these examples as guidelines for your prompt. Follow the relationships formed below.

        Do you eat meat?: Y--> Meat products and dairy contribute twice as much as plant products to emmisions according to a study.
        Do you eat meat?: Y--> Meat accounts for 14.5% of global emmissions according to the UN
        Do you eat meat?: N--> Plant-based products help keep your emmissions low. Continue to eat plant based products if you wish to keep your CO2 emmissions low.

        What's your monthly electric bill?: 0--> 
        What's your monthly electric bill?: 10000000--> Because your monthly electic bills are so high, I reccomend that you look into decreasing your energy consumption.
        '''

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