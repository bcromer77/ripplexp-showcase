import streamlit as st

# Page configuration
st.set_page_config(page_title="RippleXp Product Suite", layout="wide")

# Hero Section
st.title("Experience the RippleXp Suite")
st.subheader("Master storytelling, guard your reputation, and track trends—all in one place.")

# Step: Create a Grid Layout
# Use st.columns to create a layout similar to Adobe's product cards
col1, col2 = st.columns(2)

# Column 1: Storytelling Courses
with col1:
    st.markdown("### ST | Storytelling Courses")
    st.markdown("*Transform your reputation into an unforgettable narrative. Master storytelling techniques to influence and engage.*")
    if st.button("Learn More", key="storytelling"):
        st.write("Here you would link to or display more details about the Storytelling Courses.")

# Column 2: Torch Search
with col2:
    st.markdown("### TC | Torch Search")
    st.markdown("*Use Torch to uncover past statements and shine a light on crucial moments with rapid video searches across various genres.*")
    if st.button("Search Now", key="torch"):
        st.write("Here you would link to or display the Torch Search Tool.")

# Adding a new row for additional products
col3, col4 = st.columns(2)

# Column 3: Mentions Monitoring
with col3:
    st.markdown("### ME | Mentions Monitoring")
    st.markdown("*Track every mention of your brand across platforms in real time. Never miss an important conversation.*")
    if st.button("View Mentions", key="mentions"):
        st.write("Here you would link to or display the Mentions Monitoring tool.")

# Column 4: Trends Analysis
with col4:
    st.markdown("### TR | Trends Analysis")
    st.markdown("*Stay ahead of the curve with insights into the latest trends shaping your industry. Discover what’s buzzing and why it matters.*")
    if st.button("Explore Trends", key="trends"):
        st.write("Here you would link to or display the Trends Analysis tool.")
