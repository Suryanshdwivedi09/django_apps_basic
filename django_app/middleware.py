class CustomHeaderMiddleware: 
    def __init__(self,get_response):
        # print('CustomHeader__init__')
        self.get_response = get_response

    def __call__(self,requset):
        # print('CustomHeader__call__ ')
        response = self.get_response(requset)
        response['X-Custom-Header'] ='My custom value'
        return response