import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import base64
from plotly.subplots import make_subplots
import resample
from dash.dependencies import Input, Output
from plotly import tools
#-----------------Calculo para Diagrama de barras----------------

#Adiciones
df = pd.read_csv('Adiciones_SumaxDia2.csv')
columnas = ['Date', 'Valor' ]
df1 = df[columnas]
df_seleccionados =  pd.DataFrame(data=df1)
#df_seleccionados_new2 = df_seleccionados.set_index("Date", inplace = True)

df_seleccionados_nuevo = resample.fun1()
figBar = px.bar(df_seleccionados_nuevo, x='Date', y='Valor')

figBar.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
figBar.update_layout(title_text='                 Adiciones a lo largo de los años')


#Retiros

df_Retiros = pd.read_csv('Retiros_SumaxDia2.csv')
columnas = ['Date', 'Valor' ]
df1_Retiros = df_Retiros[columnas]
df_seleccionados_retiros =  pd.DataFrame(data=df1_Retiros)
#df_seleccionados_new2 = df_seleccionados.set_index("Date", inplace = True)

df_seleccionados_retiros_nuevo = resample.funRetiros()
figBar_Retiros = px.bar(df_seleccionados_retiros_nuevo, x='Date', y='Valor')

figBar_Retiros.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
figBar_Retiros.update_layout(title_text='                 Retiros a lo largo de los años')

#Cancelaciones

df_Cancelaciones = pd.read_csv('Cancelaciones_SumaxDia2.csv')
columnas = ['Date', 'Valor' ]
df1_Cancelaciones = df_Cancelaciones[columnas]
df_seleccionados_cancelaciones =  pd.DataFrame(data=df1_Cancelaciones)
#df_seleccionados_new2 = df_seleccionados.set_index("Date", inplace = True)

df_seleccionados_cancelaciones_nuevo = resample.funCancelaciones()
figBar_Cancelaciones = px.bar(df_seleccionados_cancelaciones_nuevo, x='Date', y='Valor')

figBar_Cancelaciones.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
figBar_Cancelaciones.update_layout(title_text='                 Cancelaciones a lo largo de los años')


#------------------------------Descompose--------------------------#

# ADICIONES
figDescompose = make_subplots(rows=2, cols=1)


result = resample.descompose()
residual = result.resid
seasonal = result.seasonal 
trend = result.trend

residual_df = residual.to_frame()
residual_df = residual_df.fillna(0)
residual_df = residual_df.reset_index()

figResidual = go.Figure([go.Scatter(x=residual_df['Date'], y=residual_df['resid'])])

seasonal_df = seasonal.to_frame()
seasonal_df = seasonal_df.fillna(0)
seasonal_df = seasonal_df.reset_index()
figSeasonal = go.Figure([go.Scatter(x=seasonal_df['Date'], y=seasonal_df['seasonal'])])

trend_df = (trend.to_frame())
trend_df = trend_df.fillna(0)
trend_df = trend_df.reset_index()
figTrend = go.Figure([go.Scatter(x=trend_df['Date'], y=trend_df['trend'])])

figDescompose.add_trace(
    go.Scatter(x=trend_df['Date'], y=trend_df['trend'], name = 'Trend'),
    row=1, col=1
)

figDescompose.add_trace(
    go.Scatter(x=seasonal_df['Date'], y=seasonal_df['seasonal'], name = 'Seasonal'),
    row=2, col=1
)

figDescompose.update_layout(
    title="Descomposición de la serie de tiempo "
)

# RETIROS

figDescompose_Retiros = make_subplots(rows=2, cols=1)


result_R = resample.descomposeRetiros()
residual_R = result_R.resid
seasonal_R = result_R.seasonal 
trend_R = result_R.trend

residual_df_R = residual_R.to_frame()
residual_df_R = residual_df_R.fillna(0)
residual_df_R = residual_df_R.reset_index()

figResidual_Retiros = go.Figure([go.Scatter(x=residual_df_R['Date'], y=residual_df_R['resid'])])

seasonal_df_R = seasonal_R.to_frame()
seasonal_df_R = seasonal_df_R.fillna(0)
seasonal_df_R = seasonal_df_R.reset_index()
figSeasonal_Retiros = go.Figure([go.Scatter(x=seasonal_df_R['Date'], y=seasonal_df_R['seasonal'])])

