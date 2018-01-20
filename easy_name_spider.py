# -*- coding:utf-8 -*-

import requests
import re
import csv
import sys
import chardet

reload(sys)
sys.setdefaultencoding('utf-8')

# print sys.getdefaultencoding()

# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding:gzip, deflate
# Accept-Language:zh-CN,zh;q=0.8
# Cache-Control:max-age=0
# Connection:keep-alive
# Host:www.yw11.com
# If-Modified-Since:Tue, 20 Jun 2017 09:24:22 GMT
# If-None-Match:W/"5948e9c6-acb3"
# Upgrade-Insecure-Requests:1


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.yw11.com',
    'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/61.0.3163.100 Safari/537.36'),
    'Cookie': ('UM_distinctid=1605f500646684-090625a1feca93-31637c00-13c680-1605f5006471f5;'
               ' bdshare_firstime=1516443807948; '
               'CNZZDATA1261714156=1810960996-1513424164-https%253A%252F%252Fwww.baidu.com%252F%7C1516442865;'
               ' Hm_lvt_401d152e19e3b99ba0d5458d826107c9=1516443794;'
               ' Hm_lpvt_401d152e19e3b99ba0d5458d826107c9=1516445088')

}

# url_surname_list = ['http://www.yw11.com/html/mi/3-{}-{}-1.htm'.format(str(i),str(y)) for i in xrange(5,509) for y in xrange(0,2)]
# url_count = url_surname_list.__len__()
#
# print url_count
#
# print url_surname_list
# url = 'http://www.yw11.com/html/mi/3-5-1-1.htm'
# res = requests.get(url, headers=headers)
# res.encoding='utf-8'


