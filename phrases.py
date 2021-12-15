import random
import weather as w

def hello():
    phrase = ["Привет, бро",
            "Здарова",
            "Оооо, привет"]
    return random.choice(phrase)

def how_are_you():
    phrase = ["Я в порядке, ты, надеюсь, тоже",
            "Всё шик",
            "Нормально, как всегда"]
    return random.choice(phrase)

def jokes():
    phrase = ["Стоят два бобра. Один другому:\n-Ты дрочить хочешь?\n-Хочу.\nКончить хочешь?\n-Хочу.\n-Так дрочи свой!",
            '''Преподаватель, поясняя неуместность слишком частого использования указателей:
-Звездочки, это конечно хорошо. Но только если они на коньяке или на погонах. В коде же мы будем стараться обходиться без них.''',
            "Все женщины делятся на 3 типа: «дам», «не дам» и «дам но не вам»"]
    return random.choice(phrase)

def not_understand():
    phrase = ["Не понял сейчас",
            "Что ты имеешь в виду?",
            "А?"]
    return random.choice(phrase)

def weather():
    phrase = "Завтра %s℃, %s"%(w.temp, w.status)
    return phrase

def sticker_id():
    id = ['CAACAgIAAxkBAAEDfKZhuQMOapZjJmznr1FhLdnmIMBbxgACzwwAAh9uuEoqPNXzBgEWGiME',
        'CAACAgIAAxkBAAEDfKhhuQNfZ8f5Eafyt2DZUzLke0XpqgACwBQAAz6ZSJSOf3plFv6oIwQ',
        'CAACAgQAAxkBAAEDfKphuQOIUC2vDSpyGEmW5F8uk4BrkgACFwADFXbpB4t0PU84Qh91IwQ',
        'CAACAgIAAxkBAAEDfKxhuQOsoY09Nkpky1khRJtTUd0hrAACLAADF3ttFy7Wn202ocQaIwQ']
    return random.choice(id)
