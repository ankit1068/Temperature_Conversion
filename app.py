from flask import Flask, render_template, request

app = Flask(__name__)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            temp = float(request.form["temperature"])
            unit = request.form["unit"]

            if unit == "C":
                result = f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F, {celsius_to_kelvin(temp):.2f}K"
            elif unit == "F":
                result = f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C, {fahrenheit_to_kelvin(temp):.2f}K"
            elif unit == "K":
                result = f"{temp}K = {kelvin_to_celsius(temp):.2f}°C, {kelvin_to_fahrenheit(temp):.2f}°F"
        except ValueError:
            error = "Invalid input. Please enter a valid temperature."
        except KeyError:
            error = "Invalid form submission. Please try again."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)