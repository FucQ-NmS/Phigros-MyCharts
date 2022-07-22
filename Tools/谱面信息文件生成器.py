#==========================================
#|      针对RPE编辑器生成的ZIP自制谱文件    |
#|      转换为@lzhch3473的Phigros模拟器    |
#|      可以读取的info.csv和line.csv       |
#|                                        |
#|             @属官一号 编写              |
#==========================================

import json

charts_data = {}
# charts_path = input("请输入谱面文件（JSON文件）路径：")
# music_path = input("请输入音乐文件路径：")
# pictures_path = input("请输入曲封图片文件路径：")
lines_data = []
info_data = []
lines_count = 0
count = 0

with open(input("请输入谱面项目文件（JSON文件）路径："),'r',encoding='utf-8') as c:
    charts_data = json.load(c)
    lines_data = charts_data['judgeLineList']
    lines_count = len(lines_data)

with open(input('请输入info.txt路径：'),'r',encoding='utf-8') as f:
    info_data = f.read().replace('#','').replace('\nName: ','').replace('\nPath: ','||').replace('\nSong: ','||').replace('\nPicture: ','||').replace('\nChart: ','||').replace('\nLevel: ','||').replace('\nComposer: ','||').replace('\nCharter: ','||').replace('\n','')
    info_data = info_data.split('||')

with open('.\\info.csv','w+',encoding='utf-8') as f:
    f.write('Chart,Music,Image,AspectRatio,ScaleRatio,GlobalAlpha,Name,Level,Illustrator,Designer\n谱面,音乐,图片,宽高比,按键缩放,背景变暗,名称,等级,曲绘,谱师\n')

    f.write(info_data[4]+','+info_data[2]+','+info_data[3]+',1.777778,8.00E+03,0.6,'+info_data[0]+','+info_data[5]+','+info_data[6]+','+info_data[7]+'\n\n\n')

with open('.\\line.csv','w+',encoding="utf-8") as f:
    f.write('Chart,LineId,Image,Vert,Horz,IsDark\n谱面,判定线id,图片,垂直宽度,水平拉伸,跟随背景变暗\n')

    for line_data in lines_data:
        if line_data['Texture'] == 'line.png':
            count += 1
            continue
        else:
            f.write(info_data[4]+','+str(count)+','+line_data['Texture']+',0.008,1.042,255\n')
        count += 1

    f.write('\n\n')

print('完成')