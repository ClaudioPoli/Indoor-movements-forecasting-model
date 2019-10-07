import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from Main.main import dff
import warnings
warnings.filterwarnings("ignore")

#Importing dataset

df=dff

#Feature Engineering
df['Area']=df['Area'].astype(str)

conditions = [
    (df['minute']<=10),
    (df['minute']>10) & (df['minute']<=20),
    (df['minute']>20) & (df['minute']<=30),
    (df['minute']>30) & (df['minute']<=40),
    (df['minute']>40) & (df['minute']<=50),
    (df['minute']>50) & (df['minute']<=59),
    ]

choices = [10,20,30,40,50,60]

df['min10'] = np.select(conditions, choices,default='0')
df['min10']=df['min10'].astype(int)
available_days=df['day'].unique()


#DASHBOARD

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}

#DASH LAYOUT
app.layout = html.Div([
    html.Div([
        dcc.Markdown('''# ** Visual Analysis **'''),
        dcc.Markdown('''**Credits:**  *[Nextome] (https://www.nextome.net)*''')
    ]),
        

    dcc.Tabs(id="tabs", 
            value='Tab1',
            children=[
                dcc.Tab(label='Vista giornaliera', 
                        id='tab1', 
                        value='Tab1',
                        children =[
                            html.Div(style={'backgroundColor': colors['background']},
                                     children=[
                                        html.Div([
                                            dcc.Markdown(children='''Selezionare il giorno che si desidera monitorare tramite il menu *dropdown* e l'ora tramite lo *slider* '''), 
                                           html.Img(src="https://www.nextome.net/wp-content/uploads/2017/02/cropped-nextome_icon_menu_300-2.png",
                                                    style={'height': '50px',
                                                            'float': 'right',
                                                            'position': 'relative',
                                                            'bottom': '170px',
                                                            'left': '5px'
                                                            },
                                                    ),
                                                ]),

                                        html.Div([
                                            dcc.Dropdown(
                                                id='day-select',
                                                options=[{'label':i,'value':i}for i in available_days],
                                                value='day',
                                                clearable=False,
                                                placeholder="Select a day"
                                                ),

                                            dcc.RadioItems(
                                                id='user-area',
                                                options=[{'label':i,'value':i} for i in ['Area','Users']],
                                                value='Area',
                                                labelStyle={'display':'inline-block'}
                                                )],
                                                style={'width': '20%'}),
                                                
                                        html.Div([
                                            dcc.Graph(
                                                id='graph-with-slider',
                                                figure={
                                                    'layout': {
                                                        'plot_bgcolor': '#111111',
                                                        'paper_bgcolor': '#111111',
                                                        'font': {
                                                            'color': colors['text']
                                                                }
                                                            }
                                                        } 
                                                    ),
                                            
                                            dcc.Slider(
                                                id='hour-slider',
                                                min=df['hour'].min(),
                                                max=df['hour'].max(),
                                                value=df['hour'].min(),
                                                marks={str(hour):str(hour) for hour in df['hour'].unique()},
                                                step=None
                                                )],
                                                style={
                                                    'width': '60%',
                                                    'display': 'inline-block', 
                                                    'horizontal-align': 'center'}),
                                        html.Div([ 
                                            dcc.Graph(
                                                id='pie-with-slider',
                                                figure={
                                                    'layout':{
                                                        'plot_bgcolor': '#FFFFFF',
                                                        'paper_bgcolor': '#FFFFFF',
                                                        'font': { 
                                                            'color': colors['text']
                                                                }
                                                            }
                                                        }
                                                    )],
                                                    style={
                                                    'width':'30%',
                                                    'display':'inline-block',
                                                    'horizontal-align': 'center'
                                                        })
                                                ])
                ]),

                dcc.Tab(label='Vista oraria',
                        id='tab2',
                        value= 'Tab2', 
                        children=[
                            html.Div(style={'backgroundColor': colors['background']},
                                     children=[
                                        html.Div([
                                            dcc.Markdown(children='''Selezionare l'orario che si desidera monitorare tramite lo *slider* , il giorno considerato
                                                                    è quello selezionato in * vista giornaliera * '''),
                                            html.Img(src="https://www.nextome.net/wp-content/uploads/2017/02/cropped-nextome_icon_menu_300-2.png",
                                                    style={'height': '50px',
                                                            'float': 'right',
                                                            'position': 'relative',
                                                            'bottom': '170px',
                                                            'left': '5px'
                                                            },
                                                    ),
                                                ]),

                                        html.Div([
                                            dcc.RadioItems(
                                                id='user-area-orario',
                                                options=[{'label':i,'value':i} for i in ['Area','Users']],
                                                value='Area',
                                                labelStyle={'display':'inline-block'}
                                                )],
                                                style={'width': '20%'}),
                                                
                                        html.Div([
                                            dcc.Graph(
                                                id='graph-with-slider-orario',
                                                figure={
                                                    'layout': {
                                                        'plot_bgcolor': '#111111',
                                                        'paper_bgcolor': '#111111',
                                                        'font': {
                                                            'color': colors['text']
                                                                }
                                                            }
                                                        } 
                                                    ),
                                            
                                            dcc.Slider(
                                                id='minute-slider',
                                                min=df['min10'].min(),
                                                max=df['min10'].max(),
                                                value=df['min10'].min(),
                                                marks={str(min10):str(min10) for min10 in df['min10'].unique()},
                                                step=None 
                                                )],
                                                style={
                                                    'width': '60%',
                                                    'display': 'inline-block', 
                                                    'horizontal-align': 'center'}),
                                        html.Div([ 
                                            dcc.Graph(
                                                id='pie-with-slider-orario',
                                                figure={
                                                    'layout':{
                                                        'plot_bgcolor': '#FFFFFF',
                                                        'paper_bgcolor': '#FFFFFF',
                                                        'font': { 
                                                            'color': colors['text']
                                                                }
                                                            }
                                                        }
                                                    )],
                                                    style={
                                                    'width':'30%',
                                                    'display':'inline-block',
                                                    'horizontal-align': 'center',
                                                        })
                                                ]),
                

                ]),

                dcc.Tab(label='Vista mensile', 
                        id='tab3', 
                        value='Tab3',
                        children =[
                            html.Div(style={'backgroundColor': colors['background']},
                                     children=[
                                        html.Div([
                                            dcc.Markdown(children='''Selezionare tramite lo *slider* il giorno che si desidera monitorare'''), 
                                            html.Img(src="https://www.nextome.net/wp-content/uploads/2017/02/cropped-nextome_icon_menu_300-2.png",
                                                    style={'height': '50px',
                                                            'float': 'right',
                                                            'position': 'relative',
                                                            'bottom': '170px',
                                                            'left': '5px'
                                                            },
                                                    ),
                                                ]),

                                        html.Div([
                                            dcc.RadioItems(
                                                id='user-area-multi',
                                                options=[{'label':i,'value':i} for i in ['Area','Users']],
                                                value='Area',
                                                labelStyle={'display':'inline-block'}
                                                )],
                                                style={'width': '20%'}),
                                                
                                        html.Div([
                                            dcc.Graph(
                                                id='graph-with-slider-multi',
                                                figure={    
                                                    'layout': {
                                                        'plot_bgcolor': '#111111',
                                                        'paper_bgcolor': '#111111',
                                                        'font': {
                                                            'color': colors['text']
                                                                }
                                                            }
                                                        } 
                                                    ),
                                            
                                            dcc.Slider(
                                                id='day-slider-multi',
                                                min=df['day'].min(),
                                                max=df['day'].max(),
                                                value=df['day'].min(),
                                                marks={str(day):str(day) for day in df['day'].unique()},
                                                step=None
                                                )],
                                                style={
                                                    'width': '60%',
                                                    'display': 'inline-block', 
                                                    'horizontal-align': 'center'}),
                                        html.Div([ 
                                            dcc.Graph(
                                                id='pie-with-slider-multi',
                                                figure={
                                                    'layout':{
                                                        'plot_bgcolor': '#FFFFFF',
                                                        'paper_bgcolor': '#FFFFFF',
                                                        'font': { 
                                                            'color': colors['text']
                                                                }
                                                            }
                                                        }
                                                    )],
                                                    style={
                                                    'width':'30%',
                                                    'display':'inline-block',
                                                    'horizontal-align': 'center'
                                                        })
                                                ])
                ])
                

    ])
])  
    


