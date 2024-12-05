from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    try:
        matches = re.findall(regex_pattern, test_string)
    except re.error as e:
        matches = [f"Regex error: {e}"]
    return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    if request.method == "POST":
        email = request.form.get("email")
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        is_valid = re.match(email_pattern, email) is not None
        return render_template("validate_email.html", email=email, is_valid=is_valid)
    return render_template("validate_email.html")

if __name__ == "__main__":
    app.run(debug=True)
