#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime

SlqBlogSettings = {
    'post_types': ('post', 'page'), # deprecated
    'allow_registration': os.environ.get('allow_registration', 'false').lower() == 'true',
    'allow_su_creation': os.environ.get('allow_su_creation', 'false').lower() == 'true',
    'allow_donate': os.environ.get('allow_donate', 'true').lower() == 'true',
    'auto_role': os.environ.get('auto_role', 'reader').lower(),
    'blog_meta': {
        'name': os.environ.get('name') if os.environ.get('name') else "Shawn's Blog",
        'subtitle': os.environ.get('subtitle') if os.environ.get('subtitle') else "The World is a Stage",
        'description': os.environ.get('description') if os.environ.get('description') else "一个分享编程经验、学习技巧、各类资源汇总的个人博客",
        'wechat_name': os.environ.get('wechat_name') if os.environ.get('wechat_name') else 'Slq Blog Wechat Root',
        'wechat_subtitle': os.environ.get('wechat_subtitle') if os.environ.get('wechat_subtitle') else 'Slq Blog Wechat Subtitle',
        'owner': os.environ.get('owner') if os.environ.get('owner') else 'shawnlinq',
        'keywords': os.environ.get('keywords') if os.environ.get('keywords') else 'python,django,flask,markdown,MongoDB',
        'google_site_verification': os.environ.get('google_site_verification') or 'nd-uzkrk3H1c_Be19bYQsmpbpDwWH5dIigRE9mUpNz8',
        'baidu_site_verification': os.environ.get('baidu_site_verification') or 'CHGIj3UoVk',
        'sogou_site_verification': os.environ.get('sogou_site_verification') or 'CJqu0SLnt0',
        'bing_site_verification': os.environ.get('bing_site_verification') or '342C90C1E0E3B92988AC6C1A01179D10',
        'get360_site_verification': os.environ.get('get360_site_verification') or 'b4a1b4b922c4169b6e73e7dbc768d54c',
    },
    'search_engine_submit_urls':{
        'baidu': os.environ.get('baidu_submit_url')
    },
    'pagination':{
        'per_page': int(os.environ.get('per_page', 6)),
        'admin_per_page': int(os.environ.get('admin_per_page', 10)),
        'archive_per_page': int(os.environ.get('admin_per_page', 20)),
    },
    'blog_comment':{
        'allow_comment': os.environ.get('allow_comment', 'true').lower() == 'true',
        'comment_type': os.environ.get('comment_type', 'slqblog').lower(), # currently, SlqBlog only supports duoshuo comment
        'comment_opt':{
            'slqblog': 'slq-blog', # shotname of slqblog
            'duoshuo': 'slq-blog', # shotname of duoshuo
            }
    },
    'donation': {
        'allow_donate': os.environ.get('allow_donate', 'true').lower() == 'true',
        'donation_msg': os.environ.get('donation_msg', '如果文章对你有价值，请Shawn喝杯咖啡吧，金额随意')
    },
    'wechat': {
        'display_wechat': os.environ.get('display_wechat', 'true').lower() == 'true',
        'wechat_msg': os.environ.get('wechat_msg', '关注我的微信公众号，获得及时的更新动态')
    },
    'copyright': {
        'display_copyright': os.environ.get('allow_donate', 'true').lower() == 'true',
        'copyright_msg': os.environ.get('copyright_msg', '转载此文，请与Shawn联系')
    },
    'only_abstract_in_feed': os.environ.get('only_abstract_in_feed', 'false').lower() == 'true',
    'allow_share_article': os.environ.get('allow_share_article', 'true').lower() == 'true',
    'gavatar_cdn_base': os.environ.get('gavatar_cdn_base', '//cdn.v2ex.com/gravatar/'),
    'gavatar_default_image': os.environ.get('gavatar_default_image', 'http://7tsygu.com1.z0.glb.clouddn.com/user-avatar.jpg'),

}

class Config(object):
    DEBUG = False
    TESTING = False

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fjdljLJDL08_80jflKzcznv*c'
    MONGODB_SETTINGS = {'DB': 'SlqBlog'}

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')
    EXPORT_PATH = os.path.join(BASE_DIR, 'exports').replace('\\', '/')

    if not os.path.exists(EXPORT_PATH):
        os.makedirs(EXPORT_PATH)

    REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=3)


    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class PrdConfig(Config):
    # DEBUG = False
    DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
    MONGODB_SETTINGS = {
            'db': 'SlqBlog',
            'host': os.environ.get('MONGO_HOST') or 'localhost',
            # 'port': 12345
        }

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {'DB': 'SlqBlogTest'}
    WTF_CSRF_ENABLED = False

config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'testing': TestingConfig,
    'default': DevConfig,
}
