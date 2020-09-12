# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:21:27 2020

@author: bhoomika
"""

import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Output
import webbrowser
import dash_bootstrap_components as dbc
import base64
import re

app=dash.Dash()
df=pd.read_csv('https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv')
print(df.head(5))
df1=df[['FIFA','Dial','Region Name','CLDR display name']]
df1['Dial']='+'+df['Dial']
print(df1.head(5))
df1.dropna(inplace=True)
#print(df1.isna().sum())

temp_list=sorted(df1['CLDR display name'].tolist())
global country_list
country_list=[{'label':str(i),'value':str(i)} for i in temp_list]

image_filename='logo.png'
global encoded_image
encoded_image=base64.b64encode(open(image_filename,'rb').read())

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
    
def create_app_ui():
    app.layout=html.Div(
        [
            
            dcc.Location(id='url',refresh=False),
            dcc.Link(html.Button(id='btn',children='Click here to login via OTP',n_clicks=0,style=dict()),href='/page-2'),
            #html.Button('Submit',id='submit',n_clicks=0),
            html.Div(id='page-content')
        ]
        )
    
@app.callback(
    
    Output('page-content','children'),
    [
     Input('url','pathname')
     ]
    )

def open_page2(pathname):
    if pathname=='/page-2':
        return html.Div([
            html.Div(style={'width':'100%','display':'flex',
        'align-items':'center','justify-content':'center'},
                     children=
                html.Img(src=app.get_asset_url('logo.png'),height='250px',width='800px')
            ),
            html.P('Enter contact number',style={'margin-left':350,'margin-bottom':0}),
            html.Div(id='trial',style={'width':'40%','display':'flex',
        'align-items':'center','margin-left':350,'justify-content':'center',
        'border-style':'solid','border-width':'2px','border-color':'yellow'},
                     children=
                [
            dcc.Dropdown(id='cont_code',
           style={'height':'30px','width':'130px','border':'0px'},
           options=country_list,placeholder='Select Country'),
            
            dcc.Input(id='number',disabled=True,style={'height':'40px','width':'50px',
                                                       'border':'0px'}),
            
            dcc.Input(id='number1', type='tel',persistence=True,
                      style={'height':'33px','width':'150px','border':'0px'},
                    pattern='^[0-9]{10}$',maxLength=10)
            ]
            ),
            html.Br(),
            html.Br(),
            html.Div(style={'width':'100%','display':'flex',
        'textAlign':'center','justify-content':'center'},children=
                (html.H3('Welcome Back'))),
            html.Div(style={'width':'100%','display':'flex',
        'textAlign':'center','justify-content':'center'},
                children=(
                html.H5('Please sign in to your account'))
                ),
            html.Div(style={'width':'100%','display':'flex',
        'textAlign':'center','justify-content':'center'},children=
            dcc.Link(html.Button(id='btn1',children='Sign In with OTP',disabled=True,
                style={'background-color':'#ff8000','color':'white',
                       'border':'0px','width':'150px','height':'30px'}),href='/page-3'))
            ]
            )
        
    elif pathname=='/page-3':
        return html.Div([
            html.Div(style={'width':'100%','display':'flex',
        'align-items':'center','justify-content':'center'},
                     children=
                html.Img(src=app.get_asset_url('page3.png'),height='300px',width='500px')
            ),
            html.H2('OTP sent successfully',
            style={'margin-left':'510px','margin-bottom':0}),
                    
            html.Br(),
            html.P(id='hi',children='An OTP has been sent to your number',
                    style={'margin-left':'510px','color':'grey','margin-bottom':0}),
            dcc.Link('Verify phone number',href='/page-2',
                     style={'margin-left':'560px','color':'#ff8000','margin-top':0}),
            html.Br(),
            dcc.Link('Change phone number',href='/page-2',
                     style={'margin-left':'560px','color':'#ff8000','margin-top':0}),
            html.Br(),
            html.Br(),
            html.P('*Enter the four-digit OTP sent to your mobile number*',
                   style={'margin-left':'510px','color':'grey','margin-below':0}),
            
            dcc.Input(id='otp', type='tel',
                      style={'height':'33px','width':'150px','margin-left':'550px'},
                    pattern='^[0-9]{4}$',maxLength=4),
            html.Br(),
            html.Div(style={'width':'100%','display':'flex',
        'justify-content':'center'},#'justify-content':'center'},
                     children=
                [
            html.P(id='again',children=([
                "Didn't receive the code?  ",
                html.Button(id='rlink',children='resend',n_clicks=0,style={
                    'color':'#ff8000','background-color':'white','border':'none',
                    'outline':'none'})
                         
                ]),
                    style={'color':'grey'})
            ]),
            html.Br(),
            dcc.Link(html.Button(id='verify',children='Verify',disabled=True,
                style={'background-color':'#ff8000','color':'white','margin-left':'550px',
                       'border':'0px','width':'150px','height':'30px'
                       }),href='/page-4'),
            dbc.Alert(
                'OTP resent successfully!',
                style={'background-color':'#90EE90','font-weight':'bolder'},
                id='alert1',
                dismissable=True,
                duration=6000,
                is_open=False
                ),
            dbc.Alert(
                'Please enter correct OTP!',
                style={'background-color':'#ffcccb','font-weight':'bolder'},
                id='alert2',
                dismissable=True,
                duration=30000,
                is_open=False
                )
            ])
    elif pathname=='/page-4':
        return html.Div([
            html.Div(style={'width':'100%','display':'flex',
        'align-items':'center','justify-content':'center'},
                     children=
                html.Img(src=app.get_asset_url('page4a.png'),height='350px',width='350px')
            ),
            html.H1(id='hi',children='Welcome to AdmitKard',style={'margin-left':'480px'}),
            html.P("In order to provide you with a custom experience,",style={'margin-left':'480px',
                                'color':'grey','margin-bottom':0}),
            html.P("we need to ask you a few questions.",style={'margin-left':'500px',
                                'font-weight':'bolder','color':'grey','margin-top':0}),
            html.Br(),
            html.Button(id='end',children='Get Started',
                        style={'background-color':'#ff8000','color':'white','margin-left':'550px',
                       'border':'0px','width':'150px','height':'30px'
                       }),
            html.P("*This will only take 5 min.",
                   style={'margin-left':'550px',
        'color':'grey','margin-top':0})
            ])
    
    
@app.callback(
    
    Output('btn1','disabled'),
    
    [Input('number1','value'),
     Input('cont_code','value')
     ]
    )
def enable_button(num_val,dd_val):
    pattern='^[0-9]{10}$'
    result=re.match(pattern,num_val)
    if result:
        if dd_val!=None and dd_val!=[]:
            return False
        else:
            return True
    else:
        return True
    
@app.callback(
    
    Output('verify','disabled'),
    
    [Input('otp','value')
     ]
    )
def enable_button2(otp_val):
    pattern='1234'
    if otp_val!=[] and otp_val==pattern:
        return False
    else:
        return True

@app.callback(
    Output('alert1','is_open'),
    [
     Input('rlink','n_clicks')
     ],
    [State('alert1','is_open')]
    
    )

def alrt(n_clicks,is_open):
    if n_clicks:

        return True
    else:
        return False
    
@app.callback(
    Output('alert2','is_open'),
    [
     Input('verify','disabled')
     ],
    [State('alert2','is_open')]
    
    )

def alrt1(disabled,is_open):
    if disabled:

        return True
    else:
        return False
    

@app.callback(
    Output('btn','style'),
    [
     Input('url','pathname')
     ]
    )     

def hide_btn(pathname):
    if pathname=='/page-2' or pathname=='/page-3' or pathname=='/page-4':
        return dict(display='none')
    else:
        pass
    

@app.callback(
    Output('number','value'),
    [
     Input('cont_code','value')
     ]
    )
    
def update_dropdown_val(val1):
    df2=df1[df1['CLDR display name']==val1] 
    print(df2)
    valout=df2['Dial']
    value=valout
    return value
    
def main():
    open_browser()
    
    create_app_ui()
    app.title=("AdmitKard|SignIn")
    app.run_server()
    
    
if __name__=='__main__':
    main()