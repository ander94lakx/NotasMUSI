from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.current_tag = ""
        self.last_href = ""
        self.last_link_name = ""
        self.is_musi = False
        self.data = {}

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.start_tag = True
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.last_href = attr[1]
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        self.start_tag = False
        if tag == 'a' and self.is_musi:
            self.data[self.current_key].append('- [' + self.last_link_name + '](' + self.last_href + ')\n')
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.current_tag == 'h1' and self.start_tag:
            self.is_musi = 'MUSI' in data
            if self.is_musi:
                self.is_musi = True
                key = ''
                title = ''
                if 'AV' in data:
                    key = 'AV'
                    title = '## Análisis de Vulnerabilidades'
                elif 'CMS' in data:
                    key = 'CMS'
                    title = '## Criptografía y Mecanismos de seguridad'
                elif '4n6' in data or 'AF' in data:
                    key = 'AF'
                    title = '## Análisis forense'
                elif 'SSO' in data:
                    key = 'SSO'
                    title = '## Seguridad en Sistemas Operativos'
                elif 'GS' in data:
                    key = 'GS'
                    title = '## Gestión de la Seguridad'
                elif 'ALR' in data:
                    key = 'ARL'
                    title = '## Aspectos Legales y Regulatorios'
                elif 'SR' in data:
                    key = 'SR'
                    title = '## Seguridad en Redes'
                else:
                    key = 'r'    
                    title = '## Random / Off-topic'

                if title != '':
                    self.current_key = key
                    self.data[key] = []
                    self.data[key].append('\n')
                    self.data[key].append(title)
                    self.data[key].append('\n\n')
        elif self.current_tag == 'a':
            self.last_link_name = data
        print("Encountered some data  :", data)

    def write_data(self):
        filename = 'links.md'
        with open(filename, mode='w', encoding="utf8") as output:
            print('File', filename, 'opened TO WRITE')
            output.write('# Links\n')
            for key in ['AV', 'SR', 'CMS', 'SSO', 'AF', 'ARL', 'GS', 'r']:
                if key in self.data.keys():
                    for line in self.data[key]:
                        output.write(line)
            print('File', filename, 'succesfully generated')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1], encoding='utf8') as file:
            print('File', sys.argv[1], 'opened')
            parser = MyHTMLParser()
            data = file.read()
            parser.feed(data)
            parser.write_data()