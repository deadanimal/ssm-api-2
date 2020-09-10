import requests
import json
import xmltodict

def get_info_fin2(url, headers, registration_number):

   payload = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:inf="http://inf.ssm.com.my">
    <soapenv:Header />
    <soapenv:Body>
        <inf:getInfoFin2>
            <!--Optional:-->
            <header>
                <!--Optional:-->
                <customerId>SSMProduk</customerId>
                <!--Optional:-->
                <customerReferenceNo></customerReferenceNo>
                <!--Optional:-->
                <customerRequestDate></customerRequestDate>
            </header>
            <!--Optional:-->
            <request>
                <!--Optional:-->
                <supplyFin2Req>
                    <!--Optional:-->
                    <coNo>""" + str(registration_number) + """</coNo>
                    <!--Optional:-->
                    <endYear>2019</endYear>
                    <!--Optional:-->
                    <ipaddress></ipaddress>
                    <!--Optional:-->
                    <remark></remark>
                    <!--Optional:-->
                    <startYear>2017</startYear>
                    <!--Optional:-->
                    <type>INFOFINHISTY</type>
                </supplyFin2Req>
            </request>
        </inf:getInfoFin2>
    </soapenv:Body>
</soapenv:Envelope>
"""

   response = requests.request("POST", url, data=payload, headers=headers)
   response_xml = response.content
   middleware_response_json = json.loads(json.dumps(xmltodict.parse(response_xml)))
   return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getInfoFin2Response']['response']['getInfoFin2Return']