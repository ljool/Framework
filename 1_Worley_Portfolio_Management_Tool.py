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
st.subheader("Institutionalising Disruptive Thinking & Breakthrough")

col1, col2 = st.columns(2)

with col1:   
    st.header("Introduction")

    markdown = """
    The Worley Portfolio Management Tool is a tool designed to minimise the complexity of managing multiple projects, production assets, offices & labour, and infrastructure scattered across the globe.
  
    The tool aims to consolidate and standardise the Worley approach to project and portfolio management by reducing the reliance on heritage spreadsheets and systems, and by bringing all project reporting under one umbrella of integrated software.

    The tool aims to enable Portfolio Managers to make informed decisions on the fly by consolidating all project and portfolio related information into one application and becoming the single source of truth.
    
    This app has been developed for the purpose of detailing and demonstrating the minimal functional and technical requirements of the Worley Portfolio Management Tool.
    
    To use the app, navigate across pages using the sidebar on the left to explore functionality and elements of the Tool.
    """
    st.markdown(markdown)

    st.header("Functionality")

    markdown = """
    1. Portfolio level reporting and analytics. Overview of all projects related to the parent portfolio (i.e., Fortescue Future Industries). 
    2. Project level reporting and analytics (i.e., Labour/Schedule Breakdown; Project Financials; Status Updates; Notes, etc...)
    3. Analytics, Visualisation, and Status of Project Related Assets.
    4. Visualisation of Worley/Customer Office Locations and Organizational Charts.
    5. Become the intranet / single source of truth for project/portfolio level reporting.

    """
    st.markdown(markdown)

    st.header("Far-Field Functionality")

    markdown = """
    1. Carbon Emissions Reporting
    2. Levelized Cost of Power / Storage / Hydrogen
    3. Enable use of the Tool to all employees - building in levels of confidentiality / access to the platform.
    4. Searching Capabilities
    5. Up-to-date analytics of all production/storage/transportation assets.
    6. Cost Estimation for Scenario Planning

    """
    st.markdown(markdown)
    
    st.header("Recommendations and Requirements")

    markdown = """
    -   It is recommended that a standardized format is established for scheduled reporting for incorporation into the PMT.
    -   Define core requirements / desired fuctionality of the Tool with Portfolio Managers and involved Stakeholders.
    -   Discuss and define how Worley systems talk to each other for smooth interoperability (i.e., EcoSys and other Project Controls Systems).
    -   Identify core functionality and introduce the PMT to a test group to see how well it is received.
       
    """
    st.markdown(markdown)


with col2:
    st.header("Elements to Include")

    markdown = """
    1. Worley Office Locations
        -   Labour Breakdown
        -   Available Resources
    2. Assets and Locations
        -   Location of Project
        -   Capacity and Output
        -   Type of Asset (Electrolyzer Plant / Wind / Solar / Hydro / Desalination / etc..)
        -   Operational Status
        -   Asset/Project Financials (TIC / OPEX / ROI / etc...)
        -   Worley Scope (Scoping / PFS / Pre-FEED / FEED / EPC / O&M)
    3. Customer
        -   Corporate/Project Organizational Chart
        -   Customer SMEs and Points of Contact
    4. Projects
        -   Project Status
        -   Schedule/Cost Performance Index
        -   Planned and Earned Progress
        -   Earned Vs Burned Progress
        -   Workshare / GID Assets
            - GID Execution Location and Hours
    """
    st.markdown(markdown)
    
    st.image('PM Plan FY22.jpg')
