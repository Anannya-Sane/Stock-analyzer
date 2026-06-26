import streamlit as st
from datetime import date as dt, timedelta
from metrics import get_stock_metrics

st.set_page_config(page_title="Stock Analyzer", page_icon="📊", layout="wide")

st.markdown("""
<style>
    body { font-family: 'Segoe UI', sans-serif; }

    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0;
    }
    .sub-title {
        font-size: 1rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .company-name {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1a1a2e;
    }
    .sector-tag {
        background: #e8f4fd;
        color: #1565c0;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin: 4px 4px 4px 0;
    }

    /* Quadrant cards with soft pastel backgrounds */
    .card-blue {
        background: #eaf4fb;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        border: 1px solid #d0e8f5;
    }
    .card-purple {
        background: #f3eefb;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        border: 1px solid #ddd0f5;
    }
    .card-green {
        background: #edf7f0;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        border: 1px solid #c8e8cf;
    }
    .card-peach {
        background: #fef6ee;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 16px;
        border: 1px solid #f5dfc8;
    }

    .section-header-blue {
        font-size: 0.95rem;
        font-weight: 700;
        color: #1565c0;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding-bottom: 8px;
        border-bottom: 2px solid #d0e8f5;
        margin-bottom: 12px;
    }
    .section-header-purple {
        font-size: 0.95rem;
        font-weight: 700;
        color: #6a1b9a;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding-bottom: 8px;
        border-bottom: 2px solid #ddd0f5;
        margin-bottom: 12px;
    }
    .section-header-green {
        font-size: 0.95rem;
        font-weight: 700;
        color: #2e7d32;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding-bottom: 8px;
        border-bottom: 2px solid #c8e8cf;
        margin-bottom: 12px;
    }
    .section-header-peach {
        font-size: 0.95rem;
        font-weight: 700;
        color: #e65100;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding-bottom: 8px;
        border-bottom: 2px solid #f5dfc8;
        margin-bottom: 12px;
    }

    .metric-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid rgba(0,0,0,0.05);
    }
    .metric-row:last-child { border-bottom: none; }
    .metric-label {
        font-size: 0.88rem;
        color: #495057;
        font-weight: 500;
    }
    .metric-hint {
        font-size: 0.72rem;
        color: #adb5bd;
        margin-top: 2px;
    }
    .metric-value {
        font-size: 1rem;
        font-weight: 700;
        color: #1a1a2e;
        text-align: right;
    }
    .badge-good {
        background: #d4edda;
        color: #155724;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 600;
        margin-left: 6px;
    }
    .badge-bad {
        background: #f8d7da;
        color: #721c24;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 600;
        margin-left: 6px;
    }
    .badge-neutral {
        background: #fff3cd;
        color: #856404;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 600;
        margin-left: 6px;
    }

    /* Small input + colored button */
    div[data-testid="column"]:first-child input {
        max-width: 280px !important;
        font-size: 0.9rem !important;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #1565c0, #42a5f5) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        padding: 0.5rem 1.2rem !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #0d47a1, #1e88e5) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(21, 101, 192, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)


def badge(condition_good, condition_bad, label_good="Good", label_bad="High", label_neutral="Fair"):
    if condition_good:
        return f'<span class="badge-good">✓ {label_good}</span>'
    elif condition_bad:
        return f'<span class="badge-bad">✗ {label_bad}</span>'
    else:
        return f'<span class="badge-neutral">~ {label_neutral}</span>'

def metric_row(label, value, hint="", badge_html=""):
    return f"""
    <div class="metric-row">
        <div>
            <div class="metric-label">{label}</div>
            {'<div class="metric-hint">' + hint + '</div>' if hint else ''}
        </div>
        <div class="metric-value">{value}{badge_html}</div>
    </div>
    """

def card(color, header_class, icon, title, content):
    return f"""
    <div class="card-{color}">
        <div class="{header_class}">{icon} {title}</div>
        {content}
    </div>
    """

# ── Header ───────────────────────────────────────────────
st.markdown('<div class="main-title">📊 Stock Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Fundamental metrics for any NSE or BSE listed stock</div>', unsafe_allow_html=True)

# ── Input ────────────────────────────────────────────────
col_input, col_btn, col_empty = st.columns([2, 1, 3])
with col_input:
    ticker_input = st.text_input("", placeholder="e.g. INFY.NS or RELIANCE.NS", label_visibility="collapsed")
with col_btn:
    analyze = st.button("🔍 Analyze")

st.caption("NSE: add .NS (e.g. HDFCBANK.NS) · BSE: add .BO (e.g. 500180.BO)")

ticker = ticker_input.upper().strip()

if analyze:
    if ticker:
        with st.spinner("Fetching data..."):
            metrics = get_stock_metrics(ticker)

        if metrics["Company"] == "N/A":
            st.error("Could not find this stock. Please check the ticker symbol!")
        else:
            st.markdown(f'<div class="company-name">{metrics["Company"]}</div>', unsafe_allow_html=True)
            st.markdown(f'''
                <span class="sector-tag">🏭 {metrics["Sector"]}</span>
                <span class="sector-tag">🔬 {metrics["Industry"]}</span>
            ''', unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                # 💰 PRICE — Blue
                price_content = (
                    metric_row("Current Price", f"₹{metrics['Current Price']}", "Live market price") +
                    metric_row("52 Week High", f"₹{metrics['52 Week High']}", "Highest price in last 1 year") +
                    metric_row("52 Week Low", f"₹{metrics['52 Week Low']}", "Lowest price in last 1 year") +
                    metric_row("50 Day Average", f"₹{metrics['52 Week Avg']}", "Short term trend indicator")
                )
                st.markdown(card("blue", "section-header-blue", "💰", "Price", price_content), unsafe_allow_html=True)

                # 📐 VALUATION — Purple
                pe = metrics["P/E Ratio"]
                pb = metrics["P/B Ratio"]
                eps = metrics["EPS"]
                pe_badge = badge(pe != "N/A" and float(pe) < 20, pe != "N/A" and float(pe) > 35, "Undervalued", "Expensive") if pe != "N/A" else ""
                pb_badge = badge(pb != "N/A" and float(pb) < 3, pb != "N/A" and float(pb) > 5, "Undervalued", "Expensive") if pb != "N/A" else ""
                valuation_content = (
                    metric_row("P/E Ratio", pe, "Ideal: < 20 · Expensive: > 35", pe_badge) +
                    metric_row("P/B Ratio", pb, "Ideal: < 3 · Expensive: > 5", pb_badge) +
                    metric_row("EPS (TTM)", eps, "Earnings per share · Trailing 12 months")
                )
                st.markdown(card("purple", "section-header-purple", "📐", "Valuation", valuation_content), unsafe_allow_html=True)

            with col2:
                # 📈 PROFITABILITY — Green
                roe = metrics["ROE (%)"]
                pm = metrics["Profit Margin (%)"]
                rg = metrics["Revenue Growth (%)"]
                roe_badge = badge(roe != "N/A" and float(roe) > 15, roe != "N/A" and float(roe) < 5, "Strong", "Weak") if roe != "N/A" else ""
                pm_badge = badge(pm != "N/A" and float(pm) > 15, pm != "N/A" and float(pm) < 5, "Strong", "Weak") if pm != "N/A" else ""
                rg_badge = badge(rg != "N/A" and float(rg) > 10, rg != "N/A" and float(rg) < 0, "Growing", "Declining") if rg != "N/A" else ""
                profit_content = (
                    metric_row("ROE", f"{roe}%", "Ideal: > 15% · Weak: < 5%", roe_badge) +
                    metric_row("Profit Margin", f"{pm}%", "Trailing 12 months · Ideal: > 15%", pm_badge) +
                    metric_row("Revenue Growth", f"{rg}%", "Year on year · Ideal: > 10%", rg_badge)
                )
                st.markdown(card("green", "section-header-green", "📈", "Profitability", profit_content), unsafe_allow_html=True)

                # 📦 OTHER — Peach
                beta = metrics["Beta"]
                dy = metrics["Dividend Yield (%)"]
                mc = metrics["Market Cap"]
                beta_badge = badge(beta != "N/A" and float(beta) < 1, beta != "N/A" and float(beta) > 1.5, "Low Risk", "High Risk") if beta != "N/A" else ""
                mc_display = f"₹{int(mc):,}" if mc != "N/A" else "N/A"
                other_content = (
                    metric_row("Market Cap", mc_display, "Total market value of company") +
                    metric_row("Dividend Yield", f"{dy}%", "Annual dividend as % of price") +
                    metric_row("Beta", beta, "< 1 = Low risk · > 1.5 = High risk", beta_badge)
                )
                st.markdown(card("peach", "section-header-peach", "📦", "Other", other_content), unsafe_allow_html=True)
    else:
        st.warning("Please enter a stock ticker!")