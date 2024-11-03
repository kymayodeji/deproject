## Application for Unemplyoyment Analysis

# 0 Import Libraries
# -- 0.1 Mathematical Libraries -- #
import pandas as pd
#import numpy as np

# ---- 0.2 Dashboard -----
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# --- 0.3 Plotting Libraries ----
import plotly.express as px

# 1.0 Import data
df = pd.read_csv("unemployment.csv")

# 2.0 Set up Dashboard Layout
# 2.1 Create dash object
app = dash.Dash(__name__)

# 2.2 Design Layout
 # 2.2a Row: Input for Dropdown for users to select
options_columns = df.columns[1:-3] # retrieve people groups from dataframe
options = []
for opt in options_columns:
    options.append({"label":opt,"value":opt})
        
app.layout = html.Div([
    # 2.2b Header
    html.H1("Web Application", style={'text-align':'center'}),
    dcc.Dropdown(id="select_group",
                 options=options,
                 multi=False,
                 value="Unemployment Rate",
                 style={"width":"60%"}
                 ),
    
    # 2.2c Row: Output row
    html.Div(id='output_container', children=[]),
    html.Br(), # space
    # 2.2d Graph Row
    dcc.Graph(id="unemployment_graph", figure={})
    
])

# 3.0 Call backs for the dropdown actions
# 3.1 Callback uses component_id and component_property pairing to connect Input with Output functions to establish relationship
@app.callback(
    [Output(component_id='output_container', component_property='children'), 
    Output(component_id='unemployment_graph', component_property='figure')], 
    [Input(component_id='select_group', component_property='value')]
    
)
def update_graph(selected_option): # argument selected_option refers to the Input(s) component_property
    # Print out the selected option along with its type
    print(selected_option)
    print(type(selected_option))
    
    # 3.1a Configure what will be dsplayed in the first output (output_container)
    container = "Unemployment when the president is a member of the {} party".format(selected_option)
    
    # 3.1b Configure the graph 
    # 3.1b.1 Configure dataframe used based on selection_option
    df_option = df.copy()

    # 3.1b.2 Configure the Unemployment graph based on the selected grouping option
    fig = px.scatter(df_option, x='date', y=selected_option, color='party')
    
    # 3.1b.3 Return the ouptputs
    return container,fig  # return the two Outputs
# 4.0 
# run the app
if __name__ == '__main__':
    app.run_server(debug=True)