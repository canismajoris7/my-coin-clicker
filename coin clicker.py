import random
from tkinter import *
import tkinter.messagebox
import time
from pickle import *



global coin
global mine
global link
global farm
global voc
global mony
global pool
global base
global inco
global hack
global ecex
global inve
global MSSC
global MSSC2
global decr
global digs
global reum
global lonk
global ranc
global pond
global site
global exot
global inst
global mrkt
inst = 0
exot = 0
digs = 0

lonk = 0
ranc = 0
pond = 0
site = 0
reum = 0
mine = 0
coin = 0
link = 0
farm = 0
pool = 0
base = 0
inco = 0
hack = 0
ecex = 0
mony = 0
voc = 10
inve = 0
mrkt = 0
MSSC = 1
MSSC2 = 1
decr = 0
UAU = .75


def bonusplus():
    global coin
    global mine
    global link
    global farm
    global voc
    global pool
    global base
    global inco
    global mony
    global hack
    global ecex
    global decr
    for x in range(0, link):
        coin = coin + random.randint(0, 2)
    for x in range(0, mine):
        coin = coin + random.randint(4, 6)
    for x in range(0, farm):
        coin = coin + random.randint(6, 8)
    for x in range(0, pool):
        coin = coin + random.randint(2, 15)
    for x in range(0, base):
        coin = coin + random.randint(4, 18)
    for x in range(0, inco):
        mony = mony + random.randint(100, 600)
    for x in range(0, hack):
        coin = coin + random.randint(50, 100)
    for x in range(0, ecex):
        mony = mony + random.randint(2000, 8000)
        coin = coin + random.randint(600, 1500)
    for x in range(0, inve):
        inco = inco + random.randint(1, 2)
        _incocount.config(text=inco)
        hack = hack + random.randint(0, 2)
        _hackcount.config(text=hack)
    voc = voc + random.randint(0, 2)
    for x in range(0, decr):
        coin = coin * 1.15


def clickfun():
    global coin
    coin = coin + 1
    _coincount.config(text=coin)
    time.sleep(UAU)
    bonusplus()


def trade():
    global coin
    global voc
    global mony
    coin = coin - 1
    mony = mony + voc
    _coincount.config(text=coin)
    _monycount.config(text=mony)


def linkstore():
    time.sleep(.25)
    global coin
    global link
    if coin > 3:
        link = link + 1
        _linkcount.config(text=link)
        coin = coin - 4
        _coincount.config(text=coin)

    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def minestore():
    time.sleep(.25)
    global mine
    global coin
    if coin > 29:
        mine = mine + 1
        _minecount.config(text=mine)
        coin = coin - 30
        _coincount.config(text=coin)

    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def farmstore():
    time.sleep(.25)
    global farm
    global coin
    if coin > 54:
        farm = farm + 1
        _farmcount.config(text=farm)
        coin = coin - 55
        _coincount.config(text=coin)

    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def poolstore():
    time.sleep(.25)
    global pool
    global coin
    global mony
    if coin > 70:
        if mony > 19:
            pool = pool + 1
            _poolcount.config(text=pool)
            coin = coin - 71
            mony = mony - 20
            _coincount.config(text=coin)
            _monycount.config(text=mony)
        else:
            tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def basestore():
    time.sleep(.25)
    global base
    global coin
    global mony
    if coin > 80:
        if mony > 29:
            if pool > 1:
                base = base + 1
                _basecount.config(text=base)
                coin = coin - 81
                mony = mony - 30
                _coincount.config(text=coin)
                _monycount.config(text=mony)
            else:
                tkinter.messagebox.showinfo('ingame message',
                                            "sorry you dont have enough of something to get that now")
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def incostore():
    time.sleep(.25)
    global inco
    global coin
    global mony
    if coin > 80:
        if mony > 34:
            if base > 2:
                inco = inco + 1
                _incocount.config(text=inco)
                coin = coin - 81
                mony = mony - 35
                _coincount.config(text=coin)
                _monycount.config(text=mony)
            else:
                tkinter.messagebox.showinfo('ingame message',
                                            "sorry you dont have enough of something to get that now")
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def hackstore():
    time.sleep(.25)
    global hack
    global coin
    if coin > 1000:
        if inco > 4:
            hack = hack + 1
            _hackcount.config(text=hack)
            coin = coin - 1001
            _coincount.config(text=coin)
            UAU = .5
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def ecexstore():
    time.sleep(.25)
    global ecex
    global coin
    global mony
    if coin > 400000:
        if mony > 3000000:
            if hack > 15:
                ecex = ecex + 1
                _ecexcount.config(text=ecex)
                coin = coin - 400011
                mony = mony - 3050001
                _coincount.config(text=coin)
                _monycount.config(text=mony)
        else:
            tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def investore():
    time.sleep(.25)
    global inve
    global coin
    global mony
    if coin > 300000:
        if mony > 2000000:
            if ecex > 2:
                inve = inve + 1
                _invecount.config(text=inve)
                coin = coin - 300011
                _coincount.config(text=coin)
                mony = mony - 2050001
                _monycount.config(text=mony)
        else:
            tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def dwam():
    tkinter.messagebox.showinfo('ingame message', " this is an idle clicker game")
    tkinter.messagebox.showinfo('game info', " links = 4{) mines = 30{) farms = 55{) pools = 71{) & 20$     _  also milestone are reached at 99 and 75 for inc & bas")
    tkinter.messagebox.showinfo('game info', " bases = 81{) & 30$  incorps = 81{) & 35$  hacenter = 1000{)  econextra = 400000{) & 3000000$ invest = 300000{) & 2000000$")

