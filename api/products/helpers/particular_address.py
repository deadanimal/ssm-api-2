import string
import pytz
import json

from datetime import datetime
from django.utils.timezone import make_aware
from .mapping import (
    state_mapping,
    time_mapping,
    comp_status_mapping,
    status_of_comp_mapping,
    comp_type_mapping,
    origin_country_mapping
)

def particular_address(mdw_1, mdw_2, lang):
    
    data_mdw_1 = mdw_1
    data_mdw_2 = mdw_2

    if mdw_1['rocCompanyInfo']['companyOldName'] == None:
        temp_old_name = 'NIL'
    else:
        temp_old_name = mdw_1['rocCompanyInfo']['companyOldName']

    if '@xsi:nil' in data_mdw_1['rocCompanyInfo']['dateOfChange']:
        temp_change_date = 'NIL'
    else:
        temp_change_date = time_mapping(data_mdw_1['rocCompanyInfo']['dateOfChange']['#text'])

    if '@xsi:nil' in data_mdw_1['rocCompanyInfo']['incorpDate']:
        temp_change_date = 'NIL'
    else:
        temp_incorp_date = time_mapping(data_mdw_1['rocCompanyInfo']['incorpDate']['#text'])
    
    if '@xsi:nil' in data_mdw_1['rocCompanyInfo']['registrationDate']:
        temp_reg_date = 'NIL'
    else:
        temp_reg_date = time_mapping(data_mdw_1['rocCompanyInfo']['registrationDate']['#text'])
    
    temp_comp_type = comp_type_mapping(data_mdw_1['rocCompanyInfo']['companyType'], lang)
    temp_comp_status = comp_status_mapping(data_mdw_1['rocCompanyInfo']['companyStatus'], lang)
    temp_status_of_company = status_of_comp_mapping(data_mdw_1['rocCompanyInfo']['statusOfCompany'])

    temp_reg_address_1 = data_mdw_1['rocRegAddressInfo']['address1']
    temp_reg_address_2 = data_mdw_1['rocRegAddressInfo']['address2']
    temp_reg_address_3 = data_mdw_1['rocRegAddressInfo']['address3']
    temp_reg_postcode = data_mdw_1['rocRegAddressInfo']['postcode']
    temp_reg_town = data_mdw_1['rocRegAddressInfo']['town']
    temp_reg_state = data_mdw_1['rocRegAddressInfo']['state']

    if temp_reg_address_1 == 'TIADA FAIL':
        temp_reg_address_1 = None
    elif temp_reg_address_1 == None:
        temp_reg_address_1 = None
    else:
        temp_reg_address_1 = temp_reg_address_1

    if temp_reg_address_2 == 'TIADA FAIL':
        temp_reg_address_2 = None
    elif temp_reg_address_2 == None:
        temp_reg_address_2 = None
    else:
        temp_reg_address_2 = temp_reg_address_2

    if temp_reg_address_3 == 'TIADA FAIL':
        temp_reg_address_3 = None
    elif temp_reg_address_3 == None:
        temp_reg_address_3 = None
    else:
        temp_reg_address_3 = temp_reg_address_3
    
    if temp_reg_postcode == 'TIADA FAIL':
        temp_reg_postcode = None
    elif temp_reg_postcode == None:
        temp_reg_postcode = None
    else:
        temp_reg_postcode = temp_reg_postcode

    if temp_reg_town == 'TIADA FAIL':
        temp_reg_town = None
    elif temp_reg_town == None:
        temp_reg_town = None
    else:
        temp_reg_town = temp_reg_town

    if temp_reg_state == 'TIADA FAIL':
        temp_reg_state = None
    elif temp_reg_state == None:
        temp_reg_state = None
    else:
        temp_reg_state = state_mapping(temp_reg_state)
    
    temp_reg_origin = origin_country_mapping(data_mdw_1['rocCompanyInfo']['companyCountry'])

    temp_biz_address_1 = data_mdw_1['rocBusinessAddressInfo']['address1']
    temp_biz_address_2 = data_mdw_1['rocBusinessAddressInfo']['address2']
    temp_biz_address_3 = data_mdw_1['rocBusinessAddressInfo']['address3']
    temp_biz_postcode = data_mdw_1['rocBusinessAddressInfo']['postcode']
    temp_biz_town = data_mdw_1['rocBusinessAddressInfo']['town']
    temp_biz_state = data_mdw_1['rocBusinessAddressInfo']['state']

    if temp_biz_address_1 == 'TIADA FAIL':
        temp_biz_address_1 = None
    elif temp_biz_address_1 == None:
        temp_biz_address_1 = None
    else:
        temp_biz_address_1 = temp_biz_address_1

    if temp_biz_address_2 == 'TIADA FAIL':
        temp_biz_address_2 = None
    elif temp_biz_address_2 == None:
        temp_biz_address_2 = None
    else:
        temp_biz_address_2 = temp_biz_address_2

    if temp_biz_address_3 == 'TIADA FAIL':
        temp_biz_address_3 = None
    elif temp_biz_address_3 == None:
        temp_biz_address_3 = None
    else:
        temp_biz_address_3 = temp_biz_address_3
    
    if temp_biz_postcode == 'TIADA FAIL':
        temp_biz_postcode = None
    elif temp_biz_postcode == None:
        temp_biz_postcode = None
    else:
        temp_biz_postcode = temp_biz_postcode

    if temp_biz_town == 'TIADA FAIL':
        temp_biz_town = None
    elif temp_biz_town == None:
        temp_biz_town = None
    else:
        temp_biz_town = temp_biz_town

    if temp_biz_state == 'TIADA FAIL':
        temp_biz_state = None
    elif temp_biz_state == None:
        temp_biz_state = None
    else:
        temp_biz_state = state_mapping(temp_biz_state)
    

    temp_last_update_date = time_mapping(data_mdw_1['rocCompanyInfo']['lastUpdateDate']['#text'])

    temp_change_reg_address = []

    for changes in mdw_1['rocChangesRegAddressListInfo']['rocChangesRegAddressInfo']['rocChangesRegAddressInfo']:

        temp_address_1 = data_mdw_1['rocRegAddressInfo']['address1']
        temp_address_2 = data_mdw_1['rocRegAddressInfo']['address2']
        temp_address_3 = data_mdw_1['rocRegAddressInfo']['address3']
        temp_postcode = data_mdw_1['rocRegAddressInfo']['postcode']
        temp_town = data_mdw_1['rocRegAddressInfo']['town']
        temp_state = data_mdw_1['rocRegAddressInfo']['state']

        if temp_address_1 == 'TIADA FAIL':
            temp_address_1 = None
        elif temp_address_1 == None:
            temp_address_1 = None
        else:
            temp_address_1 = temp_address_1

        if temp_address_2 == 'TIADA FAIL':
            temp_address_2 = None
        elif temp_address_2 == None:
            temp_address_2 = None
        else:
            temp_address_2 = temp_address_2

        if temp_address_3 == 'TIADA FAIL':
            temp_address_3 = None
        elif temp_address_3 == None:
            temp_address_3 = None
        else:
            temp_address_3 = temp_address_3
        
        if temp_postcode == 'TIADA FAIL':
            temp_postcode = None
        elif temp_postcode == None:
            temp_postcode = None
        else:
            temp_postcode = temp_postcode

        if temp_town == 'TIADA FAIL':
            temp_town = None
        elif temp_town == None:
            temp_town = None
        else:
            temp_town = temp_town

        if temp_state == 'TIADA FAIL':
            temp_state = None
        elif temp_state == None:
            temp_state = None
        else:
            temp_state = state_mapping(temp_state)

        if '@xsi:nil' in data_mdw_1['rocCompanyInfo']['dateOfChange']:
            temp_date = 'NIL'
        else:
            temp_date = time_mapping(data_mdw_1['rocCompanyInfo']['dateOfChange']['#text'])

        temp_change_reg_address.append({
            'address1': temp_address_1,
            'address2': temp_address_2,
            'adress3': temp_address_3,
            'postcode': temp_postcode,
            'town': temp_town,
            'state': temp_state,
            'changeDate': temp_date 
        })
        
    data_ready = {
        'corpInfo': {
            'compName': mdw_1['rocCompanyInfo']['companyName'],
            'compNameOld': temp_old_name,
            'changeDate': temp_change_date,
            'compNo': data_mdw_2['newFormatNo'] + ' (' + data_mdw_2['oldFormatNo'] + ')',
            'incorpDate': temp_incorp_date,
            'regDate': temp_reg_date,
            'compType': temp_comp_type,
            'compStatus': temp_comp_status,
            'statusOfCompany': temp_status_of_company,
            'regAddress1': temp_reg_address_1,
            'regAddress2': temp_reg_address_2,
            'regAddress3': temp_reg_address_3,
            'regTown': temp_reg_town,
            'regPostcode': temp_reg_postcode,
            'regState': temp_reg_state,
            'regOrigin': temp_reg_origin,
            'bizAddress1': temp_biz_address_1,
            'bizAddress2': temp_biz_address_2,
            'bizAddress3': temp_biz_address_3,
            'bizTown': temp_biz_town,
            'bizPostcode': temp_biz_postcode,
            'bizState': temp_biz_state,
            'bizNature': mdw_1['rocCompanyInfo']['businessDescription']
        },
        'lastUpdateDate': temp_last_update_date,
        'changeRegAddress': temp_change_reg_address
    }

    print(data_ready)

    return data_ready