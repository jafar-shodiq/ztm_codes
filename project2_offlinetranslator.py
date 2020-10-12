from translate import Translator

translator = Translator(to_lang='ja')
try:
    with open('D:/pythonProject/udemy/ZeroToMastery_Python/textfile/translate.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        # with open('./textfile/translated-ja.txt', mode='w') as my_file2:
        #     my_file2.write(translation)
except FileNotFoundError as err:
    print('file does not exist')

print(translation)