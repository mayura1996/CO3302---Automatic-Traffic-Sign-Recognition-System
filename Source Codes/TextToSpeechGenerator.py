from gtts import gTTS
import os

signList = ['roundabout ahead', 'maximum speed 50', 'maximum speed 70', 'railway crossing ahead', 'school zone',
            'stop sign',
            'pedestrian crossing ahead', 'curve left', 'curve right', 'no u turn', 'give way']
i = 0
for x in signList:
    tts = gTTS(x, lang='en')
    tts.save(str(i) + '.mp3')
    print("done")
    i = i + 1

# for i in range(15):
#     os.system('mpg123 /home/manawadu/PycharmProjects/untitled/'+str(i)+'.mp3')


# signListSin = ['ඉදිරියෙන් වටරවුමක්', 'උපරිම වේගය පැයට කිලෝමීටර් 50 කි',
#                'උපරිම වේගය පැයට කිලෝමීටර 70 කි', 'දුම්රිය හරස් මාර්ගය ඉදිරියෙන්','පාසල් කලාපය ඉදිරියෙන්', 'නැවතුම් ලකුණ',
#                'ඉදිරියෙන් පදික මාරුව','ඉදිරියෙන් දකුණට වංගුවක් තිබේ', 'ඉදිරියෙන් වමට වංගුවක් තිබේ','යූ-හැරීම් තහනම්', 'ඉඩ දෙන්න']
#
# i=0
# for x in signListSin:
#     tts = gTTS(x, lang='si')
#     tts.save(str(i)+'SI.mp3')
#     print("done")
#     i=i+1

# for i in range(11):
#      os.system('mpg123 /home/manawadu/PycharmProjects/untitled/'+str(i)+'SI.mp3')



# signListTA = ['சுற்றுவட்டம் முன்னால்', 'அதிகூடிய வேக எல்லை 50', 'அதிகூடிய வேக எல்லை 70', 'புகையிரதக் கடவை முன்னால்',
#               'பாடசாலை வலயம்', 'நிறுத்து', 'பாதசாரிகள் கடவை முன்னால்', 'வளைவு வலப்புறம்', 'வளைவு இடப்புறம்',
#               'U வளைவு தடை', 'வழி விடு']
#
#
# i = 0
# for x in signListTA:
#     tts = gTTS(x, lang='ta')
#     tts.save(str(i) + 'TA.mp3')
#     print("done")
#     i = i + 1

# for i in range(16):
#     os.system('mpg123 /home/manawadu/PycharmProjects/untitled/' + str(i) + 'TA.mp3')
#
# # m="i am mayura"
# # tts = gTTS(m, lang='en')
# # tts.save('hello.mp3')
