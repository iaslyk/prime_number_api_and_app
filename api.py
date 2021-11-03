import time
from flask import Flask
from flask_caching import Cache

# Flask_Cache config
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "FileSystemCache",  # Flask-Caching related configs
    'CACHE_DIR': '/tmp'
}

# Initializing Flask API and Flask_Cache
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# Different messages and inputs
welcome_message = "Welcome! Enter the url/prime/int to see your list of prime numbers."
bounds_error = "The number you entered is out of bounds."
cache_cleared = "Cache has been cleared."
cache_time = input("Enter cache time (in seconds): ")
cache_time = int(cache_time)


# Welcome route
@app.route('/')
def index():
    return str(welcome_message)


# Prime number route
@app.route('/prime/<int:number>', methods=['GET'])
@cache.cached(timeout=cache_time)
def display_prime(number):
    
    if number < 1:
        return str(bounds_error)
    # Start timer
    t0 = time.time()
    prime_numbers = [2, 3]
    if number < 3:
        return str(prime_numbers[:number])
    for i in range(2, number):
        next_pn = prime_numbers[-1] + 2
        while any(not(next_pn % pn) for pn in prime_numbers):
            next_pn += 2
        prime_numbers.append(next_pn)        
    # End timer
    t1 = time.time()
    print("Execution time:", t1 - t0)
    return str(prime_numbers)


# Clearing cache
@app.route('/prime/clear', methods=['GET', 'POST'])
def display():
    cache.clear()
    return str(cache_cleared)


if __name__ == "__main__":
    app.run(debug=True)
