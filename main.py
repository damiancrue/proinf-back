from fastapi import FastAPI, File, UploadFile, Form
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import shutil
from typing import List

app = FastAPI()

# Configura CORS para permitir solicitudes desde http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

insp_desde= '202201'
insp_hasta= '202308'

f931 = [
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 1, 1, 0, 0), 'id': '202301', 'empleados': '15', 'rem4': 2242310.77, 'rem8': 2244165.72, 'rem5': 2242310.77, 'apSS': 302338.92, 'apOS': 53353.92, 'coSS': 53353.92, 'coOS': 106802.46, 'retPA': 0.0, 'retPe': 110869.28, 'retSS': 90334.52, 'retOS': 20534.76, 'art': 71416.47, 'svo': 558.15},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 2, 1, 0, 0), 'id': '202302', 'empleados': '14', 'rem4': 2166036.46, 'rem8': 2166036.46, 'rem5': 2166036.46, 'apSS': 291317.3, 'apOS': 51408.91, 'coSS': 51408.91, 'coOS': 102817.87, 'retPA': 0.0, 'retPe': 103911.11, 'retSS': 84453.18, 'retOS': 19457.93, 'art': 68982.72, 'svo': 520.94},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 3, 1, 0, 0), 'id': '202303', 'empleados': '14', 'rem4': 2020203.74, 'rem8': 2020203.74, 'rem5': 2020203.74, 'apSS': 270244.47, 'apOS': 47690.19, 'coSS': 47690.19, 'coOS': 95380.4, 'retPA': 0.0, 'retPe': 86669.51, 'retSS': 70343.95, 'retOS': 16325.56, 'art': 64618.23, 'svo': 1097.04},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 4, 1, 0, 0), 'id': '202304', 'empleados': '12', 'rem4': 1687050.77, 'rem8': 1687050.77, 'rem5': 1687050.77, 'apSS': 243778.81, 'apOS': 43019.78, 'coSS': 43019.78, 'coOS': 86039.59, 'retPA': 0.0, 'retPe': 34214.04, 'retSS': 27729.49, 'retOS': 6484.55, 'art': 54227.75, 'svo': 940.32},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 5, 1, 0, 0), 'id': '202305', 'empleados': '10', 'rem4': 1913153.4, 'rem8': 1913153.4, 'rem5': 1913153.4, 'apSS': 276450.67, 'apOS': 48785.43, 'coOS': 97570.8, 'retPA': 0.0, 'retPe': 226148.96, 
'retSS': 183534.03, 'retOS': 42614.93, 'art': 60922.49, 'svo': 783.6},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 6, 1, 0, 0), 'id': '202206', 'empleados': '19', 'rem4': 3074481.11, 'rem8': 3074481.11, 'rem5': 3074481.11, 'apSS': 411750.0, 'apOS': 72661.8, 'coSS': 72661.8, 'coOS': 145323.52, 'retPA': 0.0, 
'retPe': 150946.77, 'retSS': 122943.84, 'retOS': 28002.93, 'art': 96758.12, 'svo': 632.57},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 6, 1, 0, 0), 'id': '202306', 'empleados': '9', 'rem4': 2342576.87, 'rem8': 2342576.87, 'rem5': 2342576.87, 'apSS': 338502.34, 'apOS': 59735.71, 'coSS': 59735.71, 'coOS': 119471.42, 'retPA': 0.0, 'retPe': 114744.08, 'retSS': 93198.94, 'retOS': 21545.14, 'art': 74040.85, 'svo': 705.24},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 7, 1, 0, 0), 'id': '202207', 'empleados': '17', 'rem4': 1183291.4, 'rem8': 1183291.4, 'rem5': 1183291.4, 'apSS': 149310.59, 'apOS': 26348.93, 'coOS': 52697.86, 'retPA': 0.0, 'retPe': 431674.37, 'retSS': 227577.28, 'retOS': 52697.86, 'art': 38605.72, 'svo': 595.36},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2023, 7, 1, 0, 0), 'id': '202307', 'empleados': '6', 'rem4': 682959.6, 'rem8': 682959.6, 'rem5': 682959.6, 'apSS': 98687.67, 'apOS': 17415.48, 'coOS': 34830.94, 'retPA': 0.0, 'retPe': 0.0, 'retSS': 0.0, 'retOS': 0.0, 'art': 22566.56, 'svo': 470.16},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 8, 1, 0, 0), 'id': '202208', 'empleados': '18', 'rem4': 1688756.67, 'rem8': 1688756.67, 'rem5': 1688756.67, 'apSS': 222350.33, 'apOS': 39238.3, 'coSS': 39238.3, 'coOS': 78476.61, 'retPA': 151399.23, 'retPe': 70795.22, 'retSS': 180883.88, 'retOS': 41310.57, 'art': 54213.95, 'svo': 669.78},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 9, 1, 0, 0), 'id': '202209', 'empleados': '18', 'rem4': 1895270.31, 'rem8': 1895269.71, 'rem5': 1895270.31, 'apSS': 252191.54, 'apOS': 44504.38, 'coOS': 89008.75, 'retPA': 0.0, 'retPe': 0.0, 'retSS': 0.0, 'retOS': 0.0, 'art': 60533.25, 'svo': 669.78},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 10, 1, 
0, 0), 'id': '202210', 'empleados': '17', 'rem4': 1990663.55, 'rem8': 1990662.72, 'rem5': 1990663.55, 'apSS': 265975.89, 'apOS': 46936.93, 'coOS': 93873.82, 'retPA': 0.0, 'retPe': 79986.73, 'retSS': 65191.42, 'retOS': 14795.31, 'art': 63311.28, 'svo': 632.57},
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 11, 1, 
0, 0), 'id': '202211', 'empleados': '16', 'rem4': 2088412.73, 'rem8': 2088411.82, 'rem5': 2088412.73, 'apSS': 280100.65, 'apOS': 49429.52, 'coSS': 49429.52, 'coOS': 98859.01, 'retPA': 0.0, 'retPe': 74786.44, 'retSS': 61018.23, 'retOS': 13768.21, 'art': 66161.4, 'svo': 595.36},   
{'empresa': 'ARVEN SRL ', 'cuit': '30-70930290-2', 'periodo': datetime(2022, 12, 1, 
0, 0), 'id': '202212', 'empleados': '14', 'rem4': 2747690.27, 'rem8': 2747690.27, 'rem5': 2747690.27, 'apSS': 375366.24, 'apOS': 66241.11, 'coSS': 66241.11, 'coOS': 132482.22, 'retPA': 0.0, 'retPe': 43447.27, 'retSS': 35412.76, 'retOS': 8034.51, 'art': 86501.32, 'svo': 520.94}  
]

