import pandas as pd
import ast


df = pd.read_csv("jobs.csv")
print(df.head())

ALIAS_SKILL = {
    "SQL": ["sql", "SQL", "structured query language"],
    "R": ["R", "r", "R language"],
    "PYTHON": ["PYTHON", "python", "PY", "python language", "PYTHON language"],
    "scikit-learn": ["sklearn", "scikit-learn"],
}

sums = {key: 0 for key in ALIAS_SKILL.keys()}

pos = input("Look for pos: ")
total_pos = 0

for _, row in df.iterrows():
    if isinstance(row["job_title"], str) and pos in row["job_title"]:
        total_pos += 1

        skills = row["job_skills"]

        # Sometimes parsed as str instead of list
        if isinstance(skills, str):
            try:
                skills = ast.literal_eval(skills)
            except (ValueError, SyntaxError):
                skills = []

        if isinstance(skills, list):
            for skill in skills:
                for key in ALIAS_SKILL.keys():
                    if skill in ALIAS_SKILL[key]:
                        sums[key] = sums.get(key, 0) + 1


print(f"Required by {pos}: ")
[print(f"{key} : {((value / total_pos) * 100):.3f} %") for key, value in sums.items()]
