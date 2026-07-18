"""Global CSS for the Workforce Intelligence dashboard.

Colors are pulled from `frontend.theme` so the stylesheet and the charts
never drift out of sync. Streamlit has no first-class theming API for this
level of detail, so injecting CSS via `st.markdown` is the supported
escape hatch for a custom, "SaaS product" look.
"""

import streamlit as st

from frontend.theme import (
    BG_PAGE,
    BG_SURFACE,
    BG_SURFACE_ALT,
    BORDER,
    BORDER_STRONG,
    INK_MUTED,
    INK_SECONDARY,
    STATUS_CRITICAL,
    STATUS_GOOD,
    STATUS_WARNING,
)


def load_css():
    st.markdown(
        f"""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        :root {{
            --bg-page: {BG_PAGE};
            --bg-surface: {BG_SURFACE};
            --bg-surface-alt: {BG_SURFACE_ALT};
            --border: {BORDER};
            --border-strong: {BORDER_STRONG};
            --ink-secondary: {INK_SECONDARY};
            --ink-muted: {INK_MUTED};
            --status-good: {STATUS_GOOD};
            --status-warning: {STATUS_WARNING};
            --status-critical: {STATUS_CRITICAL};
            --accent-blue: #60A5FA;
            --accent-violet: #A78BFA;
        }}

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif !important;
        }}

        /* ==================================================
        BASE LAYOUT
        ================================================== */

        /* Streamlit's actual solid-background element is [data-testid="stApp"]
        (the ".main" class from older Streamlit versions no longer exists) —
        style it directly and keep every wrapper above it transparent so the
        dark page color is never hidden behind Streamlit's own light theme. */
        [data-testid="stApp"] {{
            background-color: var(--bg-page) !important;
        }}

        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        [data-testid="stHeader"] {{
            background-color: transparent !important;
        }}

        .main {{
            background-color: var(--bg-page);
        }}

        .block-container {{
            padding: 2rem 2.5rem 3rem 2.5rem;
            max-width: 1440px;
        }}

        #MainMenu, footer {{
            visibility: hidden;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        hr {{
            margin: 2rem 0;
            border: 0;
            border-top: 1px solid var(--border);
        }}

        .element-container {{
            margin-bottom: 1rem;
        }}

        /* ==================================================
        SIDEBAR
        ================================================== */

        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #0F172A 0%, #111827 45%, #1E293B 100%);
            border-right: 1px solid var(--border);
        }}

        section[data-testid="stSidebar"] * {{
            color: white;
        }}

        section[data-testid="stSidebar"] ::-webkit-scrollbar {{
            width: 6px;
        }}

        section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {{
            background: rgba(255,255,255,0.15);
            border-radius: 10px;
        }}

        section[data-testid="stSidebar"] label[data-baseweb="radio"] {{
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid var(--border-strong) !important;
            border-radius: 20px !important;
            padding: 16px 18px !important;
            margin-bottom: 10px !important;
            transition: all 0.2s ease !important;
            display: flex !important;
        }}

        section[data-testid="stSidebar"] label[data-baseweb="radio"]:hover {{
            transform: translateX(4px);
            border: 1px solid rgba(168,85,247,0.35) !important;
            background: rgba(168,85,247,0.10) !important;
        }}

        section[data-testid="stSidebar"] label[data-baseweb="radio"]:has(input:checked) {{
            background: linear-gradient(135deg, rgba(59,130,246,0.20), rgba(96,165,250,0.10)) !important;
            border: 1px solid rgba(96,165,250,0.40) !important;
            box-shadow: 0 0 20px rgba(59,130,246,0.18);
            transform: translateX(4px);
        }}

        section[data-testid="stSidebar"] label[data-baseweb="radio"] p {{
            font-size: 15px !important;
            font-weight: 650 !important;
        }}

        section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"],
        section[data-testid="stSidebar"] [data-testid="stFileUploaderDropzone"] > div {{
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }}

        section[data-testid="stSidebar"] button[kind="secondary"] {{
            border-radius: 20px !important;
            background: rgba(99,102,241,0.14) !important;
            border: 1px solid rgba(129,140,248,0.28) !important;
        }}

        /* ==================================================
        TYPOGRAPHY / HEADINGS
        ================================================== */

        h1, h2, h3 {{
            color: white;
            font-weight: 800;
        }}

        [data-testid="stHeading"] {{
            margin-top: 6px !important;
            margin-bottom: 18px !important;
        }}

        /* ==================================================
        PAGE HEADER (hero banner)
        ================================================== */

        .page-header {{
            background: linear-gradient(135deg, rgba(15,23,42,0.95), rgba(30,41,59,0.88));
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 30px 36px;
            margin-bottom: 28px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 24px;
            flex-wrap: wrap;
            box-shadow: 0 12px 30px rgba(0,0,0,0.20);
        }}

        .ph-eyebrow {{
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1.4px;
            text-transform: uppercase;
            color: var(--accent-violet);
            margin-bottom: 10px;
        }}

        .ph-title {{
            font-size: 32px;
            font-weight: 750;
            color: white;
            letter-spacing: -0.8px;
            margin-bottom: 12px;
        }}

        .ph-description {{
            font-size: 16px;
            line-height: 1.75;
            color: var(--ink-secondary);
            max-width: 760px;
        }}

        .ph-badge {{
            padding: 10px 18px;
            border-radius: 999px;
            background: color-mix(in srgb, var(--badge-color) 14%, transparent);
            border: 1px solid color-mix(in srgb, var(--badge-color) 30%, transparent);
            color: var(--badge-color);
            font-size: 14px;
            font-weight: 600;
            white-space: nowrap;
        }}

        /* ==================================================
        SECTION TITLES
        ================================================== */

        .section-title-block {{
            background: linear-gradient(135deg, rgba(17,24,39,0.95), rgba(30,41,59,0.90));
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 16px 24px;
            margin: 10px 0 18px 0;
            box-shadow: 0 8px 20px rgba(0,0,0,0.18);
        }}

        .section-title {{
            font-size: 20px;
            font-weight: 750;
            color: white;
            letter-spacing: -0.4px;
            line-height: 1.3;
        }}

        .section-subtitle {{
            font-size: 14px;
            color: var(--ink-muted);
            margin-top: 4px;
            line-height: 1.5;
        }}

        .soft-divider {{
            height: 1px;
            background: linear-gradient(90deg, rgba(96,165,250,0), rgba(96,165,250,0.55), rgba(96,165,250,0));
            margin: 30px 0;
        }}

        /* ==================================================
        BADGES
        ================================================== */

        .status-badge {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 999px;
            background: color-mix(in srgb, var(--badge-color) 12%, transparent);
            border: 1px solid color-mix(in srgb, var(--badge-color) 28%, transparent);
            color: var(--badge-color);
            font-size: 13px;
            font-weight: 700;
        }}

        /* ==================================================
        KPI CARDS
        ================================================== */

        .kpi-card {{
            background: linear-gradient(135deg, rgba(17,24,39,0.96), rgba(30,41,59,0.94));
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 20px 22px;
            min-height: 128px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 24px rgba(0,0,0,0.22);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }}

        .kpi-card::before {{
            content: "";
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 3px;
            background: var(--kpi-accent);
        }}

        .kpi-card:hover {{
            transform: translateY(-4px);
            border-color: color-mix(in srgb, var(--kpi-accent) 40%, transparent);
        }}

        .kpi-top {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 14px;
        }}

        .kpi-icon {{
            font-size: 16px;
        }}

        .kpi-label {{
            font-size: 13px;
            font-weight: 600;
            color: var(--ink-muted);
        }}

        .kpi-value {{
            font-size: 32px;
            font-weight: 750;
            color: white;
            letter-spacing: -1px;
            line-height: 1.1;
        }}

        .kpi-sub {{
            font-size: 13px;
            color: var(--kpi-accent);
            font-weight: 600;
            margin-top: 8px;
        }}

        /* Native st.metric — still used in a couple of spots; keep it
        visually aligned with the custom KPI cards above. */

        div[data-testid="stMetric"] {{
            background: linear-gradient(135deg, rgba(17,24,39,0.96), rgba(30,41,59,0.94)) !important;
            border: 1px solid var(--border) !important;
            border-radius: 22px !important;
            padding: 20px 22px !important;
            box-shadow: 0 10px 24px rgba(0,0,0,0.22);
            transition: transform 0.2s ease !important;
        }}

        div[data-testid="stMetric"]:hover {{
            transform: translateY(-4px);
        }}

        label[data-testid="stMetricLabel"] {{
            color: var(--ink-muted) !important;
            font-size: 13px !important;
            font-weight: 600 !important;
        }}

        div[data-testid="stMetricValue"] {{
            font-size: 32px !important;
            font-weight: 750 !important;
            letter-spacing: -1px;
            color: white !important;
        }}

        /* ==================================================
        PROGRESS BARS
        ================================================== */

        .progress-track {{
            width: 100%;
            height: 10px;
            background: rgba(255,255,255,0.08);
            border-radius: 999px;
            overflow: hidden;
            margin: 12px 0 4px 0;
        }}

        .progress-fill {{
            height: 100%;
            border-radius: 999px;
        }}

        /* ==================================================
        STAT ROWS (icon + title/subtitle + value)
        ================================================== */

        .stat-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 16px;
            padding: 6px 0;
        }}

        .stat-row-left {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}

        .stat-icon {{
            width: 56px;
            height: 56px;
            min-width: 56px;
            border-radius: 50%;
            border: 2px solid color-mix(in srgb, var(--stat-color) 45%, transparent);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: var(--stat-color);
        }}

        .stat-title {{
            font-size: 16px;
            font-weight: 700;
            color: white;
        }}

        .stat-subtitle {{
            font-size: 13px;
            color: var(--ink-muted);
            margin-top: 2px;
        }}

        .stat-row-right {{
            text-align: right;
        }}

        .stat-value {{
            font-size: 28px;
            font-weight: 800;
            line-height: 1;
        }}

        .stat-caption {{
            font-size: 12px;
            color: var(--ink-muted);
            margin-top: 4px;
        }}

        .stat-row-hr {{
            border-top: 1px solid var(--border);
            margin: 14px 0;
        }}

        /* ==================================================
        RING METRICS (conic-gradient donuts)
        ================================================== */

        .ring-metric {{
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
        }}

        .ring-outer {{
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .ring-inner {{
            border-radius: 50%;
            background: var(--bg-page);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            color: white;
            line-height: 1.2;
        }}

        .ring-caption {{
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            color: #93C5FD;
            margin-top: 2px;
        }}

        .ring-label {{
            font-size: 12px;
            font-weight: 700;
            color: var(--ink-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* ==================================================
        GENERIC SURFACES
        ================================================== */

        .glass-card,
        div[class*="st-key-glasscard_"] {{
            background: linear-gradient(135deg, rgba(17,24,39,0.95), rgba(30,41,59,0.92)) !important;
            border: 1px solid var(--border) !important;
            border-radius: 26px !important;
            padding: 28px !important;
            box-shadow: 0 12px 28px rgba(0,0,0,0.22) !important;
        }}

        .card-eyebrow {{
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1.4px;
            text-transform: uppercase;
            margin-bottom: 14px;
        }}

        .card-title {{
            font-size: 18px;
            font-weight: 750;
            color: white;
            letter-spacing: -0.2px;
            margin-bottom: 16px;
        }}

        /* ==================================================
        EXECUTIVE CARD (position / signal / assessment boxes)
        ================================================== */

        .exec-card {{
            background: linear-gradient(135deg, rgba(17,24,39,0.95), rgba(30,41,59,0.92));
            border: 1px solid var(--border);
            border-radius: 26px;
            padding: 32px 36px;
            height: 100%;
        }}

        .exec-card-tinted {{
            background: color-mix(in srgb, var(--exec-accent) 8%, transparent);
            border: 1px solid color-mix(in srgb, var(--exec-accent) 22%, transparent);
        }}

        .exec-eyebrow {{
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1.6px;
            text-transform: uppercase;
            margin-bottom: 16px;
        }}

        .exec-eyebrow-row {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
        }}

        .exec-eyebrow-row .exec-eyebrow {{
            margin-bottom: 0;
        }}

        .exec-dot {{
            width: 10px;
            height: 10px;
            min-width: 10px;
            border-radius: 50%;
        }}

        .exec-title {{
            font-size: 30px;
            font-weight: 800;
            color: white;
            line-height: 1.2;
            margin-bottom: 16px;
        }}

        .exec-text {{
            font-size: 16px;
            line-height: 1.8;
            color: var(--ink-secondary);
            max-width: 780px;
        }}

        .exec-badges {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-top: 24px;
        }}

        /* ==================================================
        METRIC LINE (label/value row, optional progress bar)
        ================================================== */

        .metric-line {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}

        .metric-line-label {{
            color: var(--ink-secondary);
            font-weight: 600;
        }}

        .metric-line-value {{
            font-weight: 800;
        }}

        .metric-line-sm .metric-line-label,
        .metric-line-sm .metric-line-value {{
            font-size: 14px;
        }}

        .metric-line-lg .metric-line-label {{
            font-size: 15px;
        }}

        .metric-line-lg .metric-line-value {{
            font-size: 22px;
        }}

        /* ==================================================
        TABS / ALERTS / DATAFRAMES / CHARTS
        ================================================== */

        button[data-baseweb="tab"] {{
            font-size: 15px;
            font-weight: 600;
            border-radius: 12px;
            padding: 10px 18px;
        }}

        button[data-baseweb="tab"][aria-selected="true"] {{
            background-color: #2563EB !important;
            color: white !important;
        }}

        .stAlert {{
            border-radius: 18px;
            padding: 18px;
            border: none;
        }}

        [data-testid="stDataFrame"] {{
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--border);
        }}

        [data-testid="stDataFrame"] * {{
            color: white !important;
        }}

        thead tr th {{
            background: linear-gradient(90deg, #111827 0%, #1F2937 100%) !important;
            color: white !important;
            font-weight: 700 !important;
        }}

        [data-testid="stPlotlyChart"],
        [data-testid="stPyplot"] {{
            background: linear-gradient(135deg, rgba(17,24,39,0.95), rgba(30,41,59,0.92)) !important;
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 14px;
            box-shadow: 0 12px 26px rgba(0,0,0,0.22);
        }}

        /* ==================================================
        BUTTONS
        ================================================== */

        .stButton>button {{
            border-radius: 12px;
            padding: 10px 20px;
            font-weight: 700;
            background: linear-gradient(90deg, #2563EB 0%, #3B82F6 100%);
            color: white;
            border: none;
            transition: 0.2s ease;
        }}

        .stButton>button:hover {{
            transform: translateY(-2px);
            box-shadow: 0px 8px 18px rgba(59,130,246,0.35);
        }}

        .stDownloadButton>button {{
            border-radius: 12px;
            background: linear-gradient(90deg, #059669 0%, #10B981 100%);
            color: white;
            font-weight: 700;
            border: none;
        }}

        /* ==================================================
        SELECT / SLIDER INPUTS
        ================================================== */

        div[data-baseweb="select"] {{
            background: rgba(255,255,255,0.06);
            border-radius: 14px;
            border: 1px solid var(--border);
            transition: 0.2s ease;
        }}

        div[data-baseweb="select"]:hover {{
            border: 1px solid #3B82F6;
            box-shadow: 0px 0px 14px rgba(59,130,246,0.30);
        }}

        div[data-baseweb="select"] * {{
            color: white !important;
            background: transparent !important;
        }}

        /* ==================================================
        FOOTER
        ================================================== */

        .app-footer {{
            text-align: center;
            padding: 28px 0 12px 0;
            color: var(--ink-muted);
            font-size: 13px;
        }}

        .app-footer-dot {{
            margin: 0 8px;
            opacity: 0.5;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )
