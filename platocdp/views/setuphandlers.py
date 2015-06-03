from collective.grok import gs
from platocdp.views import MessageFactory as _

@gs.importstep(
    name=u'platocdp.views', 
    title=_('platocdp.views import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('platocdp.views.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
