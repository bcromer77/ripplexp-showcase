import streamlit as st

# Step 2: Basic Streamlit Layout
# Page configuration
st.set_page_config(page_title="RippleXp Product Suite", layout="wide")

# Hero Section
st.title("Experience the RippleXp Suite")
st.subheader("Master storytelling, guard your reputation, and track trends—all in one place.")

# Step 3: Create Product Blocks

# Storytelling Courses Block
st.markdown("## ST | Storytelling Courses")
st.markdown("*Transform your reputation into an unforgettable narrative. Master storytelling techniques to influence and engage.*")
if st.button("Learn More", key="storytelling"):
    st.write("Here you would link to or display more details about the Storytelling Courses.")

st.markdown("---")  # Separator line

# Greenwashing & Genre Searches Block
st.markdown("## GW | Greenwashing & Genre Searches")
st.markdown("*Uncover potential reputational risks with genre-specific video searches. Start with Greenwashing or explore new categories like sports and politics.*")
if st.button("Search Now", key="greenwashing"):
    st.write("Here you would link to or display the Greenwashing Search Tool.")

st.markdown("---")

# Mentions Monitoring Block
st.markdown("## ME | Mentions Monitoring")
st.markdown("*Track every mention of your brand across platforms in real time. Never miss an important conversation.*")
if st.button("View Mentions", key="mentions"):
    st.write("Here you would link to or display the Mentions Monitoring tool.")

st.markdown("---")

# Trends Analysis Block
st.markdown("## TR | Trends Analysis")
st.markdown("*Stay ahead of the curve with insights into the latest trends shaping your industry. Discover what’s buzzing and why it matters.*")
if st.button("Explore Trends", key="trends"):
    st.write("Here you would link to or display the Trends Analysis tool.")
