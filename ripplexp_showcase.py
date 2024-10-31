import streamlit as st

# Page configuration (must be the first Streamlit command)
st.set_page_config(page_title="RippleXp Product Suite", layout="wide")

# Custom CSS for a Johnny Ive-inspired minimalist design
st.markdown("""
    <style>
        .main {
            background-color: #fefefe;
            color: #333;
            padding: 3rem;
            font-family: 'Helvetica Neue', sans-serif;
        }
        .product-card {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: box-shadow 0.3s, transform 0.3s;
            margin-bottom: 20px;
        }
        .product-card:hover {
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
            transform: translateY(-5px);
        }
        .product-title {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .product-description {
            font-size: 1rem;
            color: #666;
            margin-bottom: 1.5rem;
        }
        .stButton button {
            background-color: #007aff;
            color: #fff;
            border: none;
            border-radius: 8px;
            padding: 10px 25px;
            font-size: 1rem;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #005ec2;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.title("✨ Experience the RippleXp Suite")
st.subheader("Master storytelling, guard your reputation, and track trends—all in one place.")

# Create a Grid Layout
col1, col2 = st.columns(2)

# Column 1: Storytelling Courses
with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<div class="product-title">ST | Storytelling Courses 📚</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-description">Transform your reputation into an unforgettable narrative. Master storytelling techniques to influence and engage.</div>', unsafe_allow_html=True)
    st.button("Learn More", key="storytelling")
    st.markdown('</div>', unsafe_allow_html=True)

# Column 2: Torch Search
with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<div class="product-title">TC | Torch Search 🔍</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-description">Use Torch to uncover past statements and shine a light on crucial moments with rapid video searches across various genres.</div>', unsafe_allow_html=True)
    st.button("Search Now", key="torch")
    st.markdown('</div>', unsafe_allow_html=True)

# New Row for Additional Products
col3, col4 = st.columns(2)

# Column 3: Mentions Monitoring
with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<div class="product-title">ME | Mentions Monitoring 📝</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-description">Track every mention of your brand across platforms in real time. Never miss an important conversation.</div>', unsafe_allow_html=True)
    st.button("View Mentions", key="mentions")
    st.markdown('</div>', unsafe_allow_html=True)

# Column 4: Trends Analysis
with col4:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.markdown('<div class="product-title">TR | Trends Analysis 📈</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-description">Stay ahead of the curve with insights into the latest trends shaping your industry. Discover what’s buzzing and why it matters.</div>', unsafe_allow_html=True)
    st.button("Explore Trends", key="trends")
    st.markdown('</div>', unsafe_allow_html=True)
