import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load saved objects
saved = pickle.load(
open(
"model.pkl",
"rb"
)
)

model = saved["model"]
scaler = saved["scaler"]
ohe = saved["ohe"]
oe = saved["oe"]

st.title(
"Student Placement Predictor"
)

# ---------- INPUT ----------

branch = st.selectbox(
"Branch",
["CSE", "ECE", "EE", "ME", "CE" , "IT" , "Chemical"]
)

college_tier = st.selectbox(
"College Tier",
["Tier-1","Tier-2","Tier-3"]
)

cgpa = st.number_input(
"CGPA",
0.0,
10.0
)

backlogs = st.number_input(
"Backlogs",
0
)

coding_skills = st.slider(
"Coding Skills",
0,
10
)

dsa_score = st.slider(
"DSA Score",
0,
100
)

aptitude_score = st.slider(
"Aptitude Score",
0,
100
)

communication_skills = st.slider(
"Communication",
0,
10
)

ml_knowledge = st.slider(
"ML Knowledge",
0,
10
)

system_design = st.slider(
"System Design",
0,
10
)

internships = st.number_input(
"Internships",
0
)

projects_count = st.number_input(
"Projects",
0
)

certifications = st.number_input(
"Certifications",
0
)

hackathons = st.number_input(
"Hackathons",
0
)

open_source_contributions = st.number_input(
"Open Source",
0
)

extracurriculars = st.slider(
"Extracurriculars",
0,
10
)

if st.button("Predict"):

    df = pd.DataFrame([[
        branch,
        college_tier,
        cgpa,
        backlogs,
        coding_skills,
        dsa_score,
        aptitude_score,
        communication_skills,
        ml_knowledge,
        system_design,
        internships,
        projects_count,
        certifications,
        hackathons,
        open_source_contributions,
        extracurriculars
    ]],

    columns=[
        "branch",
        "college_tier",
        "cgpa",
        "backlogs",
        "coding_skills",
        "dsa_score",
        "aptitude_score",
        "communication_skills",
        "ml_knowledge",
        "system_design",
        "internships",
        "projects_count",
        "certifications",
        "hackathons",
        "open_source_contributions",
        "extracurriculars"
    ])

    # Scale numeric
    num_cols = [
        "cgpa",
        "backlogs",
        "coding_skills",
        "dsa_score",
        "aptitude_score",
        "communication_skills",
        "ml_knowledge",
        "system_design",
        "internships",
        "projects_count",
        "certifications",
        "hackathons",
        "open_source_contributions",
        "extracurriculars"
    ]

    df[num_cols] = scaler.transform(
        df[num_cols]
    )

    # Encode
    branch_enc = ohe.transform(
        df[["branch"]]
    )

    tier_enc = oe.transform(
        df[["college_tier"]]
    )

    remaining = df.drop(
        [
        "branch",
        "college_tier"
        ],
        axis=1
    )

    final = np.concatenate(
        [
        branch_enc,
        tier_enc,
        remaining
        ],
        axis=1
    )

    pred = model.predict(
        final
    )[0]

    if pred == 1:
        st.success(
        "PLACED ✅"
        )
    else:
        st.error(
        "NOT PLACED ❌"
        )