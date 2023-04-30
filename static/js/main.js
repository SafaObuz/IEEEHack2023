// Variables for Car/Plane/Train Travel
const carPlaneTrainTravelRange = document.getElementById('car-plane-train-travel');
const selectedOption = document.getElementById('selected-option');
let carPlaneTrainTravelValue = 0;

carPlaneTrainTravelRange.addEventListener('input', (e) => {
  const value = e.target.value;
  carPlaneTrainTravelValue = parseInt(value); // Convert string value to integer
  switch (value) {
    case '1':
      selectedOption.innerText = 'Never';
      break;
    case '2':
      selectedOption.innerText = 'Rarely';
      break;
    case '3':
      selectedOption.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption.innerText = 'Frequently';
      break;
    case '5':
      selectedOption.innerText = 'Very frequently';
      break;
    default:
      selectedOption.innerText = '';
      break;
  }
  // Do calculations with carPlaneTrainTravelValue variable here
});

// Variables for Public Transportation
const publicTransportationRange = document.getElementById('public-transportation');
const selectedOption2 = document.getElementById('selected-option-2');
let publicTransportationValue = 0;

publicTransportationRange.addEventListener('input', (e) => {
  const value = e.target.value;
  publicTransportationValue = parseInt(value); // Convert string value to integer
  switch (value) {
    case '1':
      selectedOption2.innerText = 'Never';
      break;
    case '2':
      selectedOption2.innerText = 'Rarely';
      break;
    case '3':
      selectedOption2.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption2.innerText = 'Frequently';
      break;
    case '5':
      selectedOption2.innerText = 'Very frequently';
      break;
    default:
      selectedOption2.innerText = '';
      break;

  }
});

// Variables for Fuel-Efficient Car
const fuelEfficientCarYes = document.getElementById('fuel-efficient-car-yes');
const fuelEfficientCarNo = document.getElementById('fuel-efficient-car-no');
let fuelEfficientCarValue = '';

fuelEfficientCarYes.addEventListener('change', (e) => {
  fuelEfficientCarValue = e.target.value;
});

fuelEfficientCarNo.addEventListener('change', (e) => {
  fuelEfficientCarValue = e.target.value;
});

// Variables for Ride Sharing
const rideSharingYes = document.getElementById('ride-sharing-yes');
const rideSharingNo = document.getElementById('ride-sharing-no');
let rideSharingValue = '';

rideSharingYes.addEventListener('change', (e) => {
  rideSharingValue = e.target.value;
});

rideSharingNo.addEventListener('change', (e) => {
  rideSharingValue = e.target.value;
});

// Variables for Weekly Distance and Submit Button
const weeklyDistance = document.getElementById('weekly-distance');
const submitButton = document.getElementById('submit-button');

submitButton.addEventListener('click', (e) => {
  e.preventDefault();
  const carPlaneTrainTravelValue = carPlaneTrainTravelRange.value;
  const weeklyDistanceValue = weeklyDistance.value;
  const publicTransportationValue = publicTransportationRange.value;

  // Perform calculations and show results
});


const planeTravel = document.getElementById('plane-travel');
const selectedOption3 = document.getElementById('selected-option3');

planeTravel.addEventListener('input', (e) => {
  const value = e.target.value;
  switch (value) {
    case '1':
      selectedOption3.innerText = 'Never';
      break;
    case '2':
      selectedOption3.innerText = 'Rarely';
      break;
    case '3':
      selectedOption3.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption3.innerText = 'Frequently';
      break;
    case '5':
      selectedOption3.innerText = 'Very frequently';
      break;
    default:
      selectedOption3.innerText = '';
      break;
  }
});

const meat = document.getElementById('meat-often');
const selectedOption4 = document.getElementById('selected-option4');
let meatFrequency; // declare global variable

meat.addEventListener('input', (e) => {
  meatFrequency = e.target.value;
  switch (meatFrequency) {
    case '1':
      selectedOption4.innerText = 'Never';
      break;
    case '2':
      selectedOption4.innerText = 'Rarely';
      break;
    case '3':
      selectedOption4.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption4.innerText = 'Frequently';
      break;
    case '5':
      selectedOption4.innerText = 'Very frequently';
      break;
    default:
      selectedOption4.innerText = '';
      break;
  }
});

