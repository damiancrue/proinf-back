from fastapi import FastAPI, File, UploadFile
from datetime import datetime
import datetime as dt
from fastapi.middleware.cors import CORSMiddleware
import shutil
from typing import List
from leer_sia_todo import leer_sia
from leerTodo import leer_carpeta

app = FastAPI()

# Configura CORS para permitir solicitudes desde http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

insp = {
    'id':"",
    'nro':"",
    'empresa': "",
    'cuit':"",
    'desde':"",
    'hasta':"",
    'dom_legal':{'calle':"", 'local':"", 'prov':"", 'cp':"", 'tel':""},
    'dom_fiscal':{'calle':"", 'local':"", 'prov':"", 'cp':"", 'tel':""},
    'dom_control':{'calle':"", 'local':"", 'prov':"", 'cp':"", 'tel':""},
    'mail':"",
}

insp_desde= '202211'
insp_hasta= '202308'

cee={'201807':110,'201808':110,'201809':110, '201810':110,'201811':110,'201812':110, '201901':110, '201902':110,
     '201907':150,'201908':150,'201909':150, '201910':150,'201911':150,'201912':150, '202001':150, '202002':150,
     '202011':200,'202012':200,'202101':200, '202102':200,'202103':200,'202104':200, '202105':200, '202106':200,
     '202107':265,'202108':265,'202109':265, '202110':265,'202111':265,'202112':265, '202201':265, '202202':265,
     '202207':430,'202208':430,'202209':430, '202210':430,'202211':430,'202212':430, '202301':430, '202302':430,
     '202307':850,'202308':850,'202309':850, '202310':850,'202311':850,'202312':850, '202401':850, '202402':850,
    }

oasys = "./uploads/"
ubicac = "./uploads/"
f931 =  [d for d in leer_carpeta(ubicac) if d['id'] >= insp_desde and d['id'] <= insp_hasta]
#print(f931)
sia = [d for d in leer_sia(oasys) if d['id'] >= insp_desde and d['id'] <= insp_hasta] 
#print (sia)

@app.get('/')
def mnsj():
    return "arrancanding"

@app.get('/f931')
def get_f931():
    return f931

@app.get('/sia')
def get_sia():
    x = [elem for elem in sia if insp_desde <= elem["id"] <= insp_hasta]
    return x

@app.get('/f05')
def get_f05():
    y=[]
    # Crear un diccionario temporal para mapear los elementos de y por 'id'
    diccionario_y = {item['id']: item for item in f931}
    # Recorrer la lista x y combinar los elementos de x y y si existe un 'id' coincidente
    for elemento_x in sia:
        id_x = elemento_x['id']
        if id_x in diccionario_y:
            elemento_y = diccionario_y[id_x]
            temp = {**elemento_y}
            if elemento_x['Contr.Pagada'] != 0.0:
                temp['fPCont'] = elemento_x['F.Pago']
            if elemento_x['Aporte'] != 0.0:
                temp['fPApo'] = elemento_x['F.Pago']
            if (elemento_x['Pago']-elemento_x['Contr.Pagada']-elemento_x['Aporte']) > 1:
                temp['Int'] = "Si"
            if (elemento_x['Pago']-elemento_x['Contr.Pagada']-elemento_x['Aporte']) < 1 :
                temp['Int'] = "No"
            if temp['Int'] =='No' and elemento_x['Inf_OS'] == 'Fuera de Termino':
                temp['infOS'] = elemento_x['Inf_OS']
            if elemento_x['Inf_OS'] == 'Impago':
                temp['infOS'] = elemento_x['Inf_OS']
            y.append(temp)
        else:
            y.append({'id':elemento_x['id']})
    return y

@app.get('/mayor')
def get_mayor():
    j=[]
    temp = get_f05()
    for elem in temp:
        k={}
        k['id'] = elem['id']
        if 'retPA' in elem:
            k['retPA']=elem['retPA']
        else:
            k['retPA']=0.0
        if 'retPe' in elem:
            k['retPe']=elem['retPe']
        else:
            k['retPe']=0.0
        if 'retSS' in elem:
            k['retSS']=elem['retSS']
        else:
            k['retSS']=0.0
        if 'retOS' in elem:
            k['retOS']=elem['retOS']
        else:
            k['retOS']=0.0
        k['retTo']= k['retPA']+k['retPe']
        k['retPP']= k['retTo']-k['retSS']-k['retOS']
        j.append(k)
    return j

