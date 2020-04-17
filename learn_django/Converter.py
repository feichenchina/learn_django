from django.urls import register_converter


class FourDigitYearConverter:
    '''
    实现年份转换器
    '''
    regex = '[0-9]{4}'

    def to_python(self, value):
        print(value+'nihao')
        return int(value)

    def to_url(self, value):
        print(value+"world")
        return '%04d' % value
#     将实现的年份转化器注册到URL配置中，并将其命名为yyyy，   使用方式为:    <yyyy:2020>
register_converter(FourDigitYearConverter, 'yyyy')