sia =[{'Mes': datetime(2022, 1, 1, 0, 0), 'id': '202201', 'Vencimiento': datetime(2022, 2, 19, 0, 0), 'Empleados': 18, 'Aporte': 37221.52, 'Retencion': 38958.91, 'Contr.Pagada': 35484.22, 'Contribuciones': 74443.13, 'Rem4': 1459666.75, 'Rem8': 1459666.75, 'Rem5': 1459666.75, 'F.Pago': datetime(2022, 5, 12, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1378575.93, 'Pago': 119672.95, 'Inspeccion': 0.0, 'Obr_Sindical': 20, 'Rem_Sindical': 1617362.93, 'Tot_Sindical': 40434.07, 'Obr_Seguro': 20, 'Rem_Seguro': 1617362.93, 'Total_Seguro': 19881.0, 'Fdo_Desempleo': 156216.53, 'FICS': 3124.33, 'Otros_Conceptos': 5300.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 2, 1, 0, 0), 'id': '202202', 'Vencimiento': datetime(2022, 3, 22, 0, 0), 'Empleados': 21, 'Aporte': 39062.48, 'Retencion': 22289.63, 'Contr.Pagada': 55835.31, 'Contribuciones': 78124.94, 'Rem4': 1531861.77, 'Rem8': 1531861.77, 'Rem5': 1531861.77, 'F.Pago': datetime(2022, 5, 12, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1446758.27, 'Pago': 124461.03, 'Inspeccion': 0.0, 'Obr_Sindical': 24, 'Rem_Sindical': 1745680.83, 'Tot_Sindical': 43642.02, 'Obr_Seguro': 24, 'Rem_Seguro': 1745680.83, 'Total_Seguro': 25024.32, 'Fdo_Desempleo': 171610.17, 'FICS': 3432.2, 'Otros_Conceptos': 6360.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 3, 1, 0, 0), 'id': '202203', 'Vencimiento': datetime(2022, 4, 19, 0, 0), 'Empleados': 23, 'Aporte': 50010.47, 'Retencion': 10994.93, 'Contr.Pagada': 89026.02, 'Contribuciones': 100020.95, 'Rem4': 1961195.18, 'Rem8': 1961195.18, 'Rem5': 1961195.18, 'F.Pago': datetime(2022, 5, 12, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1852239.75, 'Pago': 155375.98, 'Inspeccion': 0.0, 'Obr_Sindical': 27, 'Rem_Sindical': 2356444.68, 'Tot_Sindical': 58911.12, 'Obr_Seguro': 27, 'Rem_Seguro': 2356444.68, 'Total_Seguro': 29735.64, 'Fdo_Desempleo': 233770.79, 'FICS': 4675.42, 'Otros_Conceptos': 7155.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 4, 1, 0, 0), 'id': '202204', 'Vencimiento': datetime(2022, 5, 20, 0, 0), 'Empleados': 19, 'Aporte': 37235.11, 'Retencion': 21105.97, 'Contr.Pagada': 53364.59, 'Contribuciones': 74470.56, 'Rem4': 1460200.29, 'Rem8': 1460200.29, 'Rem5': 1460200.29, 'F.Pago': datetime(2022, 5, 12, 0, 0), 'Inf_OS': '', 'Pago': 112042.69, 'Inspeccion': 0.0, 'Obr_Sindical': 17, 'Rem_Sindical': 1531665.56, 'Tot_Sindical': 38291.64, 'Obr_Seguro': 17, 'Rem_Seguro': 1531665.56, 'Total_Seguro': 18722.44, 'Fdo_Desempleo': 149809.65, 'FICS': 2996.19, 'Otros_Conceptos': 4505.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 5, 1, 0, 0), 'id': '202205', 'Vencimiento': datetime(2022, 6, 19, 0, 0), 'Empleados': 15, 'Aporte': 44131.14, 'Retencion': 6985.22, 'Contr.Pagada': 81277.09, 'Contribuciones': 88262.31, 'Rem4': 1730632.86, 'Rem8': 1730632.86, 'Rem5': 1730632.86, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1634487.04, 'Pago': 141877.24, 'Inspeccion': 0.0, 'Obr_Sindical': 17, 'Rem_Sindical': 1908607.08, 'Tot_Sindical': 47715.18, 'Obr_Seguro': 17, 'Rem_Seguro': 1908607.08, 'Total_Seguro': 20594.82, 'Fdo_Desempleo': 185397.46, 'FICS': 3707.95, 'Otros_Conceptos': 4505.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 6, 1, 0, 0), 'id': '202206', 'Vencimiento': datetime(2022, 7, 20, 0, 0), 'Empleados': 14, 'Aporte': 57477.9, 'Retencion': 14914.8, 'Contr.Pagada': 100040.95, 'Contribuciones': 114955.75, 'Rem4': 2254034.41, 'Rem8': 2254034.41, 'Rem5': 2254034.41, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 2128810.49, 'Pago': 183591.26, 'Inspeccion': 0.0, 'Obr_Sindical': 9, 'Rem_Sindical': 1633276.25, 'Tot_Sindical': 40831.91, 'Obr_Seguro': 9, 'Rem_Seguro': 1633276.25, 'Total_Seguro': 11894.22, 'Fdo_Desempleo': 143548.25, 'FICS': 2870.97, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 7, 1, 0, 0), 'id': '202207', 'Vencimiento': datetime(2022, 8, 19, 0, 0), 'Empleados': 13, 'Aporte': 20526.27, 'Retencion': 41052.53, 'Contr.Pagada': 0.0, 'Contribuciones': 41052.53, 'Rem4': 804951.7, 'Rem8': 804951.7, 'Rem5': 804951.7, 'F.Pago': datetime(2022, 11, 8, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 760232.1, 'Pago': 65244.55, 'Inspeccion': 0.0, 'Obr_Sindical': 9, 'Rem_Sindical': 894056.0, 'Tot_Sindical': 22351.4, 'Obr_Seguro': 9, 'Rem_Seguro': 894056.0, 'Total_Seguro': 11894.22, 'Fdo_Desempleo': 81986.94, 'FICS': 1639.74, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 8, 1, 0, 0), 'id': '202208', 'Vencimiento': datetime(2022, 9, 19, 0, 0), 'Empleados': 15, 'Aporte': 33023.55, 'Retencion': 32910.85, 'Contr.Pagada': 33136.26, 'Contribuciones': 66047.11, 'Rem4': 1295040.92, 'Rem8': 1295040.92, 'Rem5': 1295040.92, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1223094.57, 'Pago': 107114.94, 'Inspeccion': 0.0, 'Obr_Sindical': 14, 'Rem_Sindical': 1287441.9, 'Tot_Sindical': 32186.05, 'Obr_Seguro': 14, 'Rem_Seguro': 1287441.9, 'Total_Seguro': 19735.8, 'Fdo_Desempleo': 126510.24, 'FICS': 2530.2, 'Otros_Conceptos': 6020.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 9, 1, 0, 0), 'id': '202209', 'Vencimiento': datetime(2022, 10, 20, 0, 0), 'Empleados': 15, 'Aporte': 37618.26, 'Retencion': 0.0, 'Contr.Pagada': 75236.53, 'Contribuciones': 75236.53, 'Rem4': 1475226.6, 'Rem8': 1475226.0, 'Rem5': 1475226.6, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1393269.01, 'Pago': 119349.46, 'Inspeccion': 0.0, 'Obr_Sindical': 13, 'Rem_Sindical': 1552859.0, 'Tot_Sindical': 38821.48, 'Obr_Seguro': 13, 'Rem_Seguro': 1552859.0, 'Total_Seguro': 20187.18, 'Fdo_Desempleo': 156065.7, 'FICS': 3121.31, 'Otros_Conceptos': 5590.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 10, 1, 0, 0), 'id': '202210', 'Vencimiento': datetime(2022, 11, 19, 0, 0), 'Empleados': 14, 'Aporte': 39600.93, 'Retencion': 13195.58, 'Contr.Pagada': 66006.17, 'Contribuciones': 79201.75, 'Rem4': 1552977.25, 'Rem8': 1552976.42, 'Rem5': 1552977.25, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1466699.75, 'Pago': 132207.49, 'Inspeccion': 0.0, 'Obr_Sindical': 11, 'Rem_Sindical': 1464077.53, 'Tot_Sindical': 36601.94, 'Obr_Seguro': 11, 'Rem_Seguro': 1464077.53, 'Total_Seguro': 18656.44, 'Fdo_Desempleo': 142380.49, 'FICS': 2847.61, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 11, 1, 0, 0), 'id': '202211', 'Vencimiento': datetime(2022, 12, 20, 0, 0), 'Empleados': 11, 'Aporte': 38559.45, 'Retencion': 10740.37, 'Contr.Pagada': 66378.51, 'Contribuciones': 77118.88, 'Rem4': 1512135.58, 'Rem8': 1512134.67, 'Rem5': 1512135.58, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1428127.53, 'Pago': 146067.28, 'Inspeccion': 0.0, 'Obr_Sindical': 11, 'Rem_Sindical': 1652925.71, 'Tot_Sindical': 41323.14, 'Obr_Seguro': 11, 'Rem_Seguro': 1652925.71, 'Total_Seguro': 20110.2, 'Fdo_Desempleo': 158546.8, 'FICS': 3170.94, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2022, 12, 1, 0, 0), 'id': '202212', 'Vencimiento': datetime(2023, 1, 19, 0, 0), 'Empleados': 9, 'Aporte': 47569.44, 'Retencion': 5769.72, 'Contr.Pagada': 89369.08, 'Contribuciones': 95138.8, 'Rem4': 1865467.64, 'Rem8': 1865467.64, 'Rem5': 1865467.64, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1761830.12, 'Pago': 153229.22, 'Inspeccion': 0.0, 'Obr_Sindical': 11, 'Rem_Sindical': 2349080.54, 'Tot_Sindical': 58727.01, 'Obr_Seguro': 11, 'Rem_Seguro': 2349080.54, 'Total_Seguro': 21079.3, 'Fdo_Desempleo': 227453.45, 'FICS': 4549.07, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2023, 1, 1, 0, 0), 'id': '202301', 'Vencimiento': datetime(2023, 2, 19, 0, 0), 'Empleados': 11, 'Aporte': 43222.95, 'Retencion': 16638.96, 'Contr.Pagada': 69901.5, 'Contribuciones': 86540.46, 'Rem4': 1695017.92, 'Rem8': 1696872.87, 'Rem5': 1695017.92, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1602017.41, 'Pago': 137786.2, 'Inspeccion': 0.0, 'Obr_Sindical': 11, 'Rem_Sindical': 1919800.12, 'Tot_Sindical': 47995.0, 'Obr_Seguro': 11, 'Rem_Seguro': 1919800.12, 'Total_Seguro': 22654.28, 'Fdo_Desempleo': 186694.46, 'FICS': 3733.89, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': datetime(2023, 3, 21, 0, 0), 'P_C_Sind': 47995.0, 'P_S_Vida': 22654.28, 'P_FICS': 47995.0, 'P_Otros': 4730.0, 'P_A_Solid': 0.0, 'P_Total': 79113.17, 'Inf_UOCRA': 'Fuera de Termino'}, {'Mes': datetime(2023, 2, 1, 0, 0), 'id': '202302', 'Vencimiento': datetime(2023, 3, 22, 0, 0), 'Empleados': 10, 'Aporte': 41684.08, 'Retencion': 15777.14, 'Contr.Pagada': 67591.06, 'Contribuciones': 83368.2, 'Rem4': 1634670.66, 'Rem8': 1634670.66, 'Rem5': 1634670.66, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1543855.31, 'Pago': 130864.63, 'Inspeccion': 0.0, 'Obr_Sindical': 11, 'Rem_Sindical': 1842205.46, 'Tot_Sindical': 46055.14, 'Obr_Seguro': 11, 'Rem_Seguro': 1842205.46, 'Total_Seguro': 24229.04, 'Fdo_Desempleo': 180957.81, 'FICS': 3619.16, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': datetime(2023, 4, 18, 0, 0), 'P_C_Sind': 46055.14, 'P_S_Vida': 24229.04, 'P_FICS': 46055.14, 'P_Otros': 4730.0, 'P_A_Solid': 0.0, 'P_Total': 78633.34, 'Inf_UOCRA': 'Fuera de Termino'}, {'Mes': datetime(2023, 3, 1, 0, 0), 'id': '202303', 'Vencimiento': datetime(2023, 4, 19, 0, 0), 'Empleados': 10, 'Aporte': 41661.07, 'Retencion': 14261.62, 'Contr.Pagada': 69060.52, 'Contribuciones': 83322.14, 'Rem4': 1633767.64, 'Rem8': 1633767.64, 'Rem5': 1633767.64, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1543002.59, 'Pago': 130436.24, 'Inspeccion': 0.0, 'Obr_Sindical': 10, 'Rem_Sindical': 1685887.14, 'Tot_Sindical': 42147.18, 'Obr_Seguro': 10, 'Rem_Seguro': 1685887.14, 'Total_Seguro': 22577.2, 'Fdo_Desempleo': 166114.12, 'FICS': 3322.28, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': datetime(2023, 5, 31, 0, 0), 'P_C_Sind': 42147.18, 'P_S_Vida': 22577.2, 'P_FICS': 42147.18, 'P_Otros': 4730.0, 'P_A_Solid': 0.0, 'P_Total': 72776.66, 'Inf_UOCRA': 'Fuera de Termino'}, {'Mes': datetime(2023, 4, 1, 0, 0), 'id': '202304', 'Vencimiento': datetime(2023, 5, 20, 0, 0), 'Empleados': 10, 'Aporte': 37354.99, 'Retencion': 5630.67, 'Contr.Pagada': 69079.32, 'Contribuciones': 74709.99, 'Rem4': 1464901.8, 'Rem8': 1464901.8, 'Rem5': 1464901.8, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1383518.27, 'Pago': 112274.68, 'Inspeccion': 0.0, 'Obr_Sindical': 9, 'Rem_Sindical': 1464901.8, 'Tot_Sindical': 36622.55, 'Obr_Seguro': 9, 'Rem_Seguro': 1464901.8, 'Total_Seguro': 22351.32, 'Fdo_Desempleo': 142942.14, 'FICS': 2858.84, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': datetime(2023, 5, 31, 0, 0), 'P_C_Sind': 36622.55, 'P_S_Vida': 22351.32, 'P_FICS': 36622.55, 'P_Otros': 4730.0, 'P_A_Solid': 0.0, 'P_Total': 66562.71, 'Inf_UOCRA': 'Fuera de Termino'}, {'Mes': datetime(2023, 5, 1, 0, 0), 'id': '202305', 'Vencimiento': datetime(2023, 6, 19, 0, 0), 'Empleados': 9, 'Aporte': 45227.91, 'Retencion': 39507.37, 'Contr.Pagada': 50948.39, 'Contribuciones': 90455.76, 'Rem4': 1773642.8, 'Rem8': 1773642.8, 'Rem5': 1773642.8, 'F.Pago': datetime(2023, 8, 14, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 1675107.04, 'Pago': 136631.02, 'Inspeccion': 0.0, 'Obr_Sindical': 8, 'Rem_Sindical': 1773642.8, 'Tot_Sindical': 44341.07, 'Obr_Seguro': 8, 'Rem_Seguro': 1773642.8, 'Total_Seguro': 21312.8, 'Fdo_Desempleo': 172576.07, 'FICS': 3451.52, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': datetime(2023, 6, 14, 0, 0), 'P_C_Sind': 44341.07, 'P_S_Vida': 21312.8, 'P_FICS': 44341.07, 'P_Otros': 4730.0, 'P_A_Solid': 0.0, 'P_Total': 73835.39, 'Inf_UOCRA': ''}, {'Mes': datetime(2023, 6, 1, 0, 0), 'id': '202306', 'Vencimiento': datetime(2023, 7, 20, 0, 0), 'Empleados': 8, 'Aporte': 57055.89, 'Retencion': 20578.6, 'Contr.Pagada': 93533.18, 'Contribuciones': 114111.78, 'Rem4': 2237485.81, 'Rem8': 2237485.81, 'Rem5': 2237485.81, 'F.Pago': datetime(2023, 8, 23, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 2113181.11, 'Pago': 171167.67, 'Inspeccion': 0.0, 'Obr_Sindical': 7, 'Rem_Sindical': 2237485.81, 'Tot_Sindical': 55937.15, 'Obr_Seguro': 7, 'Rem_Seguro': 2237485.81, 'Total_Seguro': 19280.8, 'Fdo_Desempleo': 209804.99, 'FICS': 4196.1, 'Otros_Conceptos': 4730.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': datetime(2023, 7, 28, 0, 0), 'P_C_Sind': 55937.15, 'P_S_Vida': 19280.8, 'P_FICS': 55937.15, 'P_Otros': 4730.0, 'P_A_Solid': 0.0, 'P_Total': 84144.05, 'Inf_UOCRA': 'Fuera de Termino'}, {'Mes': datetime(2023, 7, 1, 0, 0), 'id': '202307', 'Vencimiento': datetime(2023, 8, 19, 0, 0), 'Empleados': 6, 'Aporte': 17415.48, 'Retencion': 0.0, 'Contr.Pagada': 34830.94, 'Contribuciones': 34830.94, 'Rem4': 682959.6, 'Rem8': 682959.6, 'Rem5': 682959.6, 'F.Pago': datetime(2023, 8, 23, 0, 0), 'Inf_OS': 'Fuera de Termino', 'Rem_p_Calculo': 645017.53, 'Pago': 52246.42, 'Inspeccion': 0.0, 'Obr_Sindical': 3, 'Rem_Sindical': 682959.6, 'Tot_Sindical': 17073.99, 'Obr_Seguro': 3, 'Rem_Seguro': 682959.6, 'Total_Seguro': 9089.58, 'Fdo_Desempleo': 61786.85, 'FICS': 1235.74, 'Otros_Conceptos': 1290.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2023, 8, 1, 0, 0), 'id': '202308', 'Vencimiento': datetime(2023, 9, 19, 0, 0), 'Empleados': 0, 'Aporte': 0.0, 'Retencion': 0.0, 'Contr.Pagada': 0.0, 'Contribuciones': 0.0, 'Rem4': 0.0, 'Rem8': 0.0, 'Rem5': 0.0, 'F.Pago': 0.0, 'Inf_OS': 'Impago', 'Pago': 0.0, 'Inspeccion': 0.0, 'Obr_Sindical': 0, 'Rem_Sindical': 0.0, 'Tot_Sindical': 0.0, 'Obr_Seguro': 0, 'Rem_Seguro': 0.0, 'Total_Seguro': 0.0, 'Fdo_Desempleo': 0.0, 'FICS': 0.0, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2023, 9, 1, 0, 0), 'id': '202309', 'Vencimiento': datetime(2023, 10, 20, 0, 0), 'Empleados': 0, 'Aporte': 0.0, 'Retencion': 0.0, 'Contr.Pagada': 0.0, 'Contribuciones': 0.0, 'Rem4': 0.0, 'Rem8': 0.0, 'Rem5': 0.0, 'F.Pago': 0.0, 'Inf_OS': 'Impago', 'Pago': 0.0, 'Inspeccion': 0.0, 'Obr_Sindical': 0, 'Rem_Sindical': 0.0, 'Tot_Sindical': 0.0, 'Obr_Seguro': 0, 'Rem_Seguro': 0.0, 'Total_Seguro': 0.0, 'Fdo_Desempleo': 0.0, 'FICS': 0.0, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2023, 10, 1, 0, 0), 'id': '202310', 'Vencimiento': datetime(2023, 11, 19, 0, 0), 'Empleados': 0, 'Aporte': 0.0, 'Retencion': 0.0, 'Contr.Pagada': 0.0, 'Contribuciones': 0.0, 'Rem4': 0.0, 'Rem8': 0.0, 'Rem5': 0.0, 'F.Pago': 0.0, 'Inf_OS': 'Impago', 'Pago': 0.0, 'Inspeccion': 0.0, 'Obr_Sindical': 0, 'Rem_Sindical': 0.0, 'Tot_Sindical': 0.0, 'Obr_Seguro': 0, 'Rem_Seguro': 0.0, 'Total_Seguro': 0.0, 'Fdo_Desempleo': 0.0, 'FICS': 0.0, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2023, 11, 1, 0, 0), 'id': '202311', 'Vencimiento': datetime(2023, 12, 20, 0, 0), 'Empleados': 0, 'Aporte': 0.0, 'Retencion': 0.0, 'Contr.Pagada': 0.0, 'Contribuciones': 0.0, 'Rem4': 0.0, 'Rem8': 0.0, 'Rem5': 0.0, 'F.Pago': 0.0, 'Inf_OS': 'Impago', 'Pago': 0.0, 'Inspeccion': 0.0, 'Obr_Sindical': 0, 'Rem_Sindical': 0.0, 'Tot_Sindical': 0.0, 'Obr_Seguro': 0, 'Rem_Seguro': 0.0, 'Total_Seguro': 0.0, 'Fdo_Desempleo': 0.0, 'FICS': 0.0, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}, {'Mes': datetime(2023, 12, 1, 0, 0), 'id': '202312', 'Vencimiento': datetime(2024, 1, 19, 0, 0), 'Empleados': 0, 'Aporte': 0.0, 'Retencion': 0.0, 'Contr.Pagada': 0.0, 'Contribuciones': 0.0, 'Rem4': 0.0, 'Rem8': 0.0, 'Rem5': 0.0, 'F.Pago': 0.0, 'Inf_OS': 'Impago', 'Pago': 0.0, 'Inspeccion': 0.0, 'Obr_Sindical': 0, 'Rem_Sindical': 0.0, 'Tot_Sindical': 0.0, 'Obr_Seguro': 0, 'Rem_Seguro': 0.0, 'Total_Seguro': 0.0, 'Fdo_Desempleo': 0.0, 'FICS': 0.0, 'Otros_Conceptos': 0.0, 'Obr_No_Afil': 0, 'Rem_No_Afil': 0.0, 'Aporte_Solid': 0.0, 'P_Fecha': 0.0, 'P_C_Sind': 0.0, 'P_S_Vida': 0.0, 'P_FICS': 0.0, 'P_Otros': 0.0, 'P_A_Solid': 0.0, 'P_Total': 0.0, 'Inf_UOCRA': 'Impago'}]
  
