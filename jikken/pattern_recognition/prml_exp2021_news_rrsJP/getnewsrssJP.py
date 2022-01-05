feedlist=['http://feeds.reuters.com/reuters/JPWorldNews',
          'http://www3.nhk.or.jp/rss/news/cat6.xml',
          'http://www.tokyo-np.co.jp/s/article/world.html']

def stripHTML(h):
    p=''
    s=0
    for c in h:
        if c=='<': s=1
        elif c=='>':
            s=0
            p+=' '
        elif s==0: p+=c
    return p.rstrip()


from feedparser import *
for feed in feedlist:
    f=parse(feed)
    for e in f.entries:
        print e.title.encode('utf8'),"|",stripHTML(e.description.encode('utf8'))
