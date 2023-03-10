import streamlit as st
from streamlit_option_menu import option_menu
import requests

# SET PAGE
st.set_page_config(
    page_title='EnergyAC', 
    page_icon=':bulb:', 
    layout='wide')

# PARAMS
# PARAMS.PY
provincias = ['', 'Buenos Aires', 'CABA', 'Catamarca', 'Chaco', 'Chubut', 'Cordoba', 'Corrientes', 'Entre Rios', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquen', 'Rio Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucuman']

buenosaires_locs = ['Azul Aero', 'Bahia Blanca Aero', 'Benito Juarez Aero', 'Bolivar Aero', 'Campo de Mayo Aero', 'Cnel. Pringles Aero', 'Cnel. Suarez Aero', 'Dolores Aero', 'El Palomar Aero', 'Ezeiza Aero', 'Junin Aero', 'La Plata Aero', 'Las Flores Aero', 'Mar del Plata Aero', 'Mariano Moreno Aero', 'Merlo Aero', 'Moron Aero', 'Nueve de Julio', 'Olavarria Aero', ' Pehuajo Aero', 'Pigue Aero', 'Punta Indio B.A.', 'San Fernando', 'Santa Tereista Aero', 'Tandil Aero', 'Trenque Lauquen Aero', 'Tres Arroyos', 'Villa Gessel Aero']

caba_locs = ['Aeroparque Aero' ,'Buenos Aires'] 

catamarca_locs = ['Catamarca Aero', 'Tinogasta']

chaco_locs = ['Pcia. Roque Saenz Peña Aero', 'Resistencia Aero']

chubut_locs = ['Comodoro Rivadavia Aero', 'Esquel Aero', 'Paso de Indios', 'Puerto Madryn Aero', 'Trelew Aero']

cordoba_locs = ['Cordoba Aero', 'Cordoba Observatorio', 'Esclavacion Militar Aero', 'Laboulaye Aero', 'Marcos Juarez Aero', 'Pilar Obs.', 'Rio Cuarto Aero', 'Villa Dolores Aero', 'Villa Maria Del Rio Seco']

corrientes_locs = ['Corrientes Aero', 'Ituzaingo', 'Mercedes Aero', 'Monte Caseros Aero', 'Paso de los Libres Aero']

entrerios_loc = ['Concordia Aero', 'Gualeguaychu Aero', 'Parana Aero']

formosa_locs = ['Formosa Aero', 'Las Lomitas Aero']

jujuy_locs = ['Juju Aero', 'Jujuy UN', 'La Quiaca Obs.']

lapampa_locs = ['General Pico Aero', 'Santa Rosa Aero', 'Victorica Aero']

larioja_locs = ['Chamical Aero', 'Chepes', 'Chilecito Aero', 'La Rioja Aero']

mendoza_locs = ['Malargue Aero', 'Mendoza Aero', 'Mendoza Observatorio', 'San Carlos', 'San Martin', 'San Rafael Aero', 'Uspallata']

misiones_locs = ['Bernardo de Irigoyen Aero', 'Iguazu Aero', 'Obera Aero', 'Posadas Aero']

neuquen_locs = ['Chapelco Aero', 'Neuquen Aero']

rionegro_locs = ['Bariloche Aero', 'Cipolleti', 'El Bolson Aero', 'Maquinchao', 'Rio Colorado', 'San Antonio Oeste Aero', 'Viedma Aero']

salta_locs = ['Metan', 'Oran Aero', 'Rivadavia', 'Salta Aero', 'Tartagal Aero']

sanjuan_locs = ['Jachal', 'San Juan Aero']

sanluis_locs = ['San Luis Aero', 'Santa Rosa de Conlara Aero', 'Villa Reynolds Aero']

santacruz_locs = ['El Cafayate Aero', 'Gobernador Gregores Aero', 'Perito Moreno Aero', 'Puerto Deseado Aero', 'Rio Gallegos Aero', 'San Julian Aero', 'Santa Cruz Aero']

santafe_locs = ['Ceres Aero', 'El Trebol Aero', 'Rafaela Aero', 'Reconquista Aero', 'Rosario Aero', 'Sauce Viejo Aero', 'Sunchales Aero', 'Venado Tuerto']

santiagodelestero_locs = ['Santiago del Estero Aero', 'Termas de Rio Hondo Aero']

tierradelfuego_locs = ['Rio Grande BA', 'Ushuaia Aero']

tucuman_locs = ['Tucuman Aero']



# HEADER



# MENU UBICACION

info = {
    'Buenos Aires': buenosaires_locs,
    'CABA': caba_locs,
    'Catamarca': catamarca_locs,
    'Chaco': chaco_locs,
    'Chubut': chubut_locs,
    'Cordoba': cordoba_locs,
    'Corrientes': corrientes_locs,
    'Entre Rios': entrerios_loc,
    'Formosa': formosa_locs,
    'Jujuy': jujuy_locs,
    'La Pampa': lapampa_locs,
    'La Rioja': larioja_locs,
    'Mendoza': mendoza_locs,
    'Misiones': misiones_locs,
    'Neuquen': neuquen_locs,
    'Rio Negro': rionegro_locs,
    'Salta': salta_locs,
    'San Juan': sanjuan_locs,
    'San Luis': sanluis_locs,
    'Santa Cruz': santacruz_locs,
    'Santa Fe': santafe_locs,
    'Santiago del Estero': santiagodelestero_locs,
    'Tierra del Fuego': tierradelfuego_locs,
    'Tucuman': tucuman_locs    
}




with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Home','Upload your photo', 'Upload manually'],
    )
if selected == 'Home':
    with st.container():
        st.subheader('Hi, we are EnergyAC :bulb:')
        st.title('Three datascientist from Argentina')
        st.write('This application allows you to predict the power consumption of an air conditioner in Argentina.')
        
if selected == 'Upload your photo':
    # adding "select" as the first and default choice
    ciudad = st.selectbox('Selecciona tu ciudad.', options=['select']+list(info.keys()))
    # display selectbox 2 if manufacturer is not "select"
    if ciudad != 'select':
        localidad = st.selectbox('Selecciona tu localidad', options=info[ciudad])
        
    imagen = st.file_uploader(label='Upload your photo here')

    
    if st.button('Submit'):
        st.write('You selected ' + ciudad + ', ' + localidad)
        params = dict(
        ciudad_elegida= ciudad,
        localidad_elegida=localidad)
        
        energyac_api_url = ' http://127.0.0.1:8000'
        response = requests.get(energyac_api_url, params=params)  
        prediction = response.json()
        pred = prediction
        #return('Your prediction is')
        
        
        
if selected == 'Upload manually':
    # adding "select" as the first and default choice
    ciudad = st.selectbox('Selecciona tu ciudad.', options=['select']+list(info.keys()))
    # display selectbox 2 if manufacturer is not "select"
    if ciudad != 'select':
        localidad = st.selectbox('Selecciona tu localidad', options=info[ciudad])
        
    capacidad_kw = st.number_input('AC capacity (KW)')
    indice_capacidad_energetica = st.number_input('Energy efficiency index')
    
    if st.button('Submit'):        
        params = dict(
        ciudad_elegida= ciudad,
        localidad_elegida=localidad,
        cap_kw = capacidad_kw,
        indice_cap_energetica = indice_capacidad_energetica)
        
        energyac_api_url = ' http://127.0.0.1:8000'
        response = requests.get(energyac_api_url, params=params)  
        prediction = response.json()
        pred = prediction
        #return('Your prediction is', pred)
    
    