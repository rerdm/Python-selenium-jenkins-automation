import logging
import sys

from bs4 import BeautifulSoup


class VerbindeHtmlReportMitAssertCss:

    def __init__(self, file_path):
        self.file_path = file_path
        self.html_content = None
        self.soup = None

    def file_oeffnen(self):
        try:
            with open(self.file_path, 'r', encoding='iso-8859-1') as file:
                self.html_content = file.read()
        except:
            logging.error("ERROR: Der html Report kann nicht bearbeitet werden\n"
                          "Eventuell ist er nicht vorhanden")
            sys.exit()

    def entferne_stylesheet_link(self):
        self.html_content = self.html_content.replace('<link href="assets/style.css" rel="stylesheet" type="text/css"/></head>', '')

    def parsen_des_html_files(self):
        self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def file_speichern(self, output_file_path):
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(str(self.soup))

    def style_tag_unter_body_tag_einfuegen(self, css_content):
        style_tag = self.soup.new_tag('style')
        style_tag.string = css_content

        body_tag = self.soup.find('body')
        if body_tag:
            body_tag.insert_before(style_tag)
        else:
            head_tag = self.soup.find('head')
            if head_tag:
                head_tag.append(style_tag)
            else:
                # Wenn kein <head>-Tag gefunden wird, füge den <style>-Tag direkt nach dem <html>-Tag ein
                html_tag = self.soup.find('html')
                if html_tag:
                    html_tag.insert(0, style_tag)

    def neues_html_file_mit_integrierte_style_tag(self, output_file_path):

        css_content = """
        body {
      font-family: Helvetica, Arial, sans-serif;
      font-size: 12px;
      /* do not increase min-width as some may use split screens */
      min-width: 800px;
      color: #999;
    }
    
    h1 {
      font-size: 24px;
      color: black;
    }
    
    h2 {
      font-size: 16px;
      color: black;
    }
    
    p {
      color: black;
    }
    
    a {
      color: #999;
    }
    
    table {
      border-collapse: collapse;
    }
    
    /******************************
     * SUMMARY INFORMATION
     ******************************/
    #environment td {
      padding: 5px;
      border: 1px solid #E6E6E6;
    }
    #environment tr:nth-child(odd) {
      background-color: #f6f6f6;
    }
    
    /******************************
     * TEST RESULT COLORS
     ******************************/
    span.passed,
    .passed .col-result {
      color: green;
    }
    
    span.skipped,
    span.xfailed,
    span.rerun,
    .skipped .col-result,
    .xfailed .col-result,
    .rerun .col-result {
      color: orange;
    }
    
    span.error,
    span.failed,
    span.xpassed,
    .error .col-result,
    .failed .col-result,
    .xpassed .col-result {
      color: red;
    }
    
    /******************************
     * RESULTS TABLE
     *
     * 1. Table Layout
     * 2. Extra
     * 3. Sorting items
     *
     ******************************/
    /*------------------
     * 1. Table Layout
     *------------------*/
    #results-table {
      border: 1px solid #e6e6e6;
      color: #999;
      font-size: 12px;
      width: 100%;
    }
    #results-table th,
    #results-table td {
      padding: 5px;
      border: 1px solid #E6E6E6;
      text-align: left;
    }
    #results-table th {
      font-weight: bold;
    }
    
    /*------------------
     * 2. Extra
     *------------------*/
    .log {
      background-color: #e6e6e6;
      border: 1px solid #e6e6e6;
      color: black;
      display: block;
      font-family: "Courier New", Courier, monospace;
      height: 230px;
      overflow-y: scroll;
      padding: 5px;
      white-space: pre-wrap;
    }
    .log:only-child {
      height: inherit;
    }
    
    div.image {
      border: 1px solid #e6e6e6;
      float: right;
      height: 240px;
      margin-left: 5px;
      overflow: hidden;
      width: 320px;
    }
    div.image img {
      width: 320px;
    }
    
    div.video {
      border: 1px solid #e6e6e6;
      float: right;
      height: 240px;
      margin-left: 5px;
      overflow: hidden;
      width: 320px;
    }
    div.video video {
      overflow: hidden;
      width: 320px;
      height: 240px;
    }
    
    .collapsed {
      display: none;
    }
    
    .expander::after {
      content: " (show details)";
      color: #BBB;
      font-style: italic;
      cursor: pointer;
    }
    
    .collapser::after {
      content: " (hide details)";
      color: #BBB;
      font-style: italic;
      cursor: pointer;
    }
    
    /*------------------
     * 3. Sorting items
     *------------------*/
    .sortable {
      cursor: pointer;
    }
    
    .sort-icon {
      font-size: 0px;
      float: left;
      margin-right: 5px;
      margin-top: 5px;
      /*triangle*/
      width: 0;
      height: 0;
      border-left: 8px solid transparent;
      border-right: 8px solid transparent;
    }
    .inactive .sort-icon {
      /*finish triangle*/
      border-top: 8px solid #E6E6E6;
    }
    .asc.active .sort-icon {
      /*finish triangle*/
      border-bottom: 8px solid #999;
    }
    .desc.active .sort-icon {
      /*finish triangle*/
      border-top: 8px solid #999;
    }
        """

        self.file_oeffnen()
        self.entferne_stylesheet_link()
        self.parsen_des_html_files()
        self.style_tag_unter_body_tag_einfuegen(css_content)
        self.file_speichern(output_file_path)


if __name__ == '__main__':

    html_file_mit_assert_css_zuamenfuegen = VerbindeHtmlReportMitAssertCss('Benutzername_anfordern.html')
    html_file_mit_assert_css_zuamenfuegen.neues_html_file_mit_integrierte_style_tag('neue_datei.html')
