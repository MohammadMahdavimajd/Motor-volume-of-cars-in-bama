import pandas as pd 
import pandas as pd 
import sklearn
import numpy as np 
import matplotlib.pyplot as plt 
import plotly.express as px
from bokeh.plotting import figure , output_notebook , show
import seaborn as sns
import json 
df_Imputed2=pd.read_csv(r'C:\Users\vira\Desktop\Data\car\cars2.csv')
df_Imputed2.nunique()

sorted_df=df_Imputed2.sort_values(by = 'سال ساخت' , ascending = False) 
df_grouped = df_Imputed2.groupby(['نوع سوخت', 'سال ساخت'])['حجم موتور(لیتر)'] \
    .agg(میانگین_حجم_موتور='mean', تعداد_خودرو='count').reset_index()
fig = px.treemap(
    df_grouped,
    path=['نوع سوخت', 'سال ساخت'],
    values='میانگین_حجم_موتور', 
    color='میانگین_حجم_موتور',   
    hover_data={
        'میانگین_حجم_موتور': ':.2f',  
        'تعداد_خودرو': True           
    },
    title='میانگین حجم موتور خودروها و تعداد آن‌ها در سایت باما',
    color_continuous_scale='RdBu'
)
fig.update_layout(
    font=dict(
        family="Vazir",
        size=14,
        color="black"
    ),
    title=dict(
        text="میانگین حجم موتور خودروها و تعداد آن‌ها در سایت باما",
        font=dict(
            family="Vazir",
            size=18,
            color="black"
        ),
        x=0.5,
        xanchor='center'
    ),
    margin=dict(t=50, l=25, r=25, b=25),
)

fig.update_traces(
    texttemplate= '%{label}',
    textposition='middle center'
)
fig.update_traces(
    texttemplate='%{label}',
    textposition='middle center',
    hovertemplate='<b>نوع سوخت:</b> %{customdata[0]}<br>' +
                  '<b>سال ساخت:</b> %{customdata[1]}<br>' +
                  '<b>میانگین حجم موتور:</b> %{customdata[2]:.2f} لیتر<br>' +
                  '<b>تعداد خودرو:</b> %{customdata[3]}<extra></extra>',
    customdata=df_grouped[['نوع سوخت', 'سال ساخت', 'میانگین_حجم_موتور', 'تعداد_خودرو']].values
)
import plotly.io as pio
pio.renderers.default = 'browser'

fig.show() 

'''app = Dash(__name__)

app.layout=html.Div([
    html.H1("Motor volume of cars from 1355 to 1404 bama "),
    dcc.Graph(figure=fig ) ,
])
if __name__ == '__main__':
    app.run_server(debug=True , port=8080)'''
import os
import webbrowser
current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, "motor_volume_treemap.html")
fig.write_html(output_file)
webbrowser.open('file://' + output_file)
print(f"فایل HTML با موفقیت ذخیره شد و در مرورگر باز شد: {output_file}")

