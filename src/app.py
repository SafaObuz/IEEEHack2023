import openai, os
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, template_folder='../templates', static_folder="../static")

@app.route("/")
def index():
    output = ""
    return render_template("index.html", output=output)

@app.route("/individual")
def individual():
    return render_template("individual.html")

@app.route("/business")
def business():
    return render_template("business.html")

@app.route("/slider")
def slider():
    return render_template("slider.html")

@app.route("/co2_footprint")
def co2_footprint():
    return render_template("co2_footprint.html")

@app.route("/reduce_co2_emissions", methods=("GET", "POST"))
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

        # Generate response using GPT-3
        response = openai.Completion.create(
             model="text-davinci-003",
             prompt=prompt,
             temperature=0,
             max_tokens=500
        )
        
        output = response.choices[0].text
        
        return render_template("individual.html", output=output)

    return render_template("individual.html")

if __name__ == "__main__":
    app.run(debug=True)