def mile():
    global coin
    global mony
    global inco
    global voc
    global MSSC
    global MSSC2

    if hack > 16:
        if coin > 400000:
            _ecexcount.config(fg="orange")

    if inco > 75:
        if MSSC == 1:
            coin = coin + 100000
            inco = inco + 125
            mony = mony + 1000000
            _monycount.config(text=mony)
            _coincount.config(text=coin)
            tkinter.messagebox.showinfo("corperation milestone", "you have reached a milestone and will get reward")
            MSSC = 0
    if base > 99:
        if MSSC2 == 1:
            voc = voc + 300
            mony = mony + 1000000
            _monycount.config(text=mony)
            tkinter.messagebox.showinfo("database milestone", "you have reached a milestone and will get reward")
            MSSC2 = 0
    else:
        tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
#    if base > 99:
 #       if inco > 75:
 #           if decryptor > 6:
 #               if reum > 500000:
 #                   if coin > 500000000:
     #                   if mony > 4000000:
     #                       tkinter.messagebox.showinfo("endgame milestone", "YOU HAVE BEAT THE GAME")
     #                   else:
     #                       tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
     #               else:
      #                  tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
      #          else:
      #              tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
      #      else:
     #           tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
     #   else:
    #        tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
   # else:
   #     tkinter.messagebox.showinfo("disapointing message", "no pending milestones")
def decryptor():
    time.sleep(.5)
    global link
    global mine
    global farm
    global mony
    global pool
    global base
    global inco
    global hack
    global ecex
    global inve
    global decr
    everything = link + mine + farm + pool + base + inco + hack + ecex + inve
    if everything > 13:
        if mony > 20000:
            if inve > 2:
                decr = decr + 1
                _decrcount.config(text=decr)

                link = link - 4
                _linkcount.config(text=link)
                mine = mine - 3
                _minecount.config(text=mine)
                farm = farm - 2
                _farmcount.config(text=farm)
                pool = pool - 1
                _poolcount.config(text=pool)
                base = base - 1
                _basecount.config(text=base)
                inco = inco - 5
                _incocount.config(text=inco)
                hack = hack - 16
                _hackcount.config(text=hack)
                ecex = ecex - 3
                _ecexcount.config(text=ecex)
                inve = inve - 1
                _invecount.config(text=inve)
                mony = mony - 20000
                _monycount.config(text=mony)
                UAU = .25
        else:
            tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
def auto():
    if pool > 0:
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        time.sleep(.25)
        bonusplus()
        if inve > 0:
            bonusplus()
            bonusplus()
            bonusplus()
            bonusplus()
    else:
        tkinter.messagebox.showinfo('ingame message', " READ this MESSAGE! sorry you dont have enough of POOL now")




