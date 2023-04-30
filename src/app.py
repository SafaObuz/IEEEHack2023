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

@app.route("/co2_calc", methods=("GET", "POST"))
def co2_calc():
    # Calculate carbon footprint based on user inputs
    carbon_footprint = 0

    if request.method == "POST": 
        form_values = request.form.items()

        response_string = ", ".join([f"{k}: {v}" for k, v in form_values])

        #PRINTS TO CONSOLE, LOOK THERE FOR RESPONSES.
        print(response_string)


        # for x in len(form_values):
        #     for k, v in form_values[x-1]:
        #         print(k,v)  
           # if travel_frequency == "never":
    #     carbon_footprint += 0
    # elif travel_frequency == "rarely":
    #     carbon_footprint += 0.5
    # elif travel_frequency == "sometimes":
    #     carbon_footprint += 1
    # elif travel_frequency == "frequently":
    #     carbon_footprint += 2
    # elif travel_frequency == "very frequently":
    #     carbon_footprint += 3

    # if weekly_driving_distance <= 50:
    #     carbon_footprint += 0
    # elif weekly_driving_distance <= 100:
    #     carbon_footprint += 1
    # elif weekly_driving_distance <= 200:
    #     carbon_footprint += 2
    # else:
    #     carbon_footprint += 3

    # if fuel_efficient_car:
    #     carbon_footprint -= 1

    # if public_transportation_frequency == "never":
    #     carbon_footprint += 1
    # elif public_transportation_frequency == "rarely":
    #     carbon_footprint += 0.5
    # elif public_transportation_frequency == "sometimes":
    #     carbon_footprint += 0
    # elif public_transportation_frequency == "frequently":
    #     carbon_footprint -= 0.5
    # elif public_transportation_frequency == "very frequently":
    #     carbon_footprint -= 1

    # if carpool_or_ridesharing:
    #     carbon_footprint -= 0.5

    # if long_distance_travel_frequency == "never":
    #     carbon_footprint += 0
    # elif long_distance_travel_frequency == "rarely":
    #     carbon_footprint += 1
    # elif long_distance_travel_frequency == "sometimes":
    #     carbon_footprint += 2
    # elif long_distance_travel_frequency == "frequently":
    #     carbon_footprint += 3
    # elif long_distance_travel_frequency == "very frequently":
    #     carbon_footprint += 4

    # # Diet-related emissions
    # if meat_consumption_frequency == "never":
    #     carbon_footprint -= 1
    # elif meat_consumption_frequency == "rarely":
    #     carbon_footprint -= 0.5
    # elif meat_consumption_frequency == "sometimes":
    #     carbon_footprint += 0.5
    # elif meat_consumption_frequency == "frequently":
    #     carbon_footprint += 1
    # elif meat_consumption_frequency == "very frequently":
    #     carbon_footprint += 2

    # if local_food_consumption:
    #     carbon_footprint -= 0.5

    # if processed_food_consumption_frequency == "never":
    #     carbon_footprint -= 0.5
    # elif processed_food_consumption_frequency == "rarely":
    #     carbon_footprint -= 0.25
    # elif processed_food_consumption_frequency == "sometimes":
    #     carbon_footprint += 0.25
    # elif processed_food_consumption_frequency == "frequently":
    #     carbon_footprint += 0.5
    # elif processed_food_consumption_frequency == "very frequently":
    #     carbon_footprint += 1

    # if food_waste_frequency == "never":
    #     carbon_footprint -= 0.5
    # elif food_waste_frequency == "rarely":
    #     carbon_footprint -= 0.25
    # elif food_waste_frequency == "sometimes":
    #     carbon_footprint += 0.25
    # elif food_waste_frequency == "frequently":
    #     carbon_footprint += 0.5
    # elif food_waste_frequency == "very frequently":
    #     carbon_footprint += 1

    # if composting:
    #     carbon_footprint -= 0.5

    # if single_use_plastics_frequency == "never":
    #     carbon_footprint -= 0.5
    # elif single_use_plastics_frequency == "rarely":
    #     carbon_footprint -= 0.25
    # elif single_use_plastics_frequency == "sometimes":
    #     carbon_footprint += 0.25
    # elif single_use_plastics_frequency == "frequently":
    #     carbon_footprint += 0.5
    # elif single_use_plastics_frequency == "very frequently":
    #     carbon_footprint += 1

    # if recycling:
    #     carbon_footprint -= 0.5

    # # Home-related emissions
    # if energy_efficient_lightbulbs == "always":
    #     carbon_footprint -= 0.5
    # elif energy_efficient_lightbulbs == "sometimes":
    #     carbon_footprint += 0.25
    # elif energy_efficient_lightbulbs == "never":
    #     carbon_footprint += 0.5

    # if programmable_thermostat:
    #     carbon_footprint -= 0.5

    # if renewable_energy_sources:
    #     carbon_footprint -= 1

    # if monthly_electricity_use <= 300:
    #     carbon_footprint -= 0.5
    # elif monthly_electricity_use <= 600:
    #     carbon_footprint -= 0.25
    # elif monthly_electricity_use <= 1000:
    #     carbon_footprint += 0.25
    # else:
    #     carbon_footprint += 0

    # if composting:
    #     carbon_footprint -= 0.5

    # if single_use_plastics_frequency == "never":
    #     carbon_footprint -= 0.5
    # elif single_use_plastics_frequency == "rarely":
    #     carbon_footprint -= 0.25
    # elif single_use_plastics_frequency == "sometimes":
    #     carbon_footprint += 0.25
    # elif single_use_plastics_frequency == "frequently":
    #     carbon_footprint += 0.5
    # elif single_use_plastics_frequency == "very frequently":
    #     carbon_footprint += 1

    # if recycling:
    #     carbon_footprint -= 0.25

    # # Home-related emissions
    # if energy_efficient_lightbulbs == "never":
    #     carbon_footprint += 0.5
    # elif energy_efficient_lightbulbs == "rarely":
    #     carbon_footprint += 0.25
    # elif energy_efficient_lightbulbs == "sometimes":
    #     carbon_footprint -= 0.25
    # elif energy_efficient_lightbulbs == "frequently":
    #     carbon_footprint -= 0.5
    # elif energy_efficient_lightbulbs == "always":
    #     carbon_footprint -= 1

    # if programmable_thermostat:
    #     carbon_footprint -= 0.5

    # if renewable_energy_sources:
    #     carbon_footprint -= 1

    # if monthly_electricity_use <= 500:
    #     carbon_footprint += 0
    # elif monthly_electricity_use <= 1000:
    #     carbon_footprint += 0.5
    # elif monthly_electricity_use <= 1500:
    #     carbon_footprint += 1
    # else:
    #     carbon_footprint += 2

    # if monthly_water_use <= 1000:
    #     carbon_footprint += 0
    # elif monthly_water_use <= 2000:
    #     carbon_footprint += 0.5
    # elif monthly_water_use <= 3000:
    #     carbon_footprint += 1
    # else:
    #     carbon_footprint += 2

    # if paper_products_consumption:
    #     carbon_footprint += 0.5

    # if second_hand_clothes:
    #     carbon_footprint -= 0.5

    # Output results


        return render_template("co2_footprint.html", carbon_footprint=carbon_footprint)

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