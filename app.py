import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🍓",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Food Recommendation")
st.write("""Craving something delicious but stuck in decision fatigue? Enter the food recommendation system,
        your culinary compass! Tell it your tastes, dietary needs, and the occasion, and watch as it conjures up personalized dish 
        suggestions. Spicy Thai curry for a solo weeknight? Check. Elegant pasta for a romantic date? Double check. 
        Never guess again—let AI guide you to your next taste bud adventure!""")
images = ["https://images.pexels.com/photos/1435735/pexels-photo-1435735.jpeg", 
          "https://images.pexels.com/photos/1854652/pexels-photo-1854652.jpeg?auto=compress&cs=tinysrgb&w=600", 
          "https://images.pexels.com/photos/3186654/pexels-photo-3186654.jpeg?auto=compress&cs=tinysrgb&w=600"]

with st.sidebar:
    st.image(images)
col = st.columns(3)
for i in range(3):
    with col[i]:
        st.image(images[2-i])
        if i == 0:
            st.write("""No more "what's for dinner?" dread. Find hidden gems and forgotten favorites, 
                     rediscover the joy of cooking, or explore new cuisines with confidence.""")