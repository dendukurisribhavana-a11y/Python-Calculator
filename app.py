from flask import Flask, render_template, request
from calculator import calculate
from database import create_database, save_history, get_history

app = Flask(__name__)

create_database()

@app.route("/")
def home():
    history = get_history()
    return render_template(
        "index.html",
        result=None,
        error=None,
        history=history
    )


@app.route("/calculate", methods=["POST"])
def calculate_result():

    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operator = request.form["operator"]

        result = calculate(num1, operator, num2)

        calculation = f"{num1} {operator} {num2}"

        save_history(calculation, result)

        history = get_history()

        return render_template(
            "index.html",
            result=result,
            error=None,
            history=history
        )

    except ZeroDivisionError as e:
        error = str(e)

    except ValueError:
        error = "Please enter valid numbers!"

    history = get_history()

    return render_template(
        "index.html",
        result=None,
        error=error,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)