@app.get('/')
def mnsj():
    return "arrancanding"
@app.get('/f931')
def get_f931():
    insp = [d for d in f931 if d['id'] > insp_desde and d['id'] < insp_hasta]
    if sia == []:
        return insp
    for dic_f931 in insp:
        id_f931 = dic_f931['id']
        for dic_sia in sia:
            if dic_sia['id'] == id_f931:
                if dic_sia['Contr.Pagada'] != 0.0:
                    dic_f931['fPCont'] = dic_sia['F.Pago']
                if dic_sia['Aporte'] != 0.0:
                    dic_f931['fPApo'] = dic_sia['F.Pago']
                if (dic_sia['Pago']-dic_sia['Contr.Pagada']-dic_sia['Aporte']) > 1:
                    dic_f931['Int'] = "Si"
                if (dic_sia['Pago']-dic_sia['Contr.Pagada']-dic_sia['Aporte']) < 1 :
                    dic_f931['Int'] = "No"
                if dic_f931['Int'] =='No' and dic_sia['Inf_OS'] == 'Fuera de Termino':
                    dic_f931['infOS'] = dic_sia['Inf_OS']
                if dic_sia['Inf_OS'] == 'Impago':
                    dic_f931['infOS'] = dic_sia['Inf_OS'] 
    return insp

