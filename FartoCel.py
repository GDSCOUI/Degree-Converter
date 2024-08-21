# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Input from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)

# Display the result
print(f"The temperature in Celsius is: {celsius:.2f}°C")

# Python code to write a CSS file
css_code = """
body {
    font-family: Arial, sans-serif;
    background-color: #f0f8ff;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    padding: 20px;
    border: 2px solid #000;
    border-radius: 10px;
    background-color: #fff;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
    color: #333;
}

p {
    color: #666;
    font-size: 18px;
}
"""

# Write the CSS code to a file
with open("style.css", "w") as file:
    file.write(css_code)

print("CSS file 'style.css' created successfully!")
