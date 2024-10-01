
def send_email(message, recipient, sender="university.help@gmail.com"):
    print(message, recipient, sender)
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(message, recipient, sender)
        return
    
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

send_email("Письмо успешно отправлено с адреса", "university.help@gmail.com", sender='vasyok1337@gmail.com')
send_email('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!', 'urban.info@mail.ru', sender='urban.fan@gmail.com')
send_email("Невозможно отправить письмо с адреса","urban.teacher@mail.uk",sender="urban.student@mail.ru")