trend_df_R = (trend_R.to_frame())
trend_df_R = trend_df_R.fillna(0)
trend_df_R = trend_df_R.reset_index()
figTrend_Retiros = go.Figure([go.Scatter(x=trend_df_R['Date'], y=trend_df_R['trend'])])

figDescompose_Retiros.add_trace(
    go.Scatter(x=trend_df_R['Date'], y=trend_df_R['trend'], name = 'Trend'),
    row=1, col=1
)

figDescompose_Retiros.add_trace(
    go.Scatter(x=seasonal_df_R['Date'], y=seasonal_df_R['seasonal'], name = 'Seasonal'),
    row=2, col=1
)

figDescompose_Retiros.update_layout(
    title="Descomposición de la serie de tiempo "
)

#Cancelaciones

figDescompose_Cancelaciones = make_subplots(rows=2, cols=1)


result_C = resample.descomposeCancelaciones()
residual_C = result_C.resid
seasonal_C = result_C.seasonal 
trend_C = result_C.trend

residual_df_C = residual_C.to_frame()
residual_df_C = residual_df_C.fillna(0)
residual_df_C = residual_df_C.reset_index()

figResidual_Cancelaciones = go.Figure([go.Scatter(x=residual_df_C['Date'], y=residual_df_C['resid'])])

seasonal_df_C = seasonal_C.to_frame()
seasonal_df_C = seasonal_df_C.fillna(0)
seasonal_df_C = seasonal_df_C.reset_index()
figSeasonal_Cancelaciones = go.Figure([go.Scatter(x=seasonal_df_C['Date'], y=seasonal_df_C['seasonal'])])

trend_df_C = (trend_C.to_frame())
trend_df_C = trend_df_C.fillna(0)
trend_df_C = trend_df_C.reset_index()
figTrend_Cancelaciones = go.Figure([go.Scatter(x=trend_df_C['Date'], y=trend_df_C['trend'])])

figDescompose_Cancelaciones.add_trace(
    go.Scatter(x=trend_df_C['Date'], y=trend_df_C['trend'], name = 'Trend'),
    row=1, col=1
)

figDescompose_Cancelaciones.add_trace(
    go.Scatter(x=seasonal_df_C['Date'], y=seasonal_df_C['seasonal'], name = 'Seasonal'),
    row=2, col=1
)

figDescompose_Cancelaciones.update_layout(
    title="Descomposición de la serie de tiempo "
)

#-----------------------------------------------------------

#---------------------------MultiBar Adiciones-----------------------

#                              2015                               #
mask = (df_seleccionados['Date'] > '2015-07-01') & (df_seleccionados['Date'] <= '2015-12-30')
df_seleccionados1 = df_seleccionados.loc[mask]

trace1 = go.Bar(
    x=df_seleccionados1['Date'],
    y=df_seleccionados1['Valor'],
    name='2015'
)

#                              2016                                #
mask1 = (df_seleccionados['Date'] > '2016-01-01') & (df_seleccionados['Date'] <= '2016-12-30')
df_seleccionados2 = df_seleccionados.loc[mask1]

trace2 = go.Bar(
    x=df_seleccionados2['Date'],
    y=df_seleccionados2['Valor'],
    name='2016'
)

#                              2017                               #
mask2 = (df_seleccionados['Date'] > '2017-01-01') & (df_seleccionados['Date'] <= '2017-12-30')
df_seleccionados3 = df_seleccionados.loc[mask2]

trace3 = go.Bar(
    x=df_seleccionados3['Date'],
    y=df_seleccionados3['Valor'],
    name='2017'
)              

#                              2018                              #
mask3 = (df_seleccionados['Date'] > '2018-01-01') & (df_seleccionados['Date'] <= '2018-12-30')
df_seleccionados4 = df_seleccionados.loc[mask3]

trace4 = go.Bar(
    x=df_seleccionados4['Date'],
    y=df_seleccionados4['Valor'],
    name='2018'
)                

#                              2019                              #
mask4 = (df_seleccionados['Date'] > '2019-01-01') & (df_seleccionados['Date'] <= '2019-12-30')
df_seleccionados5 = df_seleccionados.loc[mask4]

