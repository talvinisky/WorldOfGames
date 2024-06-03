from flask import Flask, render_template
from pathlib import Path
from Utils import BAD_RETURN_CODE

app = Flask(__name__)


def process_scores(lines):
    name = lines[0].strip()
    scores = [int(score.strip()) for score in lines[1:] if
              score.strip().isdigit()]
    total_score = sum(scores)
    return name, total_score


@app.route("/")
def score_server():
    try:
        # Open the Scores.txt file for reading
        with open(Path("Scores.txt"), "r") as score_file:
            lines = score_file.readlines()

            if lines:
                name, total_score = process_scores(lines)

                # Check if total_score has a value (i.e., it is not None)
                if total_score is not None:
                    rendered_template = render_template('Scores.html', NAME=name.capitalize(), SCORE=total_score)
                else:
                    rendered_template = render_template('Error.html', ERROR=BAD_RETURN_CODE)



                return rendered_template
            else:
                return render_template('Error.html', ERROR=BAD_RETURN_CODE)
    except FileNotFoundError:
        return render_template('Error.html', ERROR=BAD_RETURN_CODE)
    except Exception as e:
        # Handle other exceptions
        return render_template('Error.html', ERROR=str(e))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8777)  # Changed the port name and make the server accessible from anywhere
