import time
from flask import Flask


app = Flask(__name__)


welcome_message = "Welcome! Enter the url/prime/int to see your list of prime numbers."
bounds_error = "The number you entered is out of bounds."

@app.route('/')
def index():
    return str(welcome_message)


@app.route('/prime/<int:number>', methods=['GET'])
def display_prime(number):
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # not a prime, else true.
    if number <= 1:
        return str(bounds_error)

    prime = [True] * int(number + 1)
    prime_index = 2
    t0 = time.time()
    while prime_index * prime_index <= number + 1:
        # If prime[primeIndex] is not changed, then it is
        # a prime
        if prime[prime_index]:
            # Update all multiples of prime index.
            for i in range(prime_index * prime_index, number + 1, prime_index):
                prime[i] = False
        prime_index += 1
    # add all prime numbers to the list to be printed
    prime_list = []
    for iterator in range(2, number + 1):
        if prime[iterator]:
            prime_list.append(str(iterator))
    t1 = time.time()
    print("Execution time:", t1 - t0)
    return str(prime_list)


if __name__ ==  "__main__":
    app.run(debug=True)