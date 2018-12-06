# -*- coding:utf-8 -*-

import scrapy,re
import requests,os

class KugouSpider(scrapy.Spider):
    name='kugou_music'
    allowed_domains=[]
    # start_urls=['https://songsearch.kugou.com/song_search_v2?callback=jQuery1124011972861619385089_1543541339021&keyword=%E5%BC%A0%E6%9D%B0&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0']

    def start_requests(self):
        key=input('请输入想要爬取的歌手名：')
        url='https://songsearch.kugou.com/song_search_v2?callback=jQuery1124011972861619385089_1543541339021&keyword='+key+'&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0'
        yield scrapy.Request(url,self.parse)

    def parse(self, response):
        # print(response.text)
        # songnames=re.findall('"SongName":"(.*?)"',response.text)
        # songname=list(set(songnames))

        filehash=re.findall('"FileHash":"(.*?)"',response.text)
        for file in filehash:
            hash_url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash='+file
            # print(hash_url)
            yield scrapy.Request(hash_url,self.play)
    def play(self, response):
        names=re.findall('"audio_name":"(.*?)"',response.text)[0]
        name=names.encode('utf-8').decode('unicode-escape')
        print(name)   #歌曲名字
        play_url = re.findall('"play_url":"(.*?)"', response.text)
        url = ''.join(play_url).replace('\\', '')  # 下载地址
        print(url)
        # play = requests.get(url)
        # with open(+name+'.mp3','wb')as f:
        #     f.write(play.content)
        # path = './kg_music/‪'
        # if os.path.exists(path):
        #     pass
        # else:
        #     os.mkdir(path)
        # with open('./kg_music/'+name+'.mp3','wb')as f:
        #     f.write(play.content)

        # k = 0
        # for i in name:
        #     k += 1
        #     print('{0}:{1}'.format(k, i))
        # xuanze=int(input('请输入想要下载的歌曲编号：'))




