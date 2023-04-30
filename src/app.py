import openai, os
from flask import Flask, redirect, render_template, request, url_for, jsonify
from dotenv import load_dotenv
import threading
import time

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, template_folder='../templates', static_folder="../static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

output = ""

def delete_output():
    global output
    time.sleep(30)
    output = ""

@app.route("/")
def index():
    global output
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
    global output
    if request.method == "POST": 
        form_values = request.form.items()
        response_string = ", ".join([f"{k}: {v}" for k, v in form_values])

        print(response_string)

        prompt = f'''
        {response_string}
      The user will give you inputs, about his region, his lifestyle, his habits and some other common informations. Based on that tell him how his activities are affecting
        the environment. If his activities are not eco-friendly, tell him what harms are his activities causing the environment and what steps he should take to 
        reduce his carbon footprint and reduce environmental pollution
        . If his activities are eco-friendly, tell him what good he is doing to the environment and what more he can do to reduce his carbon footprint.
        Also tell him how his region is currently in risk due to climate change and tell him what future events might event due to climate change in his region.
        '''

        # Generate response using GPT-3
        response = openai.Completion.create(
             model="text-davinci-003",
             prompt=prompt,
             temperature=0,
             max_tokens=800
        )
        
        output = response.choices[0].text
        threading.Thread(target=delete_output).start()
        
        return render_template("individual.html", output=output)

    return render_template("individual.html")

if __name__ == "__main__":
    app.run(debug=True)