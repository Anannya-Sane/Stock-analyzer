import streamlit as st
from metrics import get_stock_metrics

st.set_page_config(page_title="Stock Analyzer", page_icon="📊", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

header[data-testid="stHeader"] { display: none !important; }
#MainMenu { display: none !important; }
footer { display: none !important; }
.block-container { padding-top: 2.5rem !important; padding-bottom: 2rem !important; }
div[data-testid="column"] { padding: 0 4px !important; }

.sa-title { font-size: 28px; font-weight: 800; color: #111827; margin: 0 0 2px; letter-spacing: -0.3px; line-height: 1.4; }
.sa-title span { color: #4f46e5; }
.sa-sub { font-size: 14px; color: #6b7280; margin: 0 0 20px; }

.sa-hint { font-size: 11px; color: #9ca3af; margin: 2px 0 8px; }
.examples-label { font-size: 10px; font-weight: 700; color: #9ca3af; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 6px; }
.search-examples { display: flex; gap: 6px; flex-wrap: wrap; }
.search-chip { font-size: 11px; background: #f0f4ff; color: #6366f1; border: 1.5px solid #c7d2fe; border-radius: 20px; padding: 3px 10px; font-weight: 600; }

.sa-company { font-size: 20px; font-weight: 700; color: #111827; margin: 0 0 6px; }
.sa-tags { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 14px; }
.sa-tag { font-size: 11px; background: #f3f4f6; color: #6b7280; border: 1px solid #e5e7eb; border-radius: 20px; padding: 3px 10px; }

.sa-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px;
}
@media (max-width: 768px) {
    .sa-grid { grid-template-columns: 1fr !important; }
}

.sa-card { border-radius: 14px; padding: 14px 16px; display: flex; flex-direction: column; }
.card-blue   { background: #eff6ff; border: 1.5px solid #bfdbfe; }
.card-purple { background: #f5f3ff; border: 1.5px solid #ddd6fe; }
.card-green  { background: #f0fdf4; border: 1.5px solid #bbf7d0; }
.card-amber  { background: #fffbeb; border: 1.5px solid #fde68a; }

.sa-card-head { display: flex; align-items: center; gap: 8px; padding-bottom: 8px; margin-bottom: 2px; }
.sa-card-icon { width: 30px; height: 30px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 15px; flex-shrink: 0; }
.icon-blue   { background: #dbeafe; }
.icon-purple { background: #ede9fe; }
.icon-green  { background: #dcfce7; }
.icon-amber  { background: #fef3c7; }

.sa-card-title-blue   { font-size: 14px; font-weight: 700; color: #1d4ed8; }
.sa-card-title-purple { font-size: 14px; font-weight: 700; color: #6d28d9; }
.sa-card-title-green  { font-size: 14px; font-weight: 700; color: #15803d; }
.sa-card-title-amber  { font-size: 14px; font-weight: 700; color: #b45309; }

.sa-divider-blue   { border: none; border-top: 1.5px solid #bfdbfe; margin: 0 0 4px; }
.sa-divider-purple { border: none; border-top: 1.5px solid #ddd6fe; margin: 0 0 4px; }
.sa-divider-green  { border: none; border-top: 1.5px solid #bbf7d0; margin: 0 0 4px; }
.sa-divider-amber  { border: none; border-top: 1.5px solid #fde68a; margin: 0 0 4px; }

.sa-row { display: flex; align-items: flex-start; justify-content: space-between; padding: 6px 0; gap: 8px; border-bottom: 1px solid rgba(0,0,0,0.05); }
.sa-row:last-child { border-bottom: none; padding-bottom: 0; }
.sa-row-left { flex: 1; min-width: 0; }
.sa-row-right { flex-shrink: 0; display: flex; flex-direction: column; align-items: flex-end; gap: 2px; }
.sa-row-label { font-size: 13px; color: #374151; font-weight: 500; line-height: 1.3; }
.sa-row-hint  { font-size: 10px; color: #9ca3af; margin-top: 1px; line-height: 1.2; }
.sa-val { font-size: 13px; font-weight: 700; color: #111827; white-space: nowrap; }

.badge { font-size: 10px; padding: 1px 7px; border-radius: 20px; font-weight: 600; white-space: nowrap; }
.badge-good { background: #dcfce7; color: #15803d; }
.badge-warn { background: #fef3c7; color: #b45309; }
.badge-bad  { background: #fee2e2; color: #dc2626; }

div[data-testid="stTextInput"] input {
    border-radius: 10px !important;
    border: 2px solid #e0e7ff !important;
    background: #f8f7ff !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    padding: 11px 16px !important;
    color: #111827 !important;
    height: 46px !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #6366f1 !important;
    background: #ffffff !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.12) !important;
}
div[data-testid="stTextInput"] input::placeholder {
    color: #a5b4fc !important;
    font-weight: 400 !important;
}
div.stButton > button {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    height: 46px !important;
    padding: 0 24px !important;
    width: 100% !important;
}
div.stButton > button:hover {
    background: linear-gradient(135deg, #4338ca, #6d28d9) !important;
    box-shadow: 0 4px 14px rgba(79,70,229,0.35) !important;
    transform: translateY(-1px) !important;
}
</style>
""", unsafe_allow_html=True)


def badge(val, good_fn, bad_fn, good_label="Good", bad_label="High", warn_label="Fair"):
    if val == "N/A":
        return ""
    try:
        v = float(val)
        if good_fn(v):
            return f'<span class="badge badge-good">✓ {good_label}</span>'
        elif bad_fn(v):
            return f'<span class="badge badge-bad">✗ {bad_label}</span>'
        else:
            return f'<span class="badge badge-warn">~ {warn_label}</span>'
    except:
        return ""

def row(label, value, hint="", badge_html=""):
    return f"""<div class="sa-row">
        <div class="sa-row-left">
            <div class="sa-row-label">{label}</div>
            {'<div class="sa-row-hint">' + hint + '</div>' if hint else ''}
        </div>
        <div class="sa-row-right">
            <span class="sa-val">{value}</span>{badge_html}
        </div>
    </div>"""

def card(color, icon, title, rows_html):
    return f"""<div class="sa-card card-{color}">
        <div class="sa-card-head">
            <div class="sa-card-icon icon-{color}">{icon}</div>
            <span class="sa-card-title-{color}">{title}</span>
        </div>
        <hr class="sa-divider-{color}">
        {rows_html}
    </div>"""

def empty_card(color, icon, title, labels):
    lines = ""
    for label in labels:
        lines += f"""<div class="sa-row">
            <div class="sa-row-left">
                <div class="sa-row-label">{label}</div>
            </div>
            <div class="sa-row-right">
                <span class="sa-val" style="color:#d1d5db;">—</span>
            </div>
        </div>"""
    return f"""<div class="sa-card card-{color}">
        <div class="sa-card-head">
            <div class="sa-card-icon icon-{color}">{icon}</div>
            <span class="sa-card-title-{color}">{title}</span>
        </div>
        <hr class="sa-divider-{color}">
        {lines}
    </div>"""


# ── Header
st.markdown('''
<p class="sa-title">📊 <span>Stock</span> Analyzer</p>
<p class="sa-sub">Fundamental metrics for any NSE or BSE listed stock</p>
''', unsafe_allow_html=True)

# ── Input + button
col_in, col_btn, col_gap = st.columns([3, 0.9, 2])
with col_in:
    ticker_input = st.text_input(
        "",
        placeholder="Enter ticker — e.g. INFY.NS or RELIANCE.NS",
        label_visibility="collapsed"
    )
with col_btn:
    analyze = st.button("🔍 Analyze", use_container_width=True)

# ── Hint + examples
st.markdown("""
<div style="max-width:660px; margin-top:-8px;">
    <p class="sa-hint">NSE: add .NS (e.g. HDFCBANK.NS) &nbsp;·&nbsp; BSE: add .BO (e.g. 500180.BO)</p>
    <div class="examples-label">Try these</div>
    <div class="search-examples">
        <span class="search-chip">INFY.NS</span>
        <span class="search-chip">RELIANCE.NS</span>
        <span class="search-chip">HDFCBANK.NS</span>
        <span class="search-chip">TCS.NS</span>
        <span class="search-chip">WIPRO.NS</span>
        <span class="search-chip">500325.BO</span>
    </div>
</div>
<br>
""", unsafe_allow_html=True)

ticker = ticker_input.upper().strip()

if analyze and ticker:
    with st.spinner("Fetching data..."):
        m = get_stock_metrics(ticker)

    if m["Company"] == "N/A":
        st.error("Could not find this stock. Please check the ticker!")
    else:
        st.markdown(f'<p class="sa-company">{m["Company"]}</p>', unsafe_allow_html=True)
        st.markdown(f'''<div class="sa-tags">
            <span class="sa-tag">🏭 {m["Sector"]}</span>
            <span class="sa-tag">🔬 {m["Industry"]}</span>
            <span class="sa-tag">📍 {ticker}</span>
        </div>''', unsafe_allow_html=True)

        pe      = str(m["P/E Ratio"])
        pb      = str(m["P/B Ratio"])
        roe     = str(m["ROE (%)"])
        pm      = str(m["Profit Margin (%)"])
        rg      = str(m["Revenue Growth (%)"])
        beta    = str(m["Beta"])
        dy      = str(m["Dividend Yield (%)"])
        eps     = str(m["EPS"])
        mc      = f'₹{int(m["Market Cap"]):,}' if m["Market Cap"] != "N/A" else "N/A"
        wk52avg = str(m.get("52 Week Avg", "N/A"))

        price_card = card("blue", "💰", "Price",
            row("Current price",   f'₹{m["Current Price"]}', "Live market price") +
            row("52-week high",    f'₹{m["52 Week High"]}',  "Highest in 1 year") +
            row("52-week low",     f'₹{m["52 Week Low"]}',   "Lowest in 1 year") +
            row("52-week average", f'₹{wk52avg}',            "Average over 1 year")
        )
        val_card = card("purple", "📐", "Valuation",
            row("P/E ratio",  pe,  "Ideal < 20 · Expensive > 35", badge(pe, lambda v: v<20, lambda v: v>35, "Good", "Expensive")) +
            row("P/B ratio",  pb,  "Ideal < 3 · Expensive > 5",   badge(pb, lambda v: v<3,  lambda v: v>5,  "Good", "Expensive")) +
            row("EPS (TTM)", eps,  "Trailing 12 months") +
            row("Market cap", mc,  "Total market value")
        )
        profit_card = card("green", "📈", "Profitability",
            row("ROE",            f'{roe}%', "Ideal > 15% · Weak < 5%",         badge(roe, lambda v: v>15, lambda v: v<5,  "Strong",  "Weak",      "Moderate")) +
            row("Profit margin",  f'{pm}%',  "Trailing 12 months · Ideal > 15%", badge(pm,  lambda v: v>15, lambda v: v<5,  "Strong",  "Weak",      "Moderate")) +
            row("Revenue growth", f'{rg}%',  "Year on year · Ideal > 10%",       badge(rg,  lambda v: v>10, lambda v: v<0,  "Growing", "Declining", "Stable"))   +
            row("Dividend yield", f'{dy}%',  "Annual dividend % of price")
        )
        risk_card = card("amber", "🛡️", "Risk & other",
            row("Beta",     beta,                "< 1 low risk · > 1.5 high risk", badge(beta, lambda v: v<1, lambda v: v>1.5, "Low risk", "High risk", "Moderate")) +
            row("Sector",   str(m["Sector"]),    "Industry classification") +
            row("Industry", str(m["Industry"]),  "Sub-sector") +
            row("Exchange", "NSE / BSE",          "Listed on")
        )

        st.markdown(f'''<div class="sa-grid">
            {price_card}{val_card}{profit_card}{risk_card}
        </div>''', unsafe_allow_html=True)

else:
    ep = empty_card("blue",   "💰", "Price",         ["Current price", "52-week high", "52-week low", "52-week average"])
    ev = empty_card("purple", "📐", "Valuation",     ["P/E ratio", "P/B ratio", "EPS (TTM)", "Market cap"])
    eg = empty_card("green",  "📈", "Profitability",  ["ROE", "Profit margin", "Revenue growth", "Dividend yield"])
    ea = empty_card("amber",  "🛡️", "Risk & other",  ["Beta", "Sector", "Industry", "Exchange"])

    st.markdown(f'''<div class="sa-grid">
        {ep}{ev}{eg}{ea}
    </div>''', unsafe_allow_html=True)
