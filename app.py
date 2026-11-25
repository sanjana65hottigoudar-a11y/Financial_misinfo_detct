import streamlit as st
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #07111f, #101c33, #08131f);
    color: #eaf4ff;
}

[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3 {
    color: #38bdf8 !important;
}

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #14253c, #0b1728);
    border: 1px solid #234567;
    padding: 18px;
    border-radius: 15px;
}

div.stButton > button {
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: bold;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #38bdf8, #60a5fa);
    color: white;
    border: 1px solid #38bdf8;
}

div[data-testid="stTextArea"] textarea {
    background-color: #102035;
    color: white;
    border: 1px solid #315477;
    border-radius: 12px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

hr {
    border-color: #29415e;
}
</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="FinShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FinShield AI")

st.subheader(
    "Financial Misinformation Detection & Spread Tracing"
)

st.write(
    "An AI-powered platform to identify suspicious "
    "financial claims and trace how rumours spread."
)

st.divider()

st.header("Welcome to FinShield AI")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Claim Detection")
    st.write(
        "Analyse financial claims and identify "
        "potential misinformation."
    )

with col2:
    st.subheader("📊 Spread Tracing")
    st.write(
        "Understand how financial rumours travel "
        "across different sources."
    )

st.divider()

st.header("Try Our Application")

claim = st.text_area(
    "Enter a financial claim:",
    placeholder="Example: This stock will double tomorrow!"
)

if st.button("Analyse Claim"):
    if claim.strip():
        st.success("Your claim has been received!")
        st.write("Submitted claim:", claim)
        st.info(
            "AI verification will be added in the next stage."
        )
    else:
        st.warning("Please enter a claim first.")

st.caption("FinShield AI | AI in Cybersecurity & FinTech Hackathon")
import streamlit as st
import re

st.set_page_config(
    page_title="FinShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FinShield AI")
st.subheader("AI-Powered Financial Misinformation Detection")
st.caption("FinShield AI | AI in Cybersecurity & FinTech Hackathon")

st.markdown("---")

st.info(
    "Enter a financial claim, investment message, or financial news statement "
    "to screen it for suspicious language and potential misinformation risks."
)

claim = st.text_area(
    "Enter a financial claim:",
    placeholder="Example: Invest ₹10,000 today and receive guaranteed double returns in 7 days!",
    height=150
)

def analyze_claim(text):
    patterns = {
        "Guaranteed returns": [
            r"guaranteed returns",
            r"guaranteed profit",
            r"guaranteed income",
            r"risk.free"
        ],
        "Unrealistic profits": [
            r"double your money",
            r"100% profit",
            r"200% return",
            r"10x your money",
            r"triple your money"
        ],
        "Urgency pressure": [
            r"limited time",
            r"act now",
            r"last chance",
            r"offer expires",
            r"today only"
        ],
        "Suspicious payment requests": [
            r"pay.*upfront",
            r"send.*fee",
            r"processing fee",
            r"deposit.*unlock"
        ],
        "Unverified endorsements": [
            r"celebrity endorsed",
            r"government approved",
            r"officially approved"
        ],
        "Suspicious solicitation": [
            r"secret investment",
            r"insider tip",
            r"exclusive opportunity"
        ]
    }

    detected = []
    score = 0

    for category, phrases in patterns.items():
        for phrase in phrases:
            if re.search(phrase, text, re.IGNORECASE):
                detected.append(category)
                score += 20
                break

    score = min(score, 100)

    if score >= 60:
        risk = "HIGH"
    elif score >= 20:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return score, risk, detected


