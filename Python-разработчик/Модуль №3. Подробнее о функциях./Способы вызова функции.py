
def address_validation_recipient(message, recipient, sender):    # Recipient validation as separate function
    global is_syntax_valid_recipient
    if recipient.__contains__('@') and recipient.__contains__('.com'):
        is_syntax_valid_recipient = 'correct'
        return is_syntax_valid_recipient
    elif recipient.__contains__('@') and recipient.__contains__('.ru'):
        is_syntax_valid_recipient = 'correct'
        return is_syntax_valid_recipient
    elif recipient.__contains__('@') and recipient.__contains__('.net'):
        is_syntax_valid_recipient = 'correct'
        return is_syntax_valid_recipient
    else:
        is_syntax_valid_recipient = 'not correct'
        return is_syntax_valid_recipient

def address_validation_sender(message, recipient, sender):   # Sender validation as separate function
    global is_syntax_valid_sender
    if sender.__contains__('@') and sender.__contains__('.com'):
        is_syntax_valid_sender = 'correct'
        return is_syntax_valid_recipient
    elif sender.__contains__('@') and sender.__contains__('.ru'):
        is_syntax_valid_sender = 'correct'
        return is_syntax_valid_recipient
    elif sender.__contains__('@') and sender.__contains__('.net'):
        is_syntax_valid_sender = 'correct'
        return is_syntax_valid_recipient
    else:
        is_syntax_valid_sender = 'not correct'
        return is_syntax_valid_recipient


def send_email(message, recipient,*, sender = 'university.help@gmail.com'):
    avs1 = message
    avs2 = recipient
    avs3 = sender

    if sender != recipient:
        address_validation_recipient(avs1, avs2, avs3)   # Address validation for syntax errors
        address_validation_sender(avs1, avs2, avs3)
        if is_syntax_valid_recipient == 'correct' and is_syntax_valid_sender == 'correct':
            if sender == 'university.help@gmail.com' or sender == 'urban.teacher@mail.ru':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print('Нельзя отправить письмо самому себе!')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')


# def send_email(sender = "university.help@gmail.com"):
#     recip = input('Enter recipient address: ')
#     if sender == 'university.help@gmail.com' or sender = 'urban.teacher@mail.ru':
#         if sender != recip:
#             if recip.__contains__('@') and recip.__contains__('.com'):
#                 msg = input('Enter your message: ')
#                 print(f'Письмо успешно отправлено с адреса {sender} на адрес {recip}')
#             elif recip.__contains__('@') and recip.__contains__('.ru'):
#                 msg = input('Enter your message: ')
#                 print(f'Письмо успешно отправлено с адреса {sender} на адрес {recip}')
#             elif recip.__contains__('@') and recip.__contains__('.net'):
#                 msg = input('Enter your message: ')
#                 print(f'Письмо успешно отправлено с адреса {sender} на адрес {recip}')
#             else:
#                 print(f'Невозможно отправить письмо с адреса {sender} на адрес {recip}')
#         else:
#             print('Нельзя отправить письмо самому себе!')
#     else:
#         print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recip}')
#
# send_email(sender = 'qwe')