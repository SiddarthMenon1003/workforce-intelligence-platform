"""Single source of truth for color and spacing tokens.

Both the CSS injected by `styles.py` and the Plotly/Matplotlib charts in the
page modules read from this file, so the dashboard's visual language stays
consistent in one place instead of being redefined per chart.
"""

# ---------------------------------------------------------------------------
# Surfaces & ink (dark theme only — this app does not support light mode)
# ---------------------------------------------------------------------------

BG_PAGE = "#0B1120"
BG_SURFACE = "#111827"
BG_SURFACE_ALT = "#1E293B"

INK_PRIMARY = "#FFFFFF"
INK_SECONDARY = "#CBD5E1"
INK_MUTED = "#94A3B8"
INK_FAINT = "#64748B"

BORDER = "rgba(255,255,255,0.08)"
BORDER_STRONG = "rgba(255,255,255,0.16)"
GRIDLINE = "rgba(255,255,255,0.08)"

# ---------------------------------------------------------------------------
# Status palette — reserved for risk/health states, never reused as a
# generic series color so "red" always means the same thing everywhere.
# ---------------------------------------------------------------------------

STATUS_GOOD = "#22C55E"
STATUS_WARNING = "#F59E0B"
STATUS_CRITICAL = "#EF4444"

RISK_COLORS = {
    "Low Risk": STATUS_GOOD,
    "Moderate Risk": STATUS_WARNING,
    "High Risk": STATUS_CRITICAL,
}

# ---------------------------------------------------------------------------
# Categorical series palette — fixed order, reused across every multi-series
# chart so the same slot always maps to the same hue.
# ---------------------------------------------------------------------------

SERIES = [
    "#60A5FA",  # blue
    "#A78BFA",  # violet
    "#34D399",  # green
    "#FBBF24",  # amber
    "#F87171",  # red
    "#22D3EE",  # cyan
]

# Single-hue sequential ramp (magnitude only — heatmaps, intensity scales)
SEQUENTIAL_BLUE = [
    "#0B1F3A", "#123A66", "#1D4E89", "#2563EB", "#3B82F6", "#60A5FA", "#93C5FD", "#DBEAFE",
]

# ---------------------------------------------------------------------------
# Chart chrome shared by every Plotly figure
# ---------------------------------------------------------------------------

PLOTLY_LAYOUT = dict(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color=INK_SECONDARY, family="Inter, sans-serif"),
    # Generous, fixed margins so the title (top) and legend (bottom) never
    # collide or get clipped within the chart's declared height.
    margin=dict(l=10, r=10, t=56, b=56),
    hoverlabel=dict(
        bgcolor=BG_SURFACE_ALT,
        bordercolor=BORDER_STRONG,
        font=dict(color=INK_PRIMARY, family="Inter, sans-serif"),
    ),
    # Legend sits below the plot area (never above, next to the title) so
    # a wrapping legend can never overlap the title or get cut off.
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        font=dict(color=INK_SECONDARY),
        orientation="h",
        yanchor="top",
        y=-0.22,
        xanchor="left",
        x=0,
    ),
)

PLOTLY_AXIS = dict(
    gridcolor=GRIDLINE,
    zerolinecolor=GRIDLINE,
    linecolor=BORDER_STRONG,
    tickfont=dict(color=INK_MUTED),
    title_font=dict(color=INK_MUTED),
)


def risk_color(label):
    """Map a RiskLevel/risk_label string to its reserved status color."""
    return RISK_COLORS.get(label, STATUS_WARNING)