@app.get('/u05')#reeever
def get_uocra():
    x = []
    d=0
    for mes in sia:
        y={}
        y['id']=mes['id']
        y['rem_total']=mes['Rem_Seguro']
        y['rem_sind']=mes['Rem_Sindical']
        y['rem_a_sol']=mes['Rem_No_Afil']
        y['obr']=mes['Obr_Seguro']
        y['c_sind']=mes['P_C_Sind']
        y['s_vida']=mes['P_S_Vida']
        y['ap_sol']=mes['P_A_Solid']
        y['venc']=mes['Vencimiento']
        y['f_pago']=mes['P_Fecha']
        y['fcl']=mes['Fdo_Desempleo']
        y['ficys']=mes['P_FICS']
        y['cee']=mes['P_Otros']
        y['p_total']=mes['P_Total']
        y['UO_inf'] ={}
        if y['id'] in cee:
            a = cee[y['id']]
        else:
            a=0
        if y['cee']-(a*d) > 1 and mes['P_Fecha']>mes['Vencimiento']:
            y['int'] ='Si'
# cuota sindical
        if y['f_pago'] == 0.0 and y['rem_sind'] == 0:
            pass
        elif y['f_pago'] == 0.0 and y['rem_sind'] > 0:
            y['UO_inf']['cs']='Impago'
        elif y['f_pago']!= 0.0 and y['rem_sind']>0 and round((y['c_sind']/0.025+1),2) >= y['rem_sind'] and y['f_pago']>y['venc']:
            y['UO_inf']['cs'] = 'Fuera de Termino'
        elif y['f_pago'] != 0.0 and y['rem_sind']>0 and round((y['c_sind']/0.025+1),2) < y['rem_sind']:
            y['UO_inf']['cs'] = 'Pago a Cuenta'
        elif y['rem_total']<mes['Rem5'] and y['f_pago'] != 0.0 and y['rem_sind']>0:
            y['UO_inf']['cs'] = 'Pago a Cuenta'
#seguro de vida
        if y['f_pago'] == 0.0 and y['obr'] == 0:
            pass
        elif y['f_pago'] == 0.0 and y['obr'] > 0:
            y['UO_inf']['sv']='Impago'
        elif y['f_pago']!= 0.0 and y['obr']>0 and y['s_vida'] == mes['Total_Seguro']and y['f_pago']>y['venc']:
            y['UO_inf']['sv'] = 'Fuera de Termino'
        elif y['f_pago'] != 0.0 and y['obr']>0 and y['s_vida']+1 < mes['Total_Seguro']:
            y['UO_inf']['sv'] = 'Pago a Cuenta'
        elif y['obr']<mes['Empleados'] and y['f_pago'] != 0.0 :
            y['UO_inf']['sv'] = 'Pago a Cuenta'
# ficys
        if y['f_pago'] == 0.0 and y['rem_total'] == 0:
            pass
        elif y['f_pago'] == 0.0 and y['rem_total'] > 0:
            y['UO_inf']['fi']='Impago'
        elif y['f_pago']!= 0.0 and y['rem_total']>0 and y['ficys'] == mes['FICS']and y['f_pago']>y['venc']:
            y['UO_inf']['fi'] = 'Fuera de Termino'
        elif y['f_pago'] != 0.0 and y['rem_total']>0 and round((y['ficys']/0.0016),2) < y['rem_total']:
            y['UO_inf']['fi'] = 'Pago a Cuenta'
        elif y['rem_total']<mes['Rem5'] and y['f_pago'] != 0.0 :
            y['UO_inf']['fi'] = 'Pago a Cuenta'
# aporte solidario
        if y['f_pago'] == 0.0 and y['rem_a_sol'] == 0:
            pass
        elif y['f_pago'] == 0.0 and y['rem_a_sol'] > 0:
            y['UO_inf']['as']='Impago'
        elif y['f_pago']!= 0.0 and y['rem_a_sol']>0 and round((y['c_sind']/0.025+1),2) >= y['rem_a_sol'] and y['f_pago']>y['venc']:
            y['UO_inf']['as'] = 'Fuera de Termino'
        elif y['f_pago'] != 0.0 and y['rem_a_sol']>0 and round((y['c_sind']/0.025+1),2) < y['rem_a_sol']:
            y['UO_inf']['as'] = 'Pago a Cuenta'
        elif y['rem_total']<mes['Rem5'] and y['f_pago'] != 0.0 and y['rem_a_sol']>0:
            y['UO_inf']['as'] = 'Pago a Cuenta'
# cee
        if y['f_pago'] == 0.0 and y['rem_total'] == 0:
            pass
        elif y['f_pago'] == 0.0 and y['id'] in cee and a>0:
            y['UO_inf']['ce']='Impago'
        elif y['f_pago']!= 0.0 and y['id'] in cee and a>0 and y['cee'] >= a*d and y['f_pago']>y['venc']:
            y['UO_inf']['ce'] = 'Fuera de Termino'
        elif y['f_pago']!= 0.0 and y['id'] in cee and a>0 and y['cee'] < a*d :
            y['UO_inf']['ce'] = 'Pago a Cuenta'
