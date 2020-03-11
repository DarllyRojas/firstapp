from tethys_sdk.base import TethysAppBase, url_map_maker


class Myfirstapp(TethysAppBase):
    """
    Tethys app class for Myfirstapp.
    """

    name = 'Myfirstapp'
    index = 'myfirstapp:home'
    icon = 'myfirstapp/images/Logo_Darlly_v1.png'
    package = 'myfirstapp'
    root_url = 'myfirstapp'
    color = '#042EC6'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='myfirstapp',
                controller='myfirstapp.controllers.home'
            ),
            UrlMap(
                name='map',
                url='myfirstapp/map',
                controller='myfirstapp.controllers.map'
            ),
        )

        return url_maps
