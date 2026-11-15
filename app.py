"""StratEdge Innovation Consulting Ltd (SICL) - company website."""
import json
import os
from datetime import datetime, timezone

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-in-production")

COMPANY = {
    "name": "StratEdge Innovation Consulting Ltd",
    "short": "SICL",
    "rc": "10003159",
    "address": "Paniel Abarka Plaza, Opposite Federal High Court, Chanchaga, Minna, Niger State",
    "city": "Minna, Niger State",
    "phone": "+234 706 922 9924",
    "email": "info@StratedgeInnovationConsulting.com",
    "emails": [
        "info@StratedgeInnovationConsulting.com",
        "jibril@StratedgeInnovationConsulting.com",
        "egba@StratedgeInnovationConsulting.com",
        "jibrinegba61@gmail.com",
    ],
    "website_url": "https://www.stratedgeinnovationconsulting.com",
    "contact_person": "Egba Jibrin",
    "tagline": "Technology. Intelligence. Compliance. Leadership.",
    "kicker": ["Innovation", "Strategy", "Transformation", "Impact"],
    "year": datetime.now().year,
}

PILLARS = [
    {
        "key": "technology", "word": "Technology", "icon": "technology",
        "title": "ICT Solutions & Digital Transformation",
        "blurb": "Systems, data and security that hold up in the real world.",
        "items": [
            "ICT infrastructure, systems integration and technology solutions",
            "Software development, digital platforms and business process automation",
            "Data analytics, artificial intelligence and machine learning",
            "Cybersecurity, information security and digital risk advisory",
            "ICT training and institutional capacity development",
        ],
    },
    {
        "key": "intelligence", "word": "Intelligence", "icon": "intelligence",
        "title": "AML/CFT/CPF Solutions & Financial Intelligence",
        "blurb": "Find financial crime risk early and report it properly.",
        "items": [
            "AML/CFT/CPF compliance solutions, advisory and training",
            "Financial intelligence, data analytics and risk-based approaches",
            "Transaction monitoring and suspicious transaction reporting",
            "Virtual assets and VASP compliance advisory",
            "Blockchain analytics and cryptocurrency investigations training",
            "AML/CFT/CPF risk assessments and institutional capacity building",
        ],
    },
    {
        "key": "compliance", "word": "Compliance", "icon": "compliance",
        "title": "Strategic Consultancy & Institutional Advisory",
        "blurb": "Clear strategy, sound governance, delivery you can measure.",
        "items": [
            "Organisational strategy, transformation and performance improvement",
            "Policy development, implementation support and institutional strengthening",
            "Business process review, redesign and optimisation",
            "Governance, enterprise risk and regulatory compliance advisory",
            "Project management, programme design and implementation support",
        ],
    },
    {
        "key": "leadership", "word": "Leadership", "icon": "leadership",
        "title": "Leadership & Executive Development",
        "blurb": "Build leaders who can run the change you plan.",
        "items": [
            "Executive leadership, management and supervisory training",
            "Strategic thinking, decision-making and problem-solving",
            "Change management and organisational leadership",
            "Public-sector leadership, governance and institutional effectiveness",
            "Professional development, mentoring and executive coaching",
        ],
    },
]

CORE_VALUES = [
    ("Innovation", "Embracing new ideas and technologies."),
    ("Integrity", "Upholding honesty and ethical conduct."),
    ("Excellence", "Delivering high-quality solutions."),
    ("Professionalism", "Maintaining the highest professional standards."),
    ("Collaboration", "Building effective partnerships."),
    ("Impact", "Delivering measurable and sustainable results."),
]

# Competitive advantage, expressed as reasons to choose the firm.
ADVANTAGES = [
    ("Multidisciplinary expertise",
     "ICT, financial intelligence, regulatory compliance, strategy and leadership development integrated in one team."),
    ("Practical, outcome-focused solutions",
     "Implementable services and tools that respond to real organisational needs, not shelf reports."),
    ("A technology-driven approach",
     "Data analytics, automation, artificial intelligence and other emerging technologies applied where they improve the result."),
    ("Institutional understanding",
     "Services tailored to the operating realities of government, regulated entities and private organisations."),
    ("Capacity development and knowledge transfer",
     "Advisory and technology combined with training, so capability stays with your institution."),
    ("Client-centred delivery",
     "Every organisation is different; solutions are shaped around your needs, priorities and operational realities."),
    ("An experienced professional team",
     "Professional knowledge, industry experience and practical insight applied to every engagement."),
    ("Strategic partnerships",
     "Partnerships that connect you to relevant expertise, innovative technologies and opportunities for growth."),
]

