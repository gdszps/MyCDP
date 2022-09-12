import json
import time

import trio
from sys import stderr
from trio_websocket import open_websocket_url

async  def new_client():
    try:
        async with open_websocket_url('ws://127.0.0.1:8000') as ws:

            while True:
                start_time=time.time()
                # xhr_data={
                #     'proxy_server':'http://127.0.0.1:888',
                #     'url':'https://ug.baidu.com/mcp/pc/pcsearch',
                #     'headers':{
                #         "Accept": "*/*",
                #         "Accept-Encoding": "gzip, deflate, br",
                #         "Accept-Language": "zh-CN,zh;q=0.9",
                #         "Cache-Control": "no-cache",
                #         "Connection": "keep-alive",
                #         "Content-Length": "56",
                #         "Content-Type": "application/json",
                #         "Cookie": "BIDUPSID=9E54F0F35E38AD6AA0B9B9C29E6B328A; PSTM=1655447593; BAIDUID=9E54F0F35E38AD6A2F51E2C7E32BAB54:FG=1; BDUSS=UzcURoaDFNT1IxamsxMXRvOVAwZmFROTM5MXJPLXQ4d2hxMG1BMX5wSVlOLXBpRVFBQUFBJCQAAAAAAAAAAAEAAADkLlRTZmc5bmYxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABiqwmIYqsJiTX; BDUSS_BFESS=UzcURoaDFNT1IxamsxMXRvOVAwZmFROTM5MXJPLXQ4d2hxMG1BMX5wSVlOLXBpRVFBQUFBJCQAAAAAAAAAAAEAAADkLlRTZmc5bmYxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABiqwmIYqsJiTX; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=zn-OJexroG0m9Djjy8EjN4mYtVaDkyjTDYLEOwXPsp3LGJLVcjL2EG0Ptsi5Gcu-ox7CogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRk8oKPyJKvDqTrP-trf5DCShUFsbtIOB2Q-XPoO3KJVbqbFMRrtDP0NjMck-p5K3I38BfbgylRp8P3y0bb2DUA1y4vp5-TrteTxoUJ2-bIhsnOGqtnWjUtebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDTAWjTPVKgTa54cbb4o2WbCQ2Jnd8pcN2b5oQT8DetOBaJFOQDrw_n6wbUQHsbvwMlOUWfAkXpJvQnJjt2JxaqRCKbcdhl5jDh3MKPc0QUbte4ROJ27y0hvctb3cShPm0MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8J5kOJb3aQ5rtKRTffjrnhPF3-nLFXP6-hnjy3bRLVlb_2tIWS4b8j-cZ5hK_QMR8aq3RymJ42-39LPO2hpRjyxv4-PITD4oxJpOJ-KKtKbOaHR7WMpOvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC0XtKPWMIvPKITD-tFO5eT22-usb5Kj2hcHMPoosIJzefO8MRcbXN3wtPrkbNcKKnvX2fbUoqRHXnJi0btQDPvxBf7pKKQroq5TtUJMqnIGQPbhqt4bjPbyKMnitKv9-pP2LpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDTvbjNRabK6aKC5bL6rJabC3JRuzXU6q2bDeQN3Lqx3B2jKOKRckJn6ZfMQpQ-RBMl0vWtv4WbbvLT7johRTWqR4HncsDxonDh83KUut0-JtHCOO_hOO5hvvhn3O3MAM0MKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRIfoKLa3e; BAIDUID_BFESS=9E54F0F35E38AD6A2F51E2C7E32BAB54:FG=1; BDSFRCVID_BFESS=zn-OJexroG0m9Djjy8EjN4mYtVaDkyjTDYLEOwXPsp3LGJLVcjL2EG0Ptsi5Gcu-ox7CogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oKPyJKvDqTrP-trf5DCShUFsbtIOB2Q-XPoO3KJVbqbFMRrtDP0NjMck-p5K3I38BfbgylRp8P3y0bb2DUA1y4vp5-TrteTxoUJ2-bIhsnOGqtnWjUtebPRiJ-b9Qg-JbpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hD0wDTAWjTPVKgTa54cbb4o2WbCQ2Jnd8pcN2b5oQT8DetOBaJFOQDrw_n6wbUQHsbvwMlOUWfAkXpJvQnJjt2JxaqRCKbcdhl5jDh3MKPc0QUbte4ROJ27y0hvctb3cShPm0MjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDHt8J5kOJb3aQ5rtKRTffjrnhPF3-nLFXP6-hnjy3bRLVlb_2tIWS4b8j-cZ5hK_QMR8aq3RymJ42-39LPO2hpRjyxv4-PITD4oxJpOJ-KKtKbOaHR7WMpOvbURvDP-g3-AJQU5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoC0XtKPWMIvPKITD-tFO5eT22-usb5Kj2hcHMPoosIJzefO8MRcbXN3wtPrkbNcKKnvX2fbUoqRHXnJi0btQDPvxBf7pKKQroq5TtUJMqnIGQPbhqt4bjPbyKMnitKv9-pP2LpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDjtBDTvbjNRabK6aKC5bL6rJabC3JRuzXU6q2bDeQN3Lqx3B2jKOKRckJn6ZfMQpQ-RBMl0vWtv4WbbvLT7johRTWqR4HncsDxonDh83KUut0-JtHCOO_hOO5hvvhn3O3MAM0MKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRIfoKLa3e; delPer=0; PSINO=6; BA_HECTOR=8h0ha5ala12l858h8l0hcom01hhjdd618; ZFY=3TFf1PPaApfksksHJ8:ABLMlLqPbEgV9BI25xz:A8eZL0:C; H_PS_PSSID=36548_36463_37300_36885_37135_37317_26350_37284_37202_37232; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm",
                #         "Host": "ug.baidu.com",
                #         "Origin": "https://www.baidu.com",
                #         "Pragma": "no-cache",
                #         "Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=python%20set%20to%20dict&rsv_spt=1&oq=Object%2520of%2520type%2520set%2520is%2520not%2520JSON%2520serializable&rsv_pq=b488c0430005a38f&rsv_t=5a7fGpnymNP4wfmc950zn0jdH%2BYGc5gKyTMAKXjUnjoNwKpLAKC9aY%2BLbkJQ3s0ffFyX&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&inputT=4686&rsv_sug3=21&rsv_sug1=13&rsv_sug7=100&rsv_sug2=0&rsv_sug4=4772",
                #         "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
                #         "sec-ch-ua-mobile": "?0",
                #         "sec-ch-ua-platform": "\"macOS\"",
                #         "Sec-Fetch-Dest": "empty",
                #         "Sec-Fetch-Mode": "cors",
                #         "Sec-Fetch-Site": "same-site",
                #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
                #     },
                #     'post_data': {"invoke_info":{"pos_1":[{}],"pos_2":[{}],"pos_3":[{}]}}
                #
                #           }
                # import requests
                # result = requests.get(
                #     'https://proxy.qg.net/allocate?Key=GIWQY0ZF&Num=1&AreaId=&DataFormat=json&DataSeparator=&Detail=0').json()
                # proxy = result['Data'][0]['host']
                # header = {
                #     "Host": "sz01.imlu9.cn",
                #     "Authorization": "C6422AF4-F414-423A-A23E-B6A1FC49991E",
                #
                # }
                # datas = {"proxy": proxy}
                # result = requests.post('http://sz01.imlu9.cn/akamai', data=datas, headers=header).json()
                # cookies = result['cookie']
                # cookiestr = ""
                # for cookie in cookies:
                #     cookiestr += cookie + "=" + cookies[cookie] + ";"

                xhr_data={
                    'proxy_server':'http://',
                    'url':"https://www.ti.com/occservices/v2/ti/addtocart",
                    'headers': {
                        "authority": "www.ti.com",
                        "accept": "*/*",
                        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                        "cache-control": "no-store, must-revalidate",
                        "content-type": "application/json",
                        "expires": "0",
                        "origin": "https://www.ti.com",
                        "cookie":'ti_ua=Mozilla%2f5.0%20(Windows%20NT%2010.0%3b%20Win64%3b%20x64)%20AppleWebKit%2f537.36%20(KHTML,%20like%20Gecko)%20Chrome%2f105.0.0.0%20Safari%2f537.36; ti_bm=; bm_sz=D7F950DB91ED1D25722ACDA4193DED84~YAAQFpZUaGmO8wCDAQAASgVZMREKeaqcmcbMipQgyYxwlvXrYrGcjT6YCQnTSRmRIXK0KL+fzc4m/MljQ6zlLsn390N5SqQROfzSzWd3oCM7fdX8MWWZU7zfKL8RyU3Lu3nhgnrOiMpJu0Q7BdJhC0reA1+Qcu3girDoBvmpXWw++l6TmJnc5UDPbBSqkahCxQhKiIqkvbVdJFfqZ71h7Iz9y2aBiVHTj++v1uLQoYeqLDDJbHLF3X1Hw/9oIOGn42mxWdzzSYO55snzwev8Aol5lRpqUPNZz7/TAQ2ZZPmIcncI6lSYxSn9a6v1aMJlR/qP1NEtKQWC+tRepS2qy/KIgYuXSzsBvMm62cIbBFVC4hOehGETgH0hiA==~4343348~4535361; ti_geo=country=HK|city=WANCHAI|continent=AS|tc_ip=218.190.235.248; CONSENTMGR=ts:1662980296853%7Cconsent:true; tiSessionID=0183315990980046985c145e822c0506f001306700b3d; userType=Anonymous; _ga=GA1.2.963521944.1662980298; _gid=GA1.2.751118872.1662980298; last-domain=www.ti.com; _gat_ga_main_tracker=1; pf-accept-language=en-US; user_pref_language="en-US"; user_pref_currency="USD"; bm_mi=45B666FF52F981CB3D1A1D733E8AAED9~YAAQJ5ZUaMJDfByDAQAAQJpZMRHn9z0KoucOad4/+bxd99z4Nb+eiZYTLPTFSV9PL3MMfiPHj+wUGD5JZkRTDmzsva9NOewQqkDWWBUdGeNF/P1FlRPtyenBz/U5zdIPKX9uKRtcWqb+k/5ULaBKWi8pw//9k3j4yVbPmVXhtEUeO6aRsMpxEvfnw2fTO/WrQa9THQzbvhDpt2/YWT7qa3/cJkLXBeLuWH5FhOuKpXB0en98p5wwcO9VkForEYlVPUsMHgJjgGNV7WstP/yUdplU8leOJwxn9vKH/5r06bhjZb/W3IQe22ncTFpkf4ishwu1oq8YVuIRw+0LK4Rvz3evnyqWk4fh24Mfe9/WFXQVlLiuUfzLnoV5~1; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; pxcts=cfbb0c4d-3289-11ed-ab07-544141704a56; _pxvid=cfbb001e-3289-11ed-ab07-544141704a56; ak_bmsc=FFE7299C55896E7FC2B39D4B66530A61~000000000000000000000000000000~YAAQJ5ZUaN1DfByDAQAATKBZMRHrOculEdHdGRsavyfMGfUF1iozbwXdMLJHYx6XgrWeZWkp/S0yIq6L5gYqEVCaF4TQB5jERJsW+lw78oyU8WmbIEYXMTauaVPEy8zKxX1SJ+1yHqNA91YjQ2BObHrd732D0hayLnWyqzVC9dsRdvAaoau2+OBBhGckq9XNrxXOrxP6s5tmnSRZpUuu8nDEtXXor6EVybEKvKwovDNwIjBU3iZzZh8FH4rO3CDcqqZNIHfC+cGytY6u6BYvT000iSKDDuczLHBviWIbB0zMyypHrgxBgpobWyAcDXNiEG0SZtR6zu2/4Kih2JrvZuF5nxDPXoME0mGf79At5m99HK1VxJX2rSL1R8UsFhhjuKANoVt4al+iVgxAZW4Zju5vv4WsoVjmUfsJ18VeEUf+GHfBPkXc+qpaD63ynNWQuFepG9Nz2gEEXT0q7kmyzltkv0qSvtaT3XQHrHsN7CQcYJBXfh0chLgJYtbh1ug1pS6eREQ9rqOFjUoRM+zwGpS6TWJkbY+lz3GQ8p/atla1RDOR93bouDXJkM7OOV3abqkFNgOfHWqkriQ0NBKtKTq3DMlPv5tZSWzBZ6lQiOx6KaUkCmAt5zkEkAXxOu2eD7SyrPQ=; alias=homepageproduct; _fbp=fb.1.1662980302858.17736972; _gcl_au=1.1.1458064635.1662980303; __adroll_fpc=f8346eb3e05f7a86e9ef8559be1dd623-1662980305974; __ar_v4=%7CYKKFGS3KORGH3CRQGUQDVV%3A20220912%3A1%7CQ7HK6VQ5PZHJXGMBA6PLOE%3A20220912%3A1%7CKB7MOHQAHRBAPJH7HJPNOV%3A20220912%3A1; ak_wfSession=1662980607~id=1D/3RqKkM6s16RnoP6LOtVLAMFGRx9ZkhIdmuvT43OQ=; gpn=Non-Product; tipage=%2Fsitesearch%2Fen-us%2Fdocs%2Fsearch%20results%20-%20ti.com; tipageshort=search%20results%20-%20ti.com; ticontent=%2Fsitesearch%2Fen-us%2Fdocs; ga_page_cookie=search%20results%20-%20ti.com; ga_content_cookie=%2Fsitesearch%2Fen-us%2Fdocs; _abck=677F8681704484E5FF0599D7978E17A3~-1~YAAQJ5ZUaDFEfByDAQAA4cJZMQjsPi7qHGq3Z3OXAUUDnEATF5GI8JRkVu/NmP/QXJ2fiei4haldJCWPhXhtfV99TxB3nm3zJU15BsSP+8GO+fGHoO1Yn712MrtbYGm69g0abheCqUDXJSxb+0u0zmwChZ5GY5/TGTJ3bJK2D0I+b4N8DJvS+dRuW02D3pHZL8Y1DvVhTbmwlhjY1ASwC4gys073lbf8cBAe4OeB1Zb767J7dur6wt1tjTH0x61V6/R5tyXjFHZIVOyXVxUNWkEj3lNGygSsniTcwD26mTd/O83NMOYYcpkpKQxBpvWhDqtRss4Bx8nEWZwyaDb8pp0s1wWmUROUgS2VQL/EVQPoL/356ZNL0LF6D1LxJrGXrJ4kJYnb6ZKGARnzK1JNfbZuiPkBhjUo1rIAl+1j+e6LMezlVVrx1s+VzlQAW2gI9U4=~-1~-1~-1; _px2=eyJ1IjoiZDRhZTYyNjAtMzI4OS0xMWVkLTlhNmYtYTc5MTEyZGY2ODY2IiwidiI6ImNmYmIwMDFlLTMyODktMTFlZC1hYjA3LTU0NDE0MTcwNGE1NiIsInQiOjE2NjI5ODA2MDk5MDUsImgiOiJhMzMwNzZkMmRkODc1NDE0NWNiNGM2YmZmNTA2N2MwMWM0YmZkNTg0YmI1ZTdiMjllMTk2MWVhYTA1MDVjZmRkIn0=; _gali=searchboxheader; ELOQUA=GUID=F77A32B16F394385A432B10C1189AEF5; ABTasty=uid=a7cb7w6njtv35gsa&fst=1662980301421&pst=-1&cst=1662980301421&ns=1&pvt=4&pvis=4&th=816192.1013836.4.4.1.1.1662980303193.1662980311505.1; ABTastySession=mrasn=&sen=9&lp=https%253A%252F%252Fwww.ti.com%252Fproduct%252FTPSM8D6B24%253Fjktype%253Dhomepageproduct; utag_main=free_trial:true$_st:1662982111540$v_id:0183315990980046985c145e822c0506f001306700b3d$_sn:1$_ss:0$_pn:4%3Bexp-session$ses_id:1662980296856%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session$dc_region:ap-east-1%3Bexp-session; ti_rid=19eb6038; bm_sv=8F96F93E916E82C6F0035DC6E400E710~YAAQJ5ZUaGFEfByDAQAAFM9ZMRGoSGrNZ++8nKEbZr27P81YzbmtShwdkCidHRqiAhH5794fhUy7GpcFgFR5pt4OiNQifBn7m4fXv+IofO4fIwvVmUencdM5SInwtLkd8No0TZyy1ttSdEzxX36dmyVkMZ/bmdxw/vfEZkqexZP7W+Z0DeNUkW2ZyXSI9IM/1zUTQ/pAlFL7/irzq2Rb7iBonHV+23MNWC3lQ3QPJVv5osh9QIc33inXG1h/~1; da_sid=B3AE34D38E3DAE8050DAAA13B76721DD6E|3|0|3; da_lid=809D07E09A7DEA1BC58BBB99F5656BD6DD|0|0|0; da_intState=; _pxde=f0596bf704a88766d6954c5939ae7f53ed9ec7241f50e8',
                        "pragma": "no-cache",
                        "referer": "https://www.ti.com/sitesearch/zh-cn/docs/universalsearch.tsp?langPref=zh-CN&searchTerm=LM2576&nr=281",

                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"macOS\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                        "x-sec-clge-req-type": "ajax"
                    },
                        'post_data': {
                            "cartRequestList": [
                                {
                                    "packageOption": None,
                                    "opnId": "TPL7407LDR",
                                    "quantity": "1",
                                    "tiAddtoCartSource": "ti.com-gpnsearch",
                                    "dienCode": "",
                                    "year": "",
                                    "week": "",
                                    "batchCode": "",
                                    "pcrCode": "",
                                    "sparam": ""
                                }
                            ],
                            "currency": "USD"
                        }

                          }
                await ws.send_message(json.dumps(xhr_data))
                message = await ws.get_message()
                print('Received message: %s' % message)
                print(json.loads(message)['code'])
                print(time.time()-start_time)
                time.sleep(11111)

    except OSError as ose:
        print('Connection attempt failed: %s' % ose, file=stderr)
async def main():
    async with trio.open_nursery() as nursery:

            nursery.start_soon(new_client)


trio.run(main)