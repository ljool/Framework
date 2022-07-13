import streamlit as st

st.set_page_config(layout="wide")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Titillium+Web');
			html, body, [class*="css"]  {
			font-family: 'Titillium Web', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image: st.sidebar.image("Worley_Logo_2019_RGB_large.png", use_column_width=True)
    st.sidebar.title("**About**")
    st.sidebar.write(
    """
    This multipage app details and demonstrates the functionality and technical requirements of the Worley Portfolio Management Tool.
    """
    )

# Customize page title
st.title("*Worley Portfolio Management Tool*")

st.header("Value Proposition")

st.subheader("Who is your target audience?")

markdown = """
The target audience for the Worley Portfolio Management Tool is **Project/Portfolio Managers.**
"""
st.markdown(markdown)

st.subheader("What are their needs or problems?")

markdown = """
A key problem identified by Portfolio Managers is how to manage numerous projects across multiple regions with different
reporting standards. 

For a particular portfolio manager or customer, consistent and standardized reporting is essential to ensure that
quality, clarity, and acccuracy is maintained across projects. 

Standardized reporting allows for portfolio managers to understand the status of their projects in real time - creating **actionable intelligence** and **enhanced productivity**.

**Accelerated delivery schedules** will require new ways of working to minimise frictions and dependencies on complicated spreadsheets. 

The unimpeded flow of information between levels of hierarchy is essential for **management of change**, with valuable or project critical information often lost in email chains and heritage systems.
"""
st.markdown(markdown)


st.subheader("What will your services do for them?")

markdown = """
Through standardized reporting, the Worley Portfolio Management Tool will provide analytics from the portfolio level down to the scope level for a particular project.

The Tool will act as the one source of truth for portfolio managers to gain insight into all projects under their jurisdiction - minimising time spent interrogating individual project reports.

The Tool will allow for smoother communication between portfolio and project managers - developing a deeper level of trust between all layers of the organizaiton.

With trust in their information, portfolio managers can communicate progress and analytics at all levels of granularity to the customer, enabling optimal resource allocation and deepening customer relationships.
"""
st.markdown(markdown)

st.subheader("How are your offerings unique? (in client perception terms)?")

markdown = """
This offering is the first of its kind to attempt to integrate Worley systems of project level reporting - reducing the need to develop complicated spreadsheets and tolerate heritage systems.


"""
st.markdown(markdown)

st.subheader("How can you prove and quantify the benefits?")

markdown = """
The value of this offering is provided internally at first, and then communicated externally to key stakeholders and customers.

The benefits of this system will be proven and quantified through feedback from portfolio managers and conversations with key stakeholders.
"""
st.markdown(markdown)

