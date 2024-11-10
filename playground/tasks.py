from celery import shared_task

from time import sleep


@shared_task
def notify_customers(message):
    print('Sending 10K emails...')
    print(message)
    sleep(10)
    print('Emails were successfully sent!s')
