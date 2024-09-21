from django.conf import settings
import vk_api
from vk_api import VkUpload

from common.vk_wall import VkAPI


vk_session = vk_api.VkApi(token=settings.BOT_TOKEN)

vk_api = VkAPI(
    settings.VK_ACCESS_TOKEN,
)
vk_upload = VkUpload(vk_session)
