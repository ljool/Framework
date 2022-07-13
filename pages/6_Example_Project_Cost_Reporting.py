from distutils import errors
from distutils.log import error
import streamlit as st
import pandas as pd 
import numpy as np
import altair as alt
from itertools import cycle

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode

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
    This multipage app details and demonstrates the functionality and technical requirements of the Worley Portfolio Management Framework.
    """
    )


#st.set_page_config(page_title="Project Cost Reporting", layout="wide") 
st.title("Scheduled Project Cost Reporting")


#Display the grid
st.header("Detailed Cost & Scheduled Cost Reporting")
st.markdown("""
    By becoming the single source of truth for all project and portfolio reporting, the Framework will allow for in-depth analysis at all levels of granularity.
""")

st.header("Cost Status Report: FFI - Scoping Study - Ethiopia.Djibouti Project")
st.subheader("Period ending:  27th May 22")

#Example controlers
st.sidebar.subheader("Spreadsheet")

sample_size = st.sidebar.number_input("rows", min_value=10, value=30)
grid_height = st.sidebar.number_input("Grid height", min_value=200, max_value=800, value=300)

return_mode = st.sidebar.selectbox("Return Mode", list(DataReturnMode.__members__), index=1)
return_mode_value = DataReturnMode.__members__[return_mode]

update_mode = st.sidebar.selectbox("Update Mode", list(GridUpdateMode.__members__), index=6)
update_mode_value = GridUpdateMode.__members__[update_mode]

#enterprise modules
enable_enterprise_modules = st.sidebar.checkbox("Enable Enterprise Modules")
enable_sidebar = True


#features
fit_columns_on_grid_load = st.sidebar.checkbox("Fit Grid Columns on Load")

enable_selection=st.sidebar.checkbox("Enable row selection", value=True)
if enable_selection:
    st.sidebar.subheader("Selection options")
    selection_mode = st.sidebar.radio("Selection Mode", ['single','multiple'], index=1)
    
    use_checkbox = st.sidebar.checkbox("Use check box for selection", value=True)
    if use_checkbox:
        groupSelectsChildren = st.sidebar.checkbox("Group checkbox select children", value=True)
        groupSelectsFiltered = st.sidebar.checkbox("Group checkbox includes filtered", value=True)

    if ((selection_mode == 'multiple') & (not use_checkbox)):
        rowMultiSelectWithClick = st.sidebar.checkbox("Multiselect with click (instead of holding CTRL)", value=False)
        if not rowMultiSelectWithClick:
            suppressRowDeselection = st.sidebar.checkbox("Suppress deselection (while holding CTRL)", value=False)
        else:
            suppressRowDeselection=False
    st.sidebar.text("___")

enable_pagination = st.sidebar.checkbox("Enable pagination", value=False)
if enable_pagination:
    st.sidebar.subheader("Pagination options")
    paginationAutoSize = st.sidebar.checkbox("Auto pagination size", value=True)
    if not paginationAutoSize:
        paginationPageSize = st.sidebar.number_input("Page size", value=20, min_value=0, max_value=sample_size)
    st.sidebar.text("___")


df = pd.read_csv("CostReport.csv")  

#Infer basic colDefs from dataframe types
gb = GridOptionsBuilder.from_dataframe(df)



#customize gridOptions
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
#gb.configure_column('Discipline', RowGroup=True)
gb.configure_column('Original Budget - Cost', type=["numericColumn","numberColumnFilter","customCurrencyFormat"],custom_currency_symbol="$" , precision=2)
gb.configure_column('Approved Variations - Cost', type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"],custom_currency_symbol="$" , precision=1,)
gb.configure_column('Current Budget - Cost', type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"], custom_currency_symbol="$" )
gb.configure_column('Original Budget - Hours', type=["numericColumn","numberColumnFilter"],custom_currency_symbol="$" , precision=2)
gb.configure_column('Approved Variations - Hours', type=["numericColumn", "numberColumnFilter"],custom_currency_symbol="$" , precision=1,)
gb.configure_column('Current Budget - Hours', type=["numericColumn", "numberColumnFilter"], custom_currency_symbol="$" )


if enable_sidebar:
    gb.configure_side_bar()

if enable_selection:
    gb.configure_selection(selection_mode)
    if use_checkbox:
        gb.configure_selection(selection_mode, use_checkbox=True, groupSelectsChildren=groupSelectsChildren, groupSelectsFiltered=groupSelectsFiltered)
    if ((selection_mode == 'multiple') & (not use_checkbox)):
        gb.configure_selection(selection_mode, use_checkbox=False, rowMultiSelectWithClick=rowMultiSelectWithClick, suppressRowDeselection=suppressRowDeselection)

if enable_pagination:
    if paginationAutoSize:
        gb.configure_pagination(paginationAutoPageSize=True)
    else:
        gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=paginationPageSize)

gb.configure_grid_options(domLayout='normal')
gridOptions = gb.build()

grid_response = AgGrid(
    df, 
    gridOptions=gridOptions,
    height=800, 
    width='100%',
    data_return_mode=return_mode_value, 
    update_mode=update_mode_value,
    fit_columns_on_grid_load=False,
    allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
    enable_enterprise_modules=True,
    )

df = grid_response['data']
selected = grid_response['selected_rows']
selected_df = pd.DataFrame(selected)

with st.spinner("Displaying results..."):
    #displays the chart
    chart_data = df.loc[:,['SDRL Code','Description', 'Original Budget - Hours', 'Current Budget - Hours','Incurred to Date - Hours']].assign(source='total')

    if not selected_df.empty :
        selected_data = selected_df.loc[:,['SDRL Code', 'Original Budget - Hours', 'Incurred to Date - Hours', 'Current Budget - Hours']].assign(source='selection')
        chart_data = pd.concat([selected_data])
    chart_data = pd.melt(chart_data, id_vars='SDRL Code', var_name="Type", value_vars=['Original Budget - Hours','Current Budget - Hours','Incurred to Date - Hours'], value_name="Hours")
    #AgGrid(chart_data)
    chart = alt.Chart(data=chart_data,height=500).mark_bar().encode(
        x=alt.X('SDRL Code:N'),
        y=alt.Y('Hours:Q',stack=False),
        tooltip=alt.Tooltip(['SDRL Code', 'Hours', 'Type']),
        color=alt.Color('Type:N'),
        )
    
    st.header("Example Outputs - Hours")

    st.altair_chart(chart, use_container_width=True)

with st.spinner("Displaying results..."):
    #displays the chart
    chart_data = df.loc[:,['SDRL Code','Description', 'Original Budget - Cost', 'Current Budget - Cost','Incurred to Date - Cost']].assign(source='total')

    if not selected_df.empty :
        selected_data = selected_df.loc[:,['SDRL Code', 'Original Budget - Cost', 'Incurred to Date - Cost', 'Current Budget - Cost']].assign(source='selection')
        chart_data = pd.concat([selected_data])
    chart_data = pd.melt(chart_data, id_vars='SDRL Code', var_name="Type", value_vars=['Original Budget - Cost', 'Current Budget - Cost','Incurred to Date - Cost'], value_name="Cost ($)")
    #AgGrid(chart_data)
    chart = alt.Chart(data=chart_data, height=500).mark_bar().encode(
    x=alt.X('SDRL Code:N'),
    y=alt.Y('Cost ($):Q'),
    tooltip=alt.Tooltip(['SDRL Code', 'Cost ($)', 'Type']),
    color=alt.Color('Type:N')
    )
    
    st.header("Example Outputs - Costing")

    st.altair_chart(chart, use_container_width=True)


    #st.write(gridOptions)