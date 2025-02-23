from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Device CO₂ Emission Data (kg CO₂)
DEVICE_EMISSIONS = {
    "Refrigerator": 800,
    "Air Conditioner": 1200,
    "Washing Machine": 600,
    "TV": 350,
    "Microwave Oven": 250,
    
    "Laptop": 200,
    "Smartphone": 55,
    "Tablet": 80,
    "PC": 300,
    "Monitor": 150,

    "Hard Drive": 50,
    "SSD": 40,
    "Pendrive": 10,
    "Earphones": 20,
    "Smartwatch": 30,
    "Bluetooth Speaker": 60
}

# Refurbished Device Marketplaces
REFURBISHED_MARKETPLACES = {
    "Refrigerator": ["Samsung Smart Fridge (Refurbished) - $700", "LG InstaView Fridge (Used) - $650"],
    "Air Conditioner": ["LG Dual Inverter AC (Refurbished) - $600", "Daikin Split AC (Used) - $500"],
    "Washing Machine": ["Whirlpool Front Load (Refurbished) - $550", "Bosch Automatic (Used) - $500"],
    "TV": ["Sony Bravia 4K (Refurbished) - $450", "Samsung QLED (Used) - $400"],
    "Microwave Oven": ["Panasonic Inverter Oven (Refurbished) - $250", "LG Solo Microwave (Used) - $200"],
    
    "Laptop": ["MacBook Pro 2020 (Refurbished) - $900", "Dell XPS 15 (Used) - $700"],
    "Smartphone": ["iPhone 12 Pro (Refurbished) - $550", "Samsung S21 Ultra (Used) - $450"],
    "Tablet": ["iPad Pro 11” (Refurbished) - $600", "Samsung Galaxy Tab S7 (Used) - $400"],
    "PC": ["HP EliteDesk (Refurbished) - $500", "Lenovo ThinkCentre (Used) - $450"],
    "Monitor": ["Dell UltraSharp 27” (Refurbished) - $250", "LG 4K Monitor (Used) - $200"],

    "Hard Drive": ["WD 1TB External HDD (Refurbished) - $80", "Seagate 2TB HDD (Used) - $70"],
    "SSD": ["Samsung 970 EVO 500GB (Used) - $100", "Crucial MX500 1TB (Refurbished) - $120"],
    "Pendrive": ["SanDisk 128GB (Refurbished) - $30", "Kingston 256GB (Used) - $40"],
    "Earphones": ["Sony WF-1000XM4 (Refurbished) - $120", "AirPods Pro (Used) - $150"],
    "Smartwatch": ["Apple Watch Series 6 (Refurbished) - $250", "Samsung Galaxy Watch 4 (Used) - $220"],
    "Bluetooth Speaker": ["JBL Charge 5 (Refurbished) - $150", "Bose SoundLink Mini (Used) - $130"]
}

