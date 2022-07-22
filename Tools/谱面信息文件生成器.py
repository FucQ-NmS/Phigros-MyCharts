#==========================================
#|      针对RPE编辑器生成的ZIP自制谱文件    |
#|      转换为@lzhch3473的Phigros模拟器    |
#|      可以读取的info.csv和line.csv       |
#|                                        |
#|             @属官一号 编写              |
#==========================================
import os
import json
import sys

charts_data = {}
# charts_path = input("请输入谱面文件（JSON文件）路径：")
# music_path = input("请输入音乐文件路径：")
# pictures_path = input("请输入曲封图片文件路径：")
charts_path = os.path.abspath(input("请输入谱面项目文件夹路径："))
if os.path.exists(charts_path) == False or os.path.isdir(charts_path) == False:
    print('路径不存在或者无效！')
    input('')
    sys.exit(0)

lines_data = []
info_data = []
lines_count = 0
count = 0

with open(charts_path+'\\info.txt','r',encoding='utf-8') as f:
    info_data = f.read().replace('#','').replace('\nName: ','').replace('\nPath: ','||').replace('\nSong: ','||').replace('\nPicture: ','||').replace('\nChart: ','||').replace('\nLevel: ','||').replace('\nComposer: ','||').replace('\nCharter: ','||').replace('\n','')
    info_data = info_data.split('||')

    print('info.txt读取成功。')

with open('.\\info.csv','w+',encoding='utf-8') as f:
    f.write('Chart,Music,Image,AspectRatio,ScaleRatio,GlobalAlpha,Name,Level,Illustrator,Designer\n谱面,音乐,图片,宽高比,按键缩放,背景变暗,名称,等级,曲绘,谱师\n')

    f.write(info_data[4]+','+info_data[2]+','+info_data[3]+',1.777778,8.00E+03,0.6,'+info_data[0]+','+info_data[5]+','+info_data[6]+','+info_data[7]+'\n\n\n')

with open(charts_path+'\\'+info_data[4],'r',encoding='utf-8') as c:
    charts_data = json.load(c)
    lines_data = charts_data['judgeLineList']
    lines_count = len(lines_data)

    print('谱面项目文件读取成功。')

with open('.\\line.csv','w+',encoding="utf-8") as f:
    f.write('Chart,LineId,Image,Vert,Horz,IsDark\n谱面,判定线id,图片,垂直宽度,水平拉伸,跟随背景变暗\n')

    print('\nline.csv中的“垂直高度”的默认值因模拟器的Bug，因此取0.21。\n但仍需自己调试其数值。\n')
    print('line.csv中的“跟随背景变暗”的默认值因模拟器的Bug，因此取255。\n更改其值将导致判定线无法显示。\n')
    for line_data in lines_data:
        if line_data['Texture'] == 'line.png':
            count += 1
            continue
        else:
            f.write(info_data[4]+','+str(count)+','+line_data['Texture']+',0.21,1.042,255\n')
        count += 1

    f.write('\n\n')

print('完成')
input('')