#CALLBACKS TAB1 
@app.callback(
    Output('pie-with-slider', 'figure'),
    [Input('hour-slider', 'value'),
    Input('day-select','value')])

def update_pie (hour_slider,day_select):
    dff=df[df.day==day_select]
    dff2= dff[dff.hour==hour_slider]
    dff2['Area']=dff2['Area'].astype(int)

    aree=dff2['Area'].tolist()
    aree=np.unique(aree)
    aree.sort()
    aree=aree.tolist()

    labels = list(map(str, aree))

    values=[]
    i=0
    k=0
    for i in aree: 
        x=len(dff2[ dff2['Area']==aree[k] ])
        k=k+1
        values.append(x)


    trace=[]
    trace.append(go.Pie(
            labels=labels,
            values=values,
            textinfo='label'
            )
    )
    return {
        "data": trace,
        "layout": go.Layout(title="", 
                            margin={'l': 100, 'b': 10, 't': 10, 'r': 0},
                            )
        }
    

@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('hour-slider', 'value'),
    Input('user-area','value'),
    Input('day-select','value')])

def update_figure(selected_hour,user_area,selected_day):
    dff=df[df.day == selected_day] 
    filtered_df = dff[dff.hour == selected_hour]
    traces = []
    if user_area=='Area':
        for i in filtered_df.Area.unique():
            df_by_Area = filtered_df[filtered_df['Area'] == i]
            traces.append(go.Scatter(
                x=df_by_Area['X'],
                y=df_by_Area['Y'],
                text=df_by_Area['Username'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))
    if user_area=='Users':
        for i in filtered_df.Username.unique():
            df_by_Users= filtered_df[filtered_df['Username'] == i]
            traces.append(go.Scatter(
                x=df_by_Users['X'],
                y=df_by_Users['Y'],
                text=df_by_Users['Area'],
                mode='markers', 
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': '','range':[0,600]},
            yaxis={'title': '', 'range': [0, 605]},
            margin={'l': 40, 'b': 30, 't': 10, 'r': 40},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            plot_bgcolor= '#111111',
            paper_bgcolor='#111111'

        )
    }


#CALLBACK TAB2
@app.callback(
    Output('graph-with-slider-orario', 'figure'),
    [Input('hour-slider', 'value'),
    Input('minute-slider', 'value'),
    Input('user-area-orario','value'),
    Input('day-select','value')])

def update_figure_oraria(hour_slider_orario,minute_slider_orario,user_area_orario,day_select_orario):
    dff=df[df.day == day_select_orario] 
    filtered_df = dff[dff.hour == hour_slider_orario]
    filtered_df=filtered_df[filtered_df.min10 == minute_slider_orario]
    traces = []
    if user_area_orario=='Area':
        for i in filtered_df.Area.unique():
            df_by_Area = filtered_df[filtered_df['Area'] == i]
            traces.append(go.Scatter(
                x=df_by_Area['X'],
                y=df_by_Area['Y'],
                text=df_by_Area['Username'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))
    if user_area_orario=='Users':
        for i in filtered_df.Username.unique():
            df_by_Users= filtered_df[filtered_df['Username'] == i]
            traces.append(go.Scatter(
                x=df_by_Users['X'],
                y=df_by_Users['Y'],
                text=df_by_Users['Area'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': '','range':[0,600]},
            yaxis={'title': '', 'range': [0, 605]},
            margin={'l': 40, 'b': 30, 't': 10, 'r': 40},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            plot_bgcolor= '#111111',
            paper_bgcolor='#111111'

        )
    }


@app.callback(
    Output('pie-with-slider-orario', 'figure'),
    [Input('hour-slider', 'value'),
    Input('day-select','value'),
    Input('minute-slider', 'value')])

def update_pie_orario (hourSlider,daySelect,minuteSelect):
    dff=df[df.day==daySelect]
    dff2= dff[dff.hour==hourSlider]
    dff2=dff2[dff2.min10 == minuteSelect]
    dff2['Area']=dff2['Area'].astype(int)

    aree=dff2['Area'].tolist()
    aree=np.unique(aree)
    aree.sort()
    aree=aree.tolist()

    labels = list(map(str, aree))

    values=[]
    i=0
    k=0
    for i in aree: 
        x=len(dff2[ dff2['Area']==aree[k] ])
        k=k+1
        values.append(x)

    trace=[]
    trace.append(go.Pie(
            labels=labels,
            values=values,
            textinfo='label'
            )
    )
    return {
        "data": trace,
        "layout": go.Layout(title="", 
                            margin={'l': 100, 'b': 10, 't': 10, 'r': 0},
                            )
        }


#CALLBACK TAB3
@app.callback(
    Output('graph-with-slider-multi', 'figure'),
    [Input('day-slider-multi', 'value'),
    Input('user-area-multi','value')
    ])

def update_figure_multi (day_slider_multi,user_area_multi):
    filtered_df=df[df.day == day_slider_multi] 
    traces = []
    if user_area_multi=='Area':
        for i in filtered_df.Area.unique():
            df_by_Area = filtered_df[filtered_df['Area'] == i]
            traces.append(go.Scatter(
                x=df_by_Area['X'],
                y=df_by_Area['Y'],
                text=df_by_Area['Username'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))
    if user_area_multi=='Users':
        for i in filtered_df.Username.unique():
            df_by_Users= filtered_df[filtered_df['Username'] == i]
            traces.append(go.Scatter(
                x=df_by_Users['X'],
                y=df_by_Users['Y'],
                text=df_by_Users['Area'],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 5,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ))
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': '','range':[0,600]},
            yaxis={'title': '', 'range': [0, 605]},
            margin={'l': 40, 'b': 30, 't': 10, 'r': 40},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            plot_bgcolor= '#111111',
            paper_bgcolor='#111111'

        )
    }


@app.callback(
    Output('pie-with-slider-multi', 'figure'),
    [Input('day-slider-multi','value')] 
    )

def update_pie_multi (day_slider):
    dff2=df[df.day==day_slider]
    dff2['Area']=dff2['Area'].astype(int)
    aree=dff2['Area'].tolist()
    aree=np.unique(aree)
    aree.sort()
    aree=aree.tolist()

    labels = list(map(str, aree))

    values=[]
    i=0
    k=0
    for i in aree: 
        x=len(dff2[ dff2['Area']==aree[k] ])
        k=k+1
        values.append(x)

    trace=[]
    trace.append(go.Pie(
            labels=labels,
            values=values,
            textinfo='label'
            )
    )
    return {
        "data": trace,
        "layout": go.Layout(title="", 
                            margin={'l': 100, 'b': 10, 't': 10, 'r': 0},
                            )
        }



if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)
