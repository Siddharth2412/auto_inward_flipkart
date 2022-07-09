import csv
from inward_flipkart import Inward
import login
import os
from os import path
import password_change_check
import success
import time


def main():
    file = open('mapping.csv')
    data = csv.reader(file)
    lids, qtys, bins = [], [], []
    fail_lids, fail_qtys, fail_bins = [], [], []
    count = 1

    for d in data:
        if count == 1:
            count = 0
        else:
            if len(d[0]) > 0:
                lids.append(''.join(str(d[0]).split(' ')))
            if len(d[1]) > 0:
                qtys.append(d[1])
            if len(d[2]) > 0:
                bins.append(d[2])

    for lid in lids:
        if len(lid) != 25:
            print(len(lid))
            return False

    if len(lids) == len(qtys) == len(bins):

        if not path.exists('chromedriver/pwd.bytes'):
            login.Show_pass()
            id = login.id
            pwd = login.pwd
            if len(id) > 0 and len(pwd) > 0:
                pwdf = open('chromedriver/pwd.txt', 'w')
                pwdf.write(login.id + '\n' + login.pwd)
                pwdf.close()
                os.rename('chromedriver/pwd.txt', 'chromedriver/pwd.bytes')
        else:
            password_change_check.confirmation()
            status = password_change_check.status
            if status:
                os.rename('chromedriver/pwd.bytes', 'chromedriver/pwd.txt')
                pwdf = open('chromedriver/pwd.txt', 'r')
                lines = pwdf.readlines()
                id = lines[0].strip()
                pwd = lines[1].strip()
                pwdf.close()
                os.rename('chromedriver/pwd.txt', 'chromedriver/pwd.bytes')
            else:
                login.Show_pass()
                id = login.id
                pwd = login.pwd
                if len(id) > 0 and len(pwd) > 0:
                    os.rename('chromedriver/pwd.bytes', 'chromedriver/pwd.txt')
                    pwdf = open('chromedriver/pwd.txt', 'w')
                    pwdf.write(login.id + '\n' + login.pwd)
                    pwdf.close()
                    os.rename('chromedriver/pwd.txt', 'chromedriver/pwd.bytes')

        if len(lids) > 0 and len(id) > 0 and len(pwd) > 0:
            iw = Inward(id, pwd)
            for lid, qty, bin in zip(lids, qtys, bins):
                fail = iw.inward_data(lid, qty, bin)
                if fail is not None:
                    if len(fail) > 0:
                        fail_lids.append(fail)
                        fail_qtys.append(qty)
                        fail_bins.append(bin)

            iw.shut_down()
            success.finish()

        file = open('mapping.csv', 'w')
        writer = csv.writer(file)
        writer.writerow(['Listing ID', 'Qty', 'Bin No'])

        if len(fail_lids) > 0:
            file = open('remaining.csv', 'w')
            writer = csv.writer(file)
            writer.writerow(['Listing ID', 'Qty', 'Bin No'])
            for lid, qty, bin in zip(fail_lids, fail_qtys, fail_bins):
                writer.writerow([str(lid).strip(), str(qty).strip(), str(bin).strip()])
        else:
            if path.exists('remaining.csv'):
                os.remove('remaining.csv')


if __name__ == "__main__":
    data = main()
    if data is False:
        success.error()

