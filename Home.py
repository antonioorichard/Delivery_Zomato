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
#=================
#        Library
#=================
#____________________________________________________________
#             Sidebar Home



st.set_page_config(page_title = 'Home', page_icon = '🏡', layout = 'wide' )


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
st.sidebar.markdown(' ### Por padrão estão todos selecionados!')

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

#Options

st.sidebar.markdown('## Dados Tratados')
st.sidebar.download_button("Donwload", data=df.to_csv(index=False), mime="text/csv")

#linhas_selecionadas2 =  df['Country_id'].isin( traffic_options1)
#df = df.loc[linhas_selecionadas2,:]
#st.dataframe(df1)
# FILTRO SLIDER


#____________---\FILTER---_______
    
    
    
    
    
st.write(" # Zomato Company - Dashboard")
st.write(" ## O Melhor lugar para encontrar seu mais novo restaurante favorito! ")
st.write(" ### Temos as seguintes informações dendro da nossa plataforma")



#========================================
#              \Barra Laterals
#========================================





with st.container(height = None, border = True):
    col0, col1, col2, col3, col4 = st.columns(5)
    with col0:
        #st.write('Restaurantes Cadastrados ')
        qru = df['Restaurant ID'].nunique()         # Quantidade de Restaurantes Únicos
        col0.metric('Restaurantes Cadastrados', qru)
        
        with st.expander("more"):
             st.write(" Total de Restaurantes Cadastrados.  ")

    with col1:
        #st.write('Países Cadastrados ')
        qpu = df['Country Code'].nunique()
        col1.metric('Países Cadastrados ', qpu)     # Quantidade de Países Únicos
        
        with st.expander("more"):
             st.write(" Total de Países Cadastrados.  ")

        
    with col2:
        #st.write('Cidades Cadastrados ')
        qcu = df['City'].nunique()
        col2.metric('Cidades Cadastradas ', qcu)     # Quantidade Cidades Únicas
   
        with st.expander("more"):
             st.write(" Total de cidades Cadastradas.  ")

    with col3:
        #st.write('Avaliações dos clientes')
        qac = df['Aggregate rating'].count()
        col3.metric('Total de Avaliações', qac)      # Quantidade Avaliações dos Clientes
   
        with st.expander("more"):
             st.write(" Quantidade total de Avaliações dos Clientes.  ")

    
    with col4:
        #st.write('Variedade de Culinárias')
        tvc = df['Cuisines'].nunique()
        col4.metric('Variedade Culinária', tvc)      # Total de variedade Culinárias    
        
        with st.expander("more"):
             st.write(" Total de Variedades Culinária.")


    
with st.container():
    st.markdown('# Country Maps ')
    df_aux= df.loc[:, ['City',  'Longitude', 'Latitude', 'Restaurant Name', 'Rating color']].groupby(['City', 'Restaurant Name', 'Rating color']).median().reset_index()  
    import folium 
    from folium.plugins import MarkerCluster
       
    map = folium.Map()
    marker_cluster=MarkerCluster().add_to(map)
    
    for index, location_info in df_aux.iterrows():
        latitude, longitude = location_info['Latitude'], location_info['Longitude']
        rating_color = location_info['Rating color']
        
        #Use a função de color_name para obter o nonme da cor
        color = color_name(rating_color)
        
        #Adicione um marcador com o ícone personalizado e a cor
        
        folium.Marker(
        
            location = [latitude, longitude],                      # Coordenadas
            popup    = location_info[['City', 'Restaurant Name']], # ADD um texto
            icon = folium.Icon(icon = 'cutlery', color = color)
                      ).add_to(marker_cluster)
    folium_static(map, width=1024, height=600)
        
    

    
    
    
        
st.markdown(

        """
        
        ### Ask for Help
        
        - Time de Data Science no Discord
            - @antonio_richard

        """)
#========================================
#\Barra Lateral
#========================================