const processedFoodsRange = document.getElementById('processed-foods');
const selectedOption5 = document.getElementById('selected-option5');
let processedFoodsValue; // declare global variable

processedFoodsRange.addEventListener('input', (e) => {
  processedFoodsValue = e.target.value; // assign value to global variable
  switch (processedFoodsValue) {
    case '1':
      selectedOption5.innerText = 'Never';
      break;
    case '2':
      selectedOption5.innerText = 'Rarely';
      break;
    case '3':
      selectedOption5.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption5.innerText = 'Frequently';
      break;
    case '5':
      selectedOption5.innerText = 'Very frequently';
      break;
    default:
      selectedOption5.innerText = '';
      break;
  }
});

const singleUsePlasticsRange = document.getElementById('single-use-plastics');
const selectedOption6 = document.getElementById('selected-option6');
let singleUsePlasticsValue = 1; // Initialize with default value of 1

singleUsePlasticsRange.addEventListener('input', (e) => {
  singleUsePlasticsValue = parseInt(e.target.value);
  switch (singleUsePlasticsValue) {
    case 1:
      selectedOption6.innerText = 'Never';
      break;
    case 2:
      selectedOption6.innerText = 'Rarely';
      break;
    case 3:
      selectedOption6.innerText = 'Sometimes';
      break;
    case 4:
      selectedOption6.innerText = 'Frequently';
      break;
    case 5:
      selectedOption6.innerText = 'Very frequently';
      break;
    default:
      selectedOption6.innerText = '';
      break;
  }
});
const lightBulbs = document.getElementById('light-bulbs');
const selectedOption7 = document.getElementById('selected-option7');
lightBulbs.addEventListener('input', (e) => {
  const value = e.target.value;
  switch (value) {
    case '1':
      selectedOption7.innerText = 'Never';
      break;
    case '2':
      selectedOption7.innerText = 'Rarely';
      break;
    case '3':
      selectedOption7.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption7.innerText = 'Frequently';
      break;
    case '5':
      selectedOption7.innerText = 'Very frequently';
      break;
    default:
      selectedOption7.innerText = '';
      break;
  }
  // Store the value in a variable for future calculations
  const lightBulbsValue = parseInt(value);
});

let foodWasteValue; // declare global variable

const foodWasteRange = document.getElementById('food-waste');
const selectedOption8 = document.getElementById('selected-option8');

