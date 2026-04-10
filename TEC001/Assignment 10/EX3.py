from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/prime_number/<int:number>")
def check_prime(number):
    if number < 2:
        result = False
    else:
        result = True
        i = 2
        while i <= number / 2:
            if number % i == 0:
                result = False
                break
            i = i + 1
    return jsonify({
        "Number": number,
        "isPrime": result
    })
app.run()