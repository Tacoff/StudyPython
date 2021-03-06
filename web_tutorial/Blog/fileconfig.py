 #!/usr/bin/env python
 # -*- coding: utf8 -*-
 
# import os
# os.urandom(24) 生成secret_key

import os
basedir = os.path.abspath(os.path.dirname(__file__))
 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_ENABLED = True
SECRET_KEY = '\x9ad.\xd1\xd2\x8a.o\xaf\x1a\xea\xa3\xfc\x1e\x81\xb6G&.=q\xfe\xca\xb5'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]