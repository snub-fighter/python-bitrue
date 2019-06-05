# coding=utf-8


class BitrueAPIException(Exception):

    def __init__(self, response):
        self.code = 0
        try:
            json_res = response.json()
        except ValueError:
            self.message = 'Invalid JSON error message from Bitrue: {}'.format(response.text)
        else:
            self.code = json_res['code']
            self.message = json_res['msg']
        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):  # pragma: no cover
        return 'APIError(code=%s): %s' % (self.code, self.message)


class BitrueRequestException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'BitrueRequestException: %s' % self.message


class BitrueOrderException(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return 'BitrueOrderException(code=%s): %s' % (self.code, self.message)


class BitrueOrderMinAmountException(BitrueOrderException):

    def __init__(self, value):
        message = "Amount must be a multiple of %s" % value
        super(BitrueOrderMinAmountException, self).__init__(-1013, message)


class BitrueOrderMinPriceException(BitrueOrderException):

    def __init__(self, value):
        message = "Price must be at least %s" % value
        super(BitrueOrderMinPriceException, self).__init__(-1013, message)


class BitrueOrderMinTotalException(BitrueOrderException):

    def __init__(self, value):
        message = "Total must be at least %s" % value
        super(BitrueOrderMinTotalException, self).__init__(-1013, message)


class BitrueOrderUnknownSymbolException(BitrueOrderException):

    def __init__(self, value):
        message = "Unknown symbol %s" % value
        super(BitrueOrderUnknownSymbolException, self).__init__(-1013, message)


class BitrueOrderInactiveSymbolException(BitrueOrderException):

    def __init__(self, value):
        message = "Attempting to trade an inactive symbol %s" % value
        super(BitrueOrderInactiveSymbolException, self).__init__(-1013, message)


class BitrueWithdrawException(Exception):
    def __init__(self, message):
        if message == u'参数异常':
            message = 'Withdraw to this address through the website first'
        self.message = message

    def __str__(self):
        return 'BitrueWithdrawException: %s' % self.message
