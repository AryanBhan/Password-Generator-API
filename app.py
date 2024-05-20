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
