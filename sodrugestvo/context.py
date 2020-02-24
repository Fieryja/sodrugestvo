from contents.models import Block


def blocks(request):
    block = {}
    for i in Block.objects.all():
        block.update({i.name: i.html})
    return {'blocks': block}