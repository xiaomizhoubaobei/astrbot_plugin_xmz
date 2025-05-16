from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.core import AstrBotConfig
from .hitokoto_handler import get_hitokoto
from .beauty_handler import get_beauty_score
from .baidu_auth import init_baidu_credentials

@register("hitokoto", "YourName", "一言插件", "1.1.0")
class HitokotoPlugin(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)
        self.config = config
        init_baidu_credentials(self.config)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
        logger.info("一言插件初始化完成")
    
    @filter.command("hitokoto")
    async def hitokoto_command(self, event: AstrMessageEvent):
        """获取一条一言。"""
        yield await get_hitokoto(event)
        
    @filter.command("测颜值")
    async def beauty_command(self, event: AstrMessageEvent):
        """发送人像图片获取颜值评分。"""
        print(event.message_obj.raw_message) # 平台下发的原始消息在这里
        print(event.message_obj.message) # AstrBot 解析出来的消息链内容
        yield await get_beauty_score(event)

    @filter.command("xmz-help")
    async def help_command(self, event: AstrMessageEvent):
        """显示插件帮助信息。"""
        help_text = """
        === 一言插件帮助 ===
        命令列表:
        1. /hitokoto - 获取一条一言
        2. /测颜值 - 发送人像图片获取颜值评分
        3. /xmz-help - 显示本帮助信息
        """
        yield event.plain_result(help_text)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        logger.info("一言插件已终止")
