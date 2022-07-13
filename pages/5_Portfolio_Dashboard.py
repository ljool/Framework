import streamlit as st
from streamlit_echarts import st_echarts
import random
import pandas as pd
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
import numpy as np

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
    This multipage app details and demonstrates the functionality and technical requirements of the Worley Portfolio Management Framework.
    """
    )

def project(n):
    OriginalBudgetHrs=random.randint(1, 1000)
    OriginalBudgetCost=random.randint(1, 10000000)
    CurrentBudgetHrs=random.randint(1, 1000)
    CurrentBudgetCost=random.randint(1, 10000000)
    SpentBudgetHrs=random.randint(1, CurrentBudgetHrs)
    SpentBudgetCost=random.randint(1, CurrentBudgetCost)
    OutstandingTasks=random.randint(1, 10) 
    #vals=[OriginalBudgetHrs,OriginalBudgetCost,CurrentBudgetHrs,CurrentBudgetCost,SpentBudgetHrs,SpentBudgetCost,OutstandingTasks]
    UtilHrs=SpentBudgetHrs/CurrentBudgetHrs
    UtilCost=SpentBudgetCost/CurrentBudgetCost
    TotalFTE=random.randint(1, 500)
    AvailFTE=random.randint(1, TotalFTE)  
    Project = "Project "+str(n+1)
    return Project,OriginalBudgetHrs,OriginalBudgetCost,CurrentBudgetHrs,CurrentBudgetCost,SpentBudgetHrs,SpentBudgetCost,OutstandingTasks,UtilHrs,UtilCost,TotalFTE,AvailFTE

# Customize page title
st.title("*Example Portfolio Dashboard*")
st.header("Project Status")


numProjects=8
Proj = []
UtilHPerf=0
UtilCPerf=0
UtilHGood=0
UtilCGood=0
UtilHBad=0
UtilCBad=0
for n in range(0,numProjects):
    Proj.append(project(n))
for n in range(len(Proj)):
    if Proj[n][8]>=0.8:
        UtilHPerf+=1
    elif Proj[n][8]>=0.5:
        UtilHGood+=1
    elif Proj[n][8]<=0.5:
        UtilHBad+=1
    if Proj[n][9]>=0.8:
        UtilCPerf+=1
    elif Proj[n][9]>=0.5:
        UtilCGood+=1
    elif Proj[n][9]<=0.5:
        UtilCBad+=1



columns=['Project','OriginalBudgetHrs','OriginalBudgetCost','CurrentBudgetHrs','CurrentBudgetCost','SpentBudgetHrs','SpentBudgetCost',\
            'OutstandingTasks','UtilHrs','UtilCost','Total FTEs','Available FTEs']

Proj_df = pd.DataFrame(Proj)
#Proj_df['Project'] = (np.arange(Proj_df.shape[0])+1).astype(str)
#Proj_
Proj_df.columns=columns
#st.write(Proj_df)
#Infer basic colDefs from dataframe types
gb = GridOptionsBuilder.from_dataframe(Proj_df)

return_mode = st.sidebar.selectbox("Return Mode", list(DataReturnMode.__members__), index=1)
return_mode_value = DataReturnMode.__members__[return_mode]

update_mode = st.sidebar.selectbox("Update Mode", list(GridUpdateMode.__members__), index=6)
update_mode_value = GridUpdateMode.__members__[update_mode]

#customize gridOptions
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
gb.configure_column('OriginalBudgetCost', type=["numericColumn","numberColumnFilter","customCurrencyFormat"],custom_currency_symbol="$" , precision=2)
gb.configure_column('SpentBudgetCost', type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"],custom_currency_symbol="$" , precision=2)
gb.configure_column('CurrentBudgetCost', type=["numericColumn", "numberColumnFilter", "customCurrencyFormat"], custom_currency_symbol="$" )
gb.configure_column('UtilHrs', type=['numericColumn','numberColumnFilter','customNumericFormat'], precision=2)
gb.configure_column('UtilCost',  type=['numericColumn','numberColumnFilter','customNumericFormat'], precision=2)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_selection('multiple', use_checkbox=False, rowMultiSelectWithClick=True, suppressRowDeselection=True)
  
gb.configure_grid_options(domLayout='normal')
gridOptions = gb.build()

def render_ring_gauge():
    option = {
        "title": {"text": "Project Health", "left": "center"},
                "tooltip": {"trigger": "item"},
        "series": [
            {
                "type": "gauge",
                "startAngle": 90,
                "endAngle": -270,
                "pointer": {"show": False},
                "progress": {
                    "show": True,
                    "overlap": False,
                    "roundCap": True,
                    "clip": False,
                    "itemStyle": {"borderWidth": 1, "borderColor": "#464646"},
                },
                "axisLine": {"lineStyle": {"width": 40}},
                "splitLine": {"show": False, "distance": 0, "length": 10},
                "axisTick": {"show": False},
                "axisLabel": {"show": False, "distance": 50},
                "data": [
                    {
                        "value": UtilHPerf/numProjects*100,
                        "name": "Perfect",
                        "title": {"offsetCenter": ["0%", "-30%"]},
                        "detail": {"offsetCenter": ["0%", "-20%"]},
                    },
                    {
                        "value": UtilHGood/numProjects*100,
                        "name": "Good",
                        "title": {"offsetCenter": ["0%", "0%"]},
                        "detail": {"offsetCenter": ["0%", "10%"]},
                    },
                    {
                        "value": UtilHBad/numProjects*100,
                        "name": "At Risk",
                        "title": {"offsetCenter": ["0%", "30%"]},
                        "detail": {"offsetCenter": ["0%", "40%"]},
                    },
                ],
                
                "detail": {
                    "width": 50,
                    "height": 14,
                    "fontSize": 14,
                    "color": "auto",
                    "borderColor": "auto",
                    "borderRadius": 20,
                    "borderWidth": 1,
                    "formatter": "{value}%",
                },
            }
        ]
    }

    st_echarts(option, height="500px", key="echarts")
    
def pie_chart():
    options = {
        "title": {"text":"Outstanding Tasks", "left": "center"},
        "tooltip": {"trigger": "item"},
        "legend": {
            "orient": "vertical",
            "left": "left",
        },
        "series": [
            {
                "name": "Outstanding Tasks",
                "type": "pie",
                "radius": "80%",
                "data": [
                    {"value": Proj[0][7], "name": "Project 1"},
                    {"value": Proj[1][7], "name": "Project 2"},
                    {"value": Proj[2][7], "name": "Project 3"},
                    {"value": Proj[3][7], "name": "Project 4"},
                    {"value": Proj[4][7], "name": "Project 5"},
                    {"value": Proj[5][7], "name": "Project 6"},
                    {"value": Proj[6][7], "name": "Project 7"},
                    {"value": Proj[7][7], "name": "Project 8"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    
    events = {
        "legendselectchanged": "function(params) { return params.selected }",
    }
    s = st_echarts(
        options=options, events=events, height="600px", key="render_pie_events"
    )

def bar_chart():
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ['Total FTEs','Available FTEs']
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["Project 1","Project 2","Project 3","Project 4","Project 5","Project 6","Project 7","Project 8"],
        },
        "series": [
            {
                "name": "Total FTEs",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [Proj[0][10],Proj[1][10],Proj[2][10],Proj[3][10],Proj[4][10],Proj[5][10],Proj[6][10],Proj[7][10]],
            },
            {
                "name": "Available FTEs",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": [Proj[0][11],Proj[1][11],Proj[2][11],Proj[3][11],Proj[4][11],Proj[5][11],Proj[6][11],Proj[7][11]],
            },
                    ],
    }
    st_echarts(options=options, height="500px")

col1, col2 = st.columns(2)

with col1:

    render_ring_gauge()

    pie_chart()
    
with col2:
    bar_chart()
grid_response = AgGrid(
    Proj_df, 
    gridOptions=gridOptions,
    height=300, 
    width='100%',
    data_return_mode=return_mode_value, 
    update_mode=update_mode_value,
    fit_columns_on_grid_load=True,
    allow_unsafe_jscode=True, #Set it to True to allow jsfunction to be injected
    enable_enterprise_modules=True,
    )