trace5 = go.Bar(
    x=df_seleccionados5['Date'],
    y=df_seleccionados5['Valor'],
    name='2019'
)  
#                              2020                              #
mask5 = (df_seleccionados['Date'] > '2020-01-01') & (df_seleccionados['Date'] <= '2020-12-30')
df_seleccionados6 = df_seleccionados.loc[mask5]

trace6 = go.Bar(
    x=df_seleccionados6['Date'],
    y=df_seleccionados6['Valor'],
    name='2020'
)  

figMultiBarChart = tools.make_subplots(rows=3, cols=2, shared_xaxes=False)

figMultiBarChart.append_trace(trace1, 1,1)
figMultiBarChart.append_trace(trace2, 1, 2)
figMultiBarChart.append_trace(trace3,2,1)
figMultiBarChart.append_trace(trace4,2,2)
figMultiBarChart.append_trace(trace5,3,1)
figMultiBarChart.append_trace(trace6,3,2)

figMultiBarChart.update_layout(title = 'Adiciones representadas año a año')

#----------------------------------------------------------------

#---------------------------MultiBar Retiros-----------------------

#                              2015                               #
mask_R1 = (df_seleccionados_retiros['Date'] > '2015-07-01') & (df_seleccionados_retiros['Date'] <= '2015-12-30')
df_seleccionados_R = df_seleccionados_retiros.loc[mask_R1]

trace_R1 = go.Bar(
    x=df_seleccionados_R['Date'],
    y=df_seleccionados_R['Valor'],
    name='2015'
)

#                              2016                                #
mask_R2 = (df_seleccionados_retiros['Date'] > '2016-01-01') & (df_seleccionados_retiros['Date'] <= '2016-12-30')
df_seleccionados_R2 = df_seleccionados_retiros.loc[mask_R2]

trace_R2 = go.Bar(
    x=df_seleccionados_R2['Date'],
    y=df_seleccionados_R2['Valor'],
    name='2016'
)

#                              2017                               #
mask_R3 = (df_seleccionados_retiros['Date'] > '2017-01-01') & (df_seleccionados_retiros['Date'] <= '2017-12-30')
df_seleccionados_R3 = df_seleccionados_retiros.loc[mask_R3]

trace_R3 = go.Bar(
    x=df_seleccionados_R3['Date'],
    y=df_seleccionados_R3['Valor'],
    name='2017'
)              

#                              2018                              #
mask_R4 = (df_seleccionados_retiros['Date'] > '2018-01-01') & (df_seleccionados_retiros['Date'] <= '2018-12-30')
df_seleccionados_R4 = df_seleccionados_retiros.loc[mask_R4]

trace_R4 = go.Bar(
    x=df_seleccionados_R4['Date'],
    y=df_seleccionados_R4['Valor'],
    name='2018'
)                

#                              2019                              #
mask_R5 = (df_seleccionados_retiros['Date'] > '2019-01-01') & (df_seleccionados_retiros['Date'] <= '2019-12-30')
df_seleccionados_R5 = df_seleccionados_retiros.loc[mask_R5]

trace_R5 = go.Bar(
    x=df_seleccionados_R5['Date'],
    y=df_seleccionados_R5['Valor'],
    name='2019'
)  
#                              2020                              #
mask_R6 = (df_seleccionados_retiros['Date'] > '2020-01-01') & (df_seleccionados_retiros['Date'] <= '2020-12-30')
df_seleccionados_R6 = df_seleccionados_retiros.loc[mask5]

trace_R6 = go.Bar(
    x=df_seleccionados_R6['Date'],
    y=df_seleccionados_R6['Valor'],
    name='2020'
)  

figMultiBarChart_Retiros = tools.make_subplots(rows=3, cols=2, shared_xaxes=False)

figMultiBarChart_Retiros.append_trace(trace_R1, 1,1)
figMultiBarChart_Retiros.append_trace(trace_R2, 1, 2)
figMultiBarChart_Retiros.append_trace(trace_R3,2,1)
figMultiBarChart_Retiros.append_trace(trace_R4,2,2)
figMultiBarChart_Retiros.append_trace(trace_R5,3,1)
figMultiBarChart_Retiros.append_trace(trace_R6,3,2)

figMultiBarChart_Retiros.update_layout(title = 'Retiros representadas año a año')