LEADER = {
    "name": "Egba Jibrin",
    "role": "Managing Director / Chief Executive Officer",
    "initials": "EJ",
    "summary": (
        "A public health data management, monitoring and evaluation, and institutional capacity "
        "development specialist with over 25 years of progressive experience across public-sector "
        "management, health information systems, data analytics, strategic planning, project "
        "management and organisational development."
    ),
    "bio": [
        "He previously served as Deputy Director, Planning, Research and Statistics, and State Health "
        "Management Information System Manager within the Niger State health sector, where he led "
        "health information management, performance monitoring, data quality assurance, strategic "
        "planning and the coordination of development programmes.",
        "In addition to his public-sector experience, he has undertaken professional programmes in "
        "Anti-Money Laundering, Countering the Financing of Terrorism and Countering the Financing of "
        "Proliferation (AML/CFT/CPF), and has facilitated AML/CFT/CPF training for financial "
        "institutions, improving awareness of financial crime risks, compliance obligations and "
        "institutional capacity.",
        "As MD/CEO he provides strategic leadership and direction, championing the company's commitment "
        "to innovation, technology-driven solutions, AML/CFT/CPF capacity development, institutional "
        "transformation, professional excellence and sustainable growth.",
    ],
    "focus": [
        ("Public-sector and institutional management",
         "Over 15 years of programme management, strategic planning and institutional coordination."),
        ("Data management and digital transformation",
         "Information systems, analytics, performance monitoring and digital solutions."),
        ("AML/CFT/CPF training and capacity development",
         "Professional training and delivery for financial institutions and regulated entities."),
    ],
    "credentials": [
        "BSc Public Health, University of Ibadan",
        "HND Statistics",
        "Health Information Management",
        "M&E in Global Health",
        "MEAL",
        "MPH (in progress)",
    ],
    "tools": "DHIS2 · Power BI · STATA · SPSS · Excel · KoboCollect · ODK",
    "quote": (
        "Our commitment is to transform ideas into practical solutions, leverage innovation to address "
        "institutional challenges, and empower organisations and people to achieve sustainable results."
    ),
}

UNITS = [
    {"icon": "technology", "name": "ICT & Digital Transformation",
     "role": "Technology delivery, software, infrastructure, data and cybersecurity."},
    {"icon": "intelligence", "name": "Financial Intelligence & Compliance Advisory",
     "role": "AML/CFT/CPF, financial crime risk, virtual assets and financial intelligence."},
    {"icon": "compass", "name": "Strategy & Institutional Consulting",
     "role": "Strategy, governance, organisational transformation and programme advisory."},
    {"icon": "cap", "name": "Leadership & Professional Development",
     "role": "Executive education, leadership programmes and professional training."},
    {"icon": "briefcase", "name": "Corporate Services",
     "role": "Finance, administration, human resources, legal support, marketing and business development."},
]

# Growth plan from the company profile, kept for future site content.
STRATEGIC_DIRECTION = [
    "Develop and deploy fit-for-purpose technology platforms and digital solutions.",
    "Build a portfolio of AML/CFT/CPF training, advisory and compliance-support services.",
    "Establish partnerships with technology companies, professional bodies, academic institutions and international organisations.",
    "Pursue government, financial-sector and private-sector consultancy assignments.",
    "Develop structured executive and professional development programmes.",
    "Expand service delivery across Nigeria and, over time, other African markets.",
]

CLIENTS = [
    "Federal, State and Local Government ministries, departments and agencies",
    "Financial Intelligence Units, law enforcement and other competent authorities",
    "Central Banks, financial regulators and supervisory institutions",
    "Banks, fintech companies and other financial institutions",
    "Designated Non-Financial Businesses and Professions (DNFBPs)",
    "Virtual Asset Service Providers (VASPs) and technology companies",
    "Development partners, international organisations and donor-funded programmes",
    "Private-sector organisations, corporate institutions and professional associations",
    "Training institutions and academic or professional development bodies",
]


@app.route("/")
def index():
    return render_template(
        "index.html", c=COMPANY, pillars=PILLARS, advantages=ADVANTAGES,
        core_values=CORE_VALUES, leader=LEADER, units=UNITS, clients=CLIENTS,
    )


@app.post("/contact")
def contact():
    f = request.form
    name, email, message = (f.get(k, "").strip() for k in ("name", "email", "message"))
    if f.get("website"):  # honeypot for bots
        return redirect(url_for("index"))
    if not (name and "@" in email and len(message) >= 10):
        flash("Please enter your name, a valid email and a message of at least 10 characters.", "error")
        return redirect(url_for("index", _anchor="contact"))
    entry = {"time": datetime.now(timezone.utc).isoformat(), "name": name, "email": email,
             "organisation": f.get("organisation", "").strip(),
             "interest": f.get("interest", ""), "message": message}
    with open(os.path.join(app.root_path, "messages.jsonl"), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry) + "\n")
    flash("Message sent. We will reply to your email shortly.", "ok")
    return redirect(url_for("index", _anchor="contact"))


if __name__ == "__main__":
    app.run(debug=True)