if st.button("🔍 Analyse Claim", type="primary"):

    if not claim.strip():
        st.warning("Please enter a financial claim first.")

    else:
        score, risk, detected = analyze_claim(claim)

        st.markdown("---")
        st.header("📊 Analysis Results")

        col1, col2, col3 = st.columns(3)

        col1.metric("Risk Score", f"{score}/100")

        col2.metric("Risk Level", risk)

        col3.metric(
            "Warning Indicators",
            len(detected)
        )

        st.progress(score / 100)

        if risk == "HIGH":
            st.error("🚨 High Risk: Several suspicious indicators were detected.")

        elif risk == "MEDIUM":
            st.warning("⚠️ Medium Risk: Some suspicious indicators were detected.")

        else:
            st.success("✅ Low Risk: Few or no suspicious indicators were detected.")

        st.subheader("🔎 Detected Indicators")

        if detected:
            for item in detected:
                st.write("⚠️", item)

        else:
            st.write("No suspicious phrases from the screening rules were detected.")

        st.subheader("📝 Explanation")

        if detected:
            st.write(
                "The claim contains language associated with potentially "
                "misleading financial promotions. These indicators do not "
                "prove that the claim is false, but they warrant further verification."
            )
        else:
            st.write(
                "The screening rules did not identify common suspicious phrases. "
                "This does not establish that the claim is genuine or safe."
            )

        st.subheader("🌐 Verify Sources")

        from urllib.parse import quote_plus

        search_query = quote_plus(claim)

        st.markdown(
            f"[🔎 Search this claim on Google](https://www.google.com/search?q={search_query})"
        )

        st.markdown(
            f"[📰 Search financial news](https://www.google.com/search?q={search_query}+financial+news)"
        )

        st.markdown(
            f"[🏛️ Search government sources](https://www.google.com/search?q={search_query}+site%3Agov.in)"
        )

        st.subheader("🌊 Misinformation Spread Pathway")

        st.caption(
            "Illustrative pathway only — this is not actual tracking of the claim."
        )

        stages = [
            "Original Message",
            "Social Media Sharing",
            "Forwarded Messages",
            "Investor Exposure"
        ]

        for i, stage in enumerate(stages):
            st.write(f"**{i + 1}.** {stage}")

            if i < len(stages) - 1:
                st.write("⬇️")

        st.subheader("🛡️ Safety Recommendations")

        recommendations = [
            "Verify investment claims using official financial sources.",
            "Avoid investments promising guaranteed or unusually high returns.",
            "Do not share OTPs, passwords, or sensitive banking information.",
            "Check whether financial intermediaries are registered with the appropriate regulator.",
            "Do not transfer money based solely on forwarded messages."
        ]

        for recommendation in recommendations:
            st.markdown(f"- {recommendation}")

        st.markdown("---")

        st.caption(
            "FinShield AI is an experimental screening tool. "
            "Its rule-based score is not a factual verdict, a financial "
            "recommendation, or a substitute for independent verification."
        )

st.markdown("---")

st.caption("FinShield AI | AI in Cybersecurity & FinTech Hackathon")
# --- Rumour Spread Network ---
st.markdown("---")
st.header("🌐 Financial Rumour Spread Network")
st.caption("Illustrative visualization of how a suspicious financial claim may travel between sources.")

st.markdown("""
<div style="background:#0b1728; border:1px solid #234567;
border-radius:18px; padding:20px; overflow-x:auto;">

<svg viewBox="0 0 700 340" width="100%"
xmlns="http://www.w3.org/2000/svg">

<!-- Connections -->
<g stroke="#38bdf8" stroke-width="2" opacity="0.65">
<line x1="350" y1="55" x2="170" y2="145"/>
<line x1="350" y1="55" x2="520" y2="145"/>
<line x1="170" y1="145" x2="100" y2="260"/>
<line x1="170" y1="145" x2="300" y2="260"/>
<line x1="520" y1="145" x2="420" y2="260"/>
<line x1="520" y1="145" x2="600" y2="260"/>
<line x1="300" y1="260" x2="420" y2="260"/>
</g>

<!-- Nodes -->
<g>
<circle cx="350" cy="55" r="38" fill="#2563eb"/>
<circle cx="170" cy="145" r="34" fill="#0ea5e9"/>
<circle cx="520" cy="145" r="34" fill="#0ea5e9"/>
<circle cx="100" cy="260" r="30" fill="#334155"/>
<circle cx="300" cy="260" r="30" fill="#334155"/>
<circle cx="420" cy="260" r="30" fill="#334155"/>
<circle cx="600" cy="260" r="30" fill="#334155"/>
</g>

<!-- Labels -->
<g fill="white" font-size="13" text-anchor="middle"
font-family="Arial">
<text x="350" y="60">Origin</text>
<text x="170" y="150">Source A</text>
<text x="520" y="150">Source B</text>
<text x="100" y="265">User 1</text>
<text x="300" y="265">User 2</text>
<text x="420" y="265">User 3</text>
<text x="600" y="265">User 4</text>
</g>

</svg>
</div>
""", unsafe_allow_html=True)

st.info("This is an illustrative network. It does not represent real social-media transmission data.")