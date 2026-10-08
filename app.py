import streamlit as st
import hashlib
import re
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Secure Information System",
    page_icon="🔐",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

if "incident_score" not in st.session_state:
    st.session_state.incident_score = 0

# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 700;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
    }

    .security-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 15px;
    }

    .danger-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #ffe5e5;
        border: 1px solid #ff9999;
    }

    .safe-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #e5ffe9;
        border: 1px solid #8bd99a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FUNCTIONS
# =========================================================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        return "Weak", score

    if score <= 4:
        return "Moderate", score

    return "Strong", score


# Demo credentials for academic demonstration only
DEMO_USERNAME = "admin"
DEMO_PASSWORD_HASH = hash_password("Secure@123")

# =========================================================
# LOGIN PAGE
# =========================================================

if not st.session_state.logged_in:

    st.markdown(
        '<div class="main-title">🔐 Secure Information System</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Information System Security Demonstration & Awareness Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    left, right = st.columns([1, 1])

    with left:

        st.subheader("🔑 Secure Login")

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        login = st.button(
            "Login",
            type="primary",
            use_container_width=True
        )

        if login:

            entered_hash = hash_password(password)

            if (
                username == DEMO_USERNAME
                and entered_hash == DEMO_PASSWORD_HASH
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Authentication successful.")

                st.rerun()

            else:

                st.session_state.login_attempts += 1

                st.error("Invalid username or password.")

                if st.session_state.login_attempts >= 3:
                    st.warning(
                        "Multiple failed login attempts detected. "
                        "Account protection should be considered."
                    )

    with right:

        st.subheader("🛡️ Security Information")

        st.info(
            """
            This application demonstrates fundamental
            Information System Security concepts.

            **Demo credentials**

            Username: `admin`

            Password: `Secure@123`

            The password is hashed before comparison.
            """
        )

        st.markdown(
            """
            **Security concepts demonstrated:**

            • Authentication  
            • Password security  
            • CIA Triad  
            • Access control  
            • Phishing awareness  
            • Malware awareness  
            • Social engineering  
            • Network security  
            • Security incident response
            """
        )

    st.stop()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🔐 Security System")

st.sidebar.success(
    f"Logged in as: {st.session_state.username}"
)

page = st.sidebar.radio(
    "Security Modules",
    [
        "🏠 Security Home",
        "🔺 CIA Triad",
        "🔑 Password Security",
        "🎣 Phishing Simulator",
        "🦠 Malware Awareness",
        "👤 Social Engineering",
        "🌐 Network Security",
        "🚨 Incident Response",
        "📝 Security Quiz",
        "📋 Security Report"
    ]
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False
    st.session_state.username = ""

    st.rerun()

# =========================================================
# HOME
# =========================================================

if page == "🏠 Security Home":

    st.markdown(
        '<div class="main-title">🛡️ Information System Security</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Interactive security learning and assessment system'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.header("What is Information System Security?")

    st.write(
        """
        Information System Security is the practice of protecting
        information systems, networks, applications and data from
        unauthorized access, modification, disclosure, destruction
        and disruption.
        """
    )

    st.header("Security Objectives")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("🔒 Confidentiality")
        st.write(
            "Ensures information is accessible only to authorized users."
        )

    with c2:
        st.subheader("🧾 Integrity")
        st.write(
            "Ensures information remains accurate and is not improperly modified."
        )

    with c3:
        st.subheader("⚡ Availability")
        st.write(
            "Ensures systems and information remain available when required."
        )

    st.divider()

    st.header("Security Modules")

    modules = {
        "🔺 CIA Triad": "Understand confidentiality, integrity and availability.",
        "🔑 Password Security": "Analyze password strength and secure authentication practices.",
        "🎣 Phishing Simulator": "Learn how to identify phishing attempts.",
        "🦠 Malware Awareness": "Understand common malware threats.",
        "👤 Social Engineering": "Learn how attackers manipulate users.",
        "🌐 Network Security": "Understand VPNs, eavesdropping and secure communication.",
        "🚨 Incident Response": "Practice responding to security incidents.",
        "📝 Security Quiz": "Test your Information System Security knowledge."
    }

    for title, description in modules.items():

        with st.expander(title):

            st.write(description)

# =========================================================
# CIA TRIAD
# =========================================================

elif page == "🔺 CIA Triad":

    st.title("🔺 CIA Triad")

    st.write(
        """
        The CIA Triad is one of the fundamental models of
        Information System Security.
        """
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "🔒 Confidentiality",
            "🧾 Integrity",
            "⚡ Availability"
        ]
    )

    with tab1:

        st.subheader("Confidentiality")

        st.write(
            """
            Confidentiality protects information from unauthorized
            disclosure or access.
            """
        )

        st.success(
            "Example: Only authorized employees should access customer records."
        )

        st.write("Common controls:")

        st.write(
            """
            • Authentication  
            • Authorization  
            • Encryption  
            • Access control  
            • Data classification
            """
        )

    with tab2:

        st.subheader("Integrity")

        st.write(
            """
            Integrity ensures information remains accurate,
            complete and protected from unauthorized modification.
            """
        )

        st.success(
            "Example: A transaction amount should not be changed by an unauthorized user."
        )

        st.write("Common controls:")

        st.write(
            """
            • Hashing  
            • Digital signatures  
            • File permissions  
            • Audit logs  
            • Change monitoring
            """
        )

    with tab3:

        st.subheader("Availability")

        st.write(
            """
            Availability ensures authorized users can access
            systems and information when required.
            """
        )

        st.success(
            "Example: An online banking service should remain available to customers."
        )

        st.write("Common controls:")

        st.write(
            """
            • Backups  
            • Redundancy  
            • Disaster recovery  
            • System monitoring  
            • Fault tolerance
            """
        )

    st.divider()

    st.subheader("CIA Scenario")

    scenario = st.selectbox(
        "A company database is modified by an unauthorized person. Which CIA principle is primarily affected?",
        [
            "Confidentiality",
            "Integrity",
            "Availability"
        ]
    )

    if st.button("Check Answer"):

        if scenario == "Integrity":
            st.success(
                "Correct! Unauthorized modification affects Integrity."
            )
        else:
            st.error(
                "Incorrect. The primary affected principle is Integrity."
            )

# =========================================================
# PASSWORD SECURITY
# =========================================================

elif page == "🔑 Password Security":

    st.title("🔑 Password Security Analyzer")

    st.write(
        """
        Passwords are an important component of authentication.
        This module evaluates password characteristics without storing
        the password.
        """
    )

    password = st.text_input(
        "Enter a password to analyze",
        type="password"
    )

    if password:

        strength, score = password_strength(password)

        st.subheader(f"Password Strength: {strength}")

        st.progress(
            min(score / 6, 1.0)
        )

        if strength == "Strong":
            st.success("Good password characteristics detected.")

        elif strength == "Moderate":
            st.warning(
                "The password can be strengthened further."
            )

        else:
            st.error(
                "This password is weak and should be improved."
            )

        st.write("Security analysis:")

        if len(password) >= 12:
            st.write("✅ Good password length")
        else:
            st.write("❌ Use at least 12 characters")

        if re.search(r"[A-Z]", password):
            st.write("✅ Contains uppercase characters")
        else:
            st.write("❌ Add uppercase characters")

        if re.search(r"[a-z]", password):
            st.write("✅ Contains lowercase characters")
        else:
            st.write("❌ Add lowercase characters")

        if re.search(r"[0-9]", password):
            st.write("✅ Contains numbers")
        else:
            st.write("❌ Add numbers")

        if re.search(r"[^A-Za-z0-9]", password):
            st.write("✅ Contains special characters")
        else:
            st.write("❌ Add special characters")

        st.info(
            "Never reuse passwords across important accounts."
        )

# =========================================================
# PHISHING SIMULATOR
# =========================================================

elif page == "🎣 Phishing Simulator":

    st.title("🎣 Phishing Awareness Simulator")

    st.write(
        """
        Examine the message below and determine whether it is
        legitimate or a phishing attempt.
        """
    )

    st.warning(
        """
        From: security-alert@example-login.com

        Subject: URGENT - Your account will be suspended

        Your account has unusual activity.

        Verify your account immediately by clicking the link below.

        [Verify Account]

        Failure to verify within 24 hours will result in account suspension.
        """
    )

    answer = st.radio(
        "What should you do?",
        [
            "Click the link immediately",
            "Reply with my password",
            "Verify the sender independently and avoid the suspicious link",
            "Forward the message to everyone"
        ]
    )

    if st.button("Analyze Message"):

        if answer == "Verify the sender independently and avoid the suspicious link":

            st.success(
                """
                Correct.

                Warning signs include:

                • Urgent language
                • Threat of account suspension
                • Suspicious sender
                • Request to click a link
                • Pressure to act quickly
                """
            )

        else:

            st.error(
                """
                Incorrect.

                This message contains multiple phishing indicators.
                Never provide credentials through suspicious links.
                """
            )

# =========================================================
# MALWARE
# =========================================================

elif page == "🦠 Malware Awareness":

    st.title("🦠 Malware Awareness")

    st.write(
        """
        Malware is malicious software designed to damage systems,
        steal information, disrupt operations or gain unauthorized access.
        """
    )

    malware_types = {
        "Virus": "Malicious code that can replicate by attaching itself to files or programs.",
        "Worm": "Malware capable of spreading between systems without requiring a host file.",
        "Trojan": "Malicious software disguised as legitimate software.",
        "Ransomware": "Malware that can encrypt or restrict access to data and demand payment.",
        "Spyware": "Software designed to secretly collect information about users or systems."
    }

    selected = st.selectbox(
        "Select malware type",
        list(malware_types.keys())
    )

    st.info(
        malware_types[selected]
    )

    st.subheader("Basic Protection")

    st.write(
        """
        ✅ Keep operating systems updated

        ✅ Use trusted security software

        ✅ Avoid unknown downloads

        ✅ Do not open suspicious attachments

        ✅ Maintain regular backups

        ✅ Use secure and trusted websites
        """
    )

# =========================================================
# SOCIAL ENGINEERING
# =========================================================

elif page == "👤 Social Engineering":

    st.title("👤 Social Engineering Awareness")

    st.write(
        """
        Social engineering involves manipulating people into
        revealing information or performing actions that compromise
        security.
        """
    )

    scenario = st.selectbox(
        "Scenario",
        [
            "A caller claims to be IT support and asks for your password.",
            "A colleague asks you to review a normal internal document.",
            "A company publishes a security awareness notice."
        ]
    )

    response = st.radio(
        "What should you do?",
        [
            "Provide the requested information",
            "Verify the person's identity through an official channel",
            "Ignore all security procedures",
            "Send sensitive information immediately"
        ]
    )

    if st.button("Evaluate Response"):

        if (
            "IT support" in scenario
            and response == "Verify the person's identity through an official channel"
        ):

            st.success(
                "Correct. Always verify unexpected requests for sensitive information."
            )

        elif "IT support" not in scenario:

            st.info(
                "Security decisions should depend on context, identity verification and data sensitivity."
            )

        else:

            st.error(
                "Incorrect. Never disclose sensitive information without verification."
            )

# =========================================================
# NETWORK SECURITY
# =========================================================

elif page == "🌐 Network Security":

    st.title("🌐 Network Security")

    st.write(
        """
        Network security protects communication, systems and data
        from unauthorized access, interception and attacks.
        """
    )

    st.subheader("Important Concepts")

    concepts = {
        "Eavesdropping":
            "Unauthorized interception or monitoring of network communication.",

        "VPN":
            "A Virtual Private Network can provide encrypted communication between a device and a VPN endpoint.",

        "Firewall":
            "A security control that monitors and controls network traffic according to defined rules.",

        "HTTPS":
            "HTTPS helps protect web communication using encryption."
    }

    for concept, description in concepts.items():

        with st.expander(concept):

            st.write(description)

    st.divider()

    network_question = st.radio(
        "You are using public Wi-Fi. Which is the safer practice?",
        [
            "Access sensitive accounts through any unknown website",
            "Use HTTPS and trusted networks or a reputable VPN",
            "Disable all security protections",
            "Share your login credentials with another user"
        ]
    )

    if st.button("Check Network Answer"):

        if network_question == "Use HTTPS and trusted networks or a reputable VPN":

            st.success("Correct security practice.")

        else:

            st.error("This choice can increase security risk.")

# =========================================================
# INCIDENT RESPONSE
# =========================================================

elif page == "🚨 Incident Response":

    st.title("🚨 Security Incident Response Simulation")

    st.write(
        """
        You receive an alert that an employee may have entered
        credentials into a suspicious website.
        """
    )

    st.subheader("What should happen first?")

    action = st.radio(
        "Choose the best initial response",
        [
            "Ignore the event",
            "Immediately publish the employee's information",
            "Report the incident and follow the organization's incident response procedure",
            "Delete all company systems"
        ]
    )

    if st.button("Evaluate Incident Response"):

        if action == "Report the incident and follow the organization's incident response procedure":

            st.success(
                """
                Correct.

                A suspected security incident should be reported
                through the organization's established incident
                response process.
                """
            )

        else:

            st.error(
                "Incorrect. Follow the organization's incident response procedure."
            )

# =========================================================
# SECURITY QUIZ
# =========================================================

elif page == "📝 Security Quiz":

    st.title("📝 Information System Security Quiz")

    questions = [
        (
            "What does the C in CIA stand for?",
            [
                "Control",
                "Confidentiality",
                "Cryptography",
                "Compliance"
            ],
            "Confidentiality"
        ),
        (
            "Which attack commonly attempts to trick users into revealing information?",
            [
                "Phishing",
                "Backup",
                "Encryption",
                "Authentication"
            ],
            "Phishing"
        ),
        (
            "Which principle protects information from unauthorized modification?",
            [
                "Availability",
                "Confidentiality",
                "Integrity",
                "Usability"
            ],
            "Integrity"
        ),
        (
            "Which is a good password practice?",
            [
                "Reuse the same password everywhere",
                "Use short passwords",
                "Use strong unique passwords",
                "Share passwords with colleagues"
            ],
            "Use strong unique passwords"
        ),
        (
            "What is malware?",
            [
                "Security policy",
                "Malicious software",
                "Backup system",
                "Network cable"
            ],
            "Malicious software"
        )
    ]

    answers = []

    for index, (question, options, correct) in enumerate(questions):

        st.subheader(f"{index + 1}. {question}")

        answer = st.radio(
            "Select an answer",
            options,
            key=f"quiz_{index}"
        )

        answers.append(
            (answer, correct)
        )

    if st.button("Submit Quiz", type="primary"):

        score = 0

        for answer, correct in answers:

            if answer == correct:
                score += 1

        st.session_state.quiz_score = score
        st.session_state.quiz_completed = True

    if st.session_state.quiz_completed:

        score = st.session_state.quiz_score

        st.divider()

        st.subheader(
            f"Quiz Result: {score}/5"
        )

        if score == 5:

            st.success(
                "Excellent! Strong understanding of the security fundamentals."
            )

        elif score >= 3:

            st.info(
                "Good attempt. Review the concepts where you made mistakes."
            )

        else:

            st.warning(
                "Review the fundamental Information System Security concepts."
            )

# =========================================================
# SECURITY REPORT
# =========================================================

elif page == "📋 Security Report":

    st.title("📋 Security Assessment Report")

    st.write(
        """
        This report summarizes the security concepts demonstrated
        through the application.
        """
    )

    st.subheader("User Information")

    st.write(
        f"**Authenticated User:** {st.session_state.username}"
    )

    st.subheader("Security Areas Demonstrated")

    report = {
        "Authentication": "Implemented",
        "Password Security": "Implemented",
        "CIA Triad": "Implemented",
        "Phishing Awareness": "Implemented",
        "Malware Awareness": "Implemented",
        "Social Engineering": "Implemented",
        "Network Security": "Implemented",
        "Incident Response": "Implemented",
        "Security Quiz": "Implemented"
    }

    report_df = st.dataframe(
        list(report.items()),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Course Concept Mapping")

    mapping = {
        "CIA Triad": "Confidentiality, Integrity and Availability",
        "Sensitive Data": "Data protection and access control",
        "Malware": "Malware types and protection",
        "Phishing": "Social engineering and phishing awareness",
        "VPN": "Secure network communication",
        "Eavesdropping": "Network security",
        "Authentication": "Account and password security"
    }

    for concept, application in mapping.items():

        st.write(
            f"**{concept}:** {application}"
        )

    st.divider()

    st.subheader("Conclusion")

    st.write(
        """
        The Secure Information System application demonstrates
        fundamental Information System Security principles through
        authentication, password analysis, CIA Triad scenarios,
        phishing awareness, malware education, social engineering
        scenarios, network security concepts and incident response.

        The application provides an interactive environment for
        understanding how security principles can be applied to
        real-world information systems.
        """
    )

# =========================================================
# FOOTER
# =========================================================

st.sidebar.divider()

st.sidebar.caption(
    "Information System Security Academic Project"
)

st.sidebar.caption(
    "Educational demonstration only"
)