CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=JetBrains+Mono:wght@400;500&family=Inter:wght@300;400;500&display=swap');

/* ─── Global Reset ─── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #07080d !important;
    color: #d4d4e8 !important;
}

/* ─── Hide Streamlit chrome ─── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stToolbar"] { display: none; }

/* ─── Main container ─── */
.main .block-container {
    max-width: 1000px !important;
    padding: 2rem 2rem 4rem !important;
}

/* ─── Hero Section ─── */
.hero {
    text-align: center;
    padding: 3rem 0 2.5rem;
    position: relative;
}
.hero-tag {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #6c63ff;
    border: 1px solid rgba(108,99,255,0.4);
    background: rgba(108,99,255,0.08);
    padding: 5px 16px;
    border-radius: 100px;
    margin-bottom: 20px;
}
.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 58px !important;
    font-weight: 800 !important;
    line-height: 1.05 !important;
    letter-spacing: -2px !important;
    color: #f0f0fa !important;
    margin: 0 0 12px !important;
}
.hero-title span {
    background: linear-gradient(135deg, #6c63ff, #ff6584);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 15px;
    color: #6868a0;
    font-weight: 300;
    letter-spacing: 0.2px;
}

/* ─── Cards ─── */
.card {
    background: #0f1018;
    border: 1px solid #1e1e30;
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(108,99,255,0.6), transparent);
}
.card-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #6c63ff;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.card-label::before {
    content: '';
    width: 20px;
    height: 1px;
    background: #6c63ff;
}

/* ─── Streamlit inputs ─── */
.stTextInput > div > div > input {
    background: #0a0b13 !important;
    border: 1px solid #1e1e30 !important;
    border-radius: 10px !important;
    color: #d4d4e8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 13px !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: #6c63ff !important;
    box-shadow: 0 0 0 2px rgba(108,99,255,0.15) !important;
}
.stTextInput > div > div > input::placeholder {
    color: #40406a !important;
}

/* ─── File uploader ─── */
[data-testid="stFileUploader"] {
    background: #0a0b13 !important;
    border: 1.5px dashed #1e1e30 !important;
    border-radius: 14px !important;
    padding: 20px !important;
    transition: border-color 0.2s !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: #6c63ff !important;
}
[data-testid="stFileUploaderDropzone"] > div {
    color: #6868a0 !important;
}

/* ─── Slider ─── */
.stSlider > div > div > div > div {
    background: linear-gradient(90deg, #6c63ff, #ff6584) !important;
}
.stSlider > div > div > div > div > div {
    background: #fff !important;
    border: 2px solid #6c63ff !important;
}

/* ─── Select/Radio ─── */
.stRadio > div {
    gap: 12px !important;
}
.stRadio > div > label {
    background: #0a0b13 !important;
    border: 1px solid #1e1e30 !important;
    border-radius: 10px !important;
    padding: 10px 18px !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    color: #6868a0 !important;
}
.stRadio > div > label:has(input:checked) {
    border-color: #6c63ff !important;
    background: rgba(108,99,255,0.1) !important;
    color: #d4d4e8 !important;
}

/* ─── Button ─── */
.stButton > button {
    background: linear-gradient(135deg, #6c63ff, #5855d6) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.5px !important;
    padding: 14px 32px !important;
    width: 100% !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 20px rgba(108,99,255,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 30px rgba(108,99,255,0.45) !important;
    background: linear-gradient(135deg, #7d75ff, #6c63ff) !important;
}

/* ─── Download button ─── */
.stDownloadButton > button {
    background: transparent !important;
    color: #6c63ff !important;
    border: 1px solid rgba(108,99,255,0.4) !important;
    border-radius: 10px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
    padding: 10px 24px !important;
    transition: all 0.2s !important;
    box-shadow: none !important;
}
.stDownloadButton > button:hover {
    background: rgba(108,99,255,0.1) !important;
    border-color: #6c63ff !important;
    transform: none !important;
}

/* ─── Tabs ─── */
.stTabs [data-baseweb="tab-list"] {
    background: #0a0b13 !important;
    border: 1px solid #1e1e30 !important;
    border-radius: 12px !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #6868a0 !important;
    border-radius: 9px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px !important;
    border: none !important;
    padding: 8px 20px !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(108,99,255,0.2) !important;
    color: #d4d4e8 !important;
}
.stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ─── Expander ─── */
.streamlit-expanderHeader {
    background: #0a0b13 !important;
    border: 1px solid #1e1e30 !important;
    border-radius: 12px !important;
    color: #d4d4e8 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}
.streamlit-expanderContent {
    background: #0a0b13 !important;
    border: 1px solid #1e1e30 !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
}

/* ─── Metric ─── */
[data-testid="stMetric"] {
    background: #0a0b13 !important;
    border: 1px solid #1e1e30 !important;
    border-radius: 14px !important;
    padding: 20px 24px !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    color: #f0f0fa !important;
}
[data-testid="stMetricLabel"] {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #6868a0 !important;
}

/* ─── Divider ─── */
hr {
    border-color: #1e1e30 !important;
    margin: 2rem 0 !important;
}

/* ─── Question Card ─── */
.q-card {
    background: #0a0b13;
    border: 1px solid #1e1e30;
    border-radius: 14px;
    padding: 22px 24px;
    margin-bottom: 16px;
    position: relative;
    transition: border-color 0.2s;
}
.q-card:hover { border-color: rgba(108,99,255,0.4); }
.q-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #6c63ff;
    letter-spacing: 2px;
    margin-bottom: 8px;
}
.q-text {
    font-size: 15px;
    color: #e0e0f0;
    font-weight: 400;
    margin-bottom: 14px;
    line-height: 1.5;
}
.q-options {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.q-option {
    font-size: 13px;
    color: #8888b8;
    padding: 7px 12px;
    border-radius: 8px;
    border: 1px solid #1e1e30;
    font-family: 'JetBrains Mono', monospace;
}
.q-option.correct {
    color: #34d399;
    border-color: rgba(52,211,153,0.3);
    background: rgba(52,211,153,0.06);
}
.difficulty-badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 100px;
}
.badge-easy { color: #34d399; background: rgba(52,211,153,0.1); border: 1px solid rgba(52,211,153,0.3); }
.badge-medium { color: #fbbf24; background: rgba(251,191,36,0.1); border: 1px solid rgba(251,191,36,0.3); }
.badge-hard { color: #f87171; background: rgba(248,113,113,0.1); border: 1px solid rgba(248,113,113,0.3); }
.badge-short { color: #a78bfa; background: rgba(167,139,250,0.1); border: 1px solid rgba(167,139,250,0.3); }

.q-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
}
.q-answer-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    color: #34d399;
    margin-top: 12px;
    text-transform: uppercase;
}
.q-answer-text {
    font-size: 13px;
    color: #a0a0c8;
    margin-top: 6px;
    line-height: 1.5;
    padding: 10px 14px;
    background: rgba(52,211,153,0.04);
    border: 1px solid rgba(52,211,153,0.15);
    border-radius: 8px;
}

/* ─── Status alert ─── */
.status-info {
    background: rgba(108,99,255,0.08);
    border: 1px solid rgba(108,99,255,0.25);
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 13px;
    color: #a0a0d0;
    margin-bottom: 16px;
}
.status-success {
    background: rgba(52,211,153,0.08);
    border: 1px solid rgba(52,211,153,0.25);
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 13px;
    color: #34d399;
    margin-bottom: 16px;
}
.status-error {
    background: rgba(248,113,113,0.08);
    border: 1px solid rgba(248,113,113,0.25);
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 13px;
    color: #f87171;
    margin-bottom: 16px;
}

/* ─── Spinner override ─── */
.stSpinner > div { border-top-color: #6c63ff !important; }

/* ─── Progress ─── */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #6c63ff, #ff6584) !important;
}

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #07080d; }
::-webkit-scrollbar-thumb { background: #1e1e30; border-radius: 3px; }
</style>
"""
