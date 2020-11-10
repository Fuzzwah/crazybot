# -*- coding: utf-8 -*-
"""

@author: Matt Sehgal
"""

def get_username(client, user_id):
    user_profile = client.users_profile_get(user=user_id)
    return user_profile['profile']['display_name'].lower()