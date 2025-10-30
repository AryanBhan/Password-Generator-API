# Password Generator API

Welcome to the Password Generator API! This API allows you to generate strong passwords with specified lengths using Python Flask and jsonify.

This is my first contribution to open source.

## API Endpoint

The API endpoint for generating passwords is:

https://password-generator-api-yg7e.onrender.com/generate?n=[Enter_desired_length]


Replace `[Enter_desired_length]` with the desired length of the password. For example, to generate a password with a length of 12 characters, you can use:

(https://password-generator-api-yg7e.onrender.com/generate?n=12)


## Usage

Simply make a GET request to the API endpoint with the desired length parameter (`n`). The API will return a JSON response containing the generated password.

## Example

Here's an example using the API endpoint to generate a password with a length of 16 characters:

https://password-generator-api-yg7e.onrender.com/generate?n=16



## Response:

```json
{
  "password": "sT7g#9u!Pm$wRfQ3"
}
```
## Code:
```ruby
from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

def generate_password(n=12):
    # Define character sets for each requirement
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special_chars = string.punctuation

    # Choose one character from each set
    password = random.choice(uppercase) + \
               random.choice(lowercase) + \
               random.choice(numbers) + \
               random.choice(special_chars)

    # Fill the rest of the password length with random characters
    remaining_length = n - len(password)
    password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length))

    # Shuffle the characters to make the password more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

@app.route('/generate', methods=['GET'])
def get_password():
    # Get the value of 'n' from the query parameters
    n = request.args.get('n', default=12, type=int)
    
    # Generate password with specified length 'n'
    password = generate_password(n)
    
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)

```

## How to Run
To run the API locally, execute the Python script provided above. Ensure you have Flask installed (pip install flask). 
Create a app.py file > Paste the Code and Run the file
The API will be accessible at http://127.0.0.1:5000/generate?n=12.






