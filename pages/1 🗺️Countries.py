#================
#        Library
#================
import streamlit as st
from PIL import Image

#        work data
import pandas as pd

## Importar map
import folium
from streamlit_folium import folium_static
from folium.plugins import Draw # desenhar
# Gráficos
import plotly.express as px
import plotly.graph_objects as go 
#=================
#        Library
#=================





st.set_page_config( page_title = 'Visão Países', page_icon = '🗺️', layout = 'wide' )



#____________---Loading data---__________
df = pd.read_csv('Dataset/zomato.csv')
#____________--\Loading data---__________



#___________---Limpeza dos dados---_______
def clean_data(df):
#Correção do espaço
    lista_cols = list(df.head(0)) 
    for cols in lista_cols:
        # Verificar
        if  type(df.loc[0 , cols]) == str:
            # Cocertar o espaço 'texto ' p/ 'texto'
            df.loc[:, cols] = df.loc[:, cols].str.strip() 
            print('Funcionou str')
            # Remover o 'NaN'
            df = df.loc[df[cols] != 'NaN', :]

        else: 
            print('Funcionou float or int')
            # Armazenar o tipo 
            classe = type(df.loc[0,cols])
            # Mudo o tipo para str
            df[cols]= df[cols].astype(str)
            # Concertar os espaços
            df.loc[:, cols] = df.loc[:, cols].str.strip()
            # Remover o 'NaN'
            df = df.loc[df[cols] != 'NaN', :]
            # Converto para tipo anterior
            df[cols]= df[cols].astype(classe)
    
    return(df)

# Chamando a função de limpeza clean_data
df =clean_data(df)
#___________--\Limpeza dos dados---_______




COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]
#__________--- Color---___________________



#========================================
#              Barra Laterals
#========================================
    
#image_path = 'C:/Users\Antonio Richard/OneDrive - acad.ifma.edu.br/Documentos/A Sala de aprendizado/repos/JupyterLab/Dashboards/Delivery_india/'

#image = Image.open(image_path + 'Delivery.jpg')
st.sidebar.markdown(' # Zomato Company !')
image = Image.open('Logo_scooter_delivery.png')

st.sidebar.image(image, width = 150)

st.sidebar.markdown('## Fastest Delivery in Town')

#_____________---FILTER---_______
    
st.sidebar.markdown("""---""")

# FILTRO DE DATA

st.sidebar.markdown(' ## Filtros ')
st.sidebar.markdown(' ### Escolha os Paises que Deseja visualizar as Informaçõess!')

# FILTRO DE CLIMA
# Options
#interessante tirar conditions dos nomes 

traffic_options1 = st.sidebar.multiselect( 
                     'Selecione o País aqui 👇!', 
                    df['Country_id'].unique(), 
                    default = ['Philippines', 'Brazil', 'Australia', 'United States of America', 'Canada', 'Singapure', 
                               'United Arab Emirates', 'India', 'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'], 
)


linhas_selecionadas2 =  df['Country_id'].isin( traffic_options1)
df = df.loc[linhas_selecionadas2,:]

#========================================
#              \Barra Laterals
#========================================



#========================================
#              ESTRUTURA
#========================================
#____________---Title---____________
st.markdown( '# 🗺️ Visão Países 🗺️')

#____________---Bloco---____________
with st.container(height = None, border = True):
    #st.markdown('Quantidade de Restaurantes Registrados por País')
    cols = ['Restaurant ID', 'Country_id']
    # Selecao de linhas
    df_aux = df.loc[:,cols].groupby('Country_id').count().reset_index().sort_values('Restaurant ID', ascending = False)
    # desenhar o gráfio de linhas
    fig = px.bar(df_aux, x='Country_id', y='Restaurant ID', text = 'Restaurant ID', color='Restaurant ID', labels={'Country_id': 'Países', 'Restaurant ID': 'Quantidade de Restaurantes'})
    fig.update_layout(title='Quantidade de Restaurantes por País', title_x=0.3, title_font=dict(size = 24)) # Ajustar a 
    # a posição do title e a fonte. 
    
    fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
    fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
    fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')

    
    st.plotly_chart(fig, use_container_width = True)
    
    
with st.container(height = None, border = True):
    #st.markdown('Quantidade de cidades Registrados por País')
    
    cols = ['City', 'Country_id']
    # Selecao de linhas
    df_aux = df.loc[:,cols].groupby('Country_id').nunique().reset_index().sort_values('City', ascending = False)
    # desenhar o gráfio de linhas
    fig = px.bar(df_aux, x='Country_id', y='City', text = 'City', color='City', labels={'Country_id': 'Países', 'City': 'Quantidade de Cidades'})
    fig.update_layout(title='Quantidade de Cidades Registradas por País', title_x=0.3, title_font=dict(size = 24)) # Ajustar a 
    # a posição do title e a fonte. 
    
    fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
    fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

    st.plotly_chart(fig, use_container_width = True)
    
    
    
    
    
with st.container(height = None, border = True):
    col0, col1 = st.columns(2)

    with col0: 
        #st.markdown('Média de Avaliações feitas por País')
        cols = ['Votes', 'Country_id']
        # Selecao de linhas
        df_aux = df.loc[:,cols].groupby('Country_id').mean().reset_index().sort_values('Votes', ascending = False)
        df_aux['Votes'] = df_aux['Votes'].round(2)
        # desenhar o gráfio de linhas
        fig = px.bar(df_aux, x='Country_id', y='Votes', text = 'Votes', color='Votes', labels={'Country_id': 'Países', 'Votes': 'Médias  de Avaliações'})
        fig.update_layout(title='Média de avaliações por País', title_x=0.3, title_font=dict(size = 24)) # Ajustar a 
        # a posição do title e a fonte. 

        fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
        fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

        st.plotly_chart(fig, use_container_width = True)


        
        
    with col1: 
        #st.markdown('Média de Preço de um prato para duas pessoas por País')
        
        cols = ['Average Cost for two', 'Country_id']
        # Selecao de linhas
        df_aux = df.loc[:,cols].groupby('Country_id').mean().reset_index().sort_values('Average Cost for two', ascending = False)
        # desenhar o gráfio de linhas
        fig = px.bar(df_aux, x='Country_id', y='Average Cost for two', text = 'Average Cost for two', color='Average Cost for two', labels={'Country_id': 'Países', 'Average Cost for two': 'Preço de prato para duas Pessoas'})
        fig.update_layout(title='Preço médio prato para dois por País', title_x=0.2, title_font=dict(size = 24)) # Ajustar a 
        # a posição do title e a fonte. 

        fig.update_xaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário
        fig.update_yaxes(title_font=dict(size=20))  # Ajuste o tamanho da fonte conforme necessário

        st.plotly_chart(fig, use_container_width = True)
        
#========================================
#              \ESTRUTURA
#========================================