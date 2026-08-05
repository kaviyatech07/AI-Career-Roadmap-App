roadmaps = {

    "AI Engineer": [
        "Learn Python",
        "Learn Data Structures and Algorithms",
        "Learn Machine Learning",
        "Learn Deep Learning",
        "Learn Generative AI",
        "Build AI Projects",
        "Learn Git and GitHub",
        "Prepare for AI Engineer Interviews"
    ],

    "Data Scientist": [
        "Learn Python",
        "Learn Statistics and Mathematics",
        "Learn SQL",
        "Learn Data Analysis",
        "Learn Machine Learning",
        "Learn Data Visualization",
        "Build Data Science Projects",
        "Prepare for Data Scientist Interviews"
    ],

    "Data Analyst": [
        "Learn Excel",
        "Learn SQL",
        "Learn Python",
        "Learn Data Visualization",
        "Learn Power BI",
        "Build Dashboard Projects",
        "Practice Data Analysis",
        "Prepare for Data Analyst Interviews"
    ],

    "Software Developer": [
        "Learn Python",
        "Learn Data Structures and Algorithms",
        "Learn Object-Oriented Programming",
        "Learn SQL",
        "Learn Web Development",
        "Build Software Projects",
        "Learn Git and GitHub",
        "Prepare for Software Developer Interviews"
    ],

    "Machine Learning Engineer": [
        "Learn Python",
        "Learn Mathematics and Statistics",
        "Learn Machine Learning",
        "Learn Deep Learning",
        "Learn TensorFlow or PyTorch",
        "Build ML Projects",
        "Learn MLOps",
        "Prepare for ML Engineer Interviews"
    ]
}


def get_roadmap(career):
    return roadmaps.get(career, [])