def uthereum():
    if decr > 3:



        def bonusplus():
            global digs
            global reum
            global lonk
            global ranc
            global pond
            global site
            global exot
            global inst
            global mrkt
            for x in range(0, lonk):
                reum = reum + random.randint(0, 2)
            for x in range(0, digs):
                reum = reum + random.randint(4, 6)
            for x in range(0, ranc):
                reum = reum + random.randint(6, 8)
            for x in range(0, pond):
                reum = reum + random.randint(2, 15)
            for x in range(0, site):
                reum = reum + random.randint(4, 18)
            for x in range(0, inst):
                site = site + random.randint(4, 18)
            for x in range(0, mrkt):
                inst = inst + random.randint(4, 18)
        def clickz():
            global reum
            reum = reum + 1
            _reumamount.config(text=reum)

            bonusplus()

        def lonkshack():

            global reum
            global lonk
            if reum > 3:
                lonk = lonk + 1
                _lonkamount.config(text=lonk)
                reum = reum - 4
                _reumamount.config(text=reum)

            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")

        def digsshack():

            global digs
            global reum
            if reum > 29:
                digs = digs + 1
                _digsamount.config(text=digs)
                reum = reum - 30
                _reumamount.config(text=reum)

            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")

        def rancshack():

            global ranc
            global reum
            if reum > 54:
                ranc = ranc + 1
                _rancamount.config(text=ranc)
                reum = reum - 55
                _reumamount.config(text=reum)

            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")

        def pondshack():

            global pond
            global reum
            global exot
            if reum > 70:
                if exot == 0:
                    pond = pond + 1
                    _pondamount.config(text=pond)
                    reum = reum - 71
                    _reumamount.config(text=reum)

                else:
                    tkinter.messagebox.showinfo('ingame message',
                                                "sorry you dont have enough of something to get that now")
            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")

        def siteshack():

            global site
            global reum
            global exot
            if reum > 80:
                if exot == 0:
                    if pond > 1:
                        site = site + 1
                        _siteamount.config(text=site)
                        reum = reum - 81
                        _reumamount.config(text=reum)
                    else:
                        tkinter.messagebox.showinfo('ingame message',
                                                    "sorry you dont have enough of something to get that now")
            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
            time.sleep(.25)

        def instshack():
            global inst
            global reum
            if reum > 20000:
                if exot == 0:
                    if exot == 0:
                        inst = inst + 1
                        _instamount.config(text=inst)
                        reum = reum - 20000
                        _reumamount.config(text=reum)
                else:
                    tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")

        def mrktshack():
            global mrkt
            global reum
            if reum > 20000:
                if exot == 0:
                    if exot == 0:
                        mrkt = mrkt + 1
                        _mrktamount.config(text=mrkt)
                        reum = reum - 200000
                        _reumamount.config(text=reum)
                else:
                    tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")
            else:
                tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")

        utheroot = Tk()
        utheroot.title("uthereum clicker")

        clicko = Button(utheroot, text='click', command=clickz)
        clicko.grid(row=0, column=5)

        r_my = Label(utheroot, text='my')
        r_my.grid(row=2, column=0, sticky=W)

        r_wallet = Label(utheroot, text='reum')
        r_wallet.grid(row=3, column=0, sticky=W)

        _reumamount = Label(utheroot, text=reum)
        _reumamount.grid(row=4, column=0)

        # number 1 is empty #

        m_title = Label(utheroot, text='uthereum')
        m_title.grid(row=0, column=2)

        m_lonk = Label(utheroot, text='lonk')
        m_lonk.grid(row=2, column=3)

        _lonkamount = Label(utheroot, text=lonk)
        _lonkamount.grid(row=3, column=3)

        lonkadd = Button(utheroot, text='buy lonks', command=lonkshack)
        lonkadd.grid(row=4, column=3)

        m_digs = Label(utheroot, text='digs')
        m_digs.grid(row=2, column=6)

        _digsamount = Label(utheroot, text=digs)
        _digsamount.grid(row=3, column=6)

        digsadd = Button(utheroot, text='buy digss', command=digsshack)
        digsadd.grid(row=4, column=6)

        m_ranc = Label(utheroot, text='ranc')
        m_ranc.grid(row=2, column=9)

        _rancamount = Label(utheroot, text=ranc)
        _rancamount.grid(row=3, column=9)

        rancadd = Button(utheroot, text='buy rancs', command=rancshack)
        rancadd.grid(row=4, column=9)

        m_pond = Label(utheroot, text='pond')
        m_pond.grid(row=2, column=12)

        _pondamount = Label(utheroot, text=pond)
        _pondamount.grid(row=3, column=12)

        pondadd = Button(utheroot, text='buy ponds', command=pondshack)
        pondadd.grid(row=4, column=12)

        m_site = Label(utheroot, text='site')
        m_site.grid(row=2, column=15)

        _siteamount = Label(utheroot, text=site)
        _siteamount.grid(row=3, column=15)

        siteadd = Button(utheroot, text='buy sites', command=siteshack)
        siteadd.grid(row=4, column=15)

        m_inst = Label(utheroot, text='stockers', fg="purple")
        m_inst.grid(row=2, column=18)

        _instamount = Label(utheroot, text=inst)
        _instamount.grid(row=3, column=18)

        instadd = Button(utheroot, text='buy inst', command=instshack)
        instadd.grid(row=4, column=18)

        m_mrkt = Label(utheroot, text='markets', fg="purple")
        m_mrkt.grid(row=2, column=21)

        _mrktamount = Label(utheroot, text=mrkt)
        _mrktamount.grid(row=3, column=21)

        mrktadd = Button(utheroot, text='buy mrkt', command=mrktshack)
        mrktadd.grid(row=4, column=21)
        utheroot.mainloop()
    else:
        tkinter.messagebox.showinfo('ingame message', "sorry you dont have enough of something to get that now")


