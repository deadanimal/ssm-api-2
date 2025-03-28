import requests
import json
import xmltodict

def get_info_charges(url, headers, registration_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoCharges>
            <header>
                <customerId>SSMProduk</customerId>
                <customerReferenceNo></customerReferenceNo>
                <customerRequestDate></customerRequestDate>
            </header>
            <request>
                <supplyChargesReq>
                    <coNo>""" + str(registration_number) + """</coNo>
                    <gstAmount>0</gstAmount>
                    <infoAmount>0</infoAmount>
                    <invoiceNo></invoiceNo>
                    <ipaddress></ipaddress>
                    <remark></remark>
                    <tableId>ROCINFO</tableId>
                    <type>INFOROCCHRGE</type>
                </supplyChargesReq>
            </request>
        </inf:getInfoCharges>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoChargesResponse']['response']['getInfoChargesReturn']