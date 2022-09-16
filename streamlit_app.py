import datetime
import http.client
import json

import streamlit as st
from loguru import logger


def userinfo(username):
    logger.info(f'Request by {username} at {datetime.datetime.today()}')
    while True:
        conn = http.client.HTTPSConnection('reddit.com')
        conn.request('GET',
                     f'https://www.reddit.com/user/{username}/about/.json')
        r = conn.getresponse()
        res = json.loads(r.read().decode())
        logger.debug(res)
        if r.status == 429:
            continue
        else:
            response = r.status
            if response == 404:
                notfound = True
                return notfound, res
            else:
                notfound = False
                return notfound, res


def main():
    _, col, _ = st.columns([1, 1, 1])
    with col:
        st.image('https://i.imgur.com/8vv9HRr.png')
    st.title('Are You Shadowbanned From Reddit?')
    st.write('')
    show_button = False
    username = st.text_input('Enter your username, then hit Enter/Return')
    if username:
        show_button = True
        notfound, res = userinfo(username)
        if notfound:
            st.markdown('## You are **shadowbanned**! 💀*')
            st.markdown('*or the account does not exist.')
        else:
            st.markdown('## You are **not** shadowbanned! 🎉')
        if show_button:
            if st.button('See full API response'):
                st.json(res)


if __name__ == '__main__':
    st.set_page_config(page_title='Reddit Shadowban Check',
                       page_icon='https://i.imgur.com/8vv9HRr.png',
                       layout='centered',
                       initial_sidebar_state='collapsed',
                       menu_items=None)
    main()
