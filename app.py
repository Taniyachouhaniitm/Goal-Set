from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store the goals
goals = []

@app.route("/", methods=["GET", "POST"])
def index():
    global goals
    if request.method == "POST" and "goal" in request.form:
        # Add the new goal to the list
        goal = request.form.get("goal")
        if goal:
            goals.append(goal)
    return render_template("index.html", goals=goals)

@app.route("/delete", methods=["POST"])
def delete_goal():
    global goals
    # Remove the selected goal
    goal_to_delete = request.form.get("goal")
    if goal_to_delete in goals:
        goals.remove(goal_to_delete)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