#----------------------------------------------------------------

#---------------------------MultiBar Cancelaciones-----------------------

#                              2015                               #
mask_C1 = (df_seleccionados_cancelaciones['Date'] > '2015-07-01') & (df_seleccionados_cancelaciones['Date'] <= '2015-12-30')
df_seleccionados_C = df_seleccionados_cancelaciones.loc[mask_C1]

trace_C1 = go.Bar(
    x=df_seleccionados_C['Date'],
    y=df_seleccionados_C['Valor'],
    name='2015'
)

#                              2016                                #
mask_C2 = (df_seleccionados_cancelaciones['Date'] > '2016-01-01') & (df_seleccionados_cancelaciones['Date'] <= '2016-12-30')
df_seleccionados_C2 = df_seleccionados_cancelaciones.loc[mask_C2]

trace_C2 = go.Bar(
    x=df_seleccionados_C2['Date'],
    y=df_seleccionados_C2['Valor'],
    name='2016'
)

#                              2017                               #
mask_C3 = (df_seleccionados_cancelaciones['Date'] > '2017-01-01') & (df_seleccionados_cancelaciones['Date'] <= '2017-12-30')
df_seleccionados_C3 = df_seleccionados_cancelaciones.loc[mask_C3]

trace_C3 = go.Bar(
    x=df_seleccionados_C3['Date'],
    y=df_seleccionados_C3['Valor'],
    name='2017'
)              

#                              2018                              #
mask_C4 = (df_seleccionados_cancelaciones['Date'] > '2018-01-01') & (df_seleccionados_cancelaciones['Date'] <= '2018-12-30')
df_seleccionados_C4 = df_seleccionados_cancelaciones.loc[mask_R4]

trace_C4 = go.Bar(
    x=df_seleccionados_C4['Date'],
    y=df_seleccionados_C4['Valor'],
    name='2018'
)                

#                              2019                              #
mask_C5 = (df_seleccionados_cancelaciones['Date'] > '2019-01-01') & (df_seleccionados_cancelaciones['Date'] <= '2019-12-30')
df_seleccionados_C5 = df_seleccionados_cancelaciones.loc[mask_C5]

trace_C5 = go.Bar(
    x=df_seleccionados_C5['Date'],
    y=df_seleccionados_C5['Valor'],
    name='2019'
)  
#                              2020                              #
mask_C6 = (df_seleccionados_cancelaciones['Date'] > '2020-01-01') & (df_seleccionados_cancelaciones['Date'] <= '2020-12-30')
df_seleccionados_C6 = df_seleccionados_cancelaciones.loc[mask5]

trace_C6 = go.Bar(
    x=df_seleccionados_C6['Date'],
    y=df_seleccionados_C6['Valor'],
    name='2020'
)  

figMultiBarChart_Cancelaciones = tools.make_subplots(rows=3, cols=2, shared_xaxes=False)

figMultiBarChart_Cancelaciones.append_trace(trace_C1, 1,1)
figMultiBarChart_Cancelaciones.append_trace(trace_C2, 1, 2)
figMultiBarChart_Cancelaciones.append_trace(trace_C3,2,1)
figMultiBarChart_Cancelaciones.append_trace(trace_C4,2,2)
figMultiBarChart_Cancelaciones.append_trace(trace_C5,3,1)
figMultiBarChart_Cancelaciones.append_trace(trace_C6,3,2)

figMultiBarChart_Cancelaciones.update_layout(title = 'Cancelaciones representadas año a año')

#----------------------------------------------------------------

#---------------Multigraph Data Train-------------------

from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(shared_xaxes= True, shared_yaxes= True)

data_Train = resample.data_Train()

pred_TrainAd = resample.pred_train()
# Add traces
fig1.add_trace(
    go.Scatter(y= data_Train[200:400], name="Adiciones reales"),
    
)

rango = []
for i in range(10,len(data_Train[200:400])+10):
    rango.append(i)

fig1.add_trace(
    go.Scatter(x=rango, y=pred_TrainAd[200:400], name="Predicción"),
    
)

# Add figure title
fig1.update_layout(
    title_text="Datos de entrenamiento para el modelo de adiciones"
)

# Set x-axis title
fig1.update_xaxes(title_text="Fechas")

# Set y-axes titles
fig1.update_yaxes(title_text="Valor en COP")

fig1.show()

# RETIROS

figRetiros = make_subplots(shared_xaxes= True, shared_yaxes= True)

data_TrainR = resample.data_TrainRetiros()

pred_TrainRetiros = resample.pred_trainRetiros()
# Add traces
figRetiros.add_trace(
    go.Scatter(y= data_TrainR[200:400], name="Retiros reales"),
    
)

rangoR = []
for i in range(10,len(data_TrainR[200:400])+10):
    rangoR.append(i)

figRetiros.add_trace(
    go.Scatter(x=rangoR, y=pred_TrainRetiros[200:400], name="Predicción"),
    
)

# Add figure title
figRetiros.update_layout(
    title_text="Datos de entrenamiento para el modelo de retiros"
)

# Set x-axis title
figRetiros.update_xaxes(title_text="Fechas")

# Set y-axes titles
figRetiros.update_yaxes(title_text="Valor en COP")

figRetiros.show()

#------------------Multigraph data test--------------------------

# Create figure with secondary y-axis
fig_Adiciones_Test = make_subplots(shared_xaxes= True, shared_yaxes= True)

data_Test = resample.data_Test()

pred_TestAd = resample.pred_test()
# Add traces
fig_Adiciones_Test.add_trace(
    go.Scatter(y= data_Test, name="Adiciones reales"),
    
)

rangoTest = []
for i in range(22,len(data_Test)+22):
    rangoTest.append(i)

fig_Adiciones_Test.add_trace(
    go.Scatter(x=rangoTest, y=pred_TestAd, name="Predicción"),
    
)

# Add figure title
fig_Adiciones_Test.update_layout(
    title_text="Datos de prueba para el modelo de adiciones"
)

# Set x-axis title
fig_Adiciones_Test.update_xaxes(title_text="Fechas")

# Set y-axes titles
fig_Adiciones_Test.update_yaxes(title_text="Valor en COP")

fig_Adiciones_Test.show()

#RETIROS

fig_Retiros_Test = make_subplots(shared_xaxes= True, shared_yaxes= True)

data_TestR = resample.data_TestRetiros()

pred_TestRetiros = resample.pred_testRetiros()
# Add traces
fig_Retiros_Test.add_trace(
    go.Scatter(y= data_TestR, name="Retiros reales"),
    
)

rangoTestR = []
for i in range(10,len(data_TestR)+10):
    rangoTestR.append(i)

fig_Retiros_Test.add_trace(
    go.Scatter(x=rangoTestR, y=pred_TestRetiros, name="Predicción"),
    
)

# Add figure title
fig_Retiros_Test.update_layout(
    title_text="Datos de prueba para el modelo de retiros"
)

# Set x-axis title
fig_Retiros_Test.update_xaxes(title_text="Fechas")

# Set y-axes titles
fig_Retiros_Test.update_yaxes(title_text="Valor en COP")

fig_Retiros_Test.show()
#---------------------------------------------------------------



#------------------LOGO----------------------#

test_png = 'BTGPACTUAL_LOGO.png'
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

#-----------------------------------------------


df = pd.read_csv('Adiciones_SumaxDia2.csv')

fig = px.line(df, x='Date', y='Valor', title='Serie de tiempo de las adiciones de clientes')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)


df_Retiros = pd.read_csv('Retiros_SumaxDia2.csv')

fig_Serie_Retiros = px.line(df_Retiros, x='Date', y='Valor', title='Serie de tiempo de los retiros de clientes')
fig_Serie_Retiros.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

df_Cancelaciones = pd.read_csv('Cancelaciones_SumaxDia2.csv')

fig_Serie_Cancelaciones = px.line(df_Cancelaciones, x='Date', y='Valor', title='Serie de tiempo de las cancelaciones de clientes')
fig_Serie_Cancelaciones.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
#---------------------- Descompose -------------------------#

#------------------------------------------------------------#


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

#------------------MAIN--------------------

