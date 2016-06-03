# bilibilib
python - bilibili - lib

( ゜- ゜)つロ 乾杯~ - 










[2016.6.3]
bilibili.py:登录、获取动态和发送评论

      |-登录：Login():登录，无需验证码
      
      |-获取动态:getOneDynamic(up),根据Up主mid码获取最新的视频AV号
      
      |-发送评论：addConment(av)，根据AV号发表评论
      
      |-设置回复：setMessage()，设置评论，可为中文
      

bilibilisofa.py:抢沙发脚本

      |-upDict字典：设置Up主mid和名称，格式'mid':'名称'，如upDict={'221648':'柚子木','883968':'暴走漫画'}
      
      |-delayTime:设置爬取动态时间间隔，单位秒