def addto():
    global mony
    global reum
    mony = mony + reum
    reum = 0











root = Tk()
root.title("coin clicker")
click = Button(root, text='click', command=clickfun)
click.grid(row=0, column=5)
milk = Button(root, text='auto click 4 2sec', command=auto)
milk.grid(row=11, column=3)
s_my = Label(root, text='my')
s_my.grid(row=2, column=0, sticky=W)
s_wallet = Label(root, text='wallet')
s_wallet.grid(row=3, column=0, sticky=W)
_coincount = Label(root, text=coin)
_coincount.grid(row=4, column=0)
trade = Button(root, text='trade', fg="green", command=trade)
trade.grid(row=0, column=6)
s_my = Label(root, text='my', fg="green")
s_my.grid(row=6, column=0, sticky=W)
s_bank = Label(root, text='bank', fg="green")
s_bank.grid(row=7, column=0, sticky=W)
_monycount = Label(root, text=mony, fg="green")
_monycount.grid(row=8, column=0)
m_title = Label(root, text='CRYPTCOIN')
m_title.grid(row=0, column=2)
m_link = Label(root, text='link')
m_link.grid(row=2, column=3)
_linkcount = Label(root, text=link)
_linkcount.grid(row=3, column=3)
linkadd = Button(root, text='buy links', command=linkstore)
linkadd.grid(row=4, column=3)
m_mine = Label(root, text='mine')
m_mine.grid(row=2, column=6)
_minecount = Label(root, text=mine)
_minecount.grid(row=3, column=6)
mineadd = Button(root, text='buy mines', command=minestore)
mineadd.grid(row=4, column=6)
m_farm = Label(root, text='farm')
m_farm.grid(row=2, column=9)
_farmcount = Label(root, text=farm)
_farmcount.grid(row=3, column=9)
farmadd = Button(root, text='buy farms', command=farmstore)
farmadd.grid(row=4, column=9)
m_pool = Label(root, text='pool')
m_pool.grid(row=2, column=12)
_poolcount = Label(root, text=pool)
_poolcount.grid(row=3, column=12)
pooladd = Button(root, text='buy pools', fg="green", command=poolstore)
pooladd.grid(row=4, column=12)
m_base = Label(root, text='base')
m_base.grid(row=2, column=15)
_basecount = Label(root, text=base)
_basecount.grid(row=3, column=15)
baseadd = Button(root, text='buy bases', fg="green", command=basestore)
baseadd.grid(row=4, column=15)
m_inco = Label(root, text='incorperate')
m_inco.grid(row=2, column=18)
_incocount = Label(root, text=inco)
_incocount.grid(row=3, column=18)
incoadd = Button(root, text='buy incos', fg="green", command=incostore)
incoadd.grid(row=4, column=18)
m_hack = Label(root, text='hack center')
m_hack.grid(row=2, column=21)
_hackcount = Label(root, text=hack)
_hackcount.grid(row=3, column=21)
hackadd = Button(root, text='buy hacks', command=hackstore)
hackadd.grid(row=4, column=21)
m_ecex = Label(root, text='economic-extraction', fg="purple")
m_ecex.grid(row=2, column=24)
_ecexcount = Label(root, text=ecex)
_ecexcount.grid(row=3, column=24)
ecexadd = Button(root, text='buy ecex', fg="green", command=ecexstore)
ecexadd.grid(row=4, column=24)
a = Button(root, text='menu', fg="red", command=dwam)
a.grid(row=8, column=26)
no = Button(root, text='retrive milestones', fg="red", command=mile)
no.grid(row=0, column=24)
m_inve = Label(root, text='investors', fg="purple")
m_inve.grid(row=2, column=25)
_invecount = Label(root, text=inve)
_invecount.grid(row=3, column=25)
inveadd = Button(root, text='buy inve', fg="green", command=investore)
inveadd.grid(row=4, column=25)
m_decr = Label(root, text='decryptors', fg="blue")
m_decr.grid(row=9, column=0)
_decrcount = Label(root, text=decr)
_decrcount.grid(row=10, column=0)
decradd = Button(root, text='buy decr', fg="green", command=decryptor)
decradd.grid(row=11, column=0)
launch = Button(root, text='go to uthereum', fg="blue", command=uthereum)
launch.grid(row=9, column=18)
tran = Button(root, text='reum to money', fg="blue", command=addto)
tran.grid(row=9, column=21)
root.mainloop()




