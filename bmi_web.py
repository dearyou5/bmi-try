import streamlit as st

# 设置页面标题
st.set_page_config(page_title="BMI 计算器", page_icon="📏", layout="centered")

st.title("📏 BMI 身体质量指数计算器")
st.markdown("**输入你的身高和体重，立即计算结果**")

# 输入区域
col1, col2 = st.columns(2)
with col1:
    height = st.number_input('身高 (米)', min_value=0.5, max_value=2.5, value=1.75, step=0.01)
with col2:
    weight = st.number_input('体重 (公斤)', min_value=20.0, max_value=300.0, value=70.0, step=0.1)

# 计算按钮
if st.button("🚀 计算 BMI", type="primary"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        
        st.success(f"**您的 BMI 指数为：{bmi:.2f}**")
        
        # 结果判断
        if bmi < 18.5:
            st.info("📉 判断：体重过轻")
        elif bmi < 25:
            st.success("✅ 判断：体重正常")
        elif bmi < 28:
            st.warning("⚠️ 判断：体重过重")
        elif bmi < 32:
            st.error("❗ 判断：肥胖")
        else:
            st.error("🚨 判断：严重肥胖")
        
        # 可视化
        st.progress(min(bmi / 40, 1.0))
        
    else:
        st.error("身高和体重必须大于 0！")

# 底部说明
st.caption("这是一个用 Python + Streamlit 制作的网页工具")