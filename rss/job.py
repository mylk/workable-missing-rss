from datetime import datetime


class Job():

    element = None
    details = None

    def __init__(self, element):
        self.element = element
        self.details = self.get_details()

    def get_details(self):
        details = self.element.select('h4')
        return details[0] if len(details) > 0 else None

    def is_valid(self):
        return True if self.details else False

    def get_position(self):
        positions = self.element.select('h2 > a')
        return positions[0].string.replace('\n', '') if len(positions) > 0 else None

    def get_company(self):
        companies = self.details.select('a')
        return companies[0].string.replace('\n', '') if len(companies) > 0 else None

    def get_date(self):
        dates = self.details.select('span.date')
        date = dates[0].string.replace('\n', '') if len(dates) > 0 else None
        datetime_object = datetime.strptime(date, '%B %d, %Y')
        return datetime_object

    def get_description(self):
        descriptions = self.element.select('p.description')
        return descriptions[0].string.replace('\n', '') if len(descriptions) > 0 else None

    def get_link(self):
        links = self.element.select('p.more > a')
        return links[0]['href'].replace('\n', '') if len(links) > 0 else None
