import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="小鼠抑郁症状实验模拟",
    page_icon="🐭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #2E7D32;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        border-left: 5px solid #2E7D32;
        padding-left: 10px;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #2E7D32;
    }
    /* Button Styling */
    .stButton button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
    
    /* Custom Box Styles */
    .mutant-box {
        border: 2px solid #FFCC80;
        border-radius: 10px;
        padding: 20px;
        background-color: #FFF3E0;
        height: 100%;
    }
    .wild-box {
        border: 2px solid #A5D6A7;
        border-radius: 10px;
        padding: 20px;
        background-color: #E8F5E9;
        height: 100%;
    }
    
    .result-box-mutant {
        border: 1px solid #EF9A9A;
        background-color: #FFEBEE;
        padding: 15px;
        border-radius: 5px;
        margin-top: 10px;
    }
    
    .result-box-wild {
        border: 1px solid #A5D6A7;
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">小鼠抑郁症状实验模拟</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">本实验展示基因突变型与野生型小鼠在脂多糖处理后的行为差异</div>', unsafe_allow_html=True)

# --- Experiment Setup Section ---
st.markdown('<div class="section-header">实验设置</div>', unsafe_allow_html=True)

# Layout for setup
col1, col2 = st.columns(2)

with col1:
    st.warning("基因突变型小鼠", icon="🧬")
    # Using columns within to simulate the selection cards
    c1, c2 = st.columns(2)
    with c1:
        st.image("https://placehold.co/150x150/FFF3E0/orange?text=Mutant+#1", caption="基因突变型 #1")
    with c2:
        # Simulating 'Selected' state with a border or mark
        st.image("https://placehold.co/150x150/e0e0e0/orange?text=Mutant+#2", caption="基因突变型 #2 (已选)")

with col2:
    st.success("野生型小鼠", icon="🐭")
    c3, c4 = st.columns(2)
    with c3:
        st.image("https://placehold.co/150x150/E8F5E9/green?text=Wild+#1", caption="野生型 #1 (已选)")
    with c4:
        st.image("https://placehold.co/150x150/white/green?text=Wild+#2", caption="野生型 #2")

# Control Buttons
st.write("") # Spacer
st.write("") 
b_col1, b_col2, b_col3 = st.columns([1, 2, 1])

with b_col2:
    # Centered buttons area
    bc1, bc2 = st.columns(2)
    with bc1:
        if st.button("选择已确认"):
            st.toast("选择已确认！")
    with bc2:
        start_analysis = st.button("处理完成", type="primary")

# State management for results
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False

if start_analysis:
    st.session_state.analysis_done = True

# --- Results Section ---
if st.session_state.analysis_done:
    st.markdown("---")
    st.markdown('<div class="section-header">实验结果</div>', unsafe_allow_html=True)
    
    r_col1, r_col2 = st.columns(2)
    
    # Mutant Results
    with r_col1:
        st.warning("基因突变型小鼠结果")
        st.markdown("""
        <div class="result-box-mutant">
            <strong>菌群分析结果 (突变型小鼠):</strong><br>
            <ul>
                <li><strong>Alpha多样性:</strong> Ace, Chao, Shannon指数无显著差异 (p > 0.05)</li>
                <li><strong>Beta多样性:</strong> 菌群结构明显分离 (PC1=34.04%)</li>
                <li><strong>菌科变化:</strong>
                    <ul>
                        <li>毛螺菌科丰度显著降低 (p < 0.01)</li>
                        <li>瘤胃菌科丰度显著降低 (p < 0.01)</li>
                    </ul>
                </li>
                <li><strong>相关性:</strong> 毛螺菌科丰度与IL-1β、IL-6呈负相关</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Wild Type Results
    with r_col2:
        st.success("野生型小鼠结果")
        st.markdown("""
        <div class="result-box-wild">
            <strong>菌群分析结果 (野生型小鼠):</strong><br>
            <ul>
                <li><strong>Alpha多样性:</strong> Ace, Chao, Shannon指数无显著差异 (p > 0.05)</li>
                <li><strong>Beta多样性:</strong> 菌群结构无明显分离 (PC1=12.36%)</li>
                <li><strong>菌科变化:</strong>
                    <ul>
                        <li>毛螺菌科丰度轻度降低 (p > 0.05)</li>
                        <li>瘤胃菌科丰度轻度降低 (p > 0.05)</li>
                    </ul>
                </li>
                <li><strong>相关性:</strong> 毛螺菌科丰度与炎症因子无显著相关</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: #888; margin-top: 50px; font-size: 0.8em;'>
        实验模拟系统 © 2025 | 用于软著申请
    </div>
    """, unsafe_allow_html=True)

