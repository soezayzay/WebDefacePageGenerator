import os,sys
os.system("clear")
#coder : $0ul
#date  : 14/2/2022
banner = """
                 \033[1;41m\033[1;37m Web Deface Page Generator \033[0m\033[1;32m
          ────────────────────────────────────────
          ─────────────▄▄██████████▄▄─────────────
          ─────────────▀▀▀───██───▀▀▀─────────────
          ─────▄██▄───▄▄████████████▄▄───▄██▄─────
          ───▄███▀──▄████▀▀▀────▀▀▀████▄──▀███▄───
          ──████▄─▄███▀──────────────▀███▄─▄████──
          ─███▀█████▀▄████▄──────▄████▄▀█████▀███─
          ─██▀──███▀─██████──────██████─▀███──▀██─
          ──▀──▄██▀──▀████▀──▄▄──▀████▀──▀██▄──▀──
          ─────███───────────▀▀───────────███─────
          ─────██████████████████████████████─────
          ─▄█──▀██──███───██────██───███──██▀──█▄─
          ─███──███─███───██────██───███▄███──███─
          ─▀██▄████████───██────██───████████▄██▀─
          ──▀███▀─▀████───██────██───████▀─▀███▀──
          ───▀███▄──▀███████────███████▀──▄███▀───
          ─────▀███────▀▀██████████▀▀▀───███▀─────
          ───────▀─────▄▄▄───██───▄▄▄──────▀──────
          ──────────── ▀▀███████████▀▀ ────────────
          ────────────────────────────────────────
                       \033[1;41m\033[1;37m Author : $0ul \033[0m\033[1;32m          
\033[0m      
"""
print(banner)
#main 
def main():
    file_name = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter File Name        \033[1;32m:\033[1;37m ")
    path = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter File Path        \033[1;32m:\033[1;37m ")
    title = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Title            \033[1;32m:\033[1;37m ")
    alert = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mAlert message          \033[1;32m:\033[1;37m ")
    img = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Your Logo        \033[1;32m:\033[1;37m ")
    bg_img = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Background Image \033[1;32m:\033[1;37m ")
    heading = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Heading          \033[1;32m:\033[1;37m ")
    message = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Message          \033[1;32m:\033[1;37m ")
    message_img = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Image Message    \033[1;32m:\033[1;37m ")
    bg_song = input(" \033[1;34m[\033[1;31m+\033[1;34m] \033[1;33mEnter Background Song  \033[1;32m:\033[1;37m ")
    file = open(file_name,"a")
    file.write('<!DOCTYPE html>')
    file.write('\n')
    file.write('<html lang="en">')
    file.write('\n')
    file.write(f"<title>{title}</title>")
    file.write("\n")
    file.write('<meta charset="utf-8">')
    file.write('\n')
    file.write('<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">')
    file.write('\n')
    file.write('<style>')
    file.write('\n')
    file.write('body{background:#000;background-image:url("'+bg_img+'");}')
    file.write('\n')
    file.write('@keyframes colorchange{')
    file.write('\n')
    file.write('25%{color:red}')
    file.write('\n')
    file.write('50%{color:#000}')
    file.write('\n')
    file.write('75%{color:#fff}')
    file.write('\n')
    file.write('100%{color:#000}')
    file.write('\n')
    file.write('}')
    file.write('\n')
    file.write('#heading{text-align:center;font-size:20px;color:red;animation-name:colorchange;animation-duration:8s;animation-iteration-count:infinite;}')
    file.write('\n')
    file.write('.logo{width:200px;height:200px;border-radius:100%;display:block;margin-left:auto;margin-right:auto;border:1px solid #fff;}')
    file.write('\n')
    file.write('.message_box{display:block;margin-left:auto;margin-right:auto;height:320px;width:320px;border:1px solid #fff;border-radius:5px;margin-top:10px;}')
    file.write('\n')
    file.write('.title{text-align:center;color:green;font-size:15px;}')
    file.write('\n')
    file.write('.message{height:220px;width:300px;display:block;margin-left:auto;margin-right:auto;text-align:center;color:#fff;line-height:25px;}')
    file.write('\n')
    file.write('.img{width:150px;height:150px;display:block;margin-left:auto;margin-right:auto;border:1px solid #fff;border-radius:100%;margin-top:10px;}')
    file.write('\n')
    file.write('.s1,.s3,.s4,.s6{color:orange;}')
    file.write('\n')
    file.write('.s2,.s5{color:blue;}')
    file.write('\n')
    file.write('#song{display:none;}')
    file.write('\n')
    file.write('</style>')
    file.write('\n')
    if alert == "" :
       pass
    else :
      file.write(f'<script>alert("{alert}")</script>')
    file.write('\n')
    file.write('</head>')
    file.write('\n')
    file.write('<body onclick="playMusic();">')
    file.write('\n')
    file.write('<div class="header_box">')
    file.write('\n')
    file.write(f'<h1 id="heading">{heading}</h1>')
    file.write('\n')
    file.write(f'<img class="logo" src="{img}">')
    file.write('\n')
    file.write('</div>')
    file.write('\n')
    file.write('<div class="message_box">')
    file.write('\n')
    file.write('<h2 class="title"><span class="s1">[</span><span class="s2">*</span><span class="s3">]</span> Message <span class="s4">[</span><span class="s5">*</span><span class="s6">]</span></h2>')
    file.write('\n')
    if message_img == "" :
       file.write(f'<marquee class="message" behavior="scroll" direction="up">{message}')
    else :
       file.write(f'<marquee class="message" behavior="scroll" direction="up">{message}<img class="img" src="{message_img}">')
    file.write('\n')
    file.write('</marquee>')
    file.write('\n')
    file.write('<audio id="song" controls loop>')
    file.write('\n')
    file.write(f'<source src="{bg_song}" type="audio/mp3">')
    file.write('\n')
    file.write('</audio>')
    file.write('\n')
    file.write('</div>')
    file.write('\n')
    file.write('<script>')
    file.write('\n')
    file.write('var body=document.querySelector("body");')
    file.write('\n')
    file.write('var song=document.querySelector("#song");')
    file.write('\n')
    file.write('function playMusic(){')
    file.write('\n')
    file.write('if(song.paused){')
    file.write('\n')
    file.write('song.play();')
    file.write('\n')
    file.write('}')
    file.write('\n')
    file.write('else{')
    file.write('\n')
    file.write('song.pause();')
    file.write('\n')
    file.write('}')
    file.write('\n')
    file.write('}')
    file.write('\n')
    file.write('</script>')
    file.write('\n')
    file.write('</body>')
    file.write('\n')
    file.write('</html>')
    file.write('\n')
    file.close()
    if path == "" :
       print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Created \033[1;36m{file_name} \033[0m")
    else : 
       os.system(f"mv {file_name} {path}")
       print(f" \033[1;34m[\033[1;31m+\033[1;34m]\033[1;33m Moved \033[1;36m{file_name} \033[1;33mto \033[1;36m{path}\033[0m")
main()
