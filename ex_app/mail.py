# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/08_mail.ipynb.

# %% auto 0
__all__ = ['sidebar_group1', 'sidebar_group2', 'mail_data', 'mail_homepage', 'NavItem', 'NavGroup', 'Sidebar', 'load_mail_data',
           'format_date', 'MailItem', 'MailList', 'MailContent', 'IconNavItem', 'IconNav', 'MailDetailView']

# %% ../ex_nbs/08_mail.ipynb 1
from fasthtml.common import *
from fasthtml.components import Uk
from fh_frankenui.components import *
from fasthtml.components import Uk_icon
from fasthtml.svg import *
from fh_matplotlib import matplotlib2fasthtml
import numpy as np
from pathlib import Path
import matplotlib.pylab as plt
import json
from datetime import datetime

# %% ../ex_nbs/08_mail.ipynb 5
def NavItem(icon, text, quantity=None):
    cls = 'flex items-center space-x-2 rounded-md px-3 py-2 text-sm font-medium hover:bg-accent hover:text-accent-foreground'
    content = [UkIcon(icon), Span(text)]
    if quantity:
        content.append(Span(quantity, cls='ml-auto text-background bg-primary rounded-full px-2 py-0.5 text-xs'))
    return Li(A(*content, href='#', cls=cls))

# %% ../ex_nbs/08_mail.ipynb 6
def NavGroup(items):
    return Ul(cls='uk-nav uk-nav-default space-y-3')(*[NavItem(i, t, q) for i, t, q in items if q or t != 'Trash'])

# %% ../ex_nbs/08_mail.ipynb 7
sidebar_group1 = (('home', 'Inbox', '128'), ('file-text', 'Drafts', '9'), (' arrow-up-right', 'Sent', ''),
    ('ban', 'Junk', '23'), ('trash', 'Trash', ''), ('folder', 'Archive', ''))

sidebar_group2 = (('world','Social','972'),('info','Updates','342'),('comments','Forums','128'),
    ('cart','Shopping','8'),('bag','Promotions','21'),)

def Sidebar():
    return Div(cls='space-y-4 py-4 px-3')(
                UkH3('Email',cls='pb-4'),
                Div(cls='space-y-6')(
                    UkButton('New message', cls=(UkButtonT.primary, 'w-full justify-start')),
                    NavGroup(sidebar_group1),
                    UkHSplit(),
                    NavGroup(sidebar_group2)))

# %% ../ex_nbs/08_mail.ipynb 8
def load_mail_data():
    with open(Path('../data/mail.json')) as f: return json.load(f)

mail_data = load_mail_data()

# %% ../ex_nbs/08_mail.ipynb 9
def format_date(date_str):
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%Y-%m-%d %I:%M %p")

# %% ../ex_nbs/08_mail.ipynb 10
def MailItem(mail):
    cls_base = 'relative rounded-lg border border-border p-3 text-sm hover:bg-accent'
    cls = f"{cls_base} {'bg-muted' if mail == mail_data[0] else ''} {'tag-unread' if not mail['read'] else ''}"
    
    return Li(cls=f"tag-mail {cls}")(
        Div(cls='flex w-full flex-col gap-1')(
            Div(cls='flex items-center')(
                Div(cls='flex items-center gap-2')(
                    Div(mail['name'], cls='font-semibold'),
                    Span(cls='flex h-2 w-2 rounded-full bg-blue-600') if not mail['read'] else ''),
                Div(format_date(mail['date']), cls='ml-auto text-xs')),
            A(mail['subject'], cls=TextT.medium_xs, href=f"#mail-{mail['id']}"),
            Div(mail['text'][:100] + '...', cls=TextT.muted_xs),
            Div(cls='flex items-center gap-2')(
                *[A(label, cls=f"uk-label relative z-10 {'uk-label-primary' if label == 'work' else ''}", href='#')
                  for label in mail['labels']])))

# %% ../ex_nbs/08_mail.ipynb 11
def MailList(mails): return Ul(cls='js-filter space-y-2 p-4 pt-0')(*[MailItem(mail) for mail in mails])

# %% ../ex_nbs/08_mail.ipynb 12
def MailContent():
    return Div(cls='flex flex-col')(
        Div(cls='flex h-14 flex-none items-center border-b border-border px-4 py-2')(
            UkH1('Inbox', cls='text-xl font-bold'),
            Ul(cls='uk-tab-alt ml-auto max-w-40')(
                Li(cls='uk-active', uk_filter_control="filter: .tag-mail")(A('All mail', href='#')),
                Li(uk_filter_control="filter: .tag-unread")(A('Unread', href='#')))),
        Div(cls='flex flex-1 flex-col')(
            Div(cls='p-4')(
                Div(cls='uk-inline w-full')(
                    Span(cls='uk-form-icon text-muted-foreground')(UkIcon('search')),
                    Input(cls='uk-input', type='text', placeholder='Search'))),
            Div(cls='max-h-[600px] flex-1 overflow-y-auto')(MailList(mail_data))))

# %% ../ex_nbs/08_mail.ipynb 13
def IconNavItem(*d): return [Li(A(UkIcon(o[0]),uk_tooltip=o[1])) for o in d]  
def IconNav(*c,cls=''): return Ul(cls=f'uk-iconnav {cls}')(*c)

# %% ../ex_nbs/08_mail.ipynb 14
def MailDetailView(mail):
    return Div(cls='flex flex-col')(
        Div(cls='flex h-14 flex-none items-center border-b border-border p-2')(
            Div(cls='flex w-full justify-between')(
                Div(cls='flex gap-x-2 divide-x divide-border')(
                    IconNav(*IconNavItem(('folder','Archive'),('ban','Move to junk'),('trash','Move to trash'))),
                    IconNav(Li(A(UkIcon('clock'), uk_tooltip='Snooze')), cls='pl-2')),
                Div(cls='flex gap-x-2 divide-x divide-border')(
                    IconNav(*IconNavItem(('reply','Reply'),('reply','Reply all'),('forward','Forward'))),
                    IconNav(Li(A(UkIcon('more-vertical'))),cls='pl-2')))),
        Div(cls='flex-1')(
            Div(cls='flex items-start p-4')(
                Div(cls='flex items-start gap-4 text-sm')(
                    Span(mail['name'][:2], cls='flex h-10 w-10 items-center justify-center rounded-full bg-muted'),
                    Div(cls='grid gap-1')(
                        Div(mail['name'], cls=TextB.wt_bold),
                        Div(mail['subject'], cls='text-xs'),
                        Div(cls=TextB.sz_xsmall)(
                            Span('Reply-To:', cls=TextB.wt_medium),
                            f" {mail['email']}"))),
                Div(format_date(mail['date']), cls=(TextT.muted_xs,'ml-auto'))),
            Div(cls='flex-1 space-y-4 border-t border-border p-4 text-sm')(P(mail['text']))),
        Div(cls='flex-none space-y-4 border-t border-border p-4')(
            UkTextArea(id='message', placeholder=f"Reply {mail['name']}"),
            Div(cls='flex justify-between')(
                    UkSwitch('Mute this thread',id='mute', cls='inline-flex items-center gap-x-2 text-xs'),
                UkButton('Send', cls=UkButtonT.primary))))

# %% ../ex_nbs/08_mail.ipynb 15
def mail_homepage():
    return Div(cls='flex divide-x divide-border')(
        Sidebar(),
        Div(cls='grid flex-1 grid-cols-2 divide-x divide-border')(
            MailContent(),
            MailDetailView(mail_data[0])))

# %% ../ex_nbs/08_mail.ipynb 17
mail_homepage = mail_homepage()
