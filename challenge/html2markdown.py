
def html2markdown(html):
    '''Take in html text as input and return markdown'''

    replaced = html.replace("<em>", "*").replace("</em>", "*")
    
    replaced = replaced.replace("\n", " ").replace("</p><p>", "\n\n").replace("<p>", "").replace("</p>", "")

    while "  " in replaced:
        replaced = replaced.replace("  ", " ")

    while replaced.find("</a>") != -1:
        start_link = replaced.find('<a href="')
        end_link = replaced.find('">', start_link)
        url = replaced[start_link + 9:end_link]
        end_tag = replaced.find("</a>", end_link)
        link_text = replaced[end_link + 2:end_tag]
        markdown_link = f"[{link_text}]({url})"
        replaced = replaced[:start_link] + markdown_link + replaced[end_tag + 4:]

    return replaced