@app.get('/sia')
def get_sia():
    return sia

@app.get('/sia/{mes}/{year}')
def get_periodo(mes:str, year:str):
    x =datetime.strptime("01/"+mes+"/"+year,"%d/%m/%Y")
    y = list(filter(lambda item: item['Mes']==x,sia))
    return y

@app.get('/infracciones')
def get_inf_os():
    inf =[]
    os_imp = []
    x = list(filter(lambda item: item['Inf_OS']=='Impago',sia))
    for i in x:
            os_imp.append(i['Mes'])
    os_pft = []
    y = list(filter(lambda item: item['Inf_OS']=='Fuera de Termino',sia))
    for i in y:
            os_pft.append(i['Mes'])
    uo_imp = []
    x = list(filter(lambda item: item['Inf_UOCRA']=='Impago',sia))
    for i in x:
            uo_imp.append(i['Mes'])
    uo_pft = []
    x = list(filter(lambda item: item['Inf_UOCRA']=='Fuera de Termino',sia))
    for i in x:
            uo_pft.append(i['Mes'])
    inf =[{'os_imp':os_imp},{'os_pft':os_pft},{'uo_imp':uo_imp},{'uo_pft':uo_pft}]
    return inf

# @app.post("/uploadfile/")
# async def upload_file(file: UploadFile):
#     with open(f"uploads/{file.filename}", "wb") as f:
#         shutil.copyfileobj(file.file, f)
#     return {"filename": file.filename}

@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        with open(f"uploads/{file.filename}", "wb") as f:
            shutil.copyfileobj(file.file, f)
    return {"message": "Archivos subidos con éxito"}