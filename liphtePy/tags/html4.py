from liphtePy.util import quoteattrs
from liphtePy.flatten import register_flattener
from liphtePy.tags import Tag, Namespace
from liphtePy.tags.html import empty_tag_names, HtmlProto, tags as htmltags

xmlns = None
xml_encoding = None
doctype = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">'''
strict_doctype = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'''

# a class to handle empty tags in html4 format
class Html4EmptyTag(Tag):
    pass


def flatten_empty_html4_tag(o):
    if o.render:
        o = o.render(o, o.data)

    attrs = u''.join(quoteattrs(o.attrs))
    return u'<%s%s>' % (o.name, attrs)


register_flattener(Html4EmptyTag, flatten_empty_html4_tag)


class Html4EmptyProto(HtmlProto):
    Class = Html4EmptyTag
    pass


def flatten_html4_empty_proto(p):
    return '<%s>' % (p)


register_flattener(Html4EmptyProto, flatten_html4_empty_proto)

tags = Namespace()

# copy the default html tag namespace
for k, v in htmltags.iteritems():
    tags[k] = v

# so we can override the empty tags without stomping on the existing tags
for t in empty_tag_names:
    tags[t] = Html4EmptyProto(t)
