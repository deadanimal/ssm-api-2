import requests
import json
import xmltodict

def get_particulars_of_cosec(url, headers, registration_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header/>
    <soapenv:Body>
        <inf:getParticularsOfCosec> 
            <!--Optional:-->
            <header>
                <!--Optional:-->
                <customerId>SSMProduk</customerId>
                <!--Optional:--> 
                <customerReferenceNo></customerReferenceNo> 
                <!--Optional:--> 
                <customerRequestDate>2019-09-10T00:00:00Z</customerRequestDate>
            </header> 
            <!--Optional:--> 
            <request>
                <!--Optional:--> 
                <req>
                    <!--Optional:--> 
                    <companyNo>""" + str(registration_number) + """</companyNo> 
                    <!--Optional:--> 
                    <designation>S</designation>
                </req> 
            </request>
        </inf:getParticularsOfCosec> 
    </soapenv:Body>
</soapenv:Envelope>
"""
    # """ + str(registration_number) + """
   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
#    return ['tak dapat middleware response lagi']
#    print(middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getParticularsOfCosecResponse']['response'])
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getParticularsOfCosecResponse']['response']['getParticularsOfCosecReturn']