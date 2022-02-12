from django.conf.urls import url

from nft.views import (
    has_nft_handler
)


urlpatterns = [
    url(r'^hasNFT/?$', has_nft_handler, name='has_nft'),
]
