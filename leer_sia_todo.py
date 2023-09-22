import tabula
import PyPDF2
import math
from datetime import datetime
import datetime as dt
import os


# Convertir el string "15/06/2023" en un objeto de fecha
def fecha_p(f_pago):

    if isinstance(f_pago, float):
    # Si ya es un float, déjalo como es
        return 0.0
    elif f_pago != 0.0: 
        return datetime.strptime(f_pago, "%d/%m/%Y")
    else:
        return ""

# Convertir el string "06/2022" en un objeto de fecha asumiendo el día 1
def fecha_m(f_mes):
    return datetime.strptime("01/" + f_mes, "%d/%m/%Y")

def convert(value):
    if isinstance(value, str):
        if value == 'nan':
            return 0.0
        else:
            try:
                return round(float(value.replace(',','').replace('*','')),2)
            except ValueError:
                # Si no se puede convertir a float, trata de manejarlo según tu lógica
                return 0.0
    elif math.isnan(value):
        # Trata NaN como 0.0 o según tu lógica
        return 0.0
    elif isinstance(value, float):
        # Si ya es un float, déjalo como está
        return round(value,2)
    else:
        # Si no es ninguno de los tipos anteriores, puedes manejarlo según tu lógica
        return 0.0  

def scan(sia):
    rec = []
    with open(sia, 'rb') as sia2:    
        pdf_reader = PyPDF2.PdfReader(sia2)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = sia  # Obtener el texto de la página
            # Pasar el texto de la página a tabula.read_pdf
            table = tabula.read_pdf(page_text, guess=True, area=(110, 0,780, 2500), pages=page_num+1, encoding='ISO-8859-1', lattice=True)[0]
            records = table.T
            #print(records)
            # for line in records:
            #     periodo = table[line].to_dict()
            #     dato ={'mes': periodo[0],'Empleados': "aa", 'Remuneracion':"bb"}
            #     rec.append(dato)
                            
            for index, row in records.iterrows():
                if index != 'CONCEPTOS / PERIODOS':
                    #OSPECON   #print(index,row)  # Iterar sobre las filas del DataFrame
                    dato = {'Mes': fecha_m(index.replace('-','/'))}  # El índice es el valor que deseas en 'mes'
                    dato['id']= index[-4:]+index[0:2]
                    if dato['id'][-2:] == '04' or dato['id'][-2:] == '06' or dato['id'][-2:] == '09' or dato['id'][-2:] == '11':
                        dato['Vencimiento'] = dato['Mes']+dt.timedelta(days=49)
                    elif dato['id'][-2:] == '02':
                        dato['Vencimiento'] = dato['Mes']+dt.timedelta(days=47)
                    else:
                        dato['Vencimiento'] = dato['Mes']+dt.timedelta(days=50)                       
                    dato['Empleados'] = int(convert(row[8]))
                    dato['Aporte'] = convert(row[2])
                    dato['Retencion'] = convert(row[5])
                    dato['Contr.Pagada'] = convert(row[4])
                    dato['Contribuciones'] = round(dato['Contr.Pagada']+dato['Retencion'],2)
                    dato['Rem4'] = convert(row[10])
                    dato['Rem8'] = convert(row[11])
                    dato['Rem5'] = convert(row[15])
                    dato['F.Pago'] = fecha_p(row[21])
                    dato['Pago'] = convert(row[22])
                    if dato['F.Pago'] == 0.0 :
                        dato['Inf_OS'] = 'Impago'
                    elif dato['F.Pago'] > dato['Vencimiento'] and dato['Pago']<=dato['Contribuciones']+dato['Aporte']:
                        dato['Inf_OS'] = 'Fuera de Termino'
                        dato['Rem_p_Calculo'] = round((dato['Contribuciones']+dato['Aporte'])/0.081,2)
                    else:
                        dato['Inf_OS'] = ""
                    #INSPECCION
                    dato['Inspeccion'] = convert(row[24])
                    #UOCRA
                    dato['Obr_Sindical'] = int(convert(row[42]))
                    dato['Rem_Sindical'] = convert(row[43])
                    dato['Tot_Sindical'] = convert(row[44])
                    dato['Obr_Seguro'] = int(convert(row[45]))
                    dato['Rem_Seguro'] = convert(row[46])
                    dato['Total_Seguro'] = convert(row[47])
                    dato['Fdo_Desempleo'] = convert(row[48])
                    dato['FICS'] = convert(row[49])
                    dato['Otros_Conceptos'] = convert(row[50])
                    dato['Obr_No_Afil'] = int(convert(row[51]))
                    dato['Rem_No_Afil'] = convert(row[52])
                    dato['Aporte_Solid'] = convert(row[53])
                    #PAGO UOCRA
                    dato['P_Fecha'] = fecha_p(row[55])
                    dato['P_C_Sind'] = convert(row[56])
                    dato['P_S_Vida'] = convert(row[57])
                    dato['P_FICS'] = convert(row[58])
                    dato['P_Otros'] = convert(row[59])
                    dato['P_A_Solid'] = convert(row[60])
                    dato['P_Total'] = convert(row[61])
                    if dato['P_Fecha'] == 0.0:
                        dato['Inf_UOCRA'] = 'Impago'                    
                    elif dato['P_Fecha'] > dato['Vencimiento']:    
                        dato['Inf_UOCRA'] = 'Fuera de Termino'
                    else:
                        dato['Inf_UOCRA']= ""
                    rec.append(dato)
    return rec

def leer_sia(path):
    siafull = []
    files = os.listdir(path)
    for file in files:
        if file.endswith('.pdf'):
            pdf_path = os.path.join(path, file)
            with open(pdf_path, 'rb') as hoja:
                pdf_reader = PyPDF2.PdfReader(hoja)
                page = pdf_reader.pages[0]
                text = page.extract_text() 
                
                # Dividir el texto en líneas y verificar la tercera línea
                lines = text.split('\n')
                for line in lines:
                    if "Fecha: Listado Integral de Empresas" in line:
                        extracted_data = scan(path+file)
                        if extracted_data:
                            # print(extracted_data)
                            siafull.append(extracted_data)
    if siafull == []:
        result = siafull
    else:
        result = siafull[0]
    return result 


