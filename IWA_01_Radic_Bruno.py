import socket, time

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)       
    
    return s

def get_source(s, ip, page):

    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get += 'Host: '
    get += ip
    get += CRLF
    get += CRLF

    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    # print (response)
    return response

def get_all_links(response):
    links = []
    beg = 0

    if "200 OK" not in response:
        return links
    while True:
        beg_str = response.find('href="', beg)   
        if beg_str == -1:
            return links

        end_str = response.find('"', beg_str + 6)   
        link = response[beg_str + 6:end_str]

        if link[-5:] == ".html":
            if link not in links:
                links.append(link)
        beg = end_str + 1
    
            
def get_the_rest(trenutni_linkovi, index):

    one_link = trenutni_linkovi[index]

    s = connect_to_server(ip, port)
    response = get_source(s, ip, one_link)

    ostali_linkovi = get_all_links(response)
    for link in ostali_linkovi:
        if link not in trenutni_linkovi:
            trenutni_linkovi.append(link)
    return trenutni_linkovi


ip = 'www.optimazadar.hr'
port = 80
page = ''

s = connect_to_server(ip, port)
response = get_source(s, ip, page)

links=[]
links = get_all_links(response)
print("Linkovi:")
print(links)
print("Ostatak:")

index = 0
while len(links) < 50 and index < len(links):
        links = get_the_rest(links, index)
        print("Provjera linkova stranicu za index: ", index)
        print(links)
        index += 1


