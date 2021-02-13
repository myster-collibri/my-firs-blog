from blog.models import Article

def run():
    for i in range(5,15):
        article=Article()
        article.title="Article no #%d"% i
        article.desc="Description article No #%d" % i
        article.image="http://default"
        article.save()
    print("operation reussi")