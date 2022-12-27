import requests
import re

session = requests.Session()
headers = {"token": "b82cc3e24ca14335a4a32c2ba1f904991672115417766token"}

sent_list = []
print('')
with open('novel.txt', 'r', encoding='utf-8')as fp:
    sent_list = re.split('。|！|？|；|——', fp.read())


order=8
for sent in sent_list[order*100:(order+1)*100]:
    # text = '她是叶哲泰的女儿叶文洁'
    sent = sent.replace('\t', '').replace('\n', '').replace('“', '').replace('”', '').replace(' ', '').replace('‘', '').replace('’', '')
    body = {'text': sent}
    response = session.post("http://comdo.hanlp.com/hanlp/v1/ner/chineseName", data=body, headers=headers).json()
    p1, p2 = None, None
    if 'msg' in response and response['msg'] == 'token is stop use!':
        print('TOKEN EXPIRED')
        break
    if 'code' in response and response['code'] == 0 and 'data' in response:
        for item in response['data']:
            if item['nature'] == 'nr':
                if p1 == None:
                    p1 = item['word']
                elif p2 == None:
                    p2 = item['word']
                else:
                    break
        if p1 != None and p2 != None:
            print(p1, p2, sent)

session.close()

# body = {'text': '杨铁心见一壶酒已喝完了，又要了一壶，三人只是痛骂秦桧'}
# print(session.post("http://comdo.hanlp.com/hanlp/v1/ner/chineseName", data=body, headers=headers).json())
