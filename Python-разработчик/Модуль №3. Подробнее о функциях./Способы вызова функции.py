# Recipient validation as separate function
def address_validation_recipient(recipient):

    if recipient.__contains__('@') and recipient.endswith('.com'):
        is_syntax_valid_recipient = True

    elif recipient.__contains__('@') and recipient.endswith('.ru'):
        is_syntax_valid_recipient = True

    elif recipient.__contains__('@') and recipient.endswith('.net'):
        is_syntax_valid_recipient = True
    else:
        is_syntax_valid_recipient = False
    return is_syntax_valid_recipient

# Sender validation as separate function
def address_validation_sender(sender):

    if sender.__contains__('@') and sender.endswith('.com'):
        is_syntax_valid_sender = True

    elif sender.__contains__('@') and sender.endswith('.ru'):
        is_syntax_valid_sender = True

    elif sender.__contains__('@') and sender.endswith('.net'):
        is_syntax_valid_sender = True

    else:
        is_syntax_valid_sender = False
    return is_syntax_valid_sender


def send_email(message, recipient,*, sender = 'university.help@gmail.com'):
    avs1 = recipient
    avs2 = sender

    if sender != recipient:
        address_validation_recipient(avs1)   # Address validation for syntax errors
        address_validation_sender(avs2)
        if address_validation_sender(recipient) and address_validation_sender(sender):
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