# AI-Based Energy-Saving Tips
# ENERGY_SAVING_TIPS = {
#     "Laptop": "Enable power-saving mode and reduce screen brightness to cut energy usage by 20%.",
#     "Smartphone": "Lower screen brightness and enable battery saver mode to reduce power consumption.",
#     "Refrigerator": "Keep the door closed as much as possible to reduce cooling energy.",
#     "Air Conditioner": "Set the temperature to 24°C instead of 18°C to reduce power usage by 30%.",
#     "PC": "Turn off your PC when not in use and use sleep mode to save energy.",
#     "TV": "Reduce screen brightness and turn off when not watching to save electricity.",
#     "Microwave Oven": "Use microwave instead of stove for reheating to save 50% energy."
# }
ENERGY_SAVING_TIPS = {
    # Large Electronics
    "Refrigerator": "Keep the door closed as much as possible. Clean condenser coils regularly for efficiency.",
    "Air Conditioner": "Set the temperature to 24°C instead of 18°C to reduce power usage by 30%. Clean filters monthly.",
    "Washing Machine": "Wash clothes in cold water. Run full loads to save energy and water.",
    "Dishwasher": "Use the eco-mode setting. Only run full loads and let dishes air dry instead of using the heat cycle.",
    "Oven": "Avoid opening the oven frequently while cooking. Use convection mode to reduce cooking time and energy.",
    "Microwave Oven": "Use the microwave instead of the stove for reheating to save 50 percent energy. Avoid running it empty.",
    "Induction Cooktop": "Use flat-bottomed cookware for maximum efficiency. Turn off early and use residual heat.",
    
    # Medium Electronics
    "TV": "Reduce screen brightness and enable eco-mode. Turn it off completely when not in use.",
    "PC": "Use sleep mode when idle. Turn off unused peripherals like printers and speakers.",
    "Monitor": "Enable auto-sleep mode. Reduce brightness to extend lifespan and save power.",
    "Laptop": "Enable power-saving mode and reduce screen brightness to cut energy usage by 20%. Unplug once fully charged.",
    "Tablet": "Reduce screen brightness and close unused background apps to save power.",
    "Printer": "Print in draft mode when possible. Use both sides of the paper to reduce waste.",
    "Gaming Console": "Enable energy-saving mode. Turn off completely instead of using standby mode.",

    # Small Electronics
    "Smartphone": "Lower screen brightness, close background apps, and enable battery saver mode.",
    "Smartwatch": "Disable always-on display. Reduce screen brightness and notifications.",
    "Bluetooth Speaker": "Turn off when not in use. Keep the battery charged between 20-80% for longevity.",
    "Wi-Fi Router": "Use a smart plug to schedule power off at night. Position it for optimal coverage to avoid signal boosting.",
    "Set-Top Box": "Turn off when not in use. Use automatic power-down settings if available.",
    
    # Micro Electronics
    "Hard Drive": "Use an external drive only when needed. Disconnect after use to save power.",
    "SSD": "Enable TRIM support to improve efficiency and extend lifespan.",
    "Pendrive": "Safely eject after use to prevent unnecessary power drain.",
    "Earphones & Headphones": "Turn off Bluetooth when not in use. Charge only when necessary.",
    "Smart Light Bulbs": "Use motion sensors or timers to turn off automatically when not needed.",
    "Power Bank": "Avoid leaving it plugged in for too long after full charge. Store in a cool place.",
    "Electric Toothbrush": "Charge only when necessary. Avoid leaving on the charger indefinitely.",
    "Hair Dryer": "Use the lowest effective heat setting. Air-dry hair when possible."
}


@app.route('/')
def home():
    return "E-Waste Carbon Footprint API is running!"

# CO₂ Emission Calculation API
@app.route('/calculate', methods=['POST'])
def calculate_emissions():
    data = request.get_json()
    device = data.get("device")
    age = int(data.get("age", 1))  # Default to 1 if no age is provided

    # if not device or device not in DEVICE_EMISSIONS:
    #     return jsonify({"error": "Invalid device"}), 400

    # base_emission = DEVICE_EMISSIONS[device]
    # total_emissions = base_emission * age  # Multiply by age

    # return jsonify({"device": device, "age": age, "total_emissions": total_emissions})
    if not device or device not in DEVICE_EMISSIONS:
        return jsonify({"error": "Invalid device"}), 400

    base_emission = DEVICE_EMISSIONS[device]
    total_emissions = base_emission * age 

    return jsonify({"device": device, "age": age, "total_emissions": total_emissions})

# Energy-Saving Tips API
@app.route('/energy-tips', methods=['GET'])
def get_energy_tips():
    device = request.args.get('device')

    if not device or device not in ENERGY_SAVING_TIPS:
        return jsonify({"tip": "No specific energy-saving tip available."})
    
    return jsonify({"tip": ENERGY_SAVING_TIPS[device]})

# Refurbished Device Suggestions API
@app.route('/refurbished', methods=['GET'])
def get_refurbished_devices():
    device = request.args.get('device')

    if not device or device not in REFURBISHED_MARKETPLACES:
        return jsonify({"error": "No refurbished options found."}), 404
    
    return jsonify(REFURBISHED_MARKETPLACES[device])

if __name__ == '__main__':
    app.run(debug=True)