import streamlit as st

def load_css():



    # =========================
    # GLOBAL UI STYLING
    # =========================

    st.markdown("""
    <style>
                
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {

        font-family: 'Inter', sans-serif !important;
    }
                

    /* ======================================================
    MAIN APP
    ====================================================== */

    .main {
        background-color: #050816;
    }

    /* ======================================================
    SIDEBAR
    ====================================================== */

    section[data-testid="stSidebar"] {

        background: linear-gradient(
            180deg,
            #0F172A 0%,
            #111827 45%,
            #1E293B 100%
        );

        border-right: 1px solid rgba(255,255,255,0.06);
    }

    /* Sidebar Scrollbar */

    section[data-testid="stSidebar"] ::-webkit-scrollbar {
        width: 6px;
    }

    section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
        background: rgba(255,255,255,0.15);
        border-radius: 10px;
    }

    /* Sidebar Text */

    section[data-testid="stSidebar"] * {
        color: white;
    }

 /* ======================================================
ACTUAL WORKING KPI CARDS
====================================================== */

div[data-testid="stMetric"] {

    background: linear-gradient(
        135deg,
        rgba(17,24,39,0.96),
        rgba(30,41,59,0.94)
    ) !important;

    border: 1px solid rgba(255,255,255,0.08) !important;

    border-radius: 28px !important;

    padding: 22px 24px !important;

    box-shadow:
        0 12px 28px rgba(0,0,0,0.26),
        inset 0 1px 0 rgba(255,255,255,0.04);

    transition: all 0.25s ease !important;

    position: relative;

    overflow: hidden;

    min-height: 140px;
}

/* top accent glow */

div[data-testid="stMetric"]::before {

    content: "";

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 4px;

    background: linear-gradient(
        90deg,
        #3B82F6,
        #60A5FA
    );
}

/* hover */

div[data-testid="stMetric"]:hover {

    transform: translateY(-6px);

    border: 1px solid rgba(96,165,250,0.20) !important;

    box-shadow:
        0 18px 35px rgba(0,0,0,0.30),
        0 0 20px rgba(59,130,246,0.12);
}

/* label */

label[data-testid="stMetricLabel"] {

    color: #94A3B8 !important;

    font-size: 14px !important;

    font-weight: 500 !important;

    letter-spacing: -0.2px;

    margin-bottom: 12px !important;

    font-family: 'Inter', sans-serif !important;
}

/* value */

div[data-testid="stMetricValue"] {

    font-size: 42px !important;

    font-weight: 750 !important;

    letter-spacing: -1.4px;

    color: white !important;

    font-family: 'Inter', sans-serif !important;
}


    /* ======================================================
    HEADERS
    ====================================================== */

    h1, h2, h3 {

        color: white;

        font-weight: 800;
    }

    /* ======================================================
    TABS
    ====================================================== */

    button[data-baseweb="tab"] {

        font-size: 16px;

        font-weight: 600;

        border-radius: 12px;

        padding: 10px 18px;

        transition: 0.3s ease;
    }

    /* Selected Tab */

    button[data-baseweb="tab"][aria-selected="true"] {

        background-color: #2563EB !important;

        color: white !important;
    }

    /* ======================================================
    INFO / SUCCESS / WARNING BOXES
    ====================================================== */

    .stAlert {

        border-radius: 18px;

        padding: 18px;

        border: none;
    }

    /* ======================================================
    DATAFRAMES
    ====================================================== */

    [data-testid="stDataFrame"] {

        border-radius: 16px;

        overflow: hidden;

        border: 1px solid rgba(255,255,255,0.06);
    }

    /* ======================================================
    BUTTONS
    ====================================================== */

    .stButton>button {

        border-radius: 12px;

        padding: 10px 20px;

        font-weight: 700;

        background: linear-gradient(
            90deg,
            #2563EB 0%,
            #3B82F6 100%
        );

        color: white;

        border: none;

        transition: 0.3s ease;
    }

    /* Button Hover */

    .stButton>button:hover {

        transform: translateY(-2px);

        box-shadow:
            0px 8px 18px rgba(59,130,246,0.35);
    }

    /* ======================================================
    DOWNLOAD BUTTON
    ====================================================== */

    .stDownloadButton>button {

        border-radius: 12px;

        background: linear-gradient(
            90deg,
            #059669 0%,
            #10B981 100%
        );

        color: white;

        font-weight: 700;

        border: none;
    }

    /* Download Hover */

    .stDownloadButton>button:hover {

        transform: translateY(-2px);

        box-shadow:
            0px 8px 18px rgba(16,185,129,0.35);
    }

    /* ======================================================
    CHART SPACING
    ====================================================== */

    .element-container {

        margin-bottom: 1rem;
    }

    /* ======================================================
    SECTION SEPARATORS
    ====================================================== */

    hr {

        margin-top: 2rem;

        margin-bottom: 2rem;

        border: 0;

        border-top: 1px solid rgba(255,255,255,0.08);
    }

    /* ======================================================
    PREMIUM SELECTBOX
    ====================================================== */

    div[data-baseweb="select"] {

        background: rgba(255,255,255,0.06);

        border-radius: 14px;

        border: 1px solid rgba(255,255,255,0.08);

        transition: 0.3s ease;

        margin-top: 8px;
    }

    div[data-baseweb="select"]:hover {

        border: 1px solid #3B82F6;

        box-shadow:
            0px 0px 14px rgba(59,130,246,0.35);
    }

    div[data-baseweb="select"] * {

        color: white !important;
    }

        

    /* ======================================================
    DATAFRAME TEXT
    ====================================================== */

    [data-testid="stDataFrame"] * {

        color: white !important;
    }
                
    thead tr th {
        background: linear-gradient(
            90deg,
            #111827 0%,
            #1F2937 100%
        ) !important;

        color: white !important;

        font-weight: 700 !important;
    }

    /* ======================================================
    GLOBAL FONT
    ====================================================== */
                
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }
    
   html {
    scroll-behavior: smooth;
}
                
/* ======================================
NAVIGATOR GLASS CARD
====================================== */

.nav-glass-card {

    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.03)
    );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    padding: 24px 22px;

    margin-top: 18px;
    margin-bottom: 18px;

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    box-shadow:
        0 10px 35px rgba(0,0,0,0.22),
        inset 0 1px 0 rgba(255,255,255,0.05);
}

.nav-title {
    color: white;
    font-size: 30px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 12px;
}

.nav-subtitle {
    color: #94A3B8;
    font-size: 13px;
    line-height: 1.8;
}
                
/* ==========================================
NUCLEAR SIDEBAR NAV FIX
========================================== */

/* each navigation card */

section[data-testid="stSidebar"]
label[data-baseweb="radio"] {

    background: rgba(255,255,255,0.06) !important;

    border: 1px solid rgba(255,255,255,0.10) !important;

    border-radius: 24px !important;

    padding: 18px 18px !important;

    margin-bottom: 12px !important;

    box-shadow:
        0 10px 24px rgba(0,0,0,0.25),
        inset 0 1px 0 rgba(255,255,255,0.05) !important;

    transition: all 0.25s ease !important;

    display: flex !important;
}

/* hover */

section[data-testid="stSidebar"]
label[data-baseweb="radio"]:hover {

    transform: translateX(4px);

    border: 1px solid rgba(168,85,247,0.30) !important;

    background: rgba(168,85,247,0.10) !important;
}

/* selected */

section[data-testid="stSidebar"]
label[data-baseweb="radio"]:has(input:checked) {

    background: linear-gradient(
        135deg,
        rgba(59,130,246,0.18),
        rgba(96,165,250,0.10)
    ) !important;

    border: 1px solid rgba(96,165,250,0.35) !important;

    box-shadow:
        0 0 0 1px rgba(96,165,250,0.12),
        0 0 20px rgba(59,130,246,0.18),
        inset 0 1px 0 rgba(255,255,255,0.04) !important;

    transform: translateX(4px);
}
                
/* text */

section[data-testid="stSidebar"]
label[data-baseweb="radio"] p {

    color: white !important;

    font-size: 16px !important;

    font-weight: 650 !important;
}
                
/* ==========================================
PREMIUM CONTENT SECTIONS
========================================== */

.glass-section {

    background: linear-gradient(
        135deg,
        rgba(17,24,39,0.92),
        rgba(30,41,59,0.92)
    );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 26px;

    margin-top: 20px;
    margin-bottom: 24px;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.22),
        inset 0 1px 0 rgba(255,255,255,0.04);
}
                
/* ======================================================
PREMIUM CHART CONTAINERS
====================================================== */

[data-testid="stPlotlyChart"],
[data-testid="stPyplot"] {

    background: linear-gradient(
        135deg,
        rgba(17,24,39,0.95),
        rgba(30,41,59,0.92)
    ) !important;

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 28px;

    padding: 16px;

    box-shadow:
        0 12px 28px rgba(0,0,0,0.25);

    margin-top: 10px;
    margin-bottom: 14px;
}
                
/* ======================================================
PREMIUM DASHBOARD HEADERS
====================================================== */

/* heading container */

[data-testid="stHeading"] {

    display: flex !important;

    justify-content: center !important;

    align-items: center !important;

    text-align: center !important;

    margin-top: 14px !important;
    margin-bottom: 26px !important;

    animation: fadeUp 0.7s ease;
}

/* h1 */

[data-testid="stHeading"] h1 {

    font-size: 3rem !important;

    font-weight: 800 !important;

    letter-spacing: -2px !important;

    color: white !important;

    position: relative;

    text-align: center !important;

    background: linear-gradient(
        180deg,
        #FFFFFF,
        #CBD5E1
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 18px rgba(96,165,250,0.10);
}

/* h2 */

[data-testid="stHeading"] h2 {

    font-size: 2.25rem !important;

    font-weight: 780 !important;

    letter-spacing: -1.8px !important;

    color: white !important;

    position: relative;

    text-align: center !important;

    background: linear-gradient(
        180deg,
        #FFFFFF,
        #CBD5E1
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* h3 */

[data-testid="stHeading"] h3 {

    font-size: 1.8rem !important;

    font-weight: 720 !important;

    letter-spacing: -1.2px !important;

    text-align: center !important;

    position: relative;

    background: linear-gradient(
        180deg,
        #FFFFFF,
        #CBD5E1
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* premium underline */

[data-testid="stHeading"] h1::after,
[data-testid="stHeading"] h2::after,
[data-testid="stHeading"] h3::after {

    content: "";

    position: absolute;

    left: 50%;
    transform: translateX(-50%);

    bottom: -10px;

    width: 80px;
    height: 4px;

    border-radius: 999px;

    background: linear-gradient(
        90deg,
        rgba(59,130,246,0.2),
        rgba(96,165,250,0.95),
        rgba(59,130,246,0.2)
    );

    box-shadow:
        0 0 18px rgba(96,165,250,0.25);
}

/* smooth entrance */

@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(18px);
    }

    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* ======================================================
PREMIUM FILE UPLOADER
====================================================== */

/* upload section spacing */

[data-testid="stFileUploader"] {

    background: linear-gradient(
        135deg,
        rgba(17,24,39,0.95),
        rgba(30,41,59,0.92)
    );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 22px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.26),
        inset 0 1px 0 rgba(255,255,255,0.04);

    transition: all 0.3s ease;

    position: relative;

    overflow: hidden;

    margin-bottom: 22px;
}

/* subtle top glow */

[data-testid="stFileUploader"]::before {

    content: "";

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 4px;

    background: linear-gradient(
        90deg,
        #8B5CF6,
        #3B82F6
    );
}

/* hover */

[data-testid="stFileUploader"]:hover {

    transform: translateY(-4px);

    border: 1px solid rgba(96,165,250,0.18);

    box-shadow:
        0 18px 35px rgba(0,0,0,0.30),
        0 0 18px rgba(59,130,246,0.10);
}

/* upload button */

[data-testid="stFileUploader"] button {

    background: linear-gradient(
        135deg,
        rgba(59,130,246,0.18),
        rgba(139,92,246,0.18)
    ) !important;

    border: 1px solid rgba(255,255,255,0.10) !important;

    border-radius: 18px !important;

    color: white !important;

    font-weight: 600 !important;

    padding: 12px 22px !important;

    transition: all 0.25s ease !important;
}

[data-testid="stFileUploader"] button:hover {

    transform: translateY(-2px);

    border: 1px solid rgba(96,165,250,0.22) !important;

    box-shadow:
        0 0 18px rgba(59,130,246,0.18);
}

    /* ======================================================
REUSABLE UI CLASSES
====================================================== */

.glass-card {

    background: rgba(255,255,255,0.03);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 28px;
}

.executive-shell {

    background: linear-gradient(
        135deg,
        rgba(17,24,39,0.95),
        rgba(30,41,59,0.92)
    );

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 34px;

    padding: 34px;
}

.signal-chip {

    border-radius: 999px;

    padding: 10px 18px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);
}
                
/* Remove black upload box background */
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* Remove inner dark container */
section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] > div {
    background: transparent !important;
    border: none !important;
}

/* Make upload button cleaner */
section[data-testid="stSidebar"] button[kind="secondary"] {
    border-radius: 24px !important;
    background: rgba(99,102,241,0.12) !important;
    border: 1px solid rgba(129,140,248,0.25) !important;
}
                            
    </style>
    """, unsafe_allow_html=True)


