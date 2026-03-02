def match_skills(user_skills, required_skills):

    matched = list(set(user_skills) & set(required_skills))
    missing = list(set(required_skills) - set(user_skills))

    score = len(matched) / len(required_skills) * 100

    return score, matched, missing