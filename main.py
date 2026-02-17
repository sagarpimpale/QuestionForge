import json

import streamlit as st

from styles import CSS
from document_parser import extract_text
from ai_engine import build_prompt, call_gemini
from exporters import questions_to_csv, badge_html

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="QuestionForge — AI Question Bank",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown(CSS, unsafe_allow_html=True)

# ─── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-tag">◈ LMS POC — Option 1</div>
  <h1 class="hero-title">Question<span>Forge</span></h1>
  <p class="hero-sub">Upload a course document · Generate MCQs & Short Answers · Export CSV / JSON</p>
</div>
""", unsafe_allow_html=True)

# ─── Main Layout ─────────────────────────────────────────────────────────────
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown('<div class="card"><div class="card-label">01 — API Configuration</div>', unsafe_allow_html=True)
    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        placeholder="AIzaSy...",
        label_visibility="collapsed",
        help="Get your key from https://aistudio.google.com/app/apikey"
    )
    if not api_key:
        st.markdown('<div class="status-info">🔑 Enter your Gemini API key to get started. <a href="https://aistudio.google.com/app/apikey" target="_blank" style="color:#6c63ff;">Get one free →</a></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-success">✓ API key entered</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card"><div class="card-label">02 — Upload Course Document</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload document",
        type=["pdf", "docx", "txt"],
        label_visibility="collapsed",
        help="PDF, Word (.docx), or plain text files supported"
    )
    if uploaded_file:
        st.markdown(f'<div class="status-success">✓ {uploaded_file.name} ({uploaded_file.size // 1024} KB)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="card"><div class="card-label">03 — Question Settings</div>', unsafe_allow_html=True)
    num_mcq = st.slider("Number of MCQs", min_value=3, max_value=20, value=5, step=1)
    num_short = st.slider("Number of Short Answer Questions", min_value=1, max_value=10, value=2, step=1)
    difficulty_mix = st.radio(
        "Difficulty Distribution",
        ["Balanced", "Easy-focused", "Hard-focused", "All Easy", "All Medium", "All Hard"],
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ─── Generate Button ──────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
gen_col1, gen_col2, gen_col3 = st.columns([1, 2, 1])
with gen_col2:
    generate = st.button("⚡ Generate Question Bank", use_container_width=True)

# ─── Generation Logic ─────────────────────────────────────────────────────────
if generate:
    if not api_key:
        st.markdown('<div class="status-error">✗ Please enter your Gemini API key first.</div>', unsafe_allow_html=True)
    elif not uploaded_file:
        st.markdown('<div class="status-error">✗ Please upload a course document first.</div>', unsafe_allow_html=True)
    else:
        with st.spinner("📖 Parsing document..."):
            file_bytes = uploaded_file.read()
            ext = uploaded_file.name.rsplit(".", 1)[-1].lower()
            try:
                content = extract_text(file_bytes, ext)
                if len(content.strip()) < 100:
                    st.markdown('<div class="status-error">✗ Could not extract enough text from the document. Try a different file.</div>', unsafe_allow_html=True)
                    st.stop()
            except Exception as e:
                st.markdown(f'<div class="status-error">✗ Error parsing file: {e}</div>', unsafe_allow_html=True)
                st.stop()

        with st.spinner("🤖 Calling Gemini 2.5 Flash..."):
            try:
                prompt = build_prompt(content, num_mcq, num_short, difficulty_mix)
                data = call_gemini(api_key, prompt)
                st.session_state["qbank"] = data
                st.session_state["filename"] = uploaded_file.name
            except json.JSONDecodeError as e:
                st.markdown(f'<div class="status-error">✗ Gemini returned invalid JSON. Try again. ({e})</div>', unsafe_allow_html=True)
                st.stop()
            except Exception as e:
                err = str(e)
                if "API_KEY_INVALID" in err or "API key" in err:
                    st.markdown('<div class="status-error">✗ Invalid API key. Please check your Gemini API key.</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="status-error">✗ Error: {err}</div>', unsafe_allow_html=True)
                st.stop()

        st.markdown('<div class="status-success">✓ Question bank generated successfully!</div>', unsafe_allow_html=True)

# ─── Display Results ──────────────────────────────────────────────────────────
if "qbank" in st.session_state:
    data = st.session_state["qbank"]
    mcqs = data.get("mcqs", [])
    shorts = data.get("short_answers", [])

    st.markdown("<hr>", unsafe_allow_html=True)

    # Stats row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("MCQs", len(mcqs))
    with m2:
        st.metric("Short Answer", len(shorts))
    with m3:
        easy_count = sum(1 for q in mcqs + shorts if (q.get("difficulty") or "").lower() == "easy")
        st.metric("Easy", easy_count)
    with m4:
        hard_count = sum(1 for q in mcqs + shorts if (q.get("difficulty") or "").lower() == "hard")
        st.metric("Hard", hard_count)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["MCQs", "Short Answers", "Export"])

    with tab1:
        if not mcqs:
            st.info("No MCQs generated.")
        for i, q in enumerate(mcqs, 1):
            opts = q.get("options", {})
            correct = q.get("correct_answer", "")
            diff = q.get("difficulty", "Medium")

            options_html = ""
            for letter, text in opts.items():
                is_correct = (letter == correct)
                css_class = "q-option correct" if is_correct else "q-option"
                check = " ✓" if is_correct else ""
                options_html += f'<li class="{css_class}">{letter}. {text}{check}</li>'

            st.markdown(f"""
            <div class="q-card">
              <div class="q-meta">
                <span class="q-number">MCQ · {i:02d}</span>
                {badge_html(diff)}
              </div>
              <div class="q-text">{q.get("question", "")}</div>
              <ul class="q-options">{options_html}</ul>
              {"<div class='q-answer-label'>Explanation</div><div class='q-answer-text'>" + q.get('explanation','') + "</div>" if q.get('explanation') else ""}
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        if not shorts:
            st.info("No short answer questions generated.")
        for i, q in enumerate(shorts, 1):
            kp = q.get("key_points", [])
            kp_html = ""
            if kp:
                kp_html = "<ul style='margin:6px 0 0 16px;padding:0;color:#8888b8;font-size:13px;'>"
                for pt in kp:
                    kp_html += f"<li style='margin-bottom:4px;'>{pt}</li>"
                kp_html += "</ul>"

            st.markdown(f"""
            <div class="q-card">
              <div class="q-meta">
                <span class="q-number">SHORT ANSWER · {i:02d}</span>
                {badge_html(q.get("difficulty","Medium"), "Short Answer")}
              </div>
              <div class="q-text">{q.get("question","")}</div>
              <div class="q-answer-label">Model Answer</div>
              <div class="q-answer-text">{q.get("model_answer","")}</div>
              {"<div class='q-answer-label' style='color:#a78bfa;margin-top:12px;'>Key Points</div>" + kp_html if kp else ""}
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="card"><div class="card-label">Export Options</div>', unsafe_allow_html=True)
        ec1, ec2 = st.columns(2)

        with ec1:
            json_str = json.dumps(data, indent=2)
            st.download_button(
                label="⬇ Download JSON",
                data=json_str,
                file_name="question_bank.json",
                mime="application/json",
                use_container_width=True
            )
        with ec2:
            csv_str = questions_to_csv(data)
            st.download_button(
                label="⬇ Download CSV",
                data=csv_str,
                file_name="question_bank.csv",
                mime="text/csv",
                use_container_width=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📋 Preview JSON"):
            st.code(json.dumps(data, indent=2), language="json")

        with st.expander("📋 Preview CSV"):
            st.code(csv_str, language="text")

        st.markdown('</div>', unsafe_allow_html=True)
