
class EmailValidator:

    def __init__(self, min_length, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):

        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):

        return mail in self.mails

    def __is_domain_valid(self, domain):

        return domain in self.domains

    def validate(self, email):

        name, mail = email.split('@')
        emails, domain_part = mail.split('.')

        return self.__is_name_valid(name) and \
               self.__is_mail_valid(emails) and \
               self.__is_domain_valid(domain_part)
