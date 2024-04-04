from flask import Flask, render_template, url_for, redirect, send_from_directory

app = Flask(__name__, static_url_path='/static')

volunteering = [
    {
        "title": "Immigration Law Center of Minnesota (ILCM)",
        "date": "03/2024 - present",
        "location": "Austin, MN",
        "role":
            [
                "Verified, registered, and assigned clients/patient information to specified case",
                "Closed over 30 cases and verified their credentials to proceed to the next stage",
                "Scanned client documents and organized them to their requested location"
            ]
    }
]

# Define the projects data as a list of dictionaries
projects = [
    {
        "title": "Evaluating Predictive Performances of Obesity Data",
        "date": "02/2024",
        "overview": "This projects covers evaluating the predictive performance of a model for predicting a quantitative response. Some analysis includes PCA, RMSE, ROC curves, and density plots for visualizations. The goal of this project was to familiarize myself with predictive performances and learning how to implement training and holdout data to test the accuracy of the data with a regression model.",
        "tools": ["R", "pROC", "RStudio"],
        "image": "images/predictive_icon.jpg",
        "pdf": "PredictivePerformance.pdf",
    },
    {
        "title": "Emotion Detection",
        "date": "03/2023 – 05/2023",
        "overview": "Developed real-time application using basics machine learning and computer vision, capable of accurately recognizing seven distinct emotions. I got a hands-on experience with computer vision. This was a project i followed along with a tutorial but gained much insights on how machine learning can be implemented into real life.",
        "tools": ["Python", "TensorFlow", "OpenCV"],
        "image": "images/emotion-detection.jpg",
        "link": "https://github.com/dom2polo/emotion-detection.git"
    },
    {
        "title": "Sleep Pattern Analysis",
        "date": "09/2023 – 10/2023",
        "overview": "Leveraged R Markdown in Posit to analyze college students’ sleep patterns. Created insightful visualizations and density plots with ggplot. This was a fun project as it sparked my joy for analyzing data. I learned about the correlation of each variables and presented them in a visual manner.",
        "tools": ["Posit", "R"],
        "image": "images/sleep-analysis.jpg",
        "link": "https://github.com/dom2polo/sleep-pattern-analysis.git"
    },
    {
        "title": "Urban Traffic Analysis",
        "date": "11/2023 – 12/2023",
        "overview": "Worked in teams and executed SQL queries for data retrieval and analysis. Designed a Flask-based client/server architecture for event search and detail retrieval. This was my first experience with Flask with python and it was informing to see the posibilities with this tool. ",
        "tools": ["MSSQL", "Python", "Flask", "Folium"],
        "image": "images/urban-traffic.jpg",
        "github_link": "https://github.com/dom2polo/trasnportation-events.git"
    },
    {
        "title": "Weather App",
        "overview": "A simple web application that allows users to check the weather conditions for a specified location (city or state). The app fetches real-time weather data using the OpenWeatherMap API and displays it in an intuitive user interface.",
        "tools": ["HTML", "CSS", "JavaScript", "API"],
        "image": "images/weather-app.jpg",
        "link": "https://github.com/dom2polo/weather-app.git"
    },
    {
        "title": "To Do List",
        "overview": "A simple web to do list that allow users to read, write, edit lists",
        "tools": ["HTML", "CSS", "JavaScript"],
        "image": "images/to-do.jpg",
        "link": "https://github.com/dom2polo/to-do-list.git"
    }
]

# Brief summary about you
about_me = "I am a K'nyaw (Karen) student that will be graduating with a B.S. in Computer Science from St. Cloud State University in May 2024. I have background as a Software Engineer Intern at Emerson. During my free time, I enjoy building my knowledge in web development in hopes to contribute to K'Nyaw (Karen) community. My career goal is to provide assistance and support to my K'nyaw community in any possible way."

skills = {
    "technical": [
        {"name": "Excel", "level": 40},
        {"name": "Word", "level": 45},
        {"name": "Powerpoint", "level": 40},
        {"name": "Python", "level": 45},
        {"name": "C#", "level": 30},
        {"name": "HTML", "level": 50},
        {"name": "R Markdown", "level": 45},
        {"name": "CSS", "level": 40},
        {"name": "JavaScript", "level": 45},
        {"name": "Github", "level": 50},
        {"name": "MSSQL", "level": 45},
        {"name": "Web-Development", "level": 65},
        {"name": "Debugging", "level": 60},
        {"name": "Data-Oriented", "level": 60},
        {"name": "Database Management", "level": 50}
    ],
    "soft": [
        {"name": "Attention to Detail", "level": 80},
        {"name": "Teamwork", "level": 85},
        {"name": "Time-Management", "level": 90},
        {"name": "Emotional Intelligence", "level": 95},
        {"name": "Adaptability", "level": 90},
        {"name": "Bilingual", "level": 100},
        {"name": "Problem-Solving", "level": 75},
        {"name": "Community Engagement", "level": 75},
        {"name": "Written Communication", "level": 95}
    ]
}


@app.route('/')
def index():
    return render_template('index.html', projects=projects, about_me=about_me, skills=skills, volunteering = volunteering)

@app.route('/project/all')
def project_all():
    return render_template('project_details_all.html', projects=projects)

@app.route('/experience')
def experience():
    return render_template('experience.html', experience=experience)

# Set up route for serving PDF files
@app.route('/static/<path:filename>')
def serve_pdf(filename):
    for project in projects:
        if filename == project['pdf']:
            return send_from_directory('static', filename)
    return "File not found", 404


@app.route('/project/<title>')
def project(title):
    for project in projects:
                return render_template('project_details.html', project=project)
    return "Project not found", 404


if __name__ == '__main__':
    app.run(debug=True)
