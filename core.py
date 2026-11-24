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




def select_specific():
    pos = input("Look for pos: ")
    total_pos = 0
    sums = {key: 0 for key in ALIAS_SKILL.keys()}
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


def check_all():
    total_pos = dict()

    skills_per_pos = dict()
    for _, row in df.iterrows():
        if isinstance(row["job_title_short"], str):
            pos = row["job_title_short"]
            total_pos[pos] = total_pos.get(pos, 0) + 1
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
                            if not pos in skills_per_pos.keys():
                                skills_per_pos[pos] = dict()
                            skills_per_pos[pos][key] = skills_per_pos[pos].get(key, 0) + 1

    for pos in total_pos.keys():
        print(f"Required by {pos}: ")
        [print(f"{key} : {((value / total_pos[pos]) * 100):.3f} %") for key, value in skills_per_pos[pos].items()]

while True:
    inp = int(input("Check specific(1) or all(2): "))
    if inp == 1:
        select_specific()
        break
    elif inp == 2:
        check_all()
        break
    else:
        print("Bro, 1 or 2 plz")