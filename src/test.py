def calculate_carbon_footprint():
    # Get user inputs
    travel_frequency = input("How often do you travel by car, bus, train, or plane? ")
    weekly_driving_distance = float(input("How much do you drive per week (in miles)? "))
    fuel_efficient_car = input("Do you use a fuel-efficient car? (yes/no) ").lower() == "yes"
    public_transportation_frequency = input("How often do you use public transportation? ")
    carpool_or_ridesharing = input("Do you carpool or use ride-sharing services? (yes/no) ").lower() == "yes"
    long_distance_travel_frequency = input("How often do you travel long distances by plane? ")
    meat_consumption_frequency = input("How often do you eat meat? ")
    local_food_consumption = input("Do you eat locally sourced food? (yes/no) ").lower() == "yes"
    processed_food_consumption_frequency = input("How often do you eat processed foods? ")
    food_waste_frequency = input("How often do you waste food? ")
    composting = input("Do you compost? (yes/no) ").lower() == "yes"
    single_use_plastics_frequency = input("How often do you use single-use plastics? ")
    recycling = input("Do you recycle? (yes/no) ").lower() == "yes"
    energy_efficient_lightbulbs = input("How often do you use energy-efficient light bulbs? ")
    programmable_thermostat = input("Do you use a programmable thermostat? (yes/no) ").lower() == "yes"
    renewable_energy_sources = input("Do you use solar panels or other renewable energy sources? (yes/no) ").lower() == "yes"
    monthly_electricity_use = float(input("How much electricity do you use per month (in kWh)? "))
    monthly_water_use = float(input("How much water do you use per month (in gallons)? "))
    paper_products_consumption = input("Do you use paper products? (yes/no) ").lower() == "yes"
    second_hand_clothes = input("Do you buy second-hand or vintage clothes? (yes/no) ").lower() == "yes"

    # Calculate carbon footprint based on user inputs
    carbon_footprint = 0

    # Transportation-related emissions
    if travel_frequency == "never":
        carbon_footprint += 0
    elif travel_frequency == "rarely":
        carbon_footprint += 0.5
    elif travel_frequency == "sometimes":
        carbon_footprint += 1
    elif travel_frequency == "frequently":
        carbon_footprint += 2
    elif travel_frequency == "very frequently":
        carbon_footprint += 3

    if weekly_driving_distance <= 50:
        carbon_footprint += 0
    elif weekly_driving_distance <= 100:
        carbon_footprint += 1
    elif weekly_driving_distance <= 200:
        carbon_footprint += 2
    else:
        carbon_footprint += 3

    if fuel_efficient_car:
        carbon_footprint -= 1

    if public_transportation_frequency == "never":
        carbon_footprint += 1
    elif public_transportation_frequency == "rarely":
        carbon_footprint += 0.5
    elif public_transportation_frequency == "sometimes":
        carbon_footprint += 0
    elif public_transportation_frequency == "frequently":
        carbon_footprint -= 0.5
    elif public_transportation_frequency == "very frequently":
        carbon_footprint -= 1

    if carpool_or_ridesharing:
        carbon_footprint -= 0.5

    if long_distance_travel_frequency == "never":
        carbon_footprint += 0
    elif long_distance_travel_frequency == "rarely":
        carbon_footprint += 1
    elif long_distance_travel_frequency == "sometimes":
        carbon_footprint += 2
    elif long_distance_travel_frequency == "frequently":
        carbon_footprint += 3
    elif long_distance_travel_frequency == "very frequently":
        carbon_footprint += 4

    # Diet-related emissions
    if meat_consumption_frequency == "never":
        carbon_footprint -= 1
    elif meat_consumption_frequency == "rarely":
        carbon_footprint -= 0.5
    elif meat_consumption_frequency == "sometimes":
        carbon_footprint += 0.5
    elif meat_consumption_frequency == "frequently":
        carbon_footprint += 1
    elif meat_consumption_frequency == "very frequently":
        carbon_footprint += 2

    if local_food_consumption:
        carbon_footprint -= 0.5

    if processed_food_consumption_frequency == "never":
        carbon_footprint -= 0.5
    elif processed_food_consumption_frequency == "rarely":
        carbon_footprint -= 0.25
    elif processed_food_consumption_frequency == "sometimes":
        carbon_footprint += 0.25
    elif processed_food_consumption_frequency == "frequently":
        carbon_footprint += 0.5
    elif processed_food_consumption_frequency == "very frequently":
        carbon_footprint += 1

    if food_waste_frequency == "never":
        carbon_footprint -= 0.5
    elif food_waste_frequency == "rarely":
        carbon_footprint -= 0.25
    elif food_waste_frequency == "sometimes":
        carbon_footprint += 0.25
    elif food_waste_frequency == "frequently":
        carbon_footprint += 0.5
    elif food_waste_frequency == "very frequently":
        carbon_footprint += 1

    if composting:
        carbon_footprint -= 0.5

    if single_use_plastics_frequency == "never":
        carbon_footprint -= 0.5
    elif single_use_plastics_frequency == "rarely":
        carbon_footprint -= 0.25
    elif single_use_plastics_frequency == "sometimes":
        carbon_footprint += 0.25
    elif single_use_plastics_frequency == "frequently":
        carbon_footprint += 0.5
    elif single_use_plastics_frequency == "very frequently":
        carbon_footprint += 1

    if recycling:
        carbon_footprint -= 0.5

    # Home-related emissions
    if energy_efficient_lightbulbs == "always":
        carbon_footprint -= 0.5
    elif energy_efficient_lightbulbs == "sometimes":
        carbon_footprint += 0.25
    elif energy_efficient_lightbulbs == "never":
        carbon_footprint += 0.5

    if programmable_thermostat:
        carbon_footprint -= 0.5

    if renewable_energy_sources:
        carbon_footprint -= 1

    if monthly_electricity_use <= 300:
        carbon_footprint -= 0.5
    elif monthly_electricity_use <= 600:
        carbon_footprint -= 0.25
    elif monthly_electricity_use <= 1000:
        carbon_footprint += 0.25
    else:
        carbon_footprint += 0

    if composting:
        carbon_footprint -= 0.5

    if single_use_plastics_frequency == "never":
        carbon_footprint -= 0.5
    elif single_use_plastics_frequency == "rarely":
        carbon_footprint -= 0.25
    elif single_use_plastics_frequency == "sometimes":
        carbon_footprint += 0.25
    elif single_use_plastics_frequency == "frequently":
        carbon_footprint += 0.5
    elif single_use_plastics_frequency == "very frequently":
        carbon_footprint += 1

    if recycling:
        carbon_footprint -= 0.25

    # Home-related emissions
    if energy_efficient_lightbulbs == "never":
        carbon_footprint += 0.5
    elif energy_efficient_lightbulbs == "rarely":
        carbon_footprint += 0.25
    elif energy_efficient_lightbulbs == "sometimes":
        carbon_footprint -= 0.25
    elif energy_efficient_lightbulbs == "frequently":
        carbon_footprint -= 0.5
    elif energy_efficient_lightbulbs == "always":
        carbon_footprint -= 1

    if programmable_thermostat:
        carbon_footprint -= 0.5

    if renewable_energy_sources:
        carbon_footprint -= 1

    if monthly_electricity_use <= 500:
        carbon_footprint += 0
    elif monthly_electricity_use <= 1000:
        carbon_footprint += 0.5
    elif monthly_electricity_use <= 1500:
        carbon_footprint += 1
    else:
        carbon_footprint += 2

    if monthly_water_use <= 1000:
        carbon_footprint += 0
    elif monthly_water_use <= 2000:
        carbon_footprint += 0.5
    elif monthly_water_use <= 3000:
        carbon_footprint += 1
    else:
        carbon_footprint += 2

    if paper_products_consumption:
        carbon_footprint += 0.5

    if second_hand_clothes:
        carbon_footprint -= 0.5

    # Output results
    print("Your carbon footprint is:", carbon_footprint)


calculate_carbon_footprint()