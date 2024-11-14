from django.urls import path
from . import views


#ruta_para_macros = 
# URL Pattern =>  Parte de la URL | funcion     | Darle nombre a la url
                #    /macros      | Referencia  | Para ubicar a la url con codigo

urlpatterns = [
    path("", views.v_index, name="v_index"), #/
    path("macros", views.v_macro, name="macros" ),
    path("powerbi", views.v_powerbi, name="powerbi"),
    path("analitica", views.v_analitica, name="analitica"),
    path("reporte_xls", views.v_reporte_xls, name="v_reporte_xls")
]