app.layout = html.Div([
    html.Div([
        
        html.Div([
            html.Div([
                html.H1(children = "MODELO DE TRANSACCIONES",
                            ),

                html.Div(children='''
                            Modelo con series de tiempo para la predicción de adiciones y retiros de los clientes
                            '''),
            ], className= 'nine columns'),

            html.Img(
                src = 'data:image/png;base64,{}'.format(test_base64),
                className = 'three columns',
                style = {
                    'height':'5%',
                    'width': '19%',
                    'float': 'right',
                    'position':'relative',
                    'margin-top':5,
                    'margin-right':5
                        },
            ),

    ], className = 'row'),   

    
    html.Div([
        dcc.Tabs(
            id="tabs-with-classes",
            value='tab-2',
            parent_className='custom-tabs',
            className='custom-tabs-container',
            children=[
                dcc.Tab(
                    label='ADICIONES',
                    value='tab-1',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                dcc.Tab(
                    label='RETIROS',
                    value='tab-2',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                dcc.Tab(
                    label='APERTURAS',
                    value='tab-3', className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                dcc.Tab(
                    label='CANCELACIONES',
                    value='tab-4',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
            ]),

            html.Div(id='tabs-content-classes'),

        ], className = 'row'),

    ], className = 'ten columns offset-by-one') ,
    
])


@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
           
                html.Div([
                    dcc.Graph(figure=fig), 
                ], className = 'row'),

                html.Div([
                    html.Div([
                        dcc.Graph(figure=figBar),
                    ], className = 'six columns'),

                    html.Div([
                        dcc.Graph(figure=figDescompose),
                    ], className= 'six columns'),

                ], className = 'row'),

                html.Div([
                    dcc.Graph(figure=figMultiBarChart,
                    ), 
                ],className = 'row'),

                html.Div([
                    dcc.Graph(figure=fig1), 
                ], className = 'row'),
                
                html.Div([
                    dcc.Graph(figure= fig_Adiciones_Test)
                ], className = 'row')

        ])
    elif tab == 'tab-2':
        return html.Div([
                
                html.Div([
                    dcc.Graph(figure=fig_Serie_Retiros), 
                ], className = 'row'),

                html.Div([
                    html.Div([
                        dcc.Graph(figure=figBar_Retiros),
                    ], className = 'six columns'),

                    html.Div([
                        dcc.Graph(figure=figDescompose_Retiros),
                    ], className= 'six columns'),

                ], className = 'row'),

                html.Div([
                    dcc.Graph(figure=figMultiBarChart_Retiros,
                    ), 
                ],className = 'row'),

                html.Div([
                    dcc.Graph(figure=figRetiros), 
                ], className = 'row'),
                
                html.Div([
                    dcc.Graph(figure=fig_Retiros_Test), 
                ], className = 'row'),

        ])
    elif tab == 'tab-3':
        return html.Div([
                html.Div([
                    dcc.Graph(figure=fig_Serie_Cancelaciones), 
                ], className = 'row'),

                html.Div([
                    html.Div([
                        dcc.Graph(figure=figBar_Cancelaciones),
                    ], className = 'six columns'),

                    html.Div([
                        dcc.Graph(figure=figDescompose_Cancelaciones),
                    ], className= 'six columns'),

                ], className = 'row'),

                html.Div([
                    dcc.Graph(figure=figMultiBarChart_Cancelaciones,
                    ), 
                ],className = 'row'),

                html.Div([
                    #dcc.Graph(figure=figCancelaciones), 
                ], className = 'row'),
                
                html.Div([
                    #dcc.Graph(figure=fig_Cancelaciones_Test), 
                ], className = 'row'),

        ])
    elif tab == 'tab-4':
        return html.Div([
            html.Div([
                    dcc.Graph(figure=fig_Serie_Cancelaciones), 
                ], className = 'row'),

                html.Div([
                    html.Div([
                        dcc.Graph(figure=figBar_Cancelaciones),
                    ], className = 'six columns'),

                    html.Div([
                        dcc.Graph(figure=figDescompose_Cancelaciones),
                    ], className= 'six columns'),

                ], className = 'row'),

                html.Div([
                    dcc.Graph(figure=figMultiBarChart_Cancelaciones,
                    ), 
                ],className = 'row'),

                html.Div([
                    #dcc.Graph(figure=figCancelaciones), 
                ], className = 'row'),
                
                html.Div([
                    #dcc.Graph(figure=fig_Cancelaciones_Test), 
                ], className = 'row'),
        ])

#------------------------------------




if __name__ == "__main__":
    app.run_server()