foodWasteRange.addEventListener('input', (e) => {
  foodWasteValue = e.target.value; // assign value to global variable
  switch (foodWasteValue) {
    case '1':
      selectedOption8.innerText = 'Never';
      break;
    case '2':
      selectedOption8.innerText = 'Rarely';
      break;
    case '3':
      selectedOption8.innerText = 'Sometimes';
      break;
    case '4':
      selectedOption8.innerText = 'Frequently';
      break;
    case '5':
      selectedOption8.innerText = 'Very frequently';
      break;
    default:
      selectedOption8.innerText = '';
      break;
  }
});
function calculateCarbonFootprint(food_waste_frequency, composting, single_use_plastics_frequency, recycling, energy_efficient_lightbulbs, programmable_thermostat, renewable_energy_sources, monthly_electricity_use, monthly_water_use, paper_products_consumption, second_hand_clothes) {
let carbon_footprint = 0;

// Transportation-related emissions
if (travel_frequency === "never") {
carbon_footprint += 0;
} else if (travel_frequency === "rarely") {
carbon_footprint += 0.5;
} else if (travel_frequency === "sometimes") {
carbon_footprint += 1;
} else if (travel_frequency === "frequently") {
carbon_footprint += 2;
} else if (travel_frequency === "very frequently") {
carbon_footprint += 3;
}

if (weekly_driving_distance <= 50) {
carbon_footprint += 0;
} else if (weekly_driving_distance <= 100) {
carbon_footprint += 1;
} else if (weekly_driving_distance <= 200) {
carbon_footprint += 2;
} else {
carbon_footprint += 3;
}

if (fuel_efficient_car) {
carbon_footprint -= 1;
}

if (public_transportation_frequency === "never") {
carbon_footprint += 1;
} else if (public_transportation_frequency === "rarely") {
carbon_footprint += 0.5;
} else if (public_transportation_frequency === "sometimes") {
carbon_footprint += 0;
} else if (public_transportation_frequency === "frequently") {
carbon_footprint -= 0.5;
} else if (public_transportation_frequency === "very frequently") {
carbon_footprint -= 1;
}

if (carpool_or_ridesharing) {
carbon_footprint -= 0.5;
}

if (long_distance_travel_frequency === "never") {
carbon_footprint += 0;
} else if (long_distance_travel_frequency === "rarely") {
carbon_footprint += 1;
} else if (long_distance_travel_frequency === "sometimes") {
carbon_footprint += 2;
} else if (long_distance_travel_frequency === "frequently") {
carbon_footprint += 3;
} else if (long_distance_travel_frequency === "very frequently") {
carbon_footprint += 4;
}

if (meat_consumption_frequency === "never") {
  carbon_footprint -= 1;
} else if (meat_consumption_frequency === "rarely") {
  carbon_footprint -= 0.5;
} else if (meat_consumption_frequency === "sometimes") {
  carbon_footprint += 0.5;
} else if (meat_consumption_frequency === "frequently") {
  carbon_footprint += 1;
} else if (meat_consumption_frequency === "very frequently") {
  carbon_footprint += 2;
}

if (local_food_consumption) {
  carbon_footprint -= 0.5;
}

if (processed_food_consumption_frequency === "never") {
  carbon_footprint -= 0.5;
} else if (processed_food_consumption_frequency === "rarely") {
  carbon_footprint -= 0.25;
} else if (processed_food_consumption_frequency === "sometimes") {
  carbon_footprint += 0.25;
} else if (processed_food_consumption_frequency === "frequently") {
  carbon_footprint += 0.5;
} else if (processed_food_consumption_frequency === "very frequently") {
  carbon_footprint += 1;
}

if (food_waste_frequency === "never") {
  carbon_footprint -= 0.5;
} else if (food_waste_frequency === "rarely") {
  carbon_footprint -= 0.25;
} else if (food_waste_frequency === "sometimes") {
  carbon_footprint += 0.25;
} else if (food_waste_frequency === "frequently") {
  carbon_footprint += 0.5;
} else if (food_waste_frequency === "very frequently") {
  carbon_footprint += 1;
}

if (composting) {
  carbon_footprint -= 0.5;
}

if (single_use_plastics_frequency === "never") {
  carbon_footprint -= 0.5;
} else if (single_use_plastics_frequency === "rarely") {
  carbon_footprint -= 0.25;
} else if (single_use_plastics_frequency === "sometimes") {
  carbon_footprint += 0.25;
} else if (single_use_plastics_frequency === "frequently") {
  carbon_footprint += 0.5;
} else if (single_use_plastics_frequency === "very frequently") {
  carbon_footprint += 1;
}

if (recycling) {
  carbon_footprint -= 0.5;
}

if (energy_efficient_lightbulbs === "never") {
  carbon_footprint += 0.5;
} else if (energy_efficient_lightbulbs === "rarely") {
  carbon_footprint += 0.25;
} else if (energy_efficient_lightbulbs === "sometimes") {
  carbon_footprint -= 0.25;
} else if (energy_efficient_lightbulbs === "frequently") {
  carbon_footprint -= 0.5;
} else if (energy_efficient_lightbulbs === "always") {
  carbon_footprint -= 1;
}

if (programmable_thermostat) {
  carbon_footprint -= 0.5;
}

if (renewable_energy_sources) {
  carbon_footprint -= 1;
}

if (monthly_electricity_use <= 500) {
  carbon_footprint += 0;
} else if (monthly_electricity_use <= 1000) {
  carbon_footprint += 0.5;
} else if (monthly_electricity_use <= 1500) {
  carbon_footprint += 1;
} else {
  carbon_footprint += 2;
}

if (monthly_water_use <= 1000) {
  carbon_footprint += 0;
} else if (monthly_water_use <= 2000) {
  carbon_footprint += 0.5;
} else if (monthly_water_use <= 3000) {
  carbon_footprint += 1;
} else {
  carbon_footprint += 2;
}

if (paper_products_consumption) {
  carbon_footprint += 0.5;
}

if (second_hand_clothes) {
  carbon_footprint -= 0.5;
}

// Output results
console.log("Your carbon footprint is:", carbon_footprint);
return carbon_footprint;
}