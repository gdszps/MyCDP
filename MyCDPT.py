'''
Get the title of a target web page.

To use this example, start Chrome (or any other browser that supports CDP) with
the option `--remote-debugging-port=9000`. The URL that Chrome is listening on
is displayed in the terminal after Chrome starts up.

Then run this script with the Chrome URL as the first argument and the target
website URL as the second argument:

$ python examples/get_title.py \
    ws://localhost:9000/devtools/browser/facfb2295-... \
    https://www.hyperiongray.com
'''
import json
import logging
import os
import sys
import time

import trio
from trio_cdp import open_cdp, dom, page, target,runtime,network
from Mymanager import MyChromeRemoteDebugInterface

log_level = os.environ.get('LOG_LEVEL', 'info').upper()
logging.basicConfig(level=getattr(logging, log_level))
logger = logging.getLogger('get_title')
logging.getLogger('trio-websocket').setLevel(logging.WARNING)


async def main():
    from trio_cdp import open_cdp, page, dom

    async with open_cdp('ws://127.0.0.1:9922/devtools/browser/4e62abb5-65f3-48f8-8b16-4b66e78ad9b4') as conn:
        # Find the first available target (usually a browser tab).
        targets = await target.get_targets()
        target_id = targets[0].target_id

        # # Create a new session with the chosen target.
        async with conn.open_session(target_id) as session:
            time1=time.time()
            print(await network.enable())
            result=await target.create_browser_context(proxy_server='SOCKS5://127.0.0.1:1081')

            new_headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-language": "zh-CN,zh;q=0.9",
                "cache-control": "no-cache",
                "pragma": "no-cache",
                "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"macOS\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "Cookie": "_pxvid=05b3c4be-1f64-11ed-bfd1-51675571535a; CONSENTMGR=ts:1662456185192%7Cconsent:true; tiSessionID=0183121c416c002a8970939485d005075001306d00c4e; _ga=GA1.2.14479655.1662456185; _gid=GA1.2.1459651685.1662456185; user_pref_language=\"en-US\"; user_pref_currency=\"USD\"; alias=homepageproduct; _gcl_au=1.1.1410833693.1662456206; ELOQUA=GUID=261DBEB07E43406E99403DBE90C112C8; _fbp=fb.1.1662457704903.1417970788; bm_sz=42DBC94A7D4278A46794F4B41BB37745~YAAQ1w7TF63jrAODAQAA5G+NFREgyvakIDaAlDmBZsuKPgXJYCSIQP96qcs4w6BJsukgMr5DR+4IuTy7+6f+GHnVflw2WgREqRUbbOvm0WhyGfori36z9aMLr2NmrAUuGRCWtRCXAkuIx1e6b5CPbAs5NugfBKh7uK5Zkt+lmGisGE1vWtbJY/G5t+Wb6Ep8U3gEpBuoBZKBqcXlxnqnW0CJDS/hb7MBLoeMTcw0UsXqtbmMg2DK57Jp46pn+d6XJh6Uh6qkPymd0TPcLwFax+tP0zExG9pT3QMD8xYs7TSvO9aS41cg8GL7SqMVYKz/ZtIDkeyiPElAi0Qjy7U+BoahbHfkzTRRrZwf5t/fHF2RjHROgkhCHpkj~4473392~3553586; ti_geo=country=CN|city=GUANGZHOU|continent=AS|tc_ip=163.125.128.38; ti_ua=Mozilla%2f5.0%20(Macintosh%3b%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2f537.36%20(KHTML,%20like%20Gecko)%20Chrome%2f105.0.0.0%20Safari%2f537.36; ti_bm=; userType=Anonymous; gpn=Non-Product; pf-accept-language=en-US; ak_bmsc=572BFA23C461E45882C1D5022F6979BC~000000000000000000000000000000~YAAQtAaK3rDU2/6CAQAADeoFFhFaAP26053EO5PEkIzucLesfQ+8sly0FDtVYb1O7JxAMOjfa/Y9bcZDPqQ6ue65+f125e/5Gcix7i93kyyNE+Nlp6ceW2IHIjbZztTDcf3DCXn8Fdw2nGVgQCeYvl3s6ayCzGbj1+ok15WNLktd9fxwnkxJf/a43bbCuah3s+aV51WjyEQmyihCAUEeYRVmNiwpWRtO54gkIupqihZbKv2B/3bafZUbFhLm7Cfo1LXkg7pi/H9BAS3rrVC5sSMSzGM3eY12A1qkAYLDx6Ti3e3AKFwCGXrMM3IHfPAOH2Zs4pIq/sWrNRYmzOvPQmSnJDlCKips3XHHrgr9sQ144RRAw0c3RBvbHWnkP/r/bRsQt1ER4n8Fv4skEgqDJJwFVjx1TYQGVJhvtZp7ArZNj6lzoWnK9yOPNYo+qVwYJkCfkg4mhXRYwWtRCAHC6BEwQzvAeMVtSp4V+N4u2XCibbEbngTIBg==; _gat_ga_main_tracker=1; PF=AoS8v7A5OJHYao2Yo2Kahz; tipage=%2Fauth%2Fas%2Fauthorization.oauth2-en; tipageshort=as%2Fauthorization.oauth2-en; ticontent=%2Fauth; ga_page_cookie=as%2Fauthorization.oauth2-en; ga_content_cookie=%2Fauth; ABTasty=uid=2bgzqp2cx1dyp8vc&fst=1662456188814&pst=1662513936461&cst=1662521829743&ns=3&pvt=23&pvis=2&th=816192.1013836.21.1.3.1.1662456188836.1662521829825.1_885349.1102864.1.1.1.1.1662514707580.1662514707580.1; ABTastySession=mrasn=&sen=3&lp=https%253A%252F%252Fwww.ti.com%252F; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; pxcts=5d8898d1-2e5e-11ed-a089-446a52685149; da_sid=12FC24B98E33AE8B746BAA13B7407DFC77|3|0|3; da_lid=6F461C239A7DEA06E684BB99F724FE0CA5|0|0|0; da_intState=; _px2=eyJ1IjoiNWQ2YjczYzAtMmU1ZS0xMWVkLTg3YTEtMDU1MTFjZjQ3M2Y0IiwidiI6IjA1YjNjNGJlLTFmNjQtMTFlZC1iZmQxLTUxNjc1NTcxNTM1YSIsInQiOjE2NjI1MjIxMzU3NzgsImgiOiJkODZhN2I5OGVhYjY0NWE0ZDg3ZWVkZWNiZGZhNWRmYjVlNDI3MGFlYTI2OGQ2NGQwZTFjZTY0YjE1ZWMxMGJkIn0=; utag_main=v_id:0183121c416c002a8970939485d005075001306d00c4e$_sn:3$_ss:0$_st:1662523635782$free_trial:false$dc_visit:3$_pn:2%3Bexp-session$ses_id:1662521829336%3Bexp-session$dc_event:2%3Bexp-session$dc_region:ap-northeast-1%3Bexp-session; _abck=EC59B53D6AF890945B7505AE4F21375E~-1~YAAQPi43F7stZACDAQAAuwEGFghI0g7T7nfytF/VsOCSrqQEx0rXxcv7TAeQG90ajoGaVjxrNBUL31nCE0VYjZ/dfS9ikEXUHDEVD4CHcnAqXgYQVotpRRu7y0J5PuLTN1f6zmd/o5kqKgM+gnhmUkbiSI7AxpinRXEMzDKLx+m7P9MS1qbmaoOSqF2piT5C6LdusEn5cmwQoUBSn8lJgbh3pVnlsZ/l0tC7pwf7UHMz4xryDGZdAihSDZnsKHjlI8/zdXf6lBKYFF2B5ZkY31yazKZ17XLTLJDKAH3ZiPcg55pS2jDm2xb7KHsDBye8eEpFd6U17h0ay9/EZ+YWIYcozeBGWjj0SDLE5jVBQa5cQRmT6uXU9nwpXFMDlLsR9z5UeEzQ0/K/iMUcKmoSkxLmYF4gTQIibM1glQ1YvYaEFLUGF6M7f5am/BWkJ7rThtjapssOzI9by4Ln2vSdwQ==~-1~-1~-1; ti_rid=30e3dfd; bm_sv=3777ABACB28E574946122D3A12FB65D8~YAAQtAaK3hDX2/6CAQAA8wgGFhG0x1xylauzzK6fbUyXwmnqum0cX86r3Zjck2emu3oxaNIK7vTZ7CfojMZL5f0/0ZX8iGwdZlEcbDB0Ba0urxBTcP3ctJGEjNL+/GDYNJ6VQc6hIRg9yc+8CeiV456S/4XEaXfWFUH5/TwsxCNeuKKmh206camKRg2bN49kUmscFT+pXAFGfLTxam/1lj/KgMi/clgVjetwfkOxVRQQlqwLNx8niblhTTU=~1; _pxde=73312745734bd5d60d6dfc32a35aaab73cca094af978aa14e3094f5fc4a216fe:eyJ0aW1lc3RhbXAiOjE2NjI1MjE4NDAyODgsImZfa2IiOjAsImlwY19pZCI6W10sImluY19pZCI6WyJiMmQxYWM5MTBjOTZkYzU1NDA5YTcwMmI2ZTg5N2NhNSJdfQ=="
            }
            header_args=new_headers
            assert isinstance(header_args, dict), "header_args must be a dict, passed type was %s" % (type(header_args),)

            ua = header_args.pop('User-Agent', None)
            ret_1 = None
            if ua:

                 await network.set_user_agent_override(user_agent=ua)



            await network.set_extra_http_headers(headers=header_args)

            expression=MyChromeRemoteDebugInterface().xhr_fetch("http://httpbin.org/ip")
            result=await runtime.evaluate(expression=expression,return_by_value=True)
            await target.create_target(url='https://tools.scrapfly.io/api/fp/ja3?extended=1',browser_context_id=result)
            print(time.time()-time1)
            print(result)
           # print(await target.get_browser_contexts())
            # Navigate to a website.

            async with session.page_enable():
                async with session.wait_for(page.LoadEventFired):
                    result=await page.navigate('http://httpbin.org/ip')
                    print(result)
                    # await session.execute()

                # Extract the page title.
                root_node = await dom.get_document()
                title_node_id = await dom.query_selector(root_node.node_id,'body')
                html = await dom.get_outer_html(title_node_id)

                print(html)

if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     sys.stderr.write('Usage: get_title.py <browser url> <target url>')
    #     sys.exit(1)
    trio.run(main, restrict_keyboard_interrupt_to_checkpoints=True)