# with open('/Users/zhenwenlei/PycharmProjects/name_spider/test.html','w') as f:
#
#     f.write(res.text)
#
#
# f.close()
# name = '<ul><li>华众伊</li><li>华玮志</li><li>华裕荥</li><li>华林华</li><li>华墨翰</li><li>华知行</li><li>华海田</li><li>华增强</li><li>华兆滦</li><li>华玉乔</li><li>华为杰</li><li>华羽立</li><li>华正逵</li><li>华长清</li><li>华朗</li><li>华沁</li><li>华兴密</li><li>华云辉</li><li>华想</li><li>华静璇</li><li>华家炜</li><li>华一卓</li><li>华欣昱</li><li>华映凯</li><li>华冠雨</li><li>华原源</li><li>华天开</li><li>华淳</li><li>华天佑</li><li>华候海</li><li>华建杆</li><li>华爱芹</li><li>华漪希</li><li>华虎</li><li>华垲</li><li>华一丁</li><li>华小宝</li><li>华苏恒</li><li>华鸿朋</li><li>华明辉</li><li>华凤明</li><li>华昕睿</li><li>华淑静</li><li>华金各</li><li>华玉灵</li><li>华中伟</li><li>华骡骐</li><li>华伯京</li><li>华新</li><li>华镜铉</li><li>华晚晴</li><li>华俊砜</li><li>华子健</li><li>华小涵</li><li>华哓</li><li>华钦若</li><li>华雨蒙</li><li>华思洋</li><li>华辉</li><li>华才圣</li><li>华世尘</li><li>华兆黄</li><li>华真瑞</li><li>华延鲆</li><li>华雍</li><li>华建华</li><li>华晨晨</li><li>华颢语</li><li>华宗尧</li><li>华东鸣</li><li>华士钧</li><li>华恬</li><li>华志忠</li><li>华嘉淋</li><li>华瑜雯</li><li>华梁清</li><li>华金卡</li><li>华锦亦</li><li>华锦辉</li><li>华珂基</li><li>华光举</li><li>华儒魁</li><li>华铭彦</li><li>华溧</li><li>华守治</li><li>华旭辉</li><li>华洪萌</li><li>华烨频</li><li>华颀雁</li><li>华韬风</li><li>华凤宜</li><li>华一俏</li><li>华奕帆</li><li>华海涛</li><li>华新宇</li><li>华翔宇</li><li>华铭阳</li><li>华延杰</li><li>华瑜亮</li><li>华丰好</li><li>华思海</li><li>华锦秀</li><li>华佳举</li><li>华春秀</li><li>华天浩</li><li>华恋珏</li><li>华分</li><li>华金祝</li><li>华叶</li><li>华雪伟</li><li>华树辉</li><li>华菲鸿</li><li>华奕凡</li><li>华君心</li><li>华叶群</li><li>华家世</li><li>华骁</li><li>华瀚淳</li><li>华启恒</li><li>华广川</li><li>华明贻</li><li>华樟珂</li><li>华勉毅</li><li>华恒运</li><li>华冰岍</li><li>华必秀</li><li>华虹仙</li><li>华昱皤</li><li>华德咏</li><li>华小明</li><li>华祖衡</li><li>华显运</li><li>华刚瑞</li><li>华炜林</li><li>华超然</li><li>华雨沛</li><li>华诗国</li><li>华晕</li><li>华尧</li><li>华四海</li><li>华竹蕙</li><li>华晓甜</li><li>华德康</li><li>华铭圣</li><li>华红香</li><li>华雅</li><li>华音</li><li>华思理</li><li>华群联</li><li>华秀月</li><li>华佳羽</li><li>华璇</li><li>华荣春</li><li>华辰斐</li><li>华熙恬</li><li>华盈</li><li>华云诗</li><li>华雨舒</li><li>华渐</li><li>华疏桐</li><li>华殷明</li><li>华广森</li><li>华庆龙</li><li>华正辉</li><li>华鑫泳</li><li>华清雯</li><li>华春生</li><li>华天韵</li><li>华飞扬</li><li>华俊良</li><li>华誉哲</li><li>华筱静</li><li>华之盛</li><li>华汀兰</li><li>华曜</li><li>华标</li><li>华麟雅</li><li>华浩</li><li>华一卜</li><li>华音</li><li>华成帅</li><li>华汶均</li><li>华东军</li><li>华成日</li><li>华辉耀</li><li>华哲培</li><li>华昭和</li><li>华延生</li><li>华重发</li><li>华玺</li><li>华金勇</li><li>华彩云</li><li>华凤莲</li><li>华艺萱</li><li>华华阳</li><li>华得珂</li><li>华爱珍</li><li>华司凝</li><li>华新莲</li><li>华立欣</li><li>华梦林</li><li>华珂云</li><li>华洛达</li><li>华增国</li><li>华菲菲</li><li>华秋亦</li><li>华天</li><li>华延琨</li><li>华飞浪</li><li>华长康</li><li>华永宏</li><li>华俊宇</li><li>华锋</li><li>华睿甫</li><li>华鸣洲</li><li>华颂疑</li><li>华学维</li><li>华自然</li><li>华晓祺</li><li>华淑桐</li><li>华明兴</li><li>华永华</li><li>华辉明</li><li>华一涵</li><li>华苋植</li><li>华波</li><li>华睫汶</li><li>华泓鹏</li><li>华旭亮</li><li>华天志</li><li>华红兵</li><li>华兴辉</li><li>华晨熙</li><li>华文曦</li><li>华彦一</li><li>华小莲</li><li>华乐宸</li><li>华义熙</li><li>华又今</li><li>华轩毅</li><li>华礼松</li><li>华健君</li><li>华仿淹</li><li>华家宝</li><li>华辰坤</li><li>华玉羚</li><li>华成锐</li><li>华凝可</li><li>华松</li><li>华一飞</li><li>华君平</li><li>华晓锋</li><li>华韧</li><li>华昌旺</li><li>华裕甜</li><li>华沐尔</li><li>华立洹</li><li>华子璇</li><li>华斯源</li><li>华晗斐</li><li>华越儿</li><li>华煜溥</li><li>华天豪</li><li>华景云</li><li>华于清</li><li>华英杰</li><li>华煊楠</li><li>华文斌</li><li>华佳祥</li><li>华晋豪</li><li>华晓龙</li><li>华一依</li><li>华鹏举</li><li>华俊峰</li><li>华敬依</li><li>华子凝</li><li>华屹川</li><li>华利剑</li><li>华轩亚</li><li>华广恩</li><li>华海贺</li><li>华襻</li><li>华乙遵</li><li>华子涵</li><li>华嘉猷</li><li>华皓静</li><li>华玉铭</li><li>华宇爨</li><li>华泓木</li><li>华文辉</li><li>华思溢</li><li>华欣蔚</li><li>华衫杉</li><li>华建辉</li><li>华俊尧</li><li>华小浩</li><li>华遵滨</li><li>华莲翔</li><li>华海海</li><li>华景和</li><li>华狄潇</li><li>华紫藤</li><li>华俊霖</li><li>华伯仑</li><li>华慕军</li><li>华振修</li><li>华涌铭</li><li>华馥</li><li>华海</li><li>华曼荻</li><li>华芳雷</li><li>华枚岩</li><li>华凯</li><li>华嘉璐</li><li>华家乐</li><li>华意圆</li><li>华金皇</li><li>华馨</li><li>华奕恬</li><li>华随心</li><li>华胜涛</li><li>华玉臻</li><li>华爱友</li><li>华甜甜</li><li>华希心</li><li>华锦芸</li><li>华皓坛</li><li>华有明</li><li>华树玮</li><li>华钰茵</li><li>华子昂</li><li>华泽宇</li><li>华宇浩</li><li>华小湄</li><li>华天懿</li><li>华家祯</li><li>华坤洲</li><li>华唯晋</li><li>华艺灵</li><li>华牧</li><li>华浏</li><li>华青勇</li><li>华茂辉</li><li>华炜</li><li>华慈心</li><li>华慧分</li><li>华云松</li><li>华庆华</li><li>华瑞熙</li><li>华睿翔</li><li>华煜希</li><li>华昊走</li><li>华俊皓</li><li>华晓全</li><li>华博亮</li><li>华鸿昌</li><li>华环肖</li><li>华如馨</li><li>华优靖</li><li>华正德</li><li>华文浩</li><li>华卓</li><li>华嘉俊</li><li>华润</li><li>华艺浠</li><li>华壹伊</li><li>华月鸣</li><li>华政彤</li><li>华雳锋</li><li>华逸</li><li>华欣译</li><li>华乾国</li><li>华羽柔</li><li>华沁业</li><li>华珏海</li><li>华三元</li><li>华馨月</li><li>华伟</li><li>华东操</li><li>华文欣</li><li>华韶熙</li><li>华天东</li><li>华丫头</li><li>华军豪</li><li>华金子</li><li>华美静</li><li>华佳佳</li><li>华通</li><li>华怀元</li><li>华文菁</li><li>华靖伟</li><li>华顺菲</li><li>华宇然</li><li>华炳海</li><li>华乾元</li><li>华巨贤</li><li>华慧凌</li><li>华竞</li><li>华呈</li><li>华建明</li><li>华雅心</li><li>华渊睿</li><li>华泓德</li><li>华崇伟</li><li>华逸华</li><li>华金炎</li><li>华峻鹜</li><li>华陈晶</li><li>华嘉铭</li><li>华峻萧</li><li>华凡佳</li><li>华咏诗</li><li>华静明</li><li>华少泽</li><li>华永超</li><li>华文冰</li><li>华一翔</li><li>华振启</li><li>华玉道</li><li>华宜南</li><li>华辉</li><li>华创辉</li><li>华中源</li><li>华翊楦</li><li>华齐</li><li>华晓康</li><li>华地主</li><li>华永华</li><li>华鑫岩</li><li>华朝利</li><li>华学俭</li><li>华董国</li><li>华晓光</li><li>华万力</li><li>华湛熙</li><li>华怀予</li><li>华宝书</li><li>华子翰</li><li>华远铭</li><li>华骐瑞</li><li>华千乔</li><li>华泠冶</li><li>华昌宏</li><li>华增袈</li><li>华枫濠</li><li>华和</li><li>华秋蕊</li><li>华诗峰</li><li>华奕龙</li><li>华古杨</li><li>华江</li><li>华铂承</li><li>华绎桑</li><li>华文潇</li><li>华欣越</li><li>华佩穗</li><li>华则桦</li><li>华芷轩</li><li>华振兴</li><li>华宇彤</li><li>华凡</li><li>华延虎</li><li>华舰锋</li><li>华羽航</li><li>华青青</li><li>华熔</li><li>华德眚</li><li>华卜拮</li><li>华亦</li><li>华钧涵</li><li>华萌</li><li>华堰菲</li><li>华嘉滔</li><li>华培智</li><li>华永会</li><li>华春盈</li><li>华杨眉</li><li>华晓军</li><li>华湾炽</li><li>华炳苏</li><li>华一依</li><li>华振强</li><li>华国凯</li><li>华妃海</li><li>华哲睿</li><li>华朝辉</li><li>华佳熙</li><li>华涵瑞</li><li>华凯东</li><li>华绎理</li><li>华毅琛</li><li>华昌威</li><li>华靖初</li><li>华蜜月</li><li>华欢</li><li>华伊涵</li><li>华冬阳</li><li>华雨田</li><li>华芸曳</li><li>华仰政</li><li>华雯</li><li>华尔权</li><li>华慧钰</li><li>华卫祥</li><li>华芝功</li><li>华海</li><li>华子皓</li><li>华清源</li><li>华展琨</li><li>华永哲</li><li>华泽远</li><li>华东南</li><li>华宏凯</li><li>华玺宇</li><li>华方鸣</li><li>华泳</li><li>华金耀</li><li>华振宁</li><li>华江</li><li>华泓帆</li><li>华雪晗</li><li>华纯鑫</li><li>华麦尼</li><li>华孜默</li><li>华健</li><li>华新辉</li><li>华雨彤</li><li>华栩匀</li><li>华大珍</li><li>华炳坚</li><li>华宏伟</li><li>华联典</li><li>华嘉汝</li><li>华艳华</li><li>华兴端</li><li>华健羽</li><li>华天数</li><li>华文斌</li><li>华天霖</li><li>华汉民</li><li>华东泽</li><li>华振雄</li><li>华扬轩</li><li>华同杨</li><li>华麟骓</li><li>华千斌</li><li>华益飞</li><li>华广成</li><li>华献平</li><li>华明吉</li><li>华自胜</li><li>华人馨</li><li>华钰渝</li><li>华韵</li><li>华庄周</li><li>华宇飞</li><li>华军豪</li><li>华光华</li><li>华维令</li><li>华翰</li><li>华智国</li><li>华民杰</li><li>华典宏</li><li>华晨日</li><li>华仲达</li><li>华君秀</li><li>华俊达</li><li>华梃埕</li><li>华新鸿</li><li>华凯中</li><li>华力军</li><li>华维进</li><li>华蔓天</li><li>华晨飞</li><li>华于</li><li>华微</li><li>华行健</li><li>华庄达</li><li>华书豪</li><li>华巍</li><li>华海元</li><li>华清淳</li><li>华依欣</li><li>华汉图</li><li>华碧异</li><li>华培佐</li><li>华湘林</li><li>华书娴</li><li>华天毅</li><li>华晟</li><li>华明安</li><li>华毅博</li><li>华宗培</li><li>华笔浈</li><li>华书昊</li><li>华小曼</li><li>华姝七</li><li>华四</li><li>华军邦</li><li>华淞任</li><li>华建国</li><li>华亨心</li><li>华天泽</li><li>华茗</li><li>华嘉强</li><li>华育桓</li><li>华丹</li><li>华宇凯</li><li>华鸿毅</li><li>华俞臣</li><li>华三</li><li>华天龙</li><li>华瑾逸</li><li>华翔丞</li><li>华海</li><li>华国泽</li><li>华志健</li><li>华忠荣</li><li>华长明</li><li>华泽鑫</li><li>华八</li><li>华武帆</li><li>华恬艺</li><li>华颍</li><li>华昂昂</li><li>华哲枫</li><li>华焱硕</li><li>华玉然</li><li>华美萱</li><li>华爱兰</li><li>华盛</li><li>华朋昌</li><li>华士骐</li><li>华利馕</li><li>华锡祥</li><li>华阳</li><li>华素云</li><li>华海芷</li><li>华宇聪</li><li>华雪云</li><li>华亚林</li><li>华枞俊</li><li>华彦冰</li><li>华萧晋</li><li>华雪煤</li><li>华欣宜</li><li>华有忠</li><li>华福和</li><li>华奕另</li><li>华安临</li><li>华仪</li><li>华美田</li><li>华城龙</li><li>华明飞</li><li>华日润</li><li>华灵儿</li><li>华熹起</li><li>华焉丹</li><li>华洋堋</li><li>华楠宣</li><li>华贝宁</li><li>华誉宇</li><li>华安棋</li><li>华雨晨</li><li>华秀</li><li>华晓渲</li><li>华玺如</li><li>华灵儿</li><li>华琮灵</li><li>华杨</li><li>华欣辰</li><li>华曾珍</li><li>华幼民</li><li>华柳吟</li><li>华家旭</li><li>华信成</li><li>华思雄</li><li>华祁炜</li><li>华方泉</li><li>华佳楠</li><li>华永南</li><li>华鱼超</li><li>华智奇</li><li>华晖鹰</li><li>华韦诣</li><li>华肇泽</li><li>华韦驿</li><li>华洲</li><li>华栗廷</li><li>华祖迪</li><li>华仕友</li><li>华琼敏</li><li>华锦宛</li><li>华春桃</li><li>华武沽</li><li>华亦枫</li><li>华广野</li><li>华邵涵</li><li>华汶妤</li><li>华子晨</li><li>华境</li><li>华熠浩</li><li>华超</li><li>华才</li><li>华道宽</li><li>华珏骝</li><li>华哲新</li><li>华汛</li><li>华接舆</li><li>华雯琦</li><li>华思雨</li><li>华子惠</li><li>华言旭</li><li>华天程</li><li>华晓薇</li><li>华语辰</li><li>华嘉嘉</li><li>华继群</li><li>华语秀</li><li>华韬</li><li>华宇杨</li><li>华昕艺</li><li>华禹茜</li><li>华夏成</li><li>华笙桐</li><li>华进进</li><li>华树利</li><li>华浩为</li><li>华霖钦</li><li>华建冬</li><li>华淞超</li><li>华五</li><li>华心逸</li><li>华启标</li><li>华昀科</li><li>华英杰</li><li>华国翊</li><li>华珂宁</li><li>华效雨</li><li>华雪原</li><li>华蕾</li><li>华恪敏</li><li>华廷耀</li><li>华翌华</li><li>华剑君</li><li>华永康</li><li>华若雨</li><li>华德窿</li><li>华财维</li><li>华正买</li><li>华锌童</li><li>华和杰</li><li>华红名</li><li>华熙</li><li>华志伟</li><li>华盈水</li><li>华思力</li><li>华晟德</li><li>华荣清</li><li>华孝良</li><li>华幸福</li><li>华翔</li><li>华永睿</li><li>华欣磊</li><li>华弋然</li><li>华思宏</li><li>华孟华</li><li>华皓煊</li><li>华作语</li><li>华苹</li><li>华壹</li><li>华晓棠</li><li>华寓玺</li><li>华枭翰</li><li>华广伟</li><li>华熠桐</li><li>华连淼</li><li>华一俊</li><li>华压政</li><li>华秀清</li><li>华茉芹</li><li>华加罗</li><li>华钧翔</li><li>华建兵</li><li>华贤熙</li><li>华沂海</li><li>华鼎原</li><li>华瑞委</li><li>华米西</li><li>华小祥</li>><li>华可帆</li><li>华艺华</li><li>华平安</li><li>华福凯</li><li>华严烽</li><li>华诺喏</li><li>华德海</li><li>华兴芝</li><li>华靖一</li><li>华子涵</li><li>华以芝</li><li>华辉</li><li>华巧珍</li><li>华欣然</li><li>华色音</li><li>华珊燃</li><li>华琼豫</li><li>华金</li><li>华海洋</li><li>华依昕</li><li>华一川</li><li>华驰</li><li>华玮萱</li><li>华洪峙</li><li>华宗晖</li><li>华刚武</li><li>华朝</li><li>华南天</li><li>华保淳</li><li>华雨露</li><li>华家彬</li><li>华玟宇</li><li>华乙鸾</li><li>华智潇</li><li>华少清</li><li>华卓豪</li><li>华明涛</li><li>华文婉</li><li>华雄海</li><li>华思蓓</li><li>华昊谦</li><li>华秦源</li><li>华泽宇</li><li>华英顺</li><li>华炎坤</li><li>华欣桐</li><li>华雅奇</li><li>华威仁</li><li>华江源</li><li>华奕凡</li><li>华惟迎</li><li>华绍伯</li></ul>'

# p =re.findall('<div class="listbox1_text">.*?<ul>(.*?)</ul>',res.text,re.S)

with open('/Users/zhenwenlei/PycharmProjects/name_spider/test.html','r') as f:
    p = f.read()

# print chardet.detect(p)
# print p

# test = 'rinimei王满ni干你吗mab'
#
# pt = re.compile('王满')
#
# mc = re.search(pt,'wangman王满xxsawe王斌').group()
# mc = re.match(pt,'王满xxsawe王斌').group()

sc = re.search('<div class="listbox1_text">.*?<ul>(.*?)</ul>',p,re.S).group()
name_list = re.findall('<li>(.*?)</li>',sc,re.S)

with open('/Users/zhenwenlei/PycharmProjects/name_spider/test.html','w') as f:
    

# print name

# print p
# name_list = re.findall('<ul>',p)
# print name_list

# print name_list

# for i in name_list:
#     n = i.decode('utf-8')
#     print n

# name = re.findall('<ul><li>(.*?)</li></ul>',res.text)

# print name_list
