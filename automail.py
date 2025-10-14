#!/usr/bin/python3
# MUlti Port Scanner
# Made by OnlyV
# v0.1.0
# https://github.com/Onlyv-1/Simple-PortScanner/


import smtplib
import schedule
import time

fromm =input("Put your email : ")
password = input("Put the app passwords code : ")
to = input("who are you sanding to : ")

subject = input("Enter subject name: ")
message = input("Enter message: ")


def send_email():
    try:
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.sock.settimeout(30)
        conn.login(fromm, password)
        conn.sendmail(fromm,to,f"Subject: {subject}\n\n{message}")
        conn.quit()
        print("Email sent successfully....waiting for the next repat")
    except Exception as e:
        print("Something went wrong : ",e)

def repeater():
    while True:
        try:
            every = int(input("Repeat every ? : "))
            if every <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive number")

    while True:
        mode = input("Pick one (hour/minutes/seconds/day : ").strip().lower()
        if mode == "hour" or "h" or "hours":
            schedule.every(every) .hours.do(send_email)
            break
        elif mode == "minutes":
            schedule.every(every) .minutes.do(send_email)
            break
        elif mode == "seconds":
            schedule.every(every) .seconds.do(send_email)
            break
        elif mode == "day":
            schedule.every(every) .days.do(send_email)
            break
        else:
            print("Invalid mode. Use hour/minutes/seconds/day).")


    try:
        while True:
            schedule.run_pending()
            idle = schedule.idle_seconds()
            time.sleep(1 if idle is None else max(1, min(idle, 60)))
    except KeyboardInterrupt:
        print("closing...")


if __name__ == "__main__":

    repeater()