#
        # if mes['P_Otros'] > 0.0 and mes['P_Fecha']>mes['Vencimiento']:
        #     y['int'] ='Si'
        d=y['obr']
        x.append(y)
    return x

@app.get('/sia/{mes}/{year}')
def get_periodo(mes:str, year:str):
    x =datetime.strptime("01/"+mes+"/"+year,"%d/%m/%Y")
    y = list(filter(lambda item: item['Mes']==x,sia))
    return y

@app.get('/infracciones')
def get_inf():
    inf =[]
    # #OS
    # os_imp = []
    # x = list(filter(lambda item: item['Inf_OS']=='Impago',sia))
    # for i in x:
    #         os_imp.append(i['id'][-2:]+'/'+i['id'][0:4])
    # os_pac = []
    # os_pft = []
    # y = list(filter(lambda item: item['Inf_OS']=='Fuera de Termino',sia))
    # for i in y:
    #         os_pft.append(i['id'][-2:]+'/'+i['id'][0:4])
    # #UOCRA
    # uo_cs=get_min_cs()
    # uo_sv=get_min_sv()
    # uo_as=get_min_as()
    # uo_ce=get_min_ce()
    # uo_fi=get_min_fi()

    # uo_imp = {'cs':[],'sv':[],'ce':[],'as':[],'fi':[]}
    # uo_pac = {'cs':[],'sv':[],'ce':[],'as':[],'fi':[]}
    # uo_pft = {'cs':[],'sv':[],'ce':[],'as':[],'fi':[]}

    # for i in uo_cs:
    #     # print(i)
    #     if i['cod']==4:
    #         uo_imp['cs'].append(i['per'])
    #     elif i['cod']==10:
    #         uo_pac['cs'].append(i['per'])
    #     elif i['cod']==1:
    #         uo_pft['cs'].append(i['per'])
    # for i in uo_sv:
    #     # print(i)
    #     if i['cod']==4:
    #         uo_imp['sv'].append(i['per'])
    #     elif i['cod']==10:
    #         uo_pac['sv'].append(i['per'])
    #     elif i['cod']==1:
    #         uo_pft['sv'].append(i['per'])
    # for i in uo_as:
    #     # print(i)
    #     if i['cod']==4:
    #         uo_imp['as'].append(i['per'])
    #     elif i['cod']==10:
    #         uo_pac['as'].append(i['per'])
    #     elif i['cod']==1:
    #         uo_pft['as'].append(i['per'])
    # for i in uo_ce:
    #     # print(i)
    #     if i['cod']==4:
    #         uo_imp['ce'].append(i['per'])
    #     elif i['cod']==10:
    #         uo_pac['ce'].append(i['per'])
    #     elif i['cod']==1:
    #         uo_pft['ce'].append(i['per'])
    # for i in uo_fi:
    #     # print(i)
    #     if i['cod']==4:
    #         uo_imp['fi'].append(i['per'])
    #     elif i['cod']==10:
    #         uo_pac['fi'].append(i['per'])
    #     elif i['cod']==1:
    #         uo_pft['fi'].append(i['per'])
 
    # inf ={'os_imp':os_imp,'os_pac':os_pac,'os_pft':os_pft,'uo_imp':uo_imp,'uo_pac':uo_pac,'uo_pft':uo_pft}
    return inf

@app.get('/min_os')
def get_min_os():
    m_os=[]
    for mes in sia:
        if mes['Inf_OS'] =='Fuera de Termino':
            temp={}
            temp['periodo']=mes['id'][-2:]+'/'+mes['id'][0:4]
            temp['obr']=mes['Empleados']
            temp['rem']=mes['Rem_p_Calculo']
            if mes['Retencion'] > 0 and mes['Contr.Pagada'] >0:
                temp2 = {**temp}
                temp['obr']=0
                temp['rem']=0
                temp2['cont_p']=mes['Retencion']
                temp2['f_p_cont']=mes['Mes']+dt.timedelta(days=37)
                m_os.append(temp2)
            if mes['Contr.Pagada']>0:
                temp['cont_p']=mes['Contr.Pagada']
                temp['f_p_cont']=mes['F.Pago']
            else:
                temp['cont_p']=mes['Retencion']
                temp['f_p_cont']=mes['Mes']+dt.timedelta(days=37)
            temp['ap_p']=mes['Aporte']
            temp['f_p_ap']=mes['F.Pago']
            m_os.append(temp)
    return m_os

