import time
import random
import IPython
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://3.bp.blogspot.com/-qbORCFE5qhk/UmTBJwEYKjI/AAAAAAAAZYY/nbjieynFcLQ/s800/job_uranaishi.png'
YOUR_ICON = 'https://1.bp.blogspot.com/-ZOg0qAG4ewU/Xub_uw6q0DI/AAAAAAABZio/MshyuVBpHUgaOKJtL47LmVkCf5Vge6MQQCNcBGAsYHQ/s1600/pose_pien_uruuru_woman.png'

def run_chat(chat = chat, start='ようこそ。あなたと相手のイメージカラーで相性を占います。', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', '占い師')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)

# フレーム 状態をもつ辞書
# 'color1', 'color2', 'asking'
frame = {}

def myuranai(input_text):
  global frame # 外部の状態を参照する
  if 'asking' in frame:  # asking から更新する
    frame[frame['asking']] = input_text
    del frame['asking']

  if 'color1' not in frame:
    frame['asking'] = 'color1' # あなたの色  
    return 'まずは赤色、黄色、青色、緑色の中からあなたのイメージカラーを入力してください。<br>(選択肢の表記と同じ様に入力してください。例えば赤色を選択した場合、赤色と入力してください。)'

  if 'color1' in frame and 'color2' not in frame:
    frame['asking'] = 'color2' # 相手の色    
    return '次に先程と同様に、赤色、黄色、青色、緑色の中からお相手のイメージカラーを入力してください。<br>(選択肢の表記と同じ様に入力してください。例えば赤色を選択した場合、赤色と入力してください。)'
  
  if 'color1' in frame and 'color2' in frame:
    
    if '赤色' in frame['color1'] and '赤色' in frame['color2']:
      return '赤色を選んだあなたとお相手は情熱的で行動力があり、とにかく一歩前へ前進する性格です。<br>お互いに赤色のオーラで相性100％です。'
    if '赤色' in frame['color1'] and '黄色' in frame['color2']:
      return '赤色を選んだあなたは情熱的で行動力があり、とにかく一歩前へ前進する性格です。黄色のお相手はとにかく明るくて、ユーモアがあり、知性溢れる性格です。<br>オレンジ色のオーラで相性95％です。'
    if '赤色' in frame['color1'] and '青色' in frame['color2']:
      return '赤色を選んだあなたは情熱的で行動力があり、とにかく一歩前へ前進する性格です。青色のお相手は冷静で争い事が好きではない平和主義な性格です。<br>紫色のオーラで相性98％です。'
    if '赤色' in frame['color1'] and '緑色' in frame['color2']:
      return '赤色を選んだあなたは情熱的で行動力があり、とにかく一歩前へ前進する性格です。緑色のお相手は内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。<br>補色の強力なオーラです。相性120％です。'
    if '黄色' in frame['color1'] and '赤色' in frame['color2']:
      return '黄色を選んだあなたはとにかく明るくて、ユーモアがあり、知性溢れる性格です。赤色のお相手は情熱的で行動力があり、とにかく一歩前へ前進する性格です。<br>オレンジ色のオーラで相性95％です。'
    if '黄色' in frame['color1'] and '黄色' in frame['color2']:
      return '黄色を選んだあなたとお相手はとにかく明るくて、ユーモアがあり、知性溢れる性格です。<br>お互いに黄色のオーラで相性100％です。'
    if '黄色' in frame['color1'] and '青色' in frame['color2']:
      return '黄色を選んだあなたはとにかく明るくて、ユーモアがあり、知性溢れる性格です。青色のお相手は冷静で争い事が好きではない平和主義な性格です。<br>緑色のオーラで相性93％です。'
    if '黄色' in frame['color1'] and '緑色' in frame['color2']:
      return '黄色を選んだあなたはとにかく明るくて、ユーモアがあり、知性溢れる性格です。緑色のお相手は内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。<br>黄緑色のオーラで相性92％です。'
    if '青色' in frame['color1'] and '赤色' in frame['color2']:
      return '青色を選んだあなたは冷静で争い事が好きではない平和主義な性格です。赤色のお相手は情熱的で行動力があり、とにかく一歩前へ前進する性格です。<br>紫色のオーラで相性98％です。'
    if '青色' in frame['color1'] and '黄色' in frame['color2']:
      return '青色を選んだあなたは冷静で争い事が好きではない平和主義な性格です。黄色のお相手はとにかく明るくて、ユーモアがあり、知性溢れる性格です。<br>緑色のオーラで相性93％です。'
    if '青色' in frame['color1'] and '青色' in frame['color2']:
      return '青色を選んだあなたとお相手は冷静で争い事が好きではない平和主義な性格です。<br>お互いに青色のオーラで相性100％です。'
    if '青色' in frame['color1'] and '緑色' in frame['color2']:
      return '青色を選んだあなたは冷静で争い事が好きではない平和主義な性格です。緑色のお相手は内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。<br>ターコイズ色のオーラで相性110％です。'
    if '緑色' in frame['color1'] and '赤色' in frame['color2']:
      return '緑色を選んだあなたは内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。赤色のお相手は情熱的で行動力があり、とにかく一歩前へ前進する性格です。<br>補色の強力なオーラです。相性120％です。'
    if '緑色' in frame['color1'] and '黄色' in frame['color2']:
      return '緑色を選んだあなたは内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。黄色のお相手はとにかく明るくて、ユーモアがあり、知性溢れる性格です。<br>黄緑色のオーラで相性92％です。'
    if '緑色' in frame['color1'] and '青色' in frame['color2']:
      return '緑色を選んだあなたは内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。青色のお相手は冷静で争い事が好きではない平和主義な性格です。<br>ターコイズ色のオーラで相性110％です。'
    if '緑色' in frame['color1'] and '緑色' in frame['color2']:
      return '緑色を選んだあなたとお相手は内に秘めた情熱を持ちつつ、視野を広く見ていける性格です。<br>お互いに緑色のオーラで相性100％です。'
    
    return 'もう一度初めからやり直してください。'

  return output_text

def start():
  run_chat(chat=myuranai)
