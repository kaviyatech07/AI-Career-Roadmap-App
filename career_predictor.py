def predict_career(python, machine_learning, sql, problem_solving, communication):

    scores = {
        "AI Engineer": (
            python * 0.30 +
            machine_learning * 0.35 +
            problem_solving * 0.20 +
            communication * 0.15
        ),

        "Data Scientist": (
            python * 0.25 +
            machine_learning * 0.30 +
            sql * 0.20 +
            problem_solving * 0.15 +
            communication * 0.10
        ),

        "Data Analyst": (
            python * 0.20 +
            sql * 0.40 +
            problem_solving * 0.20 +
            communication * 0.20
        ),

        "Software Developer": (
            python * 0.35 +
            problem_solving * 0.35 +
            sql * 0.15 +
            communication * 0.15
        )
    }

    recommended_career = max(scores, key=scores.get)

    return recommended_career, scores
