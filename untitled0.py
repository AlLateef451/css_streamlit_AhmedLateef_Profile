# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 23:48:24 2026

@author: Lateef
"""

import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="Ahmed Lateef Timilehin | CV", layout="wide")

# ----------------------------
# CV DATA (edit these safely)
# ----------------------------
PROFILE = {
    "name": "Ahmed Lateef Timilehin",
    "headline": "Computer Engineering | Embedded Systems | IoT | AI Prototyping",
    "email": "Latmore99@gmail.com",
    "phone": "+27 62 368 8317",
    "location": "Cape Town, South Africa",
    "nationality": "Nigerian",
    "driver_license": "Code C10 (3 years experience)",
    "relocation": "Available for relocation starting in 2026",
}

ABOUT = (
    "I am an individual who strives for excellence in any field I find myself in. "
    "I have a teachable spirit and always aim to be the best I can be. "
    "I believe in collective success and the power of collaboration. "
    "I am both hardworking and smart working, and I think outside the box to create innovative solutions."
)

SKILLS = {
    "Programming": [
        "Python (automation, AI/ML prototypes, IoT, image processing; NumPy, OpenCV, TensorFlow)",
        "C/C++ (embedded systems: Arduino, ESP32, STM32)",
        "Java (OOP, data structures, backend basics; Android fundamentals)",
        "JavaScript (interactive web apps)",
        "MATLAB (analysis, simulations; signal processing/control)",
        "HTML",
        "WebGL (3D rendering/visualization exposure)",
    ],
    "Technology": ["Linux (Ubuntu)", "Windows", "GitHub"],
    "Networking/Systems": ["Cisco & VyOS router configuration", "Layer 2/Layer 3 switching (advanced configs)"],
    "Databases": ["MySQL (relational)", "Neo4j (graph databases)"],
}

EXPERIENCE_TIMELINE = [
    {
        "year": "2016",
        "items": [
            "Completed matric; served as a prefect; graduated top three in Grade 12.",
            "Waiter at Mugg & Bean (Canal Walk): served customers, handled orders, provided service.",
        ],
    },
    {
        "year": "2017–2020",
        "items": [
            "Accepted to study Electrical Engineering (Wits University) but postponed due to financial constraints.",
            "Worked at Mugg & Bean for three years to save for education.",
        ],
    },
    {
        "year": "2020",
        "items": [
            "Started car rental logistics (weekly rentals) to fund tuition and living costs.",
            "Balanced business + first year National Diploma in Computer Engineering (CPUT) + work at Mugg & Bean.",
            "Voted class representative.",
        ],
    },
    {
        "year": "2021",
        "items": [
            "Exited car rental business; completed and graduated National Diploma (Computer Engineering).",
            "Continued working at Mugg & Bean.",
        ],
    },
    {
        "year": "2022",
        "items": [
            "Bike rental/maintenance partnership with Mr D (delivery services).",
            "Gained people management and fast problem-solving through real-world challenges.",
        ],
    },
    {
        "year": "2023",
        "items": [
            "Opened a driving school; later refocused on completing Bachelor’s in Computer Engineering.",
        ],
    },
    {
        "year": "2024",
        "items": [
            "Started Bachelor’s degree full-time.",
            "Voted class representative.",
        ],
    },
    {
        "year": "2025",
        "items": [
            "Final year of Bachelor’s degree.",
            "Completed 3-month university entrepreneurship program.",
            "2nd place (team) in FinTech Hackathon: prototype using Interledger Protocol; USSD-based transfers without internet/smartphone.",
            "Tutored matric Maths and Physics.",
        ],
    },
]

EDUCATION = [
    {
        "title": "National Diploma in Computer Engineering (Engineering Technology)",
        "institution": "Cape Peninsula University of Technology (CPUT)",
        "dates": "Jan 2020 – Dec 2021",
        "details": [
            "Average: 70.6%",
            "Core modules: Engineering Physics, Electronics, Systems Analysis, Software Development",
        ],
    },
    {
        "title": "Bachelor of Engineering Technology in Computer Engineering",
        "institution": "Cape Peninsula University of Technology (CPUT)",
        "dates": "Jan 2024 – Present",
        "details": [
            "Embedded Systems (Arduino, ESP32, STM32, Raspberry Pi)",
            "Network Systems (Cisco/VyOS routers; advanced Layer 2/3 switching)",
            "Industrial Computing Design (automation, real-time systems, fault-tolerant design)",
            "Database Systems (MySQL + Neo4j hybrid approaches)",
        ],
    },
]

PROJECTS = [
    {
        "name": "Final-Year Project (Diploma): Prototyping Embedded Systems",
        "bullets": [
            "Designed optimized embedded systems for real-time operations (Arduino, ESP32, STM32).",
            "Integrated sensors/actuators for responsive systems; focused on power-efficient circuits.",
        ],
    },
    {
        "name": "Final-Year Project (Bachelor): AI-Powered Hydroponic Farming System",
        "bullets": [
            "Smart hydroponics system using AI + IoT + embedded systems to monitor and manage plant growth.",
            "Raspberry Pi processes real-time image data (cameras detect plant color changes).",
            "ESP32 controls sensors/actuators (temperature, humidity, pH) and triggers alerts/notifications.",
            "Includes harvest readiness notifications to optimize efficiency and reduce waste.",
        ],
    },
    {
        "name": "FinTech Hackathon (Team) – 2nd Place",
        "bullets": [
            "Prototype app to serve underbanked/overbanked using Interledger Protocol.",
            "USSD-based send/receive money without internet connectivity or smartphone.",
        ],
    },
]

CERTIFICATIONS = [
    {
        "name": "University of Cape Town (UCT) — Design Thinking Week (Client Project)",
        "date": "Nov 2025",
        "bullets": [
            "Field research with tourists and local food vendors; mapped barriers (visibility, trust, accessibility).",
            "Co-designed and prototyped a solution to help local African food vendors reach higher-spend customers.",
            "Delivered roadmap and activation/marketing ideas; pitched recommendations to client.",
        ],
    },
    {
        "name": "Computational & Data Science Training — CHPC & NITheCS (Intensive Short Course)",
        "date": "Jan – Feb 2026",
        "bullets": [
            "Coding practices & Bash scripting",
            "Data pipelines & workflow automation",
            "Data visualization (Jupyter, Streamlit)",
            "Scientific computing; probability, statistics, ML fundamentals",
            "Applied computing in bioinformatics and Earth observation data",
        ],
    },
]

VOLUNTEERING = [
    "Netcare 911: assistant nurse for one week (supporting elderly and sick individuals).",
    "Mentored first-year students during orientation.",
]

REFERENCES = [
    {"name": "Mr Goldstone", "role": "Physics and Math Teacher (High School)", "contact": "cgoldsto@gmail.com"},
    {"name": "Dr Ekron", "role": "Communications Lecturer (University)", "contact": "+27 (83) 383-1409"},
    {"name": "Mr Tyson", "role": "Manager (Mugg & Bean)", "contact": "+27 (61) 288-2126"},
    {"name": "Mr Chris", "role": "Entrepreneurship Program Facilitator", "contact": "+27 (82) 579-2835"},
]

# ----------------------------
# Sidebar navigation
# ----------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Home", "Experience", "Education", "Projects", "Skills", "Certifications", "Volunteering", "References", "Contact"],
)

# Optional: small header on every page
st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit • Hosted on GitHub")

# ----------------------------
# Pages
# ----------------------------
if menu == "Home":
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.title(PROFILE["name"])
        st.subheader(PROFILE["headline"])
        st.write(ABOUT)

        st.markdown("### Quick Highlights")
        st.markdown(
            "- Final-year Computer Engineering student\n"
            "- Embedded Systems, IoT, AI prototyping\n"
            "- 2nd place FinTech Hackathon (team)\n"
            "- Class representative (2020, 2024)\n"
        )

    with col2:
        st.markdown("### Details")
        st.write(f"📍 **Location:** {PROFILE['location']}")
        st.write(f"🌍 **Nationality:** {PROFILE['nationality']}")
        st.write(f"🚗 **Driver’s License:** {PROFILE['driver_license']}")
        st.write(f"🧳 **Relocation:** {PROFILE['relocation']}")
        st.write(f"✉️ **Email:** {PROFILE['email']}")
        st.write(f"📞 **Phone:** {PROFILE['phone']}")

        st.markdown("---")
        st.caption("Tip: Keep sensitive personal info off public CV pages.")

elif menu == "Experience":
    st.title("Experience Timeline")
    for block in EXPERIENCE_TIMELINE:
        with st.expander(block["year"], expanded=(block["year"] in ["2025", "2024"])):
            for item in block["items"]:
                st.write(f"• {item}")

elif menu == "Education":
    st.title("Education")
    for edu in EDUCATION:
        st.subheader(edu["title"])
        st.caption(f"{edu['institution']} • {edu['dates']}")
        for d in edu["details"]:
            st.write(f"• {d}")
        st.markdown("---")

elif menu == "Projects":
    st.title("Projects")
    for p in PROJECTS:
        st.subheader(p["name"])
        for b in p["bullets"]:
            st.write(f"• {b}")
        st.markdown("---")

elif menu == "Skills":
    st.title("Skills")
    tabs = st.tabs(list(SKILLS.keys()))
    for tab, category in zip(tabs, SKILLS.keys()):
        with tab:
            for s in SKILLS[category]:
                st.write(f"• {s}")

elif menu == "Certifications":
    st.title("Certifications & Training")
    for c in CERTIFICATIONS:
        st.subheader(c["name"])
        st.caption(c["date"])
        for b in c["bullets"]:
            st.write(f"• {b}")
        st.markdown("---")

elif menu == "Volunteering":
    st.title("Volunteering")
    for v in VOLUNTEERING:
        st.write(f"• {v}")

elif menu == "References":
    st.title("References")
    st.info("Consider asking permission before publishing reference contact details online.")
    for r in REFERENCES:
        st.subheader(r["name"])
        st.write(f"**Role:** {r['role']}")
        st.write(f"**Contact:** {r['contact']}")
        st.markdown("---")

elif menu == "Contact":
    st.title("Contact")
    st.write("Use the form below to send a message (you can connect this to email later).")

    with st.form("contact_form"):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")

    if submitted:
        st.success("Thanks! (This demo form doesn't send emails yet.)")

    st.markdown("### Direct Contact")
    st.write(f"✉️ **Email:** {PROFILE['email']}")
    st.write(f"📞 **Phone:** {PROFILE['phone']}")
