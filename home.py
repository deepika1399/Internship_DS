import streamlit as st

st.balloons()
st.title(":red[My First Streamlit Data App]:tada::confetti_ball:")

st.subheader("Here in this app we can see the analysis of iris data and titanic data ")
st.markdown("Click the dashboards to see the analysis in the slide bar")
# Create button
button_clicked = st.button("About me!")

# Check if button was clicked
if button_clicked:
    st.header("Hello everyone!")
    st.write("I'am Deepika")
    st.write("Data Science Intern :red[@] **Innnomatics Research Labs**")
    st.write("I have completed my **MBA** and currently pursuing **Data Science**")
    st.write("I aim to pursue a challenging and innovative career in field of commerce and data science that provides ample opportunities to improvise my skills and knowledge thereby acknowledging proper wisdom ,contributing positively towards growth of the organization")
    st.subheader("**Connect with me using below links**")

    st.write("**LinkedIn**https://www.linkedin.com/in/deepika-j-866978234")
    st.write("**GitHub**https://github.com/deepika1399")
    st.write(":e-mail:**Email**Deepikajaiswal1312@gmail.com")

