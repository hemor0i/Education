# Задача "Рассылка писем":
def send_email(message, recipient, sender="university.help@gmail.com"):
    exceptions = ['.com', '.ru', '.net']    # Добавляем рабочие домены
    if (('@' not in sender) or ('@' not in recipient)   # Если нет @, то отправка не возможна
        or not any(sender.endswith(i) for i in exceptions)      # Если домен почты не сопадает с доментами в списке
        or not any(recipient.endswith(i) for i in exceptions)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
