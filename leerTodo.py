import os
import PyPDF2
import re
from leer_sia_todo import fecha_p, fecha_m

def extract_data_from_pdf(pdf_path):
    data = {}  # Aquí almacenaremos los datos extraídos
    # Abre el archivo PDF
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Itera a través de las páginas del PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()  # Extrae el texto de la página
            #print(text)
            # Define patrones de búsqueda para encontrar datos específicos
            # Aquí necesitas conocer la estructura del PDF y los patrones de texto
            # para identificar los datos que deseas extraer.
            # Utiliza expresiones regulares u otros métodos para hacer coincidir el texto.
            pattern_empresa = re.compile(r'Suma de R em. 7: 0,00\n(.+)\d{6}')
            pattern_cuit = re.compile(r'S.U.S.S.C.U.I.T. (.+)')
            pattern_periodo = re.compile(r'(.+) Servicios Ev entuales: No')
            pattern_empleados = re.compile(r'Empleados en nómina: (.+)')
            pattern_rem4 = re.compile(r'Suma de R em. 4: (.+)')
            pattern_rem8 = re.compile(r'Suma de R em. 8: (.+)')
            pattern_rem5 = re.compile(r'Suma de R em. 5: (.+)')
            pattern_apSS = re.compile(r'a1 -Total de aportes (.+) a1 - Total de aportes')
            pattern_apOS = re.compile(r' a1 - Total de aportes (.+)')
            pattern_coSS = re.compile(r'b1 -Total de contribuciones (.+)  b2 - Excedentes de contribuciones')
            pattern_coOS = re.compile(r' b1 - Total de contribuciones (.+)')
            pattern_retPA = re.compile(r'Saldo r etenciones período anterior (.+) Monto base de cálculo 0,00')
            pattern_retPe = re.compile(r'Retenciones del período (.+) Contribuciones, Vales Alimentarios')
            pattern_retSS = re.compile(r'Retenciones apl icadas a S eguridad S ocial (.+)')
            pattern_retOS = re.compile(r'Retenciones apl icadas a Obr a Social (.+)V - RENATRE')
            pattern_art = re.compile(r'L.R.T. total a pagar (.+) S.C.V.O. a Pagar:')
            pattern_svo = re.compile(r'S.C.V.O. a Pagar: (.+)')

            #pattern_periodo = re.findall(r'\d{2}/\d{4}',text)
            # Define más patrones según tus necesidades
            
            # Busca los datos en el texto
            match_empresa = pattern_empresa.search(text)
            match_cuit = pattern_cuit.search(text)
            match_periodo = pattern_periodo.search(text)
            match_empleados = pattern_empleados.search(text)
            match_rem4 = pattern_rem4.search(text)
            match_rem8 = pattern_rem8.search(text)
            match_rem5 = pattern_rem5.search(text)
            match_apSS = pattern_apSS.search(text)
            match_apOS = pattern_apOS.search(text)
            match_coSS = pattern_coSS.search(text)
            match_coOS = pattern_coOS.search(text)
            match_retPA = pattern_retPA.search(text)
            match_retPe = pattern_retPe.search(text)
            match_retSS = pattern_retSS.search(text)
            match_retOS = pattern_retOS.search(text)
            match_art = pattern_art.search(text)
            match_svo = pattern_svo.search(text)
            # Encuentra más coincidencias según los patrones definidos
            
            # Almacena los datos en el diccionario si se encuentran coincidencias
            if match_empresa:
                data['empresa'] = match_empresa.group(1)
            if match_cuit:
                data['cuit'] = match_cuit.group(1)
            if match_periodo:
                data['periodo'] = fecha_m(match_periodo.group(1))
                data['id']= match_periodo.group(1)[-4:]+match_periodo.group(1)[0:2]
            if match_empleados:
                data['empleados'] = match_empleados.group(1)
            if match_rem4:
                data['rem4'] = float(match_rem4.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_rem8:
                data['rem8'] = float(match_rem8.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_rem5:
                data['rem5'] = float(match_rem5.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_apSS:
                data['apSS'] = float(match_apSS.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_apOS:
                data['apOS'] = float(match_apOS.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_coSS:
                data['coSS'] = float(match_apOS.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_coOS:
                data['coOS'] = float(match_coOS.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_retPA:
                data['retPA'] = float(match_retPA.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_retPe:
                data['retPe'] = float(match_retPe.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_retSS:
                data['retSS'] = float(match_retSS.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_retOS:
                data['retOS'] = float(match_retOS.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_art:
                data['art'] = float(match_art.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            if match_svo:
                data['svo'] = float(match_svo.group(1).replace(".", "").replace(",", ".").replace(" ",""))
            
            # Almacena más datos en el diccionario
            #data['text'] = text
            # Repite el proceso para otros datos que necesites extraer
    return data

#path = "/Users/Damian/OneDrive/Escritorio/inspecciones"

def leer_carpeta(path):
    F05 = []
    files = os.listdir(path)
    #print(files)
    for file in files:
        if file.endswith('.pdf'):
            #print(file)
            extracted_data = extract_data_from_pdf(path+file)
            if extracted_data:
                F05.append(extracted_data)
    return F05            
# Ruta al archivo PDF que deseas procesar
#carpeta = leer_carpeta(ubicac)
#sorted = carpeta['periodo'].sort()

#for hoja in carpeta:
 #   print(hoja)
