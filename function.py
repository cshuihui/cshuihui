def morse_code_decryption(txt):
    """接收明文字符串为参数，返回用摩斯密码加密后的字符串。"""
    char = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '.:,;?=\'/!-_"()$&@ –'
    morse_letter = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morse_digit = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    morse_spec = ['.-.-.-', '---...', '--..--', '-.-.-.', '..- -..', '-...-', '.----.', '-..-.', '-.-.--', '-....-',
                  '..--.-', '.-..-.', '-.--.', '-.--.-', '...-..-', '·-···', '.--.-.', ' ',
                  '–']    # '.:,;?=\'/!-_"()$&@'的摩斯码
    # 补充你的代码
    trans = ""
    dicts = dict(zip(morse_letter + morse_digit + morse_spec, list(char)))
    wordlist = txt.split(sep = '   ')
    for i in wordlist:
        alphaslist = i.split(sep = ' ')
        for I in alphaslist:
            trans += dicts.get(I, '')
        trans += ' '
    return trans




if __name__ == '__main__':
    ciphertext = input()                      # 输入一个密文
    print(morse_code_decryption(ciphertext))  # 调用函数，并输出返回值
