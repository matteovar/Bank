from .main_page import show_main
from .page3 import campanha
from .page4 import advanced
from .page_2 import tendencias

pages = {
    "Visão Geral": show_main,
    "Tendencias": tendencias,
    "Campanhas": campanha,
    "Insights Avançados": advanced,
}
