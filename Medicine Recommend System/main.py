from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import ast
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector


#LoadDataset-------------
sym_des = pd.read_csv("Datasets/symtoms_df.csv")
precautions = pd.read_csv("Datasets/precautions_df.csv")
workout = pd.read_csv("Datasets/workout_df.csv")
description = pd.read_csv("Datasets/description.csv")
medications = pd.read_csv('Datasets/medications.csv')
diets = pd.read_csv("Datasets/diets.csv")

#LoadModel-----------------
svc = pickle.load(open('Models/svc.pkl','rb'))



app=Flask(__name__)
def helper(dis):
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [item for sublist in [ast.literal_eval(d) if isinstance(d, str) else [d] for d in med.values] for item in sublist]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [item for sublist in [ast.literal_eval(d) if isinstance(d, str) else [d] for d in die.values] for item in sublist]

    wrkout = workout[workout['disease'] == dis] ['workout']


    return desc,pre,med,die,wrkout

symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
diseases_list = {'Fungal infection': 'Fungal infection', 'Allergy': 'Allergy', 'GERD': 'GERD', 'Chronic cholestasis': 'Chronic cholestasis', 'Drug Reaction': 'Drug Reaction', 'Peptic ulcer diseae': 'Peptic ulcer diseae', 'AIDS': 'AIDS', 'Diabetes': 'Diabetes ', 'Gastroenteritis': 'Gastroenteritis', 'Bronchial Asthma': 'Bronchial Asthma', 'Hypertension': 'Hypertension', 'Migraine': 'Migraine', 'Cervical spondylosis': 'Cervical spondylosis', 'Paralysis (brain hemorrhage)': 'Paralysis (brain hemorrhage)', 'Jaundice': 'Jaundice', 'Malaria': 'Malaria', 'Chicken pox': 'Chicken pox', 'Dengue': 'Dengue', 'Typhoid': 'Typhoid', 'hepatitis A': 'hepatitis A', 'Hepatitis B': 'Hepatitis B', 'Hepatitis C': 'Hepatitis C', 'Hepatitis D': 'Hepatitis D', 'Hepatitis E': 'Hepatitis E', 'Alcoholic hepatitis': 'Alcoholic hepatitis', 'Tuberculosis': 'Tuberculosis', 'Common Cold': 'Common Cold', 'Pneumonia': 'Pneumonia', 'Dimorphic hemmorhoids(piles)': 'Dimorphic hemmorhoids(piles)', 'Heart attack': 'Heart attack', 'Varicose veins': 'Varicose veins', 'Hypothyroidism': 'Hypothyroidism', 'Hyperthyroidism': 'Hyperthyroidism', 'Hypoglycemia': 'Hypoglycemia', 'Osteoarthristis': 'Osteoarthristis', 'Arthritis': 'Arthritis', '(vertigo) Paroymsal  Positional Vertigo': '(vertigo) Paroymsal  Positional Vertigo', 'Acne': 'Acne', 'Urinary tract infection': 'Urinary tract infection', 'Psoriasis': 'Psoriasis', 'Impetigo': 'Impetigo'}

# Model Prediction function
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        input_vector[symptoms_dict[item]] = 1
    return diseases_list[svc.predict([input_vector])[0]]

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="userdb"
)
cursor = db.cursor()
@app.route('/signup', methods=['GET', 'POST'])
def signup():
        if request.method == 'POST':
            name = request.form['Name']
            dob = request.form['dob']
            gender = request.form['gender']
            city = request.form['city']
            state = request.form['state']
            mobile = request.form['mobile']
            password = request.form['password']
            confirm_password = request.form['confirm_password']

            if password != confirm_password:
                flash("Passwords do not match.")
                return redirect(url_for('signup'))
            print(f"Signup data: {name}, {dob}, {gender}, {city}, {state}, {mobile}, {password}")
            cursor.execute("SHOW TABLES")
            print(cursor.fetchall())

            try:
                cursor.execute("""
                    INSERT INTO users (name, dob, gender, city, state, mobile, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (name, dob, gender, city, state, mobile, password))
                db.commit()
                flash("Registration successful! Please login.")
                return redirect(url_for('login'))
            except mysql.connector.IntegrityError:
                flash("Mobile number already exists.")
                return redirect(url_for('signup'))

        return render_template('signup.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/Developer')
def developer():
    return render_template("Developer.html")

@app.route('/Blog')
def blog():
    return render_template("Blog.html")

@app.route('/login')
def login():
    return render_template("login.html")

# @app.route("/signup")
# def signup():
#     return render_template("signup.html")

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method=='POST':
        symptoms=request.form.get("symptoms")
        user_symptoms = [s.strip() for s in symptoms.split(',')]
        # Remove any extra characters, if any
        user_symptoms = [symptom.strip("[]' ") for symptom in user_symptoms]
        predicted_disease = get_predicted_value(user_symptoms)

        desc, pre, med, die, wrkout = helper(predicted_disease)

        my_pre = []
        for i in pre[0]:
           my_pre.append(i)

        return render_template('index.html', predicted_disease=predicted_disease, dis_disc=desc, dis_med=med, dis_pre=my_pre, dis_diet=die, dis_wrkout=wrkout)

        # @app.route('/signup', methods=['GET', 'POST'])
    # def signup():
    #     if request.method == 'POST':
    #         name = request.form['Name']
    #         dob = request.form['dob']
    #         gender = request.form['gender']
    #         city = request.form['city']
    #         state = request.form['state']
    #         mobile = request.form['mobile']
    #         password = request.form['password']
    #         confirm_password = request.form['confirm_password']
    #
    #         if password != confirm_password:
    #             flash("Passwords do not match.")
    #             return redirect(url_for('signup'))
    #
    #         try:
    #             cursor.execute("""
    #                 INSERT INTO users (name, dob, gender, city, state, mobile, password)
    #                 VALUES (%s, %s, %s, %s, %s, %s, %s)
    #             """, (name, dob, gender, city, state, mobile, password))
    #             db.commit()
    #             flash("Registration successful! Please login.")
    #             return redirect(url_for('login'))
    #         except mysql.connector.IntegrityError:
    #             flash("Mobile number already exists.")
    #             return redirect(url_for('signup'))
    #
    #     return render_template('signup.html')


#python main

if __name__=="__main__":
    app.run(debug=True)