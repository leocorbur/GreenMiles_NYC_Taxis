import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit.components.v1 import html
from streamlit_lottie import st_lottie

# Función para cargar la animación Lottie desde un archivo local.
def load_lottieurl(file_path: str):
    try:
        with open(file_path, 'r') as file:
            lottie_data = json.load(file)
        return lottie_data
    except Exception as e:
        st.error(f"Error al cargar la animación Lottie: {str(e)}")
        return None

# Ruta archivo JSON Lottie para la animación de carga
lottie_file_path = 'coding.json'
lottie_json = load_lottieurl(lottie_file_path)

# Ruta archivo JSON Lottie para la animación de Github
Github_file_path = 'github.json'
Github_file_path_json = load_lottieurl(Github_file_path)

# Navegación en la barra lateral
with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Home', 'Analytics', 'Demand Predictor', 'Fleet Optimization', 'Developers','Support','Documentation'],
        icons=['house', 'bar-chart-line-fill', 'robot','car-front-fill','people-fill','envelope','github'],
        menu_icon='cast',
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#AEB2AF"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#05AD26"},
        },
    )

    st.image("green.png", use_column_width=False, output_format="PNG", width=300)

#  Modo oscuro____________
st.markdown("""
    <style>
        body {
            color: white;
            background-color: #FAFCFA;
        }
        .sidebar .sidebar-content {
            background-color: #FAFCFA;
        }
        .Widget>label {
            color: white;
        }
        .st-bb {
            background-color: #FAFCFA;
        }
    </style>
""", unsafe_allow_html=True)

# Contenido de las pestañas______________
if selected == 'Home':
    st.markdown("<h1 style='color: #05AD26 ; text-align: center; font-size: 36px;'>GREEN MILES TAXIS</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 26px;'>MILES THAT CONTRIBUTE TO THE ENVIRONMENT</h1>", unsafe_allow_html=True)

    if lottie_json:
        st_lottie(lottie_json, speed=1, width=0, height=0, key="home_lottie")
    else:
        st.error("Error cargando la animación Lottie en la pestaña Home")

elif selected == 'Analytics': # Power BI con la analitica Bruno y Rafael_______________
    st.markdown("<h1 style='color: #05AD26 ; text-align: center; font-size: 36px;'>ANALYTICS</h1>", unsafe_allow_html=True)
    st.markdown('<iframe title="Report Section" width="600" height="636" src="https://app.powerbi.com/view?r=eyJrIjoiOTFhMDRlNzEtYzNhYy00YzZiLWFhYmYtM2FjZmUxZWZlMTg1IiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

elif selected == 'Demand Predictor':# Modelo Predicción de demanda Sebastian______________
    st.markdown("<h1 style='color: #05AD26 ; text-align: center; font-size: 36px;'>DEMAND PREDICTOR</h1>", unsafe_allow_html=True)
    enlace_streamlit = "https://prediccion-demanda.streamlit.app/"
    st.markdown(f'<iframe src="{enlace_streamlit}?embed=true" height="500" style="width: 100%; border: none;"></iframe>', unsafe_allow_html=True)

elif selected == 'Fleet Optimization':# Modelo Optimización de la flota Roberto______________
    st.markdown("<h1 style='color: #05AD26  ; text-align: center; font-size: 36px;'>FLEET OPTIMIZATION</h1>", unsafe_allow_html=True)
    enlace_streamlit = "https://optimizacionflota1212314564.streamlit.app/"
    st.markdown(f'<iframe src="{enlace_streamlit}?embed=true" height="500" style="width: 100%; border: none;"></iframe>', unsafe_allow_html=True)
elif selected == 'Developers':
    st.markdown("<h1 style='color: #05AD26  ; text-align: center; font-size: 36px;'>DEVELOPERS</h1>", unsafe_allow_html=True)
    st.image('equipo.png', caption='Creative-Data Technology-2024', use_column_width=True)

elif selected == 'Support': # Formulario de soporte___________
    st.markdown("<h1 style='color: #05AD26  ; text-align: center; font-size: 36px;'>SUPPORT</h1>", unsafe_allow_html=True)
    st.title("Contact Form")
    st.write("Please fill out the following form:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit_button = st.markdown(
        """
        <style>
            .custom-button {
                background-color: #05AD26 ;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                text-align: center;
            }
        </style>
        <div class="custom-button" onclick="submitForm()">Submit</div>
        <script>
            function submitForm() {
                alert("Form submitted successfully!");
            }
        </script>
        """,
        unsafe_allow_html=True
    )

elif selected == 'Documentation':
    st.markdown("<h1 style='color: #05AD26  ; text-align: center; font-size: 36px;'>DOCUMENTATION</h1>", unsafe_allow_html=True)
    if Github_file_path_json:
        st_lottie(Github_file_path_json, speed=1, width=None, height=350, reverse=False, loop=True, key="home_lottie")
    else:
        st.error("Error cargando la animación Lottie en la pestaña Home")

    st.markdown(
        """
        <div class="container-with-bg">
            <p style="text-align: center; margin-top: 20px;">
                <a href="https://github.com/leocorbur/GreenMiles_NYC_Taxis" 
                   style="text-decoration: none; color: #F9FCF9  ;">
                   <button style="padding: 10px 20px; background-color: #05AD26  ; color: #F9FCF9  ; border: none; border-radius: 5px; cursor: pointer;">
                       GO TO GITHUB REPOSITORY
                   </button>
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #05AD26 ;
            color: #FFFFFF;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="footer">
        Developed by DATAPT-04/Group 05 - SOY HENRY - 2023
    </div>
    """,
    unsafe_allow_html=True
)
