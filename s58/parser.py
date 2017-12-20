from html.parser import HTMLParser
import re


class ListHTMLParser(HTMLParser):
    __pattern = re.compile(r'^(http://.*\.5858\.com)\?psid=\d*&entinfo=\d*_j')

    contactSet = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href":
                    match = self.__pattern.match(str(v))
                    if match:
                        self.contactSet.add(match.group(1)+"/contactus/")

    def getConcatSet(self, html):
        self.feed(html)
        return self.contactSet

    def getAndSaveFileConcatSet(self, html, file_name='concatUrl.txt'):
        self.feed(html)
        for url in self.contactSet:
            with open(file_name, 'a') as f:
                f.write(url + '\n')
        return self.contactSet


class ContactHTMLParser(HTMLParser):

    isli = False
    isName = False
    isSpan = False
    isTel = False

    _comp_tel_name = list()

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.isli = True
        if tag == "span":
            self.isSpan = True
        if tag == "input":
            for k, v in attrs:
                if k == "class":
                    if v == "company-contact-name":
                        self._comp_tel_name.append(attrs[2][-1])
                    if v == "company-contact-telphone" and str(attrs[2][-1]).startswith("1"):
                        self.isTel = True
                        self._comp_tel_name.append(str(attrs[2][-1]))
                    elif v == "company-contact-telphone2" and not self.isTel:
                        self._comp_tel_name.append(str(attrs[2][-1]))

    def handle_data(self, data):
        if self.isli and data == "联  系  人：":
            self.isName = True
        if self.isSpan and self.isName:
            self._comp_tel_name.append(data)
            self.isName = False

    def handle_endtag(self, tag):
        if tag == "li":
            self.isli = False
        if tag == "span":
            self.isSpan = False

    def getDetailList(self, html):
        self.feed(html)
        return self._comp_tel_name

