#!/usr/bin/python3

import email
import imaplib
import re
import clipboard as c
from datetime import datetime

def main():
    session = imaplib.IMAP4_SSL('imap.naver.com')

    id = ''
    pw = ''
    from_email = ''

    session.login(id, pw)

    session.select('Inbox')

    result, data = session.search(None, f'(UNSEEN FROM "{from_email}")')

    for num in reversed(data[0].split()):

        result, data = session.fetch(num, '(RFC822)')

        # 메일의 기본 정보 출력하기
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        # print('From: ', email_message['From'])
        # print('Sender: ', email_message['Sender'])
        # print('To: ', email_message['To'])
        # print('Date: ', email_message['Date'])

        # subject, encode = find_encoding_info(email_message['Subject'])
        # print('Subject', subject)

        # print('Subject', email_message['Subject'])

        message = ''

        # print('[CONTENT]')
        # print('=' * 80)
        if email_message.is_multipart():
            for part in email_message.get_payload():
                if part.get_content_type() == 'text/plain':
                    bytes = part.get_payload(decode=True)
                    encode = part.get_content_charset()
                    message = message + str(bytes, encode)
        # print(message)
        # print('=' * 80)

        if '[NSA] OTP number' in email_message['Subject']:
            m = re.search('\[NSA\] OTP number: \[(\d{6})\]', email_message['Subject'])
            otp = m.group(1)

            # temp = datetime.strptime(email_message.get("Date"), '%a, %d %b %Y %H:%M:%S %z')
            # date = temp.strftime('%Y년 %m월 %d일')

            # print(temp)
            # print(date)

            print(f'{otp} {email_message.get("Date")}', end='')

            c.copy(otp)

            session.store(num, '+FLAGS', '\\SEEN')
            session.store(num, '+FLAGS', '\\DELETED')

            # delete mail

            break

    session.close()
    session.logout()

if __name__ == '__main__':
    main()
