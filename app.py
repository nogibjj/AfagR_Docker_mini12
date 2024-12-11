from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load workout data
with open("workout_data.json", "r") as f:
    workouts = json.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the body part from the form
        body_part = request.form.get("part", "").lower()

        # Check if the body part exists in the workouts
        if not body_part:
            return render_template("index.html", error="Please specify a body part.")
        
        if body_part not in workouts:
            return render_template("index.html", error=f"Sorry, we don't have a workout plan for '{body_part}'.")
        
        # Return the exercises for the body part
        exercises = workouts[body_part]
        return render_template("index.html", exercises=exercises, body_part=body_part)

    return render_template("index.html")


@app.route("/workout", methods=["GET"])
def get_workout():
    """
    Get a workout plan for a specific body part.
    Query Parameter: part (e.g., arms, legs, chest)
    """
    body_part = request.args.get("part", "").lower()

    if not body_part:
        return (
            jsonify(
                {
                    "error": "Please specify a body part using the 'part' query parameter."
                }
            ),
            400,
        )

    if body_part not in workouts:
        return (
            jsonify(
                {"error": f"Sorry, we don't have a workout plan for '{body_part}'."}
            ),
            404,
        )

    return jsonify({"body_part": body_part, "exercises": workouts[body_part]}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