@app.get('/min_cs')
def get_min_cs():
    m_cs=[]
    uocra=get_uocra()
    for mes in uocra:
        temp={}
        if 'cs' in mes['UO_inf']:
            temp['per']=mes['id'][-2:]+'/'+mes['id'][0:4]
            if mes['UO_inf']['cs'] == 'Impago':
                temp['cod']=4
            elif mes['UO_inf']['cs'] == 'Pago a Cuenta':
                temp['cod']=10
            elif mes['UO_inf']['cs'] == 'Fuera de Termino'and 'int' not in mes:
                temp['cod']=1
            else:
                temp['cod']=0
            temp['rem']=mes['rem_sind']
            if mes['c_sind']>0 and 'int' not in mes:
                temp['c_sind']=mes['c_sind']
                temp['f_p_cs']=mes['f_pago']
        m_cs.append(temp)
    minu = [d for d in m_cs if 'per' in d]
    min = [e for e in minu if e['cod']!= 0]
    return min

@app.get('/min_sv')#ojo pago a cuenta por mayor valor en sia ospecon
def get_min_sv():
    m_sv=[]
    uocra=get_uocra()
    for mes in uocra:
        temp={}
        if 'sv' in mes['UO_inf']:
            temp['per']=mes['id'][-2:]+'/'+mes['id'][0:4]
            if mes['UO_inf']['sv'] == 'Impago':
                temp['cod']=4
            elif mes['UO_inf']['sv'] == 'Pago a Cuenta':
                temp['cod']=10
            elif mes['UO_inf']['sv'] == 'Fuera de Termino'and 'int' not in mes:
                temp['cod']=1
            else:
                temp['cod']=0
            temp['obr']=mes['obr']
            if mes['s_vida']>0 and 'int' not in mes:
                temp['s_vida']=mes['s_vida']
                temp['f_p_sv']=mes['f_pago']
        m_sv.append(temp)
    minu = [d for d in m_sv if 'per' in d]
    min = [e for e in minu if e['cod']!= 0]
    return min

@app.get('/min_as')
def get_min_as():
    m_as=[]
    uocra=get_uocra()
    for mes in uocra:
        temp={}
        if 'as' in mes['UO_inf']:
            temp['per']=mes['id'][-2:]+'/'+mes['id'][0:4]
            if mes['UO_inf']['as'] == 'Impago':
                temp['cod']=4
            elif mes['UO_inf']['as'] == 'Pago a Cuenta':
                temp['cod']=10
            elif mes['UO_inf']['as'] == 'Fuera de Termino'and 'int' not in mes:
                temp['cod']=1
            else:
                temp['cod']=0
            temp['rem']=mes['rem_a_sol']
            if mes['a_sol']>0 and 'int' not in mes:
                temp['a_sol']=mes['a_sol']
                temp['f_p_as']=mes['f_pago']
        m_as.append(temp)
    minu = [d for d in m_as if 'per' in d]
    min = [e for e in minu if e['cod']!= 0]
    return min

@app.get('/min_ce')
def get_min_ce():
    m_ce=[]
    uocra=get_uocra()
    c= uocra[0]['obr']
    for mes in uocra:
        temp={}
        if 'ce' in mes['UO_inf']:
            temp['per']=mes['id'][-2:]+'/'+mes['id'][0:4]
            if mes['UO_inf']['ce'] == 'Impago':
                temp['cod']=4
            elif mes['UO_inf']['ce'] == 'Pago a Cuenta':
                temp['cod']=10
            elif mes['UO_inf']['ce'] == 'Fuera de Termino' and 'int' not in mes:
                temp['cod']=1
            else:
                temp['cod']=0
            temp['obr']=c
            if mes['cee']>0 and 'int' not in mes:
                temp['cee']=mes['cee']
                temp['f_p_ce']=mes['f_pago']
            c=mes['obr']
        m_ce.append(temp)
    minu = [d for d in m_ce if 'per' in d]
    min = [e for e in minu if e['cod']!= 0]
    return min

@app.get('/min_fi')
def get_min_fi():
    m_fi=[]
    uocra=get_uocra()
    for mes in uocra:
        temp={}
        if 'fi' in mes['UO_inf']:
            temp['per']=mes['id'][-2:]+'/'+mes['id'][0:4]
            if mes['UO_inf']['fi'] == 'Impago':
                temp['cod']=4
                temp['rem']=round(mes['fcl']/0.12,2)
            elif mes['UO_inf']['fi'] == 'Pago a Cuenta':
                temp['cod']=10
                temp['rem']=mes['rem_total']
            elif mes['UO_inf']['fi'] == 'Fuera de Termino' and 'int' not in mes:
                temp['cod']=1
                temp['rem']=round(mes['fcl']/0.12,2)
            else:
                temp['cod']=0
            if mes['ficys']>0 and 'int' not in mes:
                temp['ficys']=mes['ficys']
                temp['f_p_fi']=mes['f_pago']
        m_fi.append(temp)
    minu = [d for d in m_fi if 'per' in d]
    min = [e for e in minu if e['cod']!= 0]
    return min


@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        with open(f"uploads/{file.filename}", "wb") as f:
            shutil.copyfileobj(file.file, f)
    return {"message": "Archivos subidos con éxito"}
