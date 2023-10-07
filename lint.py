"""file linter"""
#lint.py

import sys

from pylint import lint

THRESHOLD = 9

run = lint.Run(["app.py"], exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:

    print("Linter failed: Score < threshold value IN: app.py. Score is: " + score)


run = lint.Run(["model.py"], exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:

    print("Linter failed: Score < threshold value IN: model.py. Score is: " + score)

run = lint.Run(["test_FlaskTests.py"], exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:

    print("Linter failed: Score < threshold value IN: test_FlaskTests.py. Score is: " + score)

if score < THRESHOLD:
    sys.exit(1)

sys.exit(0)
