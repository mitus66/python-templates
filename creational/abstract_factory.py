'''Паттерн проектування, який дозволяє створювати сімейства пов'язаних об'єктів, не прив'язуючись до конкретних класів об'єктів, що створюються. '''

from abc import ABC, abstractmethod


class AbstractReport(ABC):

    @abstractmethod
    def create_month_report(self):
        pass


    @abstractmethod
    def create_quarter_report(self):
        pass

    @abstractmethod
    def create_year_report(self):
        pass


class PdfReport(AbstractReport):

    def create_month_report(self):
        return PdfMonthReport()

    def create_quarter_report(self):
        return PdfQuarterReport()

    def create_year_report(self):
        return PdfYearReport()


class HtmlReport(AbstractReport):

    def create_month_report(self):
        return HtmlMonthReport()

    def create_quarter_report(self):
        return HtmlQuarterReport()

    def create_year_report(self):
        return HtmlYearReport()



class CsvReport(AbstractReport):

    def create_month_report(self):
        return CsvMonthReport()

    def create_quarter_report(self):
        return CsvQuarterReport()

    def create_year_report(self):
        return CsvYearReport()
