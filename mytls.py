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

import time


import trio
from trio_cdp import open_cdp, dom, page, target,runtime,network,fetch
from Mymanager import MyChromeRemoteDebugInterface
from trio_websocket import serve_websocket, ConnectionClosed




class my_tls:


    async def setHeader(self,header):
        try:

            if "Content-Length" in header:
                header.pop("Content-Length")
            if "content-length" in header:
                header.pop("content-length")

            if "Host" in header:
                header.pop("Host")




            header_args = header
            assert isinstance(header_args, dict), "header_args must be a dict, passed type was %s" % (
                type(header_args),)

            ua = header_args.pop('User-Agent', None)
            if ua:
                await network.set_user_agent_override(user_agent=ua)

            await network.set_extra_http_headers(headers=network.Headers(header_args))
            return header
        except:
            raise 'setHeader Error'
            return False



    async def getIp(self, proxy_server,ws,xhr_data):
        conn=self.conn
        time1 = time.time()

        browserContextId = await target.create_browser_context()

        newtargetid = await target.create_target(url="ti.com", browser_context_id=browserContextId)

        async with conn.open_session(newtargetid) as session:
            await network.enable()

            print(time.time() - time1)

            # async for event in session.listen(network.RequestWillBeSent):
            #     print("got event", event)

            header=await self.setHeader(xhr_data['headers'])
            expression = MyChromeRemoteDebugInterface().xhr_fetch(url=xhr_data['url'],headers=header,post_data=json.dumps(xhr_data.get('post_data')),post_type=xhr_data.get('Content-Type'))

            result = await runtime.evaluate(expression=expression, return_by_value=True)

            # async for event in session.listen(network.RequestWillBeSent):
            #     print("got event", event)
            await  target.dispose_browser_context(browserContextId)
            try:
                result=result[0].value
                #print(eval(result['response'])['origin'])

                await ws.send_message(json.dumps(result))
            except Exception as e:
                print('error')




    async def echo_server(self,request):
        ws = await request.accept()

        while True:
            try:
                async with trio.open_nursery() as nursery:
                    xhr_data = await ws.get_message()
                    xhr_data=json.loads(xhr_data)
                    # xhr_data['headers']=await  self.filterHeader(xhr_data['headers'])
                    nursery.start_soon(self.getIp,xhr_data['proxy_server'], ws,xhr_data)
                    #await self.getIp(message,request)

                #time.sleep(1)
            except ConnectionClosed:
                break

    async def main(self):
        async with open_cdp('ws://127.0.0.1:9922/devtools/browser/31be28be-7893-45b6-bf62-ead0e929a84d') as conn:
            self.conn=conn
            await serve_websocket(self.echo_server, '0.0.0.0', 8000, ssl_context=None)
        # async with open_cdp('ws://127.0.0.1:9922/devtools/browser/8699199f-2309-4f5e-a341-58468e0e55f2') as conn:
        # async with trio.open_nursery() as nursery:
        #     for i in range(100):
        #         #proxy=requests.get('http://api.shenlongip.com/ip?key=hqyf7y7c&pattern=txt&count=1&protocol=1&sign=26b54d03bf1c761d90a25d944ecffc1b').text.strip()
        #         print(nursery.start_soon(getIp, conn,'HTTP://'))

        # await getIp(conn,'HTTP://' )

if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     sys.stderr.write('Usage: get_title.py <browser url> <target url>')
    #     sys.exit(1)

    trio.run(my_tls().main, restrict_keyboard_interrupt_to_checkpoints=True)
