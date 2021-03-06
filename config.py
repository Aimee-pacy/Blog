import os

class Config:
    
    SECRET_KEY = '12345'

    # SQLALCHEMY_DATABASE_URI = 'postgres://olaxeopvvvaovc:2e9199e55fc98030a8843ced2950c34be63a60514637c6a925676bc3d0ef5ef0@ec2-52-201-55-4.compute-1.amazonaws.com:5432/d29v2atrpmeual'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ishimwe:12345@localhost/